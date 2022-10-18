#print(20+200)
print('Hello')
print('Hello'); print('Hello')
print('\t')
print('\t')
'''
ESC문자
- 문자열 안에서 특수한 동작을 해주는 것.
- \n : 엔터값과 비슷하다.
- \t : tab크기(스페이스 8칸 정도)만큼 커서를 오른쪽으로 이동.
- \" : 큰 따옴표를 출력
- \' : 작은 따옴표를 출력
- \\ : \를 표현
'''
print('\t')
print('\t')
print( "안\n녕\n하\n세\n요" )
print( 'Have\t a\t good\t time' )
print( '1234567\t1\t12345678\t55')
print('\t')
print('\t')
print(" '안녕 ''' ") #큰 따옴표 사이 작은 따옴표는 괜찮다.
print(" \"안녕\" ") #큰 따옴표 사이 큰 따옴표는 문법에 오류를 초래한다. 그래서 \"를 사용한다. 작은 따옴표도 동일하다. 
print('\t')
print('\t')
print('\t\t####회비정보####')
print('================================================')
print('이름\t\t나이\t전화번호\t회비')
print('================================================')
print('홍길동\t\t"15"\t"010-123-1234"\t\\20,000')
print('임꺽정\t\t"20"\t"010-234-2345"\t\\30,000')
print('김말이\t\t"28"\t"010-345-3456"\t\\50,000')
print('------------------------------------------------')
print('총합계\t\t\t\t\t\\100,000')
print('================================================')
print('\t')
print('\t')
print('안녕',123+123)
print('안녕'+'하세요')
print('100'+'100')
print('\t')
print('\t')
print('12 + 54 = 66 입니다')
print('268 - 42 = 226 입니다')
print('2 * 23 = 46 입니다')
print('120 / 3 = 40.0 입니다')
print('\t')
print('\t')
print('12 + 54 =', 12+54, '입니다')
print('268 - 42 =', 268-42, '입니다')
print('2 * 23 = ', 2*23, '입니다')
print('120 / 3 = ', 120/3, '입니다')
print('\t')
print('\t')
print(f'12+54={12+54} 입니다')
print('12+54={} 입니다.'.format(12+54))
print('{2} + {1} = {0}' .format(10,20,30))
print('\t')
print('\t')
print("{:,}" .format(10000000000))
print('\t')
print('\t')
print("{:<10}왼쪽정렬{:0<10}". format('안녕', '하세요'))
print("{:>10}오른쪽정렬{:8>10}". format('안녕', '하세요'))
print("{:^10}가운데정렬{:8^10}". format('안녕', '하세요'))
print('\t')
print('\t')
'''
변수
- 데이터를 저장하기 위한 공간
- 데이터는 언제든지 변경 가능
변수 작명 규칙
- 의미를 부여해서 만든다
- 키워드(예약어)는 사용 불가 예) print, format
- 한글로도 만들 수 있으나 영어로 만들자
- 'a = b' b라는 값을 a라는 위치에 저장
'''
print('\t')
print('\t')
num = 1000
print( num, '입니다' )
print( f'저장값 {num} 입니다')
print( '저장값 {} 입니다' .format(num))
print('\t')
print('\t')
num = 5
print('변경후 :', num)
print('\t')
print('\t')
num = num + 100
print('연산 후 :', num)
print('\t')
print('\t')
num1 = 5
num2 = 10
sum_ = num1 + num2
print('n1 :', num1)
print('n2 :', num2)
print('sum :', sum_)
print('\t')
print('\t')
num1 = 10
num2 = 20
print('\t---출럭결과---')
print('num1(',num1,')+num2(',num2,') =', num1+num2)
print(f'num1({num1}) + num2({num2})={num1+num2}')
