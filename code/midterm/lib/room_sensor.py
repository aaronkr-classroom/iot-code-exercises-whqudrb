class RoomSensor:
    def __init__(self, name, temperature, humidity, light):
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light

    def show_info(self):
        print("Sensor : ", self.name)
        print("Temperature : ", self.temperature)
        print("Humidity : ", self.humidity)
        print("Light : ", self.light)

    def comfort_level(self):
        if (self.temperature >= 20 and self.temperature <= 26) and (self.humidity >= 40 and self.humidity <= 60):
            return "Comfortable"
        elif self.temperature >= 30 or self.humidity >= 70:
            return "Warning"
        else:
            return "Normal"
    
    def light_status(self):
        if self.light < 200:
            return "Dark"
        elif self.light >= 200:
            return "Bright"
    
