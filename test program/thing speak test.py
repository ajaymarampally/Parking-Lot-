import urllib.request as urllib
import re
from time import sleep
#define send1():
    

#data=urllib.urlopen("https://api.thingspeak.com/update?api_key=EDLC8KHZZ4EV4KKZ&field1="+str(900));
#print data;

f1=0
f2=2

"""
datafromwebsite1=urllib.urlopen("https://api.thingspeak.com/update?api_key=70HJS9ECYJCTT7X2&field1=1");

datafromwebsite2=urllib.urlopen("https://api.thingspeak.com/update?api_key=70HJS9ECYJCTT7X2&field2=1");

datafromwebsite3=urllib.urlopen("https://api.thingspeak.com/update?api_key=70HJS9ECYJCTT7X2&field3=1");
#sleep(1)
"""
datafromwebsite4=urllib.urlopen("https://api.thingspeak.com/update?api_key=70HJS9ECYJCTT7X2&f"+'&field1=%s&field2=%s' % (f1, f2));


"""select=repr(datafromwebsite.read());
select=select[300:];

pick=re.search('field1":"(.+?)",',select);
if pick:
 print (pick.group(1));"""
