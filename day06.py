'''
for i in range(0,3,1):
    for k in range(0,5,1):
        print(f'이중 for문 i:{i}, k:{k}')

#해설

for i in range(i=0,i(0)<3,i=i+1):

    for k in range(k=0,k(1)<5,k=k+1):
        print(f'이중 for문 i:{i}, k:{k}')


for i in range(0,3,1):
    print('상위 for문 실행')
    for k in range(0,5,1):
        print(f'이중 for문 i:{i}, k:{k}')
    print('상위 for문 종료')

'''

# 구구단

print('구구단을 외자')
for i in range(1,10,1):
    for k in range(1,10,1):
        print(f'{i} * {k} = {i*k}')
print('구구단 다 외웠니?')


#문제

for i in range(0,5,1):
    print(f'상위포문 {i}일 때 하위포문 : ', end=' ')
    for k in range(0,5,1):
        print(f'{i*k}', end=' ')
    print()




#문제

for i in range(0,21,5):
    for k in range(1,6,1):
        print(f'{i+k}', end=' ')
    print()

'''
#해설

for i in range(0, i(0)<5,i=i+1):
    for k in range(j=1,j<6,j=j+1):
        print(f'{j +(5*1)}', end=' ')
    print()
'''
============================================
'''
WHILE (Ctrl+C 무한반복 강제종료)

i = 0
while i<5:
    print(i, '종속문장실행')
    i+=1
print('다음 문장들 실행')





for i in range(0,5,1):
    print(f'{i} 종속문장실행')
print('다음 문장들 실행')




i=1
odd,even=0,0
while i<=10:
    if i%2 == 0:
        even += i
    else:
        odd +=i
    i+=1
print('1~10까지의 짝수 합: ', even)
print('1~10까지의 홀수 합: ', odd)

'''
============================================
'''
Break, Continue

i = 0
while True:
    if i == 3:
        print('33333333')
    print('i : ',i)
    i+= 1


i = 0
while i<5:
    if i == 3:
        print('33333333')
    print('i : ',i)
    i+= 1
print('다음 문장들 실행')


i = 0
while i<5:
    if i == 3:
        print('33333333')
        break
    print('i : ',i)
    i+= 1
print('다음 문장들 실행')
print('-'*10)

i = 0
while i<5:
    i += 1
    if i == 3:
        print('33333333')
        continue
    print('i : ',i)
print('다음 문장들 실행')

'''

#쌀 100kg
#쥐 1쌍 (2마리)
#하루 20g 씩
#10일 마다 쥐 2배씩 증가

r = 0
d = 0
while r < 100000:
    r += (2**2 * 40)
    if d == 0:
        d += 10
print()

'''
# 풀이

rice = 100000; mouse = 2; day=1
while True:
    rice = rice - mouse*20
    if day % 10 == 0:
        mouse *= 2
    #print(f"{day}일 {mouse}마리 {rice}g")
    if rice <= 0:
        break
    day += 1
print( f"{day}일 {mouse}마리")

money, j = 0,0
money = int(input("요금 투입 : "))
while True:
    print("==== 커피 자판기 ====")
    print("1.커피(200) 2.코코아(250) 3.반환 4.종료")
    j = int( input("메뉴 선택 : "))
    if j == 4:
        print("종료")
        break
    elif (j==1 and money >= 200) or (j==2 and money >= 250):
        print("맛있게 드세요")
        if j == 1:
            money -= 200
        else:
            money -= 250
    elif j == 3:
        print(money, "원 반환 금액")
        money = 0
    else:
        print("요금이 부족합니다")
'''
