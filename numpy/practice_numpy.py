import numpy as np

test_array = np.array(([1,2,3,4],[1,2,3,4],[1,2,3,4]), float)
print(test_array)
"""
print(test_array)
print(type(test_array)) # test_array 변수의 type 출력
print(test_array.dtype) # test_array 내부 원소들의 type 출력
print(test_array.shape)
"""


"""
new_array = test_array.reshape(12,) # 3 * 4 matrix 8 * 1로 reshape

new_array2 = test_array.reshape(-1,) # 값들을 알아서 지정
new_array3 = test_array.reshape(-1,2) # n * 2 matrix를 만들건데 n은 알아서 지정

print(new_array)
print(new_array2)
print(new_array3)

new_array_flat = test_array.flatten() # test_array에 있는 원소들을 하나로 쭉 펴서 사용함

print(new_array_flat) 
"""

"""
print(test_array[:,2:]) # 세로는 전체, 가로는 index 2부터 끝까지
print(test_array[:,1:3]) # 세로는 전체, 가로는 index 1~3까지 출력

print(test_array[:,::2]) # 세로는 전체, 가로는 전체에서 2칸씩
print(test_array[::2,::3]) # 가로는 전체에서 2카씩, 세로는 전체에서 3칸씩
"""

"""
# shape는 tuple 형식으로 적어줘야함
print(np.arange(30)) # 0 ~ 30 까지의 배열 생성
print(np.arange(0,30,0.5)) # 0 ~ 30 까지 0.5 step으로 배열 생성
print(np.zeros(shape=(2,5), dtype=np.float)) # 0으로 가득찬 2*5 matrix 생성
print(np.ones_like(test_array)) # test_array와 같은 모양으로 1로 만듬
"""

"""
print(np.random.uniform(0,1,10)) # 균등 분포
print(np.random.normal(0,1,10)) # w정규분포
"""

"""
# (a,b,c)라는 numpy array가 있다면
# axis 0, 1, 2는 a축, b축, c축이 됨
# (b,c)에서 axis = 0은 b를 의미하고 이것은 세로를 의미
# (b,c)에서 axis = 1은 c축을 의미하고 이것은 가로를 의미
print(test_array.sum(axis=1)) # 가로
print(test_array.sum(axis=0)) # 세로
"""

"""
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.vstack((a,b))) # vertical 
print(np.hstack((a,b))) # horigental
"""

"""
print(test_array + test_array) # 원소들 끼리 합
print(test_array - test_array) # 원소들 끼리 차
print(test_array * test_array) # 원소들 끼리 곱 element wise
print(test_array * 3)          # 원소곱
print(np.dot(test_array, test_array.T)) # 행렬곱
"""



# ALL은 전체, Any는 하나
a = np.arange(10)

print(a<4) # a 원소들 각각 4보다 작은지 비교하고 boolean list로 나옴
print(np.any(a>4)) # a중에 하나라도 true면 true
print(np.all(a>5)) # a 모두가 true 여야 true