from os import sep
import pandas as pd
from pandas import Series, DataFrame

data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'

"""
df_data = pd.read_csv(data_url, sep="\s+",header=None)

print(df_data.head()) # 상위 5개의 데이터 호출

df_data.columns = ["CRIM",
                    "ZN",
                    "INDUS",
                    "CHAS",
                    "NOX",
                    "RM",
                    "AGE",
                    "DIS",
                    "RAD",
                    "TAX",
                    "PTRATIO",
                    "B",
                    "LSTAT",
                    "MEDV"] # columns index 설정

print(df_data.head()) # index 설정된 상위 5개 데이터 호출
"""

"""
list_data = [1.0,2.0,3.0,4.0,5.0]
list_name = ["a","b","c","d","e"]


example_obj = Series(data=list_data, index=list_name) # list data 중 list_name으로 indexing 하여 생성
print(example_obj.index)
print(example_obj.values)
print(type(example_obj))
print(example_obj)

example_obj = example_obj.astype(int) # data type 변형 float -> int

print(example_obj)
"""

"""
dict_data = {"a":1,"b":2,"c":3,"d":4,"e":5}
indexes = ["a","b","c","d","e","f","g","h"]

example_obj = Series(dict_data, index=indexes)
print(example_obj) # index 값을 기준으로 series를 생성
"""

"""
df_data = pd.read_csv(data_url, sep="\s+",header=None)

df_data.columns = ["CRIM",
                    "ZN",
                    "INDUS",
                    "CHAS",
                    "NOX",
                    "RM",
                    "AGE",
                    "DIS",
                    "RAD",
                    "TAX",
                    "PTRATIO",
                    "B",
                    "LSTAT",
                    "MEDV"] # columns index 설정

print(df_data[["CRIM","ZN","INDUS"]].head(3)) # "CRIM","ZN","INDUS" column의 데이터 상위 3개 출력

print(df_data[:3]) # df_data의 index 0, 1, 2 3개를 출력 row를 기준으로 표시
print(df_data["CRIM"][:3]) # column 이름과 함께 row index 사용시 해당 column만 표시

# 데이터를 가져오는 3가지 방식
# 1) col 이름 지정후 index
# 2) loc
# 3) iloc

df_data.reset_index(inplace=True) # 일반적으로 Dataframe의 함수는 원본을 바꾸지 않지만 inplace를 true로 해주면 원본이 바뀜

print(df_data)
"""

import numpy as np
test1 = Series(np.arange(10)) # test1 에 0~10까지 Series 생성
print(test1.head(5))
print(test1.map(lambda x: x**2).head()) # lambda를 활용해 각 원소들을 제곱함