from plyer import notification
import speedtest
import math 
  
st = speedtest.Speedtest()

ds = st.download()
dsinKB = math.ceil(ds/(1024*8))
notification.notify("Download:", dsinKB, "KB/S")  

us = st.upload(pre_allocate=False)
usinKB = math.ceil(us/(1024*8))
print("Upload:", usinKB, "KB/S")

servernames =[]    
st.get_servers(servernames)  
print(st.results.ping)  
