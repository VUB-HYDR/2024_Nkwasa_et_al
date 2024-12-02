2024_Nkwasa_et_al
Scripts used in the analyis of Nkwasa et al 2024 (CoSWAT-WQ v1.0: a high-resolution community global SWATplus water quality model)

To Install
Python scripts should be run on python3.
The model source code releases are at (https://github.com/swat-model/swatplus/releases)

For users
This repository includes the processing  scripts used in Nkwasa et al, 2024. Python is used to extract data from global datasets and generate decision tables for agricultural HRUs in the SWAT+ model 
for large scale hydrological applications.

For the python code:  
 (a) 'extract_fertilizer.py' extracts the crop data from GCCMI data and creates fertilizer applications for the required simulation period using the ISIMIP N fertilizer files (Hurtt et al., 2020)  and the P fertilizer files from (Zhang et al., 2017) 
 (b) 'eval_TN_TP_daily.py' generates TN and TP evaulation of simulated model results and GEMstat observations including KGE, nRMSE, PBIAS, NSE, R-squared. 
 (c) 'generate_annual_TN_TP_general_loads.py' extracts annual river TN and TP loads.
 (d) 'plot_all_TN_TP.py'  plots all the TN and TP concetrations for observed and simulated river stations.


Versions
Version 0.1.0 - November 2024