'''
round -> 소수점 기능

flt = 123.567
print(flt)
print('round(flt):',round(flt))
print('round(flt,1):',round(flt,1))
print('round(flt,2):',round(flt,2))

정수형태 = 'int'
실수형태 = 'float'
문자형태 = 'str'

형변환

str() = 문자로 형변환
float() = 실수로 형변환
int() = 정수로 형변환
'1.111' 문자형태의 실수를 정수로 바꾸려면, 실수로 먼저 형변환을 시켜준 뒤 정수로 변환을 시켜준다. print(int(float('1.111')))

형변환은 미리 변환을 시켜놓은 뒤에 사용할 수 있다.
예)
name = input('이름입력 :')
age = int(input('나이입력 :'))
flt = float(input('실수입력 :'))
print(f'{name}, type:{type(name)}')
print(f'{age}, type:{type(age)}')
print(f'{flt}, type:{type(flt)}')

'''


flt = 123.567
print(flt)
print('round(flt):',round(flt))
print('round(flt,1):',round(flt,1))
print('round(flt,2):',round(flt,2))
print('\t')
print('\t')
a = (99+96+97)/3
print('Ave:',round(a,2))
print('\t')
print('\t')
b = (37/11)
print('Min:',round(b,2))
print('\t')
print('\t')
c = (260*13+500.23)/100
print('Height(m):',round(c,3))
print('\t')
print('\t')
flt = 123.123
print( flt + 20 )
st = '파'; st1 = '이썬'
print( st + st1 )
print('\t')
print('\t')
num=100
print(type(num))
print(type(1.123))
st = '안녕하세요'
print(type(st))
print(st + str(num))
print('\t')
print('\t')
su = 100
num = '100'
flt = "1.111"
print(su + int(num))
print(int(num) + float(flt))
print(num+ str(su))
print('\t')
print('\t')
num = input('수 입력 :')
print('입력 받은 수 :',num)
print('\t')
print('\t')
name = input('이름입력 :')
age = input('나이입력 :')
print(f'{name}님의 나이는 {age}살 입니다.')
print('\t')
print('\t')
print("두 수의 합을 구해줍니다!!!")
n1 = input('숫자 :')
n2 = input('숫자 :')
n3 = int(n1) + int(n2)
print('두 수의 합 :', n3)
print('{}+{}+={}'.format(n1,n2,n3))
name = input('이름입력 :')
age = int(input('나이입력 :'))
flt = float(input('실수입력 :'))
print(f'{name}, type:{type(name)}')
print(f'{age}, type:{type(age)}')
print(f'{flt}, type:{type(flt)}')

#문제풀이

print('\t')
print('\t')
crtyear = input('올해연도 :')
bthyear = input('태어난연도 :')
print('당신의 나이는 {}살 입니다.'. format(int(crtyear)-int(bthyear)))
print('\t')
print('\t')
n1 = float(input('첫 번째 물건 :'))
n2 = float(input('두 번째 물건 :'))
n3 = float(600)-n1-n2
print('현재 엘리베이터에 허용 무게는 {}kg입니다.'.format(n3))
print('\t')
print('\t')
'''
문제 풀이 해설

CrtYear = input('올해 년도 4자리 입력 :')
BthYear = input('태어난 년도 4자리 입력 :')
age = int(CrtYear) - int(BthYear)
print('나이는 {}살 입니다.'.format(age))

Cargo1 = float(input('첫 무게 입력 :'))
Cargo2 = float(input('두 무게 입력 :'))
RemainingWeight = 600 - (Cargo1+Cargo2)
print('허용 무게 :',RemainingWeight,'kg입니다.')
'''

#문제풀이


print('\t')
print('\t')
CrtHeight = int(input('키를 입력하세요?'))
AveWeight = (CrtHeight-100)*0.9
print('표준 체중은 {}입니다.'.format(AveWeight))
print('\t')
print('\t')
CH = int(input('키를 입력하세요?'))
CW = int(input('현재 체중을 입력하세요?'))
AV = (CH-100)*0.9
FR = (CW/AV)*100
print('표준 체중은 {}이고 비만도는 {}입니다.'. format(AV,round(FR,2)))
print('\t')
print('\t')
NAME = input('학생이름:')
ML = int(input('국어점수:'))
ENG = int(input('영어점수:'))
MM = int(input('수학점수:'))
TT = ML+ENG+MM
AVE = round(TT/3,2)
print('='*18+'학생정보'+'='*18)
print('이름\t국어\t영어\t수학\t합계\t평균')
print('-'*44)
print('{}\t{}\t{}\t{}\t{}\t{}'.format(NAME,ML,ENG,MM,TT,AVE))
print('\t')
print('\t')


'''
문제 풀이 해설

Height = int(input('키 입력 :'))
StandardWeight = (Height - 100)*0.9
print('표준 체중 :', StandardWeight)

Weight = int(input('체중 입력:'))
Obesity = (Weight/StandardWeight)*100
print('표준 체중 :',StandardWeight)
print('비만도 :',round(Obesity,2))

name = input('이름 입력:')
kor = int(input('국어점수:'))
eng = int(input('영어점수:'))
math = int(input('수학점수:'))
print('{:=^20}'.format('학생정보'))
print('이름\t국어\t영어\t수학\t합계\t평균')
print('-'*30)
sum_ = kor+eng+math
avg = round(sum_/3,2)
print(f'{name}\t{}kor\t{eng}\t{math}\t{sum_}\t{avg}')
'''



















