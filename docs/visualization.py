import pandas as pd
import psycopg2 as psy
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

# The purpose of this file is to Take in database data, trim it into the necessary form


print(data)
# Pull the full dataframe from the AWS RDS server. 
#main_df = pd.read_sql("main", con= "postgresql://postgres:password@wind-turbine-analysis.chv2nnusygyy.us-west-1.rds.amazonaws.com:5432/wind_turbine_analysis")

#main_df.drop(columns=["index", "suspect", "wind_bucket"], inplace=True)

# Read in each turbines data
#turbine_dataframes = {}

#for turbine in main_df["turbine_id"].unique():

    #turbine_dataframes[turbine] = main_df[main_df["turbine_id"] == turbine].drop_duplicates("time_stamp")