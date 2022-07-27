import pandas as pd
<<<<<<< HEAD
import config
import json
import sys
=======
import json
>>>>>>> cleanest
import os
from pathlib import Path

# A global variable to reference once make_turbine_dataframes is run at least once.
turbine_dataframes = {}

def make_turbine_dataframes(): 
    # Pull the full dataframe from the AWS RDS server. 
<<<<<<< HEAD
    main_df = pd.read_sql("main", con= f"postgresql://postgres:{config.rds_password}@wind-turbine-analysis.chv2nnusygyy.us-west-1.rds.amazonaws.com:5432/wind_turbine_analysis")
=======
    main_df = pd.read_sql("main", con= f"postgresql://postgres:password@wind-turbine-analysis.chv2nnusygyy.us-west-1.rds.amazonaws.com:5432/wind_turbine_analysis")
>>>>>>> cleanest

    # clean incoming dataset, this can be resolved at the database level eventually. 
    main_df.drop(columns=["index", "suspect"], inplace=True)

    #We're converting from Timestamp obj to JSON readable ISO 8601 format. 
    main_df['time_stamp'] = main_df['time_stamp'].copy().apply(lambda x: x.isoformat())

    # Read in each turbines data

    for turbine in main_df["turbine_id"].unique():

        turbine_dataframes[turbine] = main_df[main_df["turbine_id"] == turbine].drop_duplicates("time_stamp")

    
    turbine_dictionaries = {}

    for turbine in turbine_dataframes: 
        turbine_dictionaries[turbine] = turbine_dataframes[turbine].copy().to_dict()

    print(os.getcwd())

    #pathing solution using pathlib's Path object
    working_directory = Path(__file__).absolute().parent
    
    with open(working_directory / 'static\\json\\declare.json', 'w') as file: 
        json.dump(turbine_dictionaries, file, indent=6)

    return