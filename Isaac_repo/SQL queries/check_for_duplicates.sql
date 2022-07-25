SELECT time_stamp, COUNT(*)
INTO temp_table
FROM main
GROUP BY time_stamp;

SELECT time_stamp, count 
FROM temp_table
WHERE count > 4; 

DROP TABLE temp_table;

/* This shows how many readings there are for each time stamp. Certain turbines are offline during certain periods, so there are 
between 1 - 4 readings for any one date. There are 12 known readings on 10/29/2016 and '17, as well as 10/30/2016 and '17 where 
there are duplicate readings for each turbine, all during 0200 hours. 

I ran this query in order to determine how to best clean the data in test_all_turbines.ipynb

We can decide whether to make the change in the database or keep the readings as an example of a pattern of misreadings. */