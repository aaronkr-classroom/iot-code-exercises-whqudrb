# main.py

from Device import SensorDevice, ActuatorDevice, TemperatureSensor, LightSensor

sensor = SensorDvice("temp sensor")
actuator = actuatorDevice("LED Controller")

sensor.connect()
actuator.connect()

print(sensor.status())
print(actuators.status())
print()

temp =TemperatureSensor("Temp1")
light = LightSensor("Light1")

print("Temp : ", temp.read())
print("Light : ", light.read())
