#file: scan-bluetooth.py
#Uses hcitool to obtain device information and processes information

import subprocess 

#['sudo', 'hcitool', 'info', '64:6C:B2:95:BD:3C']

subprocess.call("hcitool dev", shell=True)  
subprocess.call("hcitool scan", shell=True)  
