# Techno-Economic Analysis of a Microgrid Integrated Solar-Powered Cold Storage Systems for TRAX Ghana
This repository contains all relevant code files for the master's thesis: Techno-Economic Analysis of a Microgrid Integrated Solar-Powered Cold Storage Systems for TRAX Ghana.
Authors: Leander Drag Eiring and Ulrik Kornelius Merok Lullau
Contact: leandere@ntnu.no/uklullau@ntnu.no

# Data Files Overview:
bolgatanga_data.dat: The Meteorological data extracted from the closest location to the site.

Full_year_average.csv: Average monthly energy consumption data for the cold storage facility, based on a weekly schedule of 1 harvest day and 6 non-harvest days.

Harvest_day.csv: Average monthly energy consumption data based on only harvest days.

Non_harvest_day.csv: Average monthly energy consumption data based on only non-harvest days.

load_profile_full_year.csv: Full year minute-based average used compatible with PVsyst simulations.

transmission_loads.csv: Writes the transmission load from Transmission_load.ipynb.

# Code Files Overview:
Economic_analysis.ipynb: Code file used for economic metric calculations and sensitivity analyses.

Load_profile_visualization.ipynb: Code file used for visualizing the load profile data.

Meteorological_data.ipynb: Code file used for visualizing the meteorological data.

RAMP_full_year_average.py: Code file created based on the repository of the open-source RAMP model for generating multi-energy loads profiles. Simulates a full year based on the average monthly energy consumption data for the cold storage facility.

RAMP_harvest_day.py: Code file created based on the repository of the open-source RAMP model for generating multi-energy loads profiles. Simulates a full year based on peak load (only harvest days) for the cold storage facility.


Operational_time.ipynb: Plot of the operational time of the compressor and temperature profile in the cold storage from 1 to 5 degrees Celcius. 

R410a_LogPH.ipynb: Plot of the air conditioning refrigeration cycle, with corresponding enthalpies and pressures. 

Thermophysical_properties: Calculates the thermophysical properties and estimates the cooling time of the different vegetables. 

Transmission_load.ipynb: Estimates the transmission load in the cold storage and writes it to the transmission_loads.csv text file. 


# RAMP Repository:
Link to the repository of the open-source RAMP model for generating multi-energy loads profiles: https://github.com/RAMP-project/RAMP


