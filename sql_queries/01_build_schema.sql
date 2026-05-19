-- 1. Create and switch to the database
CREATE DATABASE DataCentre_Intelligence;
GO

USE DataCentre_Intelligence;
GO

-- 2. Create the Master Dimension Table
CREATE TABLE Facility_Master (
    Facility_ID VARCHAR(50) PRIMARY KEY,
    Region VARCHAR(50),
    Country VARCHAR(50),
    Tier_Level VARCHAR(20)
);
GO

-- 3. Create the Asset Dimension Table
CREATE TABLE Asset_Inventory (
    Asset_ID VARCHAR(50) PRIMARY KEY,
    Facility_ID VARCHAR(50),
    Asset_Type VARCHAR(50),
    Installation_Date DATE,
    Power_Consumption_kW DECIMAL(10,2),
    Age_Years DECIMAL(5,2),
    FOREIGN KEY (Facility_ID) REFERENCES Facility_Master(Facility_ID)
);
GO

-- 4. Create the Incidents Fact Table
CREATE TABLE Incidents (
    Incident_ID VARCHAR(50) PRIMARY KEY,
    Date DATETIME,
    Facility_ID VARCHAR(50),
    Failure_Category VARCHAR(50),
    Failure_Subcategory VARCHAR(50),
    Severity VARCHAR(20),
    Downtime_Minutes INT,
    Revenue_Impact_USD DECIMAL(15,2),
    Engineer_Assigned VARCHAR(100),
    FOREIGN KEY (Facility_ID) REFERENCES Facility_Master(Facility_ID)
);
GO

-- 5. Create the Maintenance Fact Table
CREATE TABLE Maintenance (
    Maintenance_ID VARCHAR(50) PRIMARY KEY,
    Asset_ID VARCHAR(50),
    Maintenance_Type VARCHAR(50),
    Date DATE,
    Cost_USD DECIMAL(10,2),
    Downtime_Minutes INT,
    Technician VARCHAR(100),
    FOREIGN KEY (Asset_ID) REFERENCES Asset_Inventory(Asset_ID)
);
GO

-- 6. Create the Telemetry Fact Table
CREATE TABLE Energy_Cooling (
    Telemetry_ID INT IDENTITY(1,1) PRIMARY KEY, -- SQL Server specific auto-increment
    Date DATE,
    Facility_ID VARCHAR(50),
    Energy_Consumption_kWh DECIMAL(15,2),
    Cooling_Load_kWh DECIMAL(15,2),
    PUE DECIMAL(5,2),
    Temperature_C DECIMAL(5,2),
    Humidity_Percent DECIMAL(5,2),
    Carbon_Emission_kg DECIMAL(15,2),
    FOREIGN KEY (Facility_ID) REFERENCES Facility_Master(Facility_ID)
);
GO