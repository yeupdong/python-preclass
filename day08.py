'''
리스트 = 하나의 자료형으로 여러개의 값을 저장할 수 있다. 

[](대괄호)로 표현되면 리스트라 생각해도 어느정도 맞다. 

각각의 값에 접근하고자 할 경우 index를 이용한다. 

Index는 0부터 시작한다.



ls = [500,200,300,400]
print( ls )
print( ls[0] )
print( ls[3] )



ls = [0,0,0]
ls[0] = int(input('값 입력 :'))
ls[1] = int(input('값 입력 :'))
ls[2] = int(input('값 입력 :'))
sum_ = ls[0] + ls[1] + ls[2]
print(ls)
print(sum_)


# len = length를 표현. 리스트 길이를 측정.

ls = [0,0,0]
sum_ = 0
print ('len :', len(ls))

for i in range(len(ls)):
    ls[i] = int(input(str(i)+'값 입력 :'))
    sum_ += ls[i]
print(ls)
print('합 :', sum_)


ls = [10,20,30,40]
print('ls :' ,ls)
print(ls[1:3])
print(ls[:2])   # ':'는 생략표시, 0~2
print(ls[1:])   # 1~끝까지
print(ls[:])    # 처음부터 끝까지







ls = [10,20,30]
arr = ls
print(id(ls))
print(id(arr))  # 두 정보가 같다는 것은 하나의 공간에 같이 창조가 되었다라는 뜻. 얕은복사
ls[1] = 12345
print(ls)
print(arr)


ls = [10,20,30]
arr = ls[:]
print(id(ls))
print(id(arr))  # 두 정보가 다르다는 것은 각각의 공간에 따로 창조가 되었다라는 뜻. 깊은복사
ls[1] = 12345
print(ls)
print(arr)


import copy # import = 다른 파일을 현제 페이지에 가지고 올 수 있는 기능.

ls = [10,20,30]
arr = copy.deepcopy(ls)
print(id(ls))
print(id(arr)) 

ls[1] = 12345
print(ls)
print(arr)


import copy


ls = [10,20,30]
arr = ls.copy()
print(id(ls))
print(id(arr))

ls[1] = 12345
print(ls)
print(arr)



ls = [10,20,30]
arr = [40,50,60]
print(ls)
print(arr)
str_ = ls + arr
print(str_)
str_ = ls*3
print(str_)



ls = [10,20,30]
arr = [40,50,60]
sum_ = [0,0,0]

for i in range(len(ls)):
    sum_[i] = ls[i]+arr[i]
print(sum_)

for i in range(len(ls)):
    sum_[i] = ls[i]*3
print(sum_)




a = 10; b = 20
print(a,b)
a, b = b, a
print(a,b)


ls = [4,8,2,7,6]

for i in range(4):
    for j in range(i+1, 5):
        if ls[i] > ls[j]:
            ls[i], ls[j]=ls[j], ls[i]
        
print(ls)


'''

mark = [82,85,76,79,96]
rank = [1,1,1,1,1]



for i in range(5):
    for j in range(5):
        if mark[i] < mark[j]:
            rank[i] += 1
            
print(mark)
print(rank)

























