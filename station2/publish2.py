import os
import time as t
import json
from dotenv import load_dotenv
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

load_dotenv()

# Define AWS parameters to connect via MQTT
ENDPOINT = os.getenv("ENDPOINT")
PATH_TO_CERT = os.getenv("CERTIFICATE_2")
PATH_TO_KEY = os.getenv("PRIVATE_KEY_2")
PATH_TO_ROOT = os.getenv("ROOT_2")

# Parameters related to the specific station
CLIENT_ID = "Air Quality Station 2"
MESSAGE = "Hello from Station Two"
TOPIC = "test/testing"
RANGE = 20

# Setting up connection with AWS IoT Core
myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

# Starting send data via MQTT
myAWSIoTMQTTClient.connect()
print('Begin Publish')
for i in range (RANGE):
    data = "{} [{}]".format(MESSAGE, i+1)
    message = {"message" : data}
    myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 1) 
    print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
    t.sleep(2)
print('Publish End')
myAWSIoTMQTTClient.disconnect()