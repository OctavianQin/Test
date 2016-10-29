import urllib.request
import re
dStr = urllib.request.urlopen('https://hk.finance.yahoo.com/q/cp?s=%5EDJI').read()
getdStr=dStr.decode('utf-8', 'ignore') 
#?python 3?urllib.read()??bytes????str???????dStr???str
#convert dStr into str, urllib.read() returns bytes objects instead of str
m = re.findall('<tr><td class="yfnc_tabledata1"><b><a href=".*?">(.*?)</a></b></td><td class="yfnc_tabledata1">(.*?)</td>.*?<b>(.*?)</b>.*?</tr>', getdStr)
for i in range(len(m)):
    a = m[i]
    print(a[0],a[2])
print (len(m))