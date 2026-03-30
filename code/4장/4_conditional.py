# 4_confitionals.py

temp = 16
msg = ""

if temp < 0:
    msg = 'cold'
elif temp < 10:
    msg = "mild"
elif temp < 20:
    msg = 'good'
else:
    msg = "hell"
print(msg)

# 변수 = 참값 if 조건식 else 거짓값(삼항조건문)
msg = "Let's play" if temp > 15 else "Stay home"
print(msg)