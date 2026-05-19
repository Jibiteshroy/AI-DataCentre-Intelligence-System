USE DataCentre_Intelligence;
GO

-- 1. Import Facilities
BULK INSERT Facility_Master
FROM 'D:\Projects & Post\AI-Powered Data Centre Intelligence & Reliability Management System\AI-DataCentre-Intelligence-System\datasets\facility_master.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '\n');
GO

-- 2. Import Assets
BULK INSERT Asset_Inventory
FROM 'D:\Projects & Post\AI-Powered Data Centre Intelligence & Reliability Management System\AI-DataCentre-Intelligence-System\datasets\asset_inventory.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '\n');
GO

-- 3. Import Incidents
BULK INSERT Incidents
FROM 'D:\Projects & Post\AI-Powered Data Centre Intelligence & Reliability Management System\AI-DataCentre-Intelligence-System\datasets\incidents.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '\n');
GO

-- 4. Import Maintenance
BULK INSERT Maintenance
FROM 'D:\Projects & Post\AI-Powered Data Centre Intelligence & Reliability Management System\AI-DataCentre-Intelligence-System\datasets\maintenance.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '\n');
GO

-- 5. Import Telemetry (Using a View to bypass the auto-generating ID)
CREATE VIEW vw_Energy_Cooling_Import AS
SELECT Date, Facility_ID, Energy_Consumption_kWh, Cooling_Load_kWh, PUE, Temperature_C, Humidity_Percent, Carbon_Emission_kg
FROM Energy_Cooling;
GO

BULK INSERT vw_Energy_Cooling_Import
FROM 'D:\Projects & Post\AI-Powered Data Centre Intelligence & Reliability Management System\AI-DataCentre-Intelligence-System\datasets\energy_cooling.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '\n');
GO

DROP VIEW vw_Energy_Cooling_Import;
GO