import subprocess
import re

from array import *

namearr = ['North CA', 'North Virginia','Ireland','Oregon','Frankfurt','London','GovCloud','Ohio','Central','Tokyo','Seoul','Singapore','Sydney','Mumbai','Sao Paulo']
myarr = ['50.18.56.1', '34.192.0.54','34.248.60.213','35.160.63.253','35.156.63.252','52.56.34.0','52.222.9.163','52.14.64.0','52.60.50.0','13.112.63.251','52.78.63.252','46.51.216.14','13.54.63.252','35.154.63.252','52.67.255.254']
pf = {}

j=0
for i in myarr:

    host = i
    ping = subprocess.Popen(
        ["ping", "-n", "3", host],
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    out, error = ping.communicate()
    responsetime = re.findall(' Average = (\d+)ms', str(out))
    numval = responsetime[0]
    pf[j]=(namearr[j],int(numval))
    j=j+1



spf = sorted(pf.items(), key=lambda pf: pf[1][1])

print("Sorted List")
for m in spf:
    print(m)