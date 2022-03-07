#!/usr/bin/env python
# coding: utf-8

# #### 1. 판다스 라이브러리
# 1. 데이터 수집, 정리에 최적화된 도구
# 2. 오픈소스
# 3. 파이썬 기반으로 배우기 쉬움
# 4. 데이터 과학의 80-90% 업무 처리 가능

# #### 2. 판다스 자료구조
# 1. 시리즈 : 1차원 배열
# 2. 데이터프레임 : 2차원 배열

# ##### 2-1. 시리즈
# - 데이터 순차적으로 나열된 1차열 배열 형태
# - 인덱스와 데이터값이 1:1 대응관계 {k:v} <=> 딕셔너리와 유사한 구조
# - 인덱스를 알면 데이터 값에 바로 접근 가능

# In[1]:


# 딕셔너리 -> 시리즈 변환
import pandas as pd

dict_data = {'a':1,'b':2,'c':3}
sr = pd.Series(dict_data)

print(type(sr))
print(sr)


# ##### 인덱스 구조
# - 자기와 짝을 이루는 데이터 값의 순서와 주소 저장
# - 인덱스를 활용해 데이터 값 탐색, 정렬, 선택, 결합 등 데이터 조작 가능
# 1. 정수형 위치 인덱스
# 2. 인덱스 이름/인덱스 라벨

# In[3]:


# 리스트 -> 시리즈 , 인덱스 별도 정의 X -> 정수형 위치 인덱스 자동 지정
list_data = ['2019-01-02',3.14,'ABC',100,True]
sr = pd.Series(list_data)
print(sr)

idx = sr.index
val = sr.values
print(idx)
print(val)


# In[7]:


# 원소 선택
# 정수형 위치 인덱스 : [] 안에 위치 나타내는 숫자 입력
# 인덱스 이름 : ['이름']
# 시리즈 원소 선택
tup_data = ('영인','2010-05-01','여',True)
sr = pd.Series(tup_data, index = ['이름','생년월일','성별','학생여부'])
print(sr)
print(sr[0])
print(sr['이름'])


# In[10]:


# 여러개의 인덱스 선택
print(sr[[1,2]])
print(sr[['생년월일','성별']])

# 인덱스 범위 지정 선택
# 정수형 위치 인덱스 -> 범위의 끝 포함 X
print(sr[1:2])
# 인덱스 이름 -> 범위의 끝 포함됨
print(sr["생년월일" : "성별"])


# ##### 2-2데이터프레임
# - 2차원 배열
# - 열은 각각 시리즈 객체 (열벡터)
# - 여러개의 열벡터들이 같은 행 인덱스를 기준으로 줄지어 결합된 2차원 행렬

# In[11]:


# 딕셔너리 -> 데이터프레임 변환
dict_data = {'c0':[1,2,3],'c1':[4,5,6],'c3':[10,11,12],'c4':[13,14,15]}
df = pd.DataFrame(dict_data)
print(type(df))
print(df)


# In[13]:


# pd.DataFrame(2차원배열, index = 행 인덱스 배열, columns = 열 이름 배열)
df = pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],
                 index = ['준서','예은'],
                 columns = ['나이','성별','학교'])
print(df)
print(df.index)
print(df.columns)


# In[16]:


# 행 인덱스, 열 이름 변경
df.index = ['학생1','학생2']
df.columns = ['연령','남녀','소속']
print(df)
print(df.index)
print(df.columns)


# In[17]:


# rename() 메소드 : 원본 객체 수정 X 새로운 데이터프레임 객체 반환
# inplace = True 옵션 사용 시 원본 객체 변경됨
df = pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],
                 index = ['준서','예은'],
                 columns = ['나이','성별','학교'])
print(df)

df.rename(columns = {'나이':'연령','성별':'남녀','학교':'소속'}, inplace = True)
df.rename(index = {'준서':'학생1','예은':'학생2'}, inplace = True)

print(df)


# In[18]:


# drop() 메소드 : 데이터프레임의 행 또는 열 삭제
# 행 삭제 : axis = 0 (디폴트), 열 삭제 : axis = 1
# 기존 객체 변경 X 새로운 객체 반환 (inplace = True : 기존 객체 직접 변경)
exam_data = {'수학':[90,80,70],'영어':[98,89,95],
             '음악':[85,95,100],'체육':[100,90,90]}
df = pd.DataFrame(exam_data, index = ['서준','우현','인아'])
print(df)

df2 = df[:] # df 복제해 df2에 저장
df2.drop('우현', inplace = True)
print(df2)

df3 = df[:]
df3.drop(['우현','인아'], axis = 0, inplace = True)
print(df3)


# In[19]:


# 열 삭제
# 반드시 axis = 1 설정
df4 = df[:]
df4.drop('수학', axis = 1, inplace = True)
print(df4)

df5 = df[:]
df5.drop(['영어','음악'], axis = 1, inplace = True)
print(df5)


# ##### 행 선택
# 1. loc
# - 탐색 대상 : 인덱스 이름
# - 범위 지정 가능 ( 범위 끝 포함 )
# 2. iloc
# - 탐색 대상 : 정수형 위치 인덱스
# - 범위 지정 가능 ( 범위 끝 제외 )

# In[20]:


label1 = df.loc['서준']
position1 = df.iloc[0]
print(label1)
print(position1)


# In[21]:


# 2개 이상의 행 선텍
label2 = df.loc[['서준','우현']]
position2 = df.iloc[[0,1]]
print(label2)
print(position2)


# In[23]:


# 슬라이싱
label3 = df.loc['서준':'우현']
position3 = df.iloc[0:1]
print(label3)
print(position3) # 0번째만 출력됨.


# ##### 열 선택
# - DataFrame객체['열이름'] 
# - DataFrame객체.열이름

# In[25]:


exam_data = {'이름':['서준','우현','인아'],
             '수학':[90,80,70],'영어':[98,89,95],
             '음악':[85,95,100],'체육':[100,90,90]}
df = pd.DataFrame(exam_data)

math1 = df['수학']
print(math1)
print(type(math1))

english = df.영어
print(english)
print(type(english))

music_gym = df[['음악','체육']]
print(music_gym)
print(type(music_gym))

math2 = df[['수학']] # 중괄호 2개 사용 시 데이터프레임으로 반환됨.
print(math2)
print(type(math2))


# In[26]:


# 범위 슬라이싱의 고급 활용
# dataFrame.iloc[시작인덱스:끝인덱스:슬라이싱간격]
print(df.iloc[::2])
print(df.iloc[0:3:2])
print(df.iloc[::-1])


# ##### 원소 선택
# - 2차원 좌표로 입력하여 원소 위치 지정

# In[27]:


# '이름' 열로 세로운 인덱스 지정
df.set_index('이름',inplace = True)
print(df)


# In[29]:


a = df.loc['서준','음악']
print(a)
b = df.iloc[0,2]
print(b)


# In[30]:


# 서준학생의 음악, 체육 점수 찾기
c = df.loc['서준',['음악','체육']]
d = df.iloc[0,[2,3]]
print(c)
print(d)
e = df.loc['서준','음악':'체육']
print(e)
f = df.iloc[0,2:]
print(f)


# In[33]:


# 서준, 우현 학생의 음악, 체육 점수 선택
g = df.loc[['서준','우현'],['음악','체육']]
h = df.iloc[[0,1],[2,3]]
i = df.loc['서준':'우현','음악':'체육']
j = df.iloc[0:2,2:]
print(g,'\n',h,'\n',i,'\n',j)


# ##### 열 추가
# - 데이터프레임의 마지막 열에 덧붙이듯 새로운 열 추가

# In[35]:


# 국어 열 추가
exam_data = {'이름':['서준','우현','인아'],
             '수학':[90,80,70],'영어':[98,89,95],
             '음악':[85,95,100],'체육':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df)

df['국어'] = 80
print(df)


# ##### 행 추가
# - loc 인덱서 사용
# - 기존 인덱스와 중복되는 경우 새로운 행 추가하지 않고 기존 행의 원소값 변경

# In[38]:


exam_data = {'이름':['서준','우현','인아'],
             '수학':[90,80,70],'영어':[98,89,95],
             '음악':[85,95,100],'체육':[100,90,90]}
df = pd.DataFrame(exam_data)
# 새로운 행 추가
df.loc[3] = 0
print(df)

df.loc[4] = ['동규',90,80,70,60]
print(df)

# 기존 행 복사해서 추가
df.loc['행5'] = df.loc[3]
print(df)


# ##### 원소 값 변경

# In[41]:


# 서준 학생의 체육 점수 변경
exam_data = {'이름':['서준','우현','인아'],
             '수학':[90,80,70],'영어':[98,89,95],
             '음악':[85,95,100],'체육':[100,90,90]}
df = pd.DataFrame(exam_data)

df.set_index('이름',inplace = True)
print(df)

df.iloc[0][3] = 80
print(df)

df.loc['서준']['체육'] = 90
print(df)

df.loc['서준','체육'] = 100
print(df)


# In[42]:


#서준학생의 음악, 체육 점수 동시에 변경
df.loc['서준',['음악','체육']] = 50
print(df)

df.loc['서준',['음악','체육']] = 100, 50
print(df)


# ##### 행,열의 위치 바꾸기
# - 기존 객체에 새로운 객체를 할당해주는 과정 필요
# - df = df.transpose()
# - df = df.T

# In[43]:


exam_data = {'이름':['서준','우현','인아'],
             '수학':[90,80,70],'영어':[98,89,95],
             '음악':[85,95,100],'체육':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df)

df = df.transpose()
print(df)

df = df.T
print(df)


# #### 3. 인덱스 활용

# ##### 특정 열을 행 인덱스로 설정
# - set_index() 사용
# - 원본 데이터프레임을 바꾸지 않고 새로운 데이터프레임 객체 반환

# In[44]:


print(df)

ndf = df.set_index(['이름'])
print(ndf)

ndf2 = ndf.set_index('음악') # 기존의 인덱스는 사라짐
print(ndf2)

ndf3 = ndf.set_index(['수학','음악'])
print(ndf3)


# ##### 행 인덱스 재배열
# - reindex()
# - 데이터프레임의 행 인덱스를 새로운 배열로 재지정
# - 새로운 데이터프레임 객체 반환
# - 기존 데이터프레임에 존재하지 않는 행 인덱스가 새롭게 추가되는 경우 그 행의 데이터값은 Nan이 됨 -> fill_value 옵션으로 원하는 값 입력

# In[46]:


dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index = ['r0','r1','r2'])
print(df)

new_index = ['r0','r1','r2','r3','r4']
ndf = df.reindex(new_index)
print(ndf)

ndf2 = df.reindex(new_index, fill_value = 0)
print(ndf2)


# ##### 행 인덱스 초기화
# - reset_index() 메소드 활용해 행 인덱스 -> 정수형 위치 인덱스로 초기화
# - 기존 행 인덱스 -> 열로 이동
# - 새로운 데이터 프레임 객체 반환

# In[47]:


dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index = ['r0','r1','r2'])
print(df)

ndf = df.reset_index()
print(ndf)


# ##### 행 인덱스 기준으로 데이터프레임 정렬
# - sort_index() 메소드 활용
# - ascending 옵션을 사용해 오름차순 또는 내림차순으로 설정
# - 새롭게 정렬된 데이터프레임 반환
# - ascending = False : 내림차순

# In[49]:


print(df)

ndf = df.sort_index(ascending = False)
print(ndf)


# ##### 특정 열 데이터 값 기준으로 데이터프레임 정렬하기
# - sort_values() 메소드 활용
# - 새롭게 정렬된 데이터프레임 객체 반환

# In[50]:


print(df)

ndf = df.sort_values(by = 'c1', ascending = False)
print(ndf)


# #### 4. 산술연산
# - 판다스 객체의 산술연산 -> 3단계 프로세스를 거침
# 1. 행/열 인덱스 기준으로 모든 원소 정렬
# 2. 동일한 위치에 있는 원소끼리 일대일 대응
# 3. 일대일 대응되는 원소끼리 연산 처리
# - 대응되는 원소가 없는 경우 NaN 처리

# ##### 4-1 시리즈 연산

# In[51]:


student1 = pd.Series({'국어':100,'영어':80,'수학':90})
print(student1)

percentage = student1 / 200
print(percentage)
print(type(percentage))


# ##### 시리즈 vs. 시리즈
# - 시리즈 사이의 사칙연산 처리
# - 모든 인덱스에 대해 같은 인덱스 가진 원소끼리 계산

# In[53]:


student1 = pd.Series({'국어':100,'영어':80,'수학':90})
student2 = pd.Series({'수학':80,'국어':90,'영어':80})

addition = student1 + student2
substraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(type(division))

result = pd.DataFrame([addition, substraction, multiplication, division],
                     index = ['덧셈','뺄셈','곱셈','나눗셈'])
print(result)


# In[54]:


# NaN값이 있는 시리즈 연산
import numpy as np

student1 = pd.Series({'국어':np.nan,'영어':80,'수학':90})
student2 = pd.Series({'수학':80,'국어':90})
addition = student1 + student2
substraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(type(division))

result = pd.DataFrame([addition, substraction, multiplication, division],
                     index = ['덧셈','뺄셈','곱셈','나눗셈'])
print(result)


# ##### 연산 메소드
# - NaN이 포함된 경우 연산 결과는 항상 NaN으로 반환됨.
# - fill_value 옵션 설정

# In[56]:


# 누락 데이터는 숫자 0 입력하기
student1 = pd.Series({'국어':np.nan,'영어':80,'수학':90})
student2 = pd.Series({'수학':80,'국어':90})

sr_add = student1.add(student2, fill_value = 0)
sr_sub = student1.sub(student2, fill_value = 0)
sr_mul = student1.mul(student2, fill_value = 0)
sr_div = student1.div(student2, fill_value = 0)

result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div],
                     index = ['덧셈','뺄셈','곱셈','나눗셈'])
print(result)


# ##### 4-2. 데이터프레임 연산
# - 행/열 인덱스 기준으로 정렬 후 일대일 대응되는 원소끼리 연산 처리

# ##### 데이터프레임 vs. 숫자
# - 기존 형태 유지한 채 원소값만 새로운 계산값으로 바뀐다.
# - 새로운 데이터프레임 객체로 반환됨.

# In[57]:


# 데이터프레임에 숫자 더하기
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]
print(df.head())
print(type(df))

addition = df + 10
print(addition.head())
print(type(addition))


# ##### 데이터프레임 vs 데이터프레임
# - 동일 위치 원소끼리 계산한 결과값 원래 위치에 다시 입력해 데이터프레임 만든다.
# - 어느 한쪽에 원소 존재하지 않거나 NaN이면 결과는 NaN으로 처리된다.

# In[58]:


# 데이터프레임끼리 더하기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]
print(df.tail())

addition = df + 10
print(addition.tail())

substraction = addition - df
print(substraction.tail())
print(type(substraction))

