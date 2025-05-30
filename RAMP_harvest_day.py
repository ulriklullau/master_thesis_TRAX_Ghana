# -*- coding: utf-8 -*-
"""
Input file for the RAMP model tailored for the solar-powered cold storage facility.
"""

# %%
# importing functions

from ramp import User, UseCase, get_day_type
from ramp.core.core import UseCase
from ramp.post_process import post_process as pp
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Initialize user list
User_list = []

# Create new user class for the cold storage facility
CS = User(user_name = "Cold Storage Facility", num_users = 1)  # One facility
User_list.append(CS)

#%%
# Add compressor appliance
Compressor = CS.add_appliance(
 name = "Compressor", # optional feature for the appliance class
 number = 2, # how many radio each household type 1 has
 power = 1900, # RAMP does not take care of units of measure (e.g., Watts), you must be consistent
 func_time = 1440, # Total functioning time of appliance in minutes
 num_windows = 1, # how many time-windows the appliance is used in
 fixed="yes",  # This means all the 'n' appliances of this kind are always switched-on together
 fixed_cycle=3,  # number of cycles
#random_var_w=0.35, # 35% randomness assigned to the size of the functioning windows
 time_fraction_random_variability=0,  # randomizes the total time the appliance is on (between 0 and 1)
)

# setting the functioning windows
Compressor.windows([0, 1440])  # always on during the whole day, for all days of the year

# assiging the specific cycles
# first cycle: low cycle
Compressor.specific_cycle_1(
    p_11=79.69/2,  # power level for the first operation segment
    t_11=420,
    p_12=79.69/2,
    t_12= 420, # duration of the first operation segment
    r_c1=0.1,  # random variability assigned to the duration of each segment
)

# second cycle: intensive cycle
Compressor.specific_cycle_2(p_21=197.03/2, t_21=120, r_c2=0.1)

# third cycle: intermediate cycle
Compressor.specific_cycle_3(p_31=120.06/2, t_31=480, r_c3=0.1)

# defining cycle behaviour
Compressor.cycle_behaviour(
    cw11=[0, 419], cw12=[1020, 1440], cw21=[420, 539], cw31=[540, 1019] 
)

# %%
# Add fan appliance
Fan = CS.add_appliance(
    name="Fan",  # Optional feature for the appliance class
    number=4,  # Number of fans
    power=138,  # Power consumption in Watts
    func_time=1440,  # Total functioning time of appliance in minutes
    num_windows=1,  # Number of time-windows the appliance is used in
    fixed="yes",  # Fan operates whenever the compressor is on
    fixed_cycle=3,  # Number of cycles
    time_fraction_random_variability=0  # No randomness in total functioning time
)

# Set the functioning windows to match the compressor
Fan.windows([0, 1440])  # Always on during the whole day

# Assign the same cycles as the compressor
Fan.specific_cycle_1(p_11=27.75/4, t_11=420, p_12=12, t_12=420, r_c1=0.1)
Fan.specific_cycle_2(p_21=68.50/4, t_21=120, r_c2=0.1)
Fan.specific_cycle_3(p_31=41.74/4, t_31=480, r_c3=0.1)

# Define cycle behavior to match the compressor
Fan.cycle_behaviour(
    cw11=[0, 419], cw12=[1020, 1440], cw21=[420, 539], cw31=[540, 1019]
)

# %%
# Add lamp appliance
Lamp = CS.add_appliance(
    name="Lamp",  # Optional feature for the appliance class
    number=4,  # Number of lamps
    power=9,  # Power consumption in Watts
    func_time=120,  # Total functioning time of appliance in minutes
    num_windows=1,  # Number of time-windows the appliance is used in
    time_fraction_random_variability = 0.2  # 35% randomness assigned to the size of the functioning windows
)

# Set the functioning windows
Lamp.windows(
    [420, 540], random_var_w=0.35  # Intensive duty: 7:00 AM to 9:00 AM
)

# %%
# Initialize the UseCase object
uc = UseCase(
    users=User_list,  # List of all users (e.g., CS for Cold Storage)
    parallel_processing=False,  # Set to True if you want to enable parallel processing
)

# Initialize the UseCase with optional parameters
uc.initialize()  # Adjust peak enlargement if needed

# Generate daily load profiles for the entire year
Profiles_list = uc.generate_daily_load_profiles(flat=False)

# Format the profiles for plotting
Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(Profiles_list)

# Plot the yearly profile as a time series
pp.Profile_series_plot(Profiles_series)

# If more than one daily profile is generated, also plot cloud plots
if len(Profiles_list) > 1:
    pp.Profile_cloud_plot(Profiles_list, Profiles_avg)

# %%
# Assuming Profiles_series contains minute-level data for a year (365 days)
time_index = pd.date_range(start="2025-01-01", end="2025-12-31 23:59:00", freq="T")  # Minute-level frequency
Profiles_series = pd.Series(Profiles_series, index=time_index)

# Calculate yearly consumption (kWh)
yearly_consumption = Profiles_series.sum() / (1000 * 60)  # Convert from W-min to kWh
print(f"Yearly Consumption: {yearly_consumption:.2f} kWh")

# Resample the data to monthly sums (kWh)
monthly_consumption = Profiles_series.resample('M').sum() / (1000 * 60)  # Convert from W-min to kWh

# Print monthly consumption
print("Monthly Consumption (kWh):")
print(monthly_consumption)

# Plot monthly consumption
monthly_consumption.plot(kind='bar', title="Monthly Energy Consumption", ylabel="Energy (kWh)", xlabel="Month")
plt.show()

# %%
#Profiles_series.to_csv("load_profile_harvest.csv", header=True)
# %%
