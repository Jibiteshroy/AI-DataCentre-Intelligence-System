import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
np.random.seed(42)

# 1. Create Facility Master Dataset
facilities = {
    'Facility_ID': ['DXB-Core-01', 'DXB-Edge-02', 'SIN-Core-01', 'FRA-Core-01', 'MUM-Zone-A', 'LHR-Core-02'],
    'Region': ['Middle East', 'Middle East', 'APAC', 'Europe', 'India', 'Europe'],
    'Country': ['UAE', 'UAE', 'Singapore', 'Germany', 'India', 'UK'],
    'Tier_Level': ['Tier IV', 'Tier III', 'Tier IV', 'Tier IV', 'Tier III', 'Tier IV']
}
df_facilities = pd.DataFrame(facilities)
df_facilities.to_csv('datasets/facility_master.csv', index=False)

# 2. Create Incidents Dataset (5,000 rows)
num_incidents = 5000
start_date = datetime(2023, 1, 1)

failure_types = {
    'Power': ['UPS Failure', 'Generator Failure', 'PDU Overload'],
    'Cooling': ['CRAC Failure', 'Chiller Failure', 'Cooling Pump Failure'],
    'Network': ['Router Failure', 'Fiber Cut', 'Switch Failure'],
    'Environmental': ['Water Leakage', 'Temperature Spike']
}

incidents = []
for i in range(num_incidents):
    incident_id = f"INC-{10000 + i}"
    date = start_date + timedelta(days=random.randint(0, 365), hours=random.randint(0, 23))
    facility = random.choice(facilities['Facility_ID'])
    category = random.choice(list(failure_types.keys()))
    subcategory = random.choice(failure_types[category])
    
    # Realistic Logic Application
    severity_roll = random.random()
    if severity_roll < 0.05:
        severity = 'Critical'
        downtime = random.randint(180, 600)
        revenue_impact = downtime * random.randint(1000, 5000)
    elif severity_roll < 0.15:
        severity = 'High'
        downtime = random.randint(60, 179)
        revenue_impact = downtime * random.randint(500, 1000)
    elif severity_roll < 0.40:
        severity = 'Medium'
        downtime = random.randint(20, 59)
        revenue_impact = downtime * random.randint(100, 500)
    else:
        severity = 'Low'
        downtime = random.randint(5, 19)
        revenue_impact = downtime * random.randint(0, 50)
        
    incidents.append([
        incident_id, date, facility, category, subcategory, 
        severity, downtime, revenue_impact, fake.name()
    ])

df_incidents = pd.DataFrame(incidents, columns=[
    'Incident_ID', 'Date', 'Facility_ID', 'Failure_Category', 
    'Failure_Subcategory', 'Severity', 'Downtime_Minutes', 
    'Revenue_Impact_USD', 'Engineer_Assigned'
])
df_incidents.to_csv('datasets/incidents.csv', index=False)