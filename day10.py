'''

얕은복사

aa = [ [1,2,3,4] , [5,6,7,8] ]

a = aa[0]
a[1] = 2000

print('aa : ', aa)
print('a : ', a)


aa :  [[1, 2000, 3, 4], [5, 6, 7, 8]]
a :  [1, 2000, 3, 4]



깊은복사

aa = [ [1,2,3,4] , [5,6,7,8] ]

# a = aa[0][:]
# a = aa[0].copy()
# import copy
  a = copy.deepcopy(aa[0])
a[1] = 2000

print('aa : ', aa)
print('a : ', a)

aa :  [[1, 2, 3, 4], [5, 6, 7, 8]]
a :  [1, 2000, 3, 4]



#문제

ls_1=[]; ls_2=[]; value=1;

for i in range(3):
    for k in range(4):        #숫자를 고정으로 넣어두면 나중에 문제가 생길 수 있음. 각 리스트마다 개수가 다르면 문제가 생김. 
        ls_1.append( value )
        value += 1
    ls_2.append( ls_1 )
    ls_1=[] #ls_1값을 초기화 

for i in ls_2:
    for k in i:
        print(k,end=' ')
    print()


print('ls_2 :', ls_2)


#map

be = ['2019','12','31']
print(be)
#test = int(be[0])+100
#print(test)

#for i in range(len(be)):
#    be[i] = int(be[i])
#print(be)

be = list(map(int,be))
print(be)



be = [ ['100','222'],['200','300'] ]

print(be)

#for i in range( len(be) ):
#    for k in range( len(be[i]) ):
#        be[i][k] = int(be[i][k])


for i in range( len(be) ):
    be[i] = list( map(int, be[i]) )

print(be)


be[0][0] = be[0][0] * 100
print(be)

for i in range (len(be) ):
    be[i] = list( map(str, be[i]) )
print(be)


'''

ls = [
    [['이름'],['나이'],['주소'],['지울값'],['연봉']], #ls_1, 0~4
    [['홍길동'],['20살'],['산골자기'],['지우세요'],['5000']], #ls_2, 0~4
    [['김개똥'],['30살'],['지구촌'],['지우세요'],['4500']] #ls_3, 0~4
    ]

for i in range( len(ls) ): #0~2
    for j in range (len(ls[i])): #0~4
        if j%3==0 and j!=0:
            del(ls[i][j])
            if i != 0:
                ls[i][j][0]=str(int(int(ls[i][j][0])*1.1))

for i in ls:
    for k in i:
        print(k, end='')
    print()





