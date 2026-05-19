import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

# Ensure directory exists
os.makedirs('datasets', exist_ok=True)
fake = Faker()
np.random.seed(42)

# Matching the exact facilities from Script 1
facilities = ['DXB-Core-01', 'DXB-Edge-02', 'SIN-Core-01', 'FRA-Core-01', 'MUM-Zone-A', 'LHR-Core-02']

# -----------------------------------------
# 1. CREATE ASSET INVENTORY
# -----------------------------------------
assets = []
asset_types = ['UPS', 'Generator', 'CRAC', 'Chiller', 'Router', 'Fire Panel', 'PDU']
asset_ids = []

for i in range(1, 501):
    asset_id = f"AST-{1000 + i}"
    asset_ids.append(asset_id)
    facility = random.choice(facilities)
    asset_type = random.choice(asset_types)
    
    # Logic: Older assets fail more and consume more power
    install_date = datetime(2015, 1, 1) + timedelta(days=random.randint(0, 3000))
    age_years = (datetime.now() - install_date).days / 365.25
    
    base_power = random.uniform(10, 100)
    power_consumption = round(base_power * (1 + (age_years * 0.02)), 2) 
    
    assets.append([asset_id, facility, asset_type, install_date.strftime('%Y-%m-%d'), power_consumption, round(age_years, 1)])

df_assets = pd.DataFrame(assets, columns=['Asset_ID', 'Facility_ID', 'Asset_Type', 'Installation_Date', 'Power_Consumption_kW', 'Age_Years'])
df_assets.to_csv('datasets/asset_inventory.csv', index=False)

# -----------------------------------------
# 2. CREATE MAINTENANCE DATASET
# -----------------------------------------
maintenance = []
maint_types = ['Preventive', 'Reactive', 'Emergency', 'Predictive']

for i in range(2500):
    maint_id = f"MNT-{5000 + i}"
    asset_id = random.choice(asset_ids)
    maint_type = random.choices(maint_types, weights=[0.4, 0.3, 0.1, 0.2])[0]
    date = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))
    
    # Logic: Reactive/Emergency = High Cost & High Downtime
    if maint_type in ['Reactive', 'Emergency']:
        cost = random.randint(2000, 15000)
        downtime = random.randint(60, 300)
    else:
        cost = random.randint(500, 2000)
        downtime = random.randint(0, 45)
        
    maintenance.append([maint_id, asset_id, maint_type, date.strftime('%Y-%m-%d'), cost, downtime, fake.name()])

df_maintenance = pd.DataFrame(maintenance, columns=['Maintenance_ID', 'Asset_ID', 'Maintenance_Type', 'Date', 'Cost_USD', 'Downtime_Minutes', 'Technician'])
df_maintenance.to_csv('datasets/maintenance.csv', index=False)

# -----------------------------------------
# 3. CREATE ENERGY & COOLING TELEMETRY
# -----------------------------------------
energy = []
for date in pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'):
    for facility in facilities:
        base_energy = random.uniform(5000, 15000)
        cooling_load = base_energy * random.uniform(0.3, 0.6)
        
        # PUE Logic: Tier IV 'Core' facilities are more efficient
        if 'Core' in facility:
            pue = round(random.uniform(1.18, 1.35), 2)
        else:
            pue = round(random.uniform(1.45, 1.85), 2)
            
        temp = round(random.uniform(19, 25), 1) # Normal Celsius
        humidity = round(random.uniform(45, 55), 1) # Normal Percentage
        
        # Inject critical thermal anomalies for Power BI Alerts
        if random.random() < 0.03:
            temp = round(random.uniform(28, 34), 1) # Alert threshold > 28C
            
        carbon_emission = round(base_energy * 0.42, 2) # kg CO2
        
        energy.append([date.strftime('%Y-%m-%d'), facility, round(base_energy, 2), round(cooling_load, 2), pue, temp, humidity, carbon_emission])

df_energy = pd.DataFrame(energy, columns=['Date', 'Facility_ID', 'Energy_Consumption_kWh', 'Cooling_Load_kWh', 'PUE', 'Temperature_C', 'Humidity_Percent', 'Carbon_Emission_kg'])
df_energy.to_csv('datasets/energy_cooling.csv', index=False)

print("SUCCESS: Asset Inventory, Maintenance Logs, and Telemetry datasets generated perfectly.")