SELECT * FROM main;

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

-- suspect count (synthetic column created by insdustry consultant) 
SELECT turbine_id, 
COUNT(suspect) AS "Suspect Count"
FROM main
WHERE suspect = 1
GROUP BY turbine_id;

-- amb_temp_avg
SELECT turbine_id AS "amb_temp_avg",
ROUND(AVG (amb_temp_avg)) AS "AVG",
MIN (amb_temp_avg) AS "MIN",
MAX (amb_temp_avg) AS "MAX",
ROUND(STDDEV(amb_temp_avg)) AS "ST. DEV.",	
ROUND(VARIANCE(amb_temp_avg)) AS "VARIANCE"
INTO amb_temp_summary
FROM main
GROUP BY turbine_id;

-- gear_bear_temp_avg 
SELECT turbine_id AS "gear_bear_temp_avg",
AVG (gear_bear_temp_avg) AS "AVG",
MIN (gear_bear_temp_avg) AS "MIN",
MAX (gear_bear_temp_avg) AS "MAX",
STDDEV(gear_bear_temp_avg) AS "ST. DEV.",	
VARIANCE(gear_bear_temp_avg) AS "VARIANCE"
FROM main
GROUP BY turbine_id;

-- nac_temp_avg
SELECT turbine_id AS "nac_temp_avg",
ROUND(AVG (nac_temp_avg)) AS "AVG",
MIN (nac_temp_avg) AS "MIN",
MAX (nac_temp_avg) AS "MAX",
ROUND(STDDEV(nac_temp_avg)) AS "ST. DEV.",	
ROUND(VARIANCE(nac_temp_avg)) AS "VARIANCE"
INTO nacelle_summary
FROM main
GROUP BY turbine_id;

