'''

if 조건식
   종속문장
else:
   종속문장
다음문장


if 문장이 거짓이면 else문장이 실행된다. 

elif는 if가 참이 아닐경우 실행되고 해당식은 참인지 다시 물어본다.

if 조건식
   종속문장
elif 조건식
   종속문장
else:
   종속문장
다음문장


'while'은 계속 반복된다. 정지하려면 Ctrl+C 

while True:
   print('Test1')
   print('Test2')
   print('Test3')
   
'break' = 빠져나와라.

data = '저장값 없음'
while True:
    print('='*20)
    print('1. 데이터 입력')
    print('2. 데이터 출력')
    print('3. 종료')
    print('='*20)
    num = int(input('>>> :'))
    if num == 1:
        data = input('데이터 입력:')
    elif num == 2:
        print('입력 데이터 :', data)
    else:
        print('종료합니다.')
        break

'''

#num = int(input('수 입력:'))
if num == 1:
    print('1입력')
else:
    print('그 외의 값 입력')
print('다음 문장들 실행')

#save_id = input('저장할 id 입력 :')
save_id = input('aaa')
print('인증 프로그램')
#input_id = input('비교할 id 입력 :')
input_id = input('aaa')
if save_id == input_id:
    print('인증 통과')
else:
    print('인증 실패')
print('\t')
print('\t')
num = 5
if num % 3 == 0:
    if num % 2 == 0:
        print('num 2,3의 배수 입니다.')
        print('num 짝수이며 3의 배수 입니다.')
else:
    print('num은 3의 배수가 아닙니다.')
print('\t')
print('\t')
num1 = 9
if num1 % 3 == 0:
    if num1 % 2 == 0:
        print('num1 2,3의 배수 입니다.')
        print('num1 짝수이며 3의 배수 입니다.')
    else:print('num1은 3의 배수이며 짝수는 아니다')
else:
    print('num1은 3의 배수가 아닙니다.')
print('다음 문장들 실행')
print('\t')
print('\t')

#문제

num = int(input('GByte의 값을 입력하시오 :'))
if num > 0:
    print('1.', num*(1024**3), 'Bytes')
    print('2.', num*(1024**2), 'KBytes')
    print('3.', num*1024, 'Mbytes')
    print(num,'GBytes :',num*1024**3,'bytes')
print('\t')
print('\t')

save_id = input('저장할 ID 입력')
save_pw = input('저장할 PW 입력')
input_id = input('입력할 ID 입력')
input_pw = input('입력할 PW 입력')


if save_id == input_id:
   if save_pw == input_pw:
      print('인증 통과')
   else:
      print('비밀번호가 틀렸습니다.')
else:
   print('해당 아이디가 존재하지 않습니다.')



'''
#문제 풀이

GByte = int(input('Gbyte 입력 :'))
num = int(input('1. Byte 2.KByte 3. MByte >>'))
if num == 1:
   print(GByte*1024**3)
if num == 2:
   print(GByte*1024**2)
if num == 3:
   print(GByte*1024)


save_id = input('저장할 ID 입력')
save_pw = input('저장할 PW 입력')
input_id = input('입력할 ID 입력')
input_pw = input('입력할 PW 입력')


if save_id == input_id:
   if save_pw == input_pw:
      print('인증 통과')
   else:
      print('비밀번호가 틀렸습니다.')
else:
   print('해당 아이디가 존재하지 않습니다.)

num = int(input('수 입력:'))
if num > 100:
    print('100보다 크다')
elif num > 50:
    print('50보다 크다')
elif num > 0:
    print('0보다 크다')
else:
    print('그 외의 값 입력')
print('다음 문장들 실행')
'''



#문제

name = input('이름 :')
year = input('학번 :')
kor = int(input('국어점수 :'))
eng = int(input('영어점수 :'))
math = int(input('수학점수 :'))
avg = (kor + eng + math) / 3
print('평균점수: ', round(avg,2))
if 101 > avg and avg >= 90:
    print('A')
elif avg >= 80:
    print('B')
elif avg >= 70:
    print('C')
elif avg >= 60:
    print('D')
elif avg < 60:
    print('F')
else:
    print('1~100의 값을 입력하시오.')




coffee = int(input('커피 잔 수를 입력하세요. :'))
price = coffee*2000
extra = ((coffee-10)*1500)+20000
if coffee < 10 and coffee > 0:
    print(price)
elif coffee > 10:
    print(extra)
else:
    print('주문이 잘못 되었습니다.')



  
num = int(input('숫자를 입력하세요. :'))
if num == 0:
    print('0은 3의 배수도 4의 배수도 아닙니다.')
elif num % 3 == 0 and num % 4 == 0:
    print('3의 배수이면서, 4의 배수입니다.')
elif num % 3 == 0:
    print('3의 배수 입니다.')
elif num % 4 == 0:
    print('4의 배수 입니다.')
else:
    print('3의 배수도, 4의 배수도 아닙니다.')


time = int(input('시간을 입력하세요. :'))
StdFare = 30000
ExtFare = 5000
if 30 >= time:
    print(StdFare)
elif 41 > time and time > 30:
    print(StdFare + ExtFare)
elif 51 > time and time > 40:
    print(StdFare+(2 * ExtFare))
elif 61 > time and time > 50:
    print(StdFare+(3 * ExtFare))
else:
    print('직접 계산해.')


'''
#문제 풀이

name = input('이름 입력 : ')
su = input('학번 입력 : ')

print('3과목의 성적을 입력하시오')
kor = int(input('국어 성적 입력 : '))
eng = int(input('영어 성적 입력 : '))
math = int(input('수학 성적 입력 : '))
sum_ = kor + eng + math;avr = sum_ / 3

if avr >= 90:    result = 'A'
elif avr >= 80:    result = 'B'
elif avr >= 70:    result = 'C'
elif avr >= 60:    result = 'D'
else:    result = 'FFFFFFFF'

print('============== 학생 정보 ==================')
print('이름 : ',name,'\n학번 : ',su)
print('국 영 수 의 합 :',sum_,'\n평균 : ',avr,'\n등급 :',result)


money=0
num = int(input('주문할 커피 개수 : '))
if num>10:
    money += 20000 + (num-10)*1500;
elif num>0 and num<=10:
    money = num*2000;
print(money,"원 입니다.\n");


num = int(input('정수 입력 : '))
if num==0: 
    print(num,"은(는) 3의 배수도 4의 배수도 아닙니다");
elif num%3==0 and num%4==0: 
    print(num,"은(는)3의 배수 이면서,4의 배수입니다");
elif num%3==0:
    print(num,"은(는)3의 배수 입니다");
elif num%4==0:
    print(num,"은(는)4의 배수 입니다");
else:
    print(num,"는 3의 배수도 4의 배수도 아님");

money=30000;
time = int(input("비행기 탄 시간(분): "))
time-=30
if time > 0:
   # money += (5000+((time-1)//10)*5000)
    if (time%10) == 0:
        money=money+time//10*5000
    else:
        money=money+time//10*5000+5000
print(money,"원 입니다.")
'''

data = '저장값 없음'
while True:
    print('='*20)
    print('1. 데이터 입력')
    print('2. 데이터 출력')
    print('3. 종료')
    print('='*20)
    num = int(input('>>> :'))
    if num == 1:
        data = input('데이터 입력:')
    elif num == 2:
        print('입력 데이터 :', data)
    else:
        print('종료합니다.')
        break
print('\t')
print('\t')

#문제

while True:
    print('='*30)
    print('{:^25}' .format('MENU'))
    print('1. 학생 이름 입력')
    print('2. 성적 3과목(국, 영, 수) 입력')
    print('3. 학생 이름 출력')
    print('4. 합계 출력')
    print('5. 평균 출력')
    print('6. 종료')
    print('='*30)
    num = int(input('>>> :'))
    if num == 1:
        name = input('이름 입력:')
    elif num == 2:
        num1 = int(input('국어점수:'))
        num2 = int(input('영어점수:'))
        num3 = int(input('수학점수:'))
    elif num == 3:
        print('이름 :', name)
    elif num == 4:
        sum_ = num1+num2+num3
        print('합 :', sum_)
    elif num == 5:
        avg = sum_ / 3
        print('평균 :', round(avg,2))
    else:
        print('종료합니다.')
        break
