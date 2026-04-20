import lib.room_sensor as room_sensor

lst = []
status = []

lst.append(room_sensor.RoomSensor("kitchen", 22, 50, 150))
lst.append(room_sensor.RoomSensor("bedroom", 28, 70, 300))
lst.append(room_sensor.RoomSensor("balcony", 18, 30, 100))

for i in range(0,len(lst)):
    lst[i].show_info()
    print("Comfort Level :", lst[i].comfort_level())
    status.append(lst[i].comfort_level())
    print("Light Status :", lst[i].light_status())
    print()


print("Comfortable :", status.count("Comfortable"))
print("Warning :", status.count("Warning"))
print("Normal :", status.count("Normal"))