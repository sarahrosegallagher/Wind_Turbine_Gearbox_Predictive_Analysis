import pandas as pd
import psycopg2 as psy
import numpy as np
import config

# A global variable to reference once make_turbine_dataframes is run at least once.
turbine_dataframes = {}

def make_turbine_dataframes(): 
    # Pull the full dataframe from the AWS RDS server. 
    main_df = pd.read_sql("main", con= f"postgresql://postgres:{config.rds_password}@wind-turbine-analysis.chv2nnusygyy.us-west-1.rds.amazonaws.com:5432/wind_turbine_analysis")

    # clean incoming dataset, this can be resolved at the database level eventually. 
    main_df.drop(columns=["index", "suspect"], inplace=True)

    # Read in each turbines data

    for turbine in main_df["turbine_id"].unique():

        turbine_dataframes[turbine] = main_df[main_df["turbine_id"] == turbine].drop_duplicates("time_stamp")

    # Read in the failure data for each turbine 
    failures_df = pd.read_sql("major_faults", con= "postgresql://postgres:password@wind-turbine-analysis.chv2nnusygyy.us-west-1.rds.amazonaws.com:5432/wind_turbine_analysis")

    turbine_failures = {}

    for turbine in failures_df["turbine_id"]:

        current_failure = failures_df[failures_df["turbine_id"] == turbine]

        current_failure['time_stamp'] = pd.to_datetime(current_failure['time_stamp'])
        current_failure.sort_values(by="time_stamp", inplace=True)
        current_failure.drop(['index'], axis=1, inplace=True)

        turbine_failures[turbine] = current_failure

    # Loop through dataframes in turbine dataframes
    for turbine in turbine_dataframes:

        # Add time_bin and failure_in_next_bin to each dataframe by checking for failures in current bin

        failure_dates = turbine_failures[turbine]['time_stamp']
        df = turbine_dataframes[turbine]

        df["time_bin"] = pd.cut(df.time_stamp, bins=48, labels=np.arange(0,48))

        failure_in_bin = {}
        failure_in_next_bin = {}

        for bin in df["time_bin"].unique():

            time_bin = df[df["time_bin"] == bin]
            
            start = time_bin.time_stamp.iloc[0]
            end = time_bin.time_stamp.iloc[-1]

            for date in failure_dates:
                if start <= date <= end:
                    failure_in_bin[bin] = 1
                    break
                else:
                    failure_in_bin[bin] = 0

        # Build failure in Next Bin by shifting failure in bin up one. 
        failure_in_next_bin = np.int_(pd.Series(failure_in_bin).shift(-1).fillna(0))
        failure_in_next_bin = dict(zip(failure_in_bin.keys(), failure_in_next_bin))

        # Add failure in NEXT bin identifier to turbine dataframe
        df["failure_in_next_bin"] = df["time_bin"].apply(lambda x: failure_in_next_bin[x])

    turbine_dictionaries = {}

    for turbine in turbine_dataframes: 
        turbine_dictionaries[turbine] = turbine_dataframes[turbine].to_dict()


    return turbine_dictionaries