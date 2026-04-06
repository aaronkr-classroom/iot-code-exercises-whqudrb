# Device.py

import random

class Device:
    '''Base IOt Device'''
    
    def __init__(self, name: str) -> None:
        self.name = name
    def connect(self) -> None:
        print(f"{self.name} connenting...")
    def status(self) -> str:
        return "unkown"

class SensorDevice(Device):
    """
    A device that reads data
    """
    def status(self) -> str:
        return "reading data..."
    
    def read(self) -> float:
        '''return sensor value'''
        return 0.0
    
class ActuatorDevice(Device):
    '''
    A Device that perform actions.
    '''
    def status(self) -> str:
        return "performing aaction..."
    
class TemperatuerSensor(SensorDevice):
    '''
    Simulated temperature sensor
    '''
    def __init__(self, name:str) -> None:
        suepr().__init__(name)
    
    def read(self) -> float:
        '''
        가짜 온도 값을 반환
        '''
        return round(random.uniform(20.0,30.0), 2)
    
class LightSensor(SensorDevice):
    '''Simulated light sensor'''
    def read(self) -> float:
     '''
     가짜 온도 값을 반환
     '''
        return round(random.uniform(0,100, 2)