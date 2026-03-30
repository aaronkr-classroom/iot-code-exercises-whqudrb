# 4_operators.py

a = 132
b = 45

fmt0 = '{:<10}' #변수 + 공백 10자리까지
fmt1= '0b{:08b} 0x{:02x} {:3}' # 0b 8자리 2진법, 0x 16진법 2자리, 10진법 3개

#bit &
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))

n = 30
print('-'*n)
print(fmt0.format('a&b'), fmt1.format(a&b,a&b,a&b))

#bit or
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))
print('-'*n)
print(fmt0.format('a|b'), fmt1.format(a|b,a|b,a|b))

#bit xor
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))
print('-'*n)
print(fmt0.format('a^b'), fmt1.format(a^b,a^b,a^b))

#bit not
print(fmt0.format('a'), fmt1.format(a,a,a))
print('-'*n)
print(fmt0.format('~a'), fmt1.format(~a&0xFF,~a&0xFF,~a&0xFF))

#left shift <<
print(fmt0.format('a'), fmt1.format(a,a,a))
print('-'*n)
print(fmt0.format('a<<2'), fmt1.format(a<<2&0xff,a<<2&0xFF,a<<2&0xFF))


#right shift <<
print(fmt0.format('a'), fmt1.format(a,a,a))
print('-'*n)
print(fmt0.format('a>>2'), fmt1.format(a>>2&0xff,a>>2&0xFF,a>>2&0xFF))