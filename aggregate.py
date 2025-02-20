import subprocess
from datetime import datetime

area = 'australia'
res = '8'
code = f'gh3_aggregate -i gedi_data/{area}/data_filtered1/ -o aggregates/{area}/filtered1/{area}_res{res} -m "[\'count\']" -r {res} -f GPKG'

subprocess.run(code, shell=True)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open('aggregates/report.txt', 'a') as file:
    file.write(f"\ncode: \n{code} \nexecution finished at {now} \n")