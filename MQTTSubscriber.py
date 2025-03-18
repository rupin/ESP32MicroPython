import network
from umqtt.simple import MQTTClient
# Use the URL https://testclient-cloud.mqtt.cool/ to test this code. 
# Wi-Fi Credentials
SSID = 'SSID'
PASSWORD = 'PWD'

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
    print(f"Received message on {topic.decode()}: {msg.decode()}")

# MQTT Setup
client = MQTTClient("ESP32_Subscriber", MQTT_BROKER)
client.set_callback(on_message)
client.connect()
client.subscribe(MQTT_TOPIC)

while True:
    client.check_msg()  # Continuously check for new messages
