import network
from machine import Pin
from umqtt.simple import MQTTClient

# Wi-Fi Credentials
SSID = 'RupinJio'
PASSWORD = '123456789'

# MQTT Settings
MQTT_BROKER = "test.mosquitto.org"  # Use your broker's IP
MQTT_TOPIC = "esp32/data"

# Wi-Fi Connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    pass
print("Connected to Wi-Fi:", wlan.ifconfig())

# Callback function to handle incoming messages
def on_message(topic, msg):
    led=Pin(2, Pin.OUT)
    print(f"Received message on {topic.decode()}: {msg.decode()}")
    message_text=msg.decode()
    if(message_text=="1"):
        led.value(1)
    if(message_text=="0"):
        led.value(0)



# MQTT Setup
client = MQTTClient("ESP32_Subscriber", MQTT_BROKER)
client.set_callback(on_message)
client.connect()
client.subscribe(MQTT_TOPIC)

while True:
    client.check_msg()  # Continuously check for new messages
# Write your code here :-)
