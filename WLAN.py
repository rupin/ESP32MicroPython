import network
import time

# Wi-Fi Credentials
SSID = "RupinJio"
PASSWORD = "123456789"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print("Connecting")
    time.sleep(1)
    pass  # Wait for connection

print(wlan.ifconfig())

10.213.136.172- IP ( Internet Protocol) Address
255.255.255.0- Subnet Mask
10.213.136.190- Router IP
10.213.136.190- Router IP Address


