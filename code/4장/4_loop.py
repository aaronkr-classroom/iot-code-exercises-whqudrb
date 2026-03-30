# 4_loop.py

cars = ['Tesla', 'Hyundai', 'Kia', 'Toyota', 'Honda', 'Ford']

for car in cars:
    print(f'My car is a {car}')
    
#리스트 컴프리헨션
prices = [i**2 for i in range(1,13) if i%2==0]

for price in prices:
    print(f'It cost ${price},000')