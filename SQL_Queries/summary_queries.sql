-- next steps: - standard dev, outliers/trends? => use pd (Isaac)
-- what columns are useful and not? identify more and less useful columns => remove noise 
-- correlations columns to faults => python (not relative predictability)

SELECT * FROM main_full;

-- record count per turbine 
SELECT turbine_id,
COUNT(turbine_id) AS "count" 
FROM main
GROUP BY turbine_id;

-- major fault category count
SELECT fault,
COUNT(fault) AS "count"
FROM major_faults
GROUP BY fault
ORDER BY count DESC;


-- count per wind bucket 
-- wind bucket = rounded m/s windspeed measurement
SELECT wind_bucket AS "Wind Speed (m/s)",
COUNT(wind_bucket) AS "Count"
FROM main
GROUP BY wind_bucket;

-- suspect count 
-- what is suspect determined by? 
SELECT turbine_id, 
COUNT(suspect) AS "Suspect Count"
FROM main
WHERE suspect = 1
GROUP BY turbine_id;

-- gear_bear_temp_avg 
SELECT turbine_id AS "gear_bear_temp_avg",
AVG (gear_bear_temp_avg) AS "AVG",
MIN (gear_bear_temp_avg) AS "MIN",
MAX (gear_bear_temp_avg) AS "MAX"
FROM main
GROUP BY turbine_id;

-- nac_temp_avg
-- units on 
SELECT turbine_id AS "nac_temp_avg",
AVG (nac_temp_avg) AS "AVG",
MIN (nac_temp_avg) AS "MIN",
MAX (nac_temp_avg) AS "MAX"
-- add std 
FROM main
GROUP BY turbine_id;

