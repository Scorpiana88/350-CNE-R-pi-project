 
##  CNE 350 Final Project
##  Instructor: Justin Eliis,
##  Christiana Freeman, csfreeman@student.rtc.edu
##  with help from TJ Dewey, tjdewey@student.rtc.edu



from scapy.all import *
import json
import threading
import http.client


# gateway and variables
UBEAC_URL = 'hub.ubeac.io'
GATEWAY_URL = 'http://####'
DEVICE_FRIENDLY_NAME = 'Rpi detector 4'
SENT_INTERNAL = 10 # Sent data interval in second


## for tracking your own devices, add them to this dictionary
devices = {"00:00:00:00:00:00" : "DEVICE 1",
           "00:00:00:00:00:00" : "DEVICE 2",
           "00:00:00:00:00:00" : "DEVICE 3",}


## function puts data into uBeac sensor format
def get_sensor(id, value, type=None, unit=None, prefix=None, dt=None):
    sensor = {
        'id': id
        'data': value
    }
    return sensor
  
  
  
## function tracks WIFI packets emitted from wireless devices
def PacketHandler(pkt):
    if pkt.haslayer(Dot11):
        dot11_layer = pkt.getlayer(Dot11)
        if dot11_layer.addr2 and (dot11_layer.addr2 in devices) and (dot11_layer.addr2 not in check_devices):
            check_devices.add(dot11_layer.addr2)
            sensors_dbm.append(get_sensor(devices[dot11_layer.addr2], {"dBm Signal" : pkt[RadioTap].dBm_AntSignal}))
        
        
        
