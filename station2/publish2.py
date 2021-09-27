import os
import sys
import time as t
import json
from dotenv import load_dotenv
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

sys.path.append(".")

load_dotenv()

# Define AWS parameters to connect via MQTT
ENDPOINT = os.getenv("ENDPOINT")
PATH_TO_CERT = os.getenv("CERTIFICATE_2")
PATH_TO_KEY = os.getenv("PRIVATE_KEY_2")
PATH_TO_ROOT = os.getenv("ROOT_2")

# Parameters related to the specific station
CLIENT_ID = "Air Quality Station 2"
LATITUDE, LONGITUDE = -23.546347, -46.627245
ADDRESS = "Parque Dom Pedro II"
TOPIC = "air-quality/station2/data"
RANGE = 10

if __name__ == "__main__":
    from data_extraction import AirQualityData
    # Setting up to get AQI data
    aqi = AirQualityData("station2/parque_dpedroii_sp_aqi.csv")
    
    # Setting up connection with AWS IoT Core
    myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
    myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
    myAWSIoTMQTTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

    # Starting send data via MQTT
    myAWSIoTMQTTClient.connect()
    print('Begin Publish')
    for i in range (RANGE):
        message = {"id" : CLIENT_ID, "address": ADDRESS,"geolocation" : [LATITUDE, LONGITUDE], "payload" : aqi.get_data()}
        myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 1) 
        print("Published: '" + json.dumps(message) + "'\n")
        t.sleep(5)
    print('Publish End')
    myAWSIoTMQTTClient.disconnect()