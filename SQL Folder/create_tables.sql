-- Creating tables for Air_Quality-FinalDB

CREATE TABLE small_PM_dataset (
	site INT NOT NULL,
	pm_value DECIMAL NOT NULL,
	units VARCHAR(40) NOT NULL,
	site_name VARCHAR(40) NOT NULL,
	latitude DECIMAL NOT NULL,
	longitude DECIMAL NOT NULL,
	dateC DATE NOT NULL,
	county VARCHAR NOT NULL
);

CREATE TABLE small_wind_dataset (
	site INT NOT NULL,
	ws DECIMAL NOT NULL,
	wd DECIMAL NOT NULL,
	mph_units VARCHAR NOT NULL,
	site_name VARCHAR(40) NOT NULL,
	latitude DECIMAL NOT NULL,
	longitude DECIMAL NOT NULL,
	dateC DATE NOT NULL,
	county VARCHAR NOT NULL	
);	

--Drop Table
--DROP TABLE small_wind_dataset;
--DROP TABLE small_PM_dataset;
-- QUERY Confirmation

SELECT * FROM small_PM_dataset;
SELECT * FROM small_wind_dataset;

--ALL CODE ABOVE WORKS!

-- Reference Queries below 

SELECT site, county, ws, wd
FROM small_wind_dataset
WHERE county = 'Sacramento';

SELECT AVG (wd)
FROM small_wind_dataset
WHERE site = '3011';

 