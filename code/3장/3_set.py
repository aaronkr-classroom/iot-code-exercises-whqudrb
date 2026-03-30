# 3_set.py
# 두 집합 정의
set1 = {1,2,3,'a',"hello"}
set2 = {"hello",3,4,5,'b'}

#합집합 Union
union_set = set1 | set2

#교집합 intersection
int_set = set1 & set2

#차집합 diffrence
diff_set = set1 - set2

#대칭 차집합 symmetric_diffrence
sym_diff_set = set1 ^ set2

print(f'union : {union_set}')
print(f'intersection : {int_set}')
print(f'diffrence : {diff_set}')
print(f'symmetric_difference : {sym_diff_set}')