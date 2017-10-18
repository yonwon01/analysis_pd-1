import pandas as pd

# Series와 dict 데이터를 활용한 DataFrame
d = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)

# dict list를 활용
d = [
    {'name': '둘리', 'age': 10, 'phone': '010-1111-1111'},
    {'name': '마이콜', 'age': 20, 'phone': '010-2222-2222'},
    {'name': '길동', 'age': 30, 'phone': '010-3333-3333'}]

df = pd.DataFrame(d)
print(df)

df2 = pd.DataFrame(d, columns=['name', 'phone'])
print(df2)

# 데이터 추가(열 추가)
df2['height'] = [150, 160, 170]
print(df2)

# 인덱스 선택
df3 = df2.set_index('name')
print(df3)

# 컬럼 선택
s = df2['name']
print(s)
print(type(s))
