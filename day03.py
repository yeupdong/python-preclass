'''
// = 나누고 나서 몫
% = 나누고 나서 나머지
** = 제곱근

관계 연산자
- >, <, <=, >=, ==, !=(같지않다) (=는 항상 오른쪽에 위치)
- Ture of False

복합대입 연산자
+=, -=, *=,,,
예)
a = 10;
- a = a + 100 => a += 100
- a = a * 100 => a *= 100

논리 연산자
- True or False를 표현
- and, or ,not
- or : 값 or 값 => 하나라도 True 면 결과는 True
- and : 값 and 값 => 모두가 True 일 때 True
- not : not 값 => 결과 값을 반전시켜 준다.

제어문
- if, 반복문, break, continue

예)
if 조건식:
   print('종속문장')
   print('다음문장은 종속문장을 계속 쓰면 된다.')
   print('종속문장의 시작점은 맨 윗 문장을 기준으로 전부 다 맞춘다.') 
'''


num1 = 9; num2 = 2
print(f'{num1}/{num2} = {num1/num2}') #4.5
print(f'{num1}//{num2} = {num1//num2}') #4
print(f'{num1}%{num2} = {num1%num2}') #1
print(f'{num1}**{num2} = {num1**num2}') #81
print('\t')
print('\t')
su1 = 3.1; su2 = 3
print('su1>=su2 :', su1>=su2)
print('su1<su2 :', su1<su2)
print('su1==su2 :', su1==su2)
print('su1!=su2 :', su1!=su2)
print('\t')
print('\t')
su1 = su2 = 5
su1 += 1; print('su1 += 1 => ' , su1) # su1 = su1(5) + 1
su1 -= 1; print('su1 -= 1 => ', su1) # su1 = su1(6) - 1
su1 *= su2; print('su1 *= su2 => ', su1) # su1 = su1(5) * su2(5)
su1 //= su2; print('su1 //= su2 => ', su1) # su1 = su1(25) // su2(5)
su1 %= su2; print('su1 %= su2 => ', su1) # su1 = su1(5) % su2(5)
print('\t')
print('\t')
su1 =5; su2 = 3
su1 **= su2 # su1(125) = su1(5) ** su2(3)
su1 -= 2 # su1(123) = su1(125) - 2
print('su1 / 4 :', su1 / 4) # su1(30.75) / 4 = su1(123) / 4
print('su1 // 4 :', su1 // 4) # su1(30) // 4 = su1(123) // 4
print('su1 % 4 :', su1 % 4) # su1(3) % 4 = su1(123) % 4
print('\t')
print('\t')
print(False or False)
print((10>20) or (10%2 == 0))
print(False and True)
print(True and True)
print('\t')
print('\t')
a = 100
10<20 and 10<30 #10<20<30 을 표현하는 방법
print(a>10 and a%2==0) # 10보다 크고 2로 나누었을 때 나머지가 0인 숫자(짝수). 
print(not True)
print(not False)
print('\t')
print('\t')
print('1.쉬운게임')
print('2.어려운게임')
print('3.게임종료')
num = int(input('>>>> :'))
if num == 1:
    print('쉬운 게임이 실행 됩니다.')
    print('다음문장은 종속문장을 계속 쓰면 된다.')
if num == 2:
    print('어려운 게임이 실행 됩니다.')
if num == 3:
    print('게임을 종료 합니다.')

print('\t')
print('\t')
num1 = 10; num2 =5
if num1 > num2:
    print('True인 경우 실행')
print('다음 문장 실행')
print('\t')
print('\t')

#문제

num = int(input('>>>> :'))
if num % 3 == 0:
    print('출력')
print('\t')
print('\t')
num1 = int(input('>>>> :'))
if num1 % 2 == 0:
    print('출력')
if num1 % 2 != 0:
    print('출력이 불가합니다.')
print('\t')
print('\t')

'''
풀이

num = int(input('수 입력 :'))
if num % 3 == 0 :
   print(num,'은 3의 배수')
if num % 2 == 0:
   print(num,'은 짝수')
if num % 2 != 0:
   print(num,'은 홀수')
    
num1 = int(input('큰 수 비교 수 입력'))
num2 = int(input('큰 수 비교 수 입력'))
if num1 > num2:
   print(num1, '큰 수')
if num2 > num1:
   print(num2, '큰 수')

or

if num1 > num2:
   max_ = num1
if num2 > num1:
   max_ = num2
print(max_, '큰 수')

num1 = int(input('절대값 수 입력'))
if num1 > 0:
   print(num1, '의 절대값은 :', num1)
if num1 < 0:
   print(num1, '의 절대값은 :', num1 * -1)
'''

# 문제

num = int(input('숫자 입력:'))
if num % 7 == 0:
   print('일요일')
if num % 7 == 1:
   print('월요일')
if num % 7 == 2:
   print('화요일')
if num % 7 == 3:
   print('수요일')
if num % 7 == 4:
   print('목요일')
if num % 7 == 5:
   print('금요일')
if num % 7 == 6:
   print('토요일')
print('\t')
print('\t')
num1 = int(input('첫번째 숫자'))
num2 = int(input('두번째 숫자'))
num3 = int(input('세번째 숫자'))
if num1 > num2:
    max_ = num1
if num2 > num1:
    max_ = num2
if num2 > num3:
    max_ = num2
if num3 > num2:
    max_ = num3
if num1 > num3:
    max_ = num1
if num3 > num1:
    max_ = num3
print(max_, '큰 수')
print('\t')
print('\t')
num1 = int(input('첫번째 숫자'))
num2 = int(input('두번째 숫자'))
if num1 > num2:
    max_ = num1
if num2 > num1:
    max_ = num2
if max_ % 2 == 0:
    print('출력')
print('\t')
print('\t')
num1 = int(input('첫번째 숫자'))
num2 = int(input('두번째 숫자'))
num3 = num1+num2
if num3 % 2 == 0 and num3 % 3 == 0:
    print('출력')

'''
풀이

num = int(input('숫자 입력:'))
if num % 7 == 0:
   print(num, ':일요일')
if num % 7 == 1:
   print(num, ':월요일')
if num % 7 == 2:
   print(num, ':화요일')
if num % 7 == 3:
   print(num, ':수요일')
if num % 7 == 4:
   print(num, ':목요일')
if num % 7 == 5:
   print(num, ':금요일')
if num % 7 == 6:
   print(num, ':토요일')


num1 = int(input('첫번째 숫자'))
num2 = int(input('두번째 숫자'))
num3 = int(input('세번째 숫자'))
if num1 > num2 and num1 > num3:
   print(n1, ':가장 큰 수')
if num2 > num1 and num2 > num3:
   print(n2, ':가장 큰 수')
if num3 > num1 and num3 > num2:
   print(n3, ':가장 큰 수')


num1 = int(input('첫번째 숫자'))
num2 = int(input('두번째 숫자'))
if num1 > num2 and n1 % 2 == 0:
   print(n1, '은 크며 짝수다.')
if num2 > num1 and n2 % 2 == 0
   print(n2, '은 크며 짝수다.')


num1 = int(input('첫번째 숫자'))
num2 = int(input('두번째 숫자'))
num3 = num1+num2
if num3 % 2 == 0 and num3 % 3 == 0:
   print(num3, '는 짝수며 3의 배수다.')

or

if num3 % 6 == 0
   print(num3, '은 짝수며 3의 배수다.')
