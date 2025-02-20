import subprocess
from datetime import datetime

# code = 'gh3_extract_shots -o ./gedi_data/europe/data -r ./shapefiles/Europe.shp -l2a shot_number root_file beam channel degrade_flag delta_time surface_flag rx_assess/rx_energy -l2b l2b_quality_flag sensitivity lon_lowestmode lat_lowestmode surface_flag -l4a l2_quality_flag l4_quality_flag agbd -rh 98 -a "{\'glad_forest_loss\':[\'loss\', \'loss_sum_3x3\', \'lossyear\']}" --geo -n 10 -A 50 -D'

code = 'gh3_extract_shots -o ./gedi_data/europe/data -r ./shapefiles/Europe.shp -l2a shot_number root_file beam channel degrade_flag delta_time surface_flag rx_assess/rx_energy -l2b l2b_quality_flag sensitivity surface_flag -l4a l2_quality_flag l4_quality_flag agbd -rh 98 --geo -D'

subprocess.run(code, shell=True)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open('gedi_data/report.txt', 'a') as file:
    file.write(f"\ncode: \n{code} \nexecution finished at {now} \n")
