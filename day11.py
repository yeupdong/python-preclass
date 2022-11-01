'''

'set'
- 중복을 허용하지 않는다.
- 순서가 없다.
- list 처름 index로 접근이 불가하다.
- { }(중괄호) 표현방식

'''


'''
s = set('안녕녕녕하세요')
print(s)
print(type(s))



s = set([1,2,3,3,3,3,'안','안','녕'])
print(s)
#print(s[0])


#리스트 접근시, 리스트 형식으로 변환해서 접근해야한다.
li = list(s)
print(li)
print(type(li))
print(li[0])


s = {1,2,3,4}
print(s)
print( type(s) )

s.add(555)
print(s)
s.update([7,8,9])
print(s)
s.remove(555)
print(s)

print(s.issuperset({9,1,3}))

'''


'''
import random #0.0부터 0.9 사이의 랜덤숫자를 뽑아주는 기능. 

for i in range(5):
    print( random.random(), end=', ')
print()

for i in range(5):
    print( int(random.random()*3), end=', ')

for i in range(5):
    print( random.randrange(0,3), end=', ') #randrange() 0부터 #<3값까지 구해준다. 

'''



#문제 (로또 만들기, set&list)

import random

s = set()

while len(s) < 6:
    s.add( random.randrange(1,7))
print(s)



ls = list()

while len(s) < 6:
    ran = random.randrange(1,7)
    if ls.count( ran ) == 0:
        ls.append( ran )
print(ls)



#문제 (Updown게임)

import  random

best = 100
while True:
    cnt = 0
    print("1.게임시작 2.최고기록 확인 3.종료" )
    num = int( input(">>> : ") )
    if num == 1:
        com = random.randrange( 1, 100 )
        print("com : ",com)
        while True:
            cnt += 1;  user = int( input("수 입력 : " ) )
            if user == com:
                print("정답")
                if(cnt < best):
                    print("최고기록 갱신" );  best = cnt
                break
            elif user > com:  print("down" )
            else:  print("up" )
    elif num == 2:
        if best == 100:  print("게임 먼저 진행하세요" )
        else:  print("최고 기록 : ", best )
    elif num == 3:  print("게임 종료" );  break


#야구게임

import  random
best = 100
while True:
    cnt = 0
    print("1.게임시작 2.최고기록 확인 3.종료" )
    num = int( input(">>> : ") )
    if num == 1:
        cnt = 0
        com_set = set()
        while True:
            com_set.add( random.randrange( 1, 10 ) )
            if len( com_set ) == 3: break
        com = list( com_set )
        print("com : ",com)
        result = [ 0, 0, 0 ]
        while True:
            cnt += 1;
            for i in range(3):
                input_user = int( input("수 입력 : " ) )
                if input_user == com[i]:  result[0] += 1
                elif com.count( input_user ) != 0:  result[1] += 1
                else:  result[2] += 1
            print(f"{result[0]}스트라이크, {result[1]}볼, {result[2]}아웃")
            if result[0] == 3:
                break
            result = [ 0, 0, 0 ]
        if cnt < best: print(cnt,"회. 최고 기록 갱신" );  best = cnt
        else:  print(cnt,"회만에 맞추셨습니다" )
               
    elif num == 2:
        if best == 100:  print("게임 먼저 진행하세요" )
        else:  print("최고 기록 : ", best )
    elif num == 3:  print("게임 종료" );  break



