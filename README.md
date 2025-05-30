# master_thesis_TRAX_Ghana
This repository contains all relevant code files for the master's thesis: Techno-Economic Analysis of a Microgrid Integrated Solar-Powered Cold Storage Systems for TRAX Ghana.
Authors: Leander Drag Eiring and Ulrik Kornelius Merok Lullau
Contact: leandere@ntnu.no/uklullau@ntnu.no

# Data Files Overview:
bolgatanga_data.dat: The Meteorological data extracted from the closest location to the site.
Full_year_average.csv: Average monthly energy consumption data for the cold storage facility, based on a weekly schedule of 1 harvest day and 6 non-harvest days.
Harvest_day.csv: Average monthly energy consumption data based on only harvest days.
Non_harvest_day.csv: Average monthly energy consumption data based on only non-harvest days.
load_profile_full_year.csv: Full year minute-based average used compatible with PVsyst simulations.

# Code Files Overview:
Economic_analysis.ipynb: Code file used for economic metric calculations and sensitivity analyses.
Load_profile_visualization.ipynb: Code file used for visualizing the load profile data.
Meteorological_data.ipynb: Code file used for visualizing the meteorological data.
RAMP_full_year_average.py: Code file created based on the repository of the open-source RAMP model for generating multi-energy loads profiles. Simulates a full year based on the average monthly energy consumption data for the cold storage facility.
RAMP_harvest_day.py: Code file created based on the repository of the open-source RAMP model for generating multi-energy loads profiles. Simulates a full year based on peak load (only harvest days) for the cold storage facility.


