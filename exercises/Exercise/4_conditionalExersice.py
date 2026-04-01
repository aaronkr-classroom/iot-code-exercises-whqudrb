month = int(input("월을 입력하시오 : "))
day = int(input("일을 입력하시오 : "))

if(((month%3==0) and (day == 15)) or ((month%2==0) and (day==16))):
    print("그날")
elif (month==8) and (day==15):
    print("광복절")
else:
    print("평일")