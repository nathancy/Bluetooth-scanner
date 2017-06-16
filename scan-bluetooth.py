import subprocess 

subprocess.call("hcitool dev", shell=True)  
subprocess.call("hcitool scan", shell=True)  

