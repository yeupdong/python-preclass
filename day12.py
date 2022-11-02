'''
튜플 (Tuple)

- 중복된 데이터를 가질 수 없다.
- 데이터 변경이 불가능
- index로 접근 가능하다.
- 소괄호가 있으면 튜플로 보면 된다.

'''

tp = (10,20,30)
print('tp:', tp)
print('tp[0] :', tp[0])
print('type(tp) :', type(tp) )
print('len(tp) :', len(tp) )

#tp[0] = 1000 개별적으로 값을 바꿀 수 없다.

tp = (111,222,333,444)
print('tp :', tp)

print('='*30)

tp = (10)
print(type(tp))

tp = (10,)
print(type(tp))

tp = 10,
print(type(tp))


'''
packing : 압축 (여러개의 값을 가지고 있다)
unpacking : 하나의 값을 여러개로 나누는 것.
'''

print('='*30)

pack = 1,2, "패킹"
print('패킹 :', pack)
print(type(pack))
a,b,c = pack
print(a,b,c)
a, *b = pack
print(a,b)
print(type(a), type(b))

print('='*30)

pack = 10,20,10,10,30
print(pack.count(10))
print(pack.index(20))

print('='*30)
str_ = 'have a nice day'
print(str_[0])
print(str_[1])

li = [1,2,3,4]
print( li[-1])
print( str_[-1] )

print('='*30)

for i in range( len(str_) ):
    print( str_[i], end=' ')
print()
for i in str_:
    print(i, end=' ')
print()

print(str_[7:11])

print('='*30)

str_ = 'Python test. 그리고 programming 할만하다 ^^'

print(str_)
print('upper :', str_.upper() )#대문자 변환
print('lower :', str_.lower() )#소문자 변환
print('swapcase :', str_.swapcase() )#대소문자 변환
print('title :', str_.title() )#첫 글자 대문자 (나머지 소문자 변환)

print('='*30)

#문제

a = 'NevEr-eVer 110gIVe up'

#print(a.lower())
print(a.title())

a1 = a.title()
print(a)
print(a1)

print('='*30)

a = 'Have a nice day'
print( a.count('a'))
print( a.count('day'))
print( a.count('dak'))

print('='*30)

print( a.startswith('Ha') )
print( a.startswith('ha') )

print('='*30)

print( a.endswith('ay'))
print( a.endswith('dday'))

print('='*30)

#문제

st = "It is a fun python class"

print( len(st) )
print( st.count('a'))
print( st.count('s'))

print('='*30)

st = 'Have a nice day'
print( st.find('a'))
print( st.find('a',2) )
print( st.find('a',6) )
print( st.find('a',14) )


c = st.find('a',2)
print(c)
c = st.find('a',c+1)
print(c)


print('='*30)

#문제

st = 'Have a nice day Have a nice day Have a nice day'
print( 'a 개수 :', st.count('a'))
cnt = 0
ls = list()
while True:
    cnt = st.find('a', cnt)
    if cnt != -1:
        ls.append(cnt)
    else:
        break
    cnt += 1
print( 'index :', ls)


li = ['AbCe test123','.acd efg','a123 TEST 123','123 TEst']

for i in li:
    lo = i.lower()
    if lo.startswith('ab') or lo.endswith('test'):
        print(i)

print('='*30)

st = '2015/04/02'

print(st)
st1 = st.replace('/','.')
print(st)
print(st1)
print(st.replace(st[0:4],'2022'))

print('='*30)

#문제

st = '''
김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018년 05월 14일
'''

st = st.replace('-',':')
print(st)


i = 0
for k in range( st.count(':')):
    i = st.find(':',i+1)
    st = st.replace(st[i+1:i+5],'1999')
print(st)














