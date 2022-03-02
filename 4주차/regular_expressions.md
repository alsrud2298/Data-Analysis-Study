## 정규 표현식
---
- 복잡한 문자열 처리할 때 사용하는 기법

### 메타문자 
- 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자

### 문자 클래스 []
- [abc] : a,b,c 중 한 개의 문자와 매치
- [0-5] == [012345]
- ^ : not 의미
- \d : 숫자와 매치 [0-9]
- \D : 숫자 아닌 것과 매치 [^0-9]
- \s : whitespace 문자와 매치 [ \t\n\r\f\v]
- \S : whitespace 문자가 이닌 것과 매치
- \w : 문자 + 숫자와 매치 [a-zA-Z0-9_]
- \W : 문자 + 숫자가 아닌 문자와 매치

### Dot(.)
- a.b : a + 모든문자 + b
- a[.]b : a + . + b

### 반복(*)
- * : 바로 앞의 문자가 0부터 무한대로 반복 가능
- ca*t → ct, cat, caaat 모두 매치

### 반복 (+)
- 최소 1번 이상 반복될 때 사용
-ca+t → ct 는 매치 X

### 반복({m,m}, ?)
- {m,n} : 반복 횟수 고정 / m부터 n까지 / m 또는 n 생략 가능
- {1,} == +
- {0,} == *
- ca{2}t : c + aa + t 만 매치 ! 
- ? == {0,1}
- ab?c : a + b(있어도 되고 없어도 됨) + c
→ ac , abc 매치 ! 

*가급적 *,+,? 를 사용하는게 좋음 !*

### re 모듈
- 파이썬 기본 라이브러리
```python
import re
p = re.compile('ab*')
```
- 패턴 : 정규식을 컴파일한 결과

### 정규식 이용한 문자열 검색
- 컴파일된 패턴 객체가 제공하는 메서드
1. match() : 문자열 처음부터 정규식과 매치되는지 조사
2. search() : 문자열 전체 검색하여 정규식과 매치되는지 조사
3. findall() : 정규식과 매치되는 모든 문자열 리스트로 반환
4. finditer() : 정규식과 매치되는 모든 문자열 반복 가능한 객체로 반환
- match 객체 : 정규식 검색 결과로 돌려주는 객체

```python
# 패턴 생성
import re
p = re.compile('[a-z]+')

# match
>>> m = p.match("python")
>>> print(m)
<re.Match object; span=(0, 6), match='python'> # match 객체 반환
# match되지 않았을 시, None 반환

# 일반적 사용 흐름
p = re.compile(정규표현식)
m = p.match( 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')

# search : 문자열 전체 검색
>>> m = p.search("3 python")
>>> print(m)
<re.Match object; span=(2, 8), match='python'>

# findall : 각 단어를 정규식과 매치해 리스트로 반환
>>> result = p.findall("life is too short")
>>> print(result)
['life', 'is', 'too', 'short']

# finditer : findall과 동일하지만 그 결과로 반복 가능한 객체 반환
>>> result = p.finditer("life is too short")
>>> print(result)
<callable_iterator object at 0x01F5E390>
>>> for r in result: print(r)
...
<re.Match object; span=(0, 4), match='life'>
<re.Match object; span=(5, 7), match='is'>
<re.Match object; span=(8, 11), match='too'>
<re.Match object; span=(12, 17), match='short'>
```

### match 객체의 메서드
1. group() : 매치된 문자열 돌려줌
2. start() : 매치된 문자열 시작 위치 돌려줌
3. end() : 매치된 문자열 끝 위치 돌려줌
4. span() : 매치된 문자열 (시작,끝)
```python
>>> m = p.match("python")
>>> m.group()
'python'
>>> m.start() # match 메서드 사용 시 항상 0 ! 
0
>>> m.end()
6
>>> m.span()
(0, 6)
```

### 컴파일 옵션
- 정규식 컴파일 시 사용 가능한 옵션
- DOTALL(S) : . 이 줄바꿈 문자를 포함해 모든 문자와 매치할 수 있도록 함.
- IGNORECASE(I) : 대소문자에 관계없이 매치할 수 있도록 함.
- MULTILINE(M) : 여러줄과 매치할 수 있도록 함.
- VERBOSE(X) : verbose 모드를 사용할 수 있도록 함.

### DOTALL, S
- . 메타 문자는 줄바꿈 문자(\n)를 제외한 모든 문자와 매치됨.
- \n 문자도 포함해 매치하려면 re.DOTALL 또는 re.S 옵션 사용
```python
>>> p = re.compile('a.b', re.DOTALL)
>>> m = p.match('a\nb')
>>> print(m)
<re.Match object; span=(0, 3), match='a\nb'>
```
### VERBOSE, X
- 정규식을 주석 또는 줄 단위로 구분
- re.VERBOSE/ re.X
- 문자열에 사용된 whitespace → 컴파일 시 제거

### 백슬래시 문제
- \\ : 백슬래시 2개 사용하여 이스케이프 처리
- Raw String 규칙 : 정규식 문자열 앞에 r 문자 삽입 
ex) p = re.compile(r'\\section') = 백슬래시 2개 쓴 것과 동일 의미 

### 문자열 소비가 없는 메타문자
- 매치가 진행될 때 검색에는 포함되지만 검색 결과에서는 제외됨
- | : or 과 동일한 의미
```python
>>> p = re.compile('Hi|Hello')
>>> m = p.match('CrowHello')
>>> print(m)
<re.Match object; span=(5, 9), match='Hello'>
```
- ^ : 문자열의 맨 처음과 일치함을 의미
```python
#  Life 문자열이 처음에 온 경우에만 매치
>>> print(re.search('^Life', 'Life is too short'))
<re.Match object; span=(0, 4), match='Life'>
>>> print(re.search('^Life', 'My Life'))
None
```
- $ : 문자열의 끝과 매치함 의미
```python
# 검색할 문자열이 short로 끝난 경우에만 매치
>>> print(re.search('short$', 'Life is too short'))
<re.Match object; span=(12, 17), match='short'>
>>> print(re.search('short$', 'Life is too short, you need python'))
None
```
- \A : 문자열의 처음과 매치됨
- \Z : 문쟈열의 끝과 매치됨
- \b : 단어 구분자
```python
# whitespace로 구분된 class라는 단어와 매치
>>> p = re.compile(r'\bclass\b')
>>> print(p.search('no class at all'))  
<re.Match object; span=(3, 8), match='class'>
```
**\b 는 백스페이스를 의미하므로 단어 구분자임을 명시하기 위해서 r문자를 앞에 꼭 붙여야함**

- \B : whitespace로 구분된 단어가 아닌 경우 매치
```python
# 단어의 앞뒤에 whitespace가 하나라도 있는 경우에는 매치 안됨
>>> p = re.compile(r'\Bclass\B')
>>> print(p.search('no class at all'))  
None
>>> print(p.search('the declassified algorithm'))
<re.Match object; span=(6, 11), match='class'>
>>> print(p.search('one subclass is'))
None
```

### 그루핑
- 반복되는 문자열을 찾을 때 사용
- () 
- 매치된 문자열 중 특정 부분의 문자열만 뽑아내기 위해서 자주 사용
```python
# 이름만 뽑아내기
# 이름에 해당하는 \w+ 그룹으로 만들기
>>> p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
>>> m = p.search("park 010-1234-1234")
>>> print(m.group(1))
```
| group(인덱스) | 설명 |
|---|---:|
|group(0)|매치된 전체 문자열|
|group(1)|첫 번째 그룹에 해당되는 문자열|
|group(n)|n 번째 그룹에 해당되는 문자열|

- 그루핑 중첩도 가능함 !
```python
# 전화번호 중 국번만 뽑아내기
>>> p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
>>> m = p.search("park 010-1234-1234")
>>> print(m.group(3))
010
```

### 그루핑된 문자열 재참조
- 재참조 메타문자 \1 : 정규식 그룹 중 첫 번째 그룹
```python
# (\b\w+)\s+\1은 (그룹) + " " + 그룹과 동일한 단어와 매치됨
>>> p = re.compile(r'(\b\w+)\s+\1')
>>> p.search('Paris in the the spring').group()
'the the'
```
### 그루핑된 문자열 이름 붙이기
- 확장 구문 사용 : (?P<그룹명>...)
- 재참조 시 (?P=그룹이름) 으로 사용
```python
>>> p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
>>> m = p.search("park 010-1234-1234")
>>> print(m.group("name"))
park
```

### 전방 탐색
- 긍정형 전방 탐색((?=...)) - ... 에 해당되는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
- 부정형 전방 탐색((?!...)) - ...에 해당되는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.

### 긍정형 전방 탐색
```python
# 주소에서 http만 뽑아내기
>>> p = re.compile(".+:") # http: 까지 반환
# 긍정형 전방 탐색 사용
>>> p = re.compile(".+(?=:)")
>>> m = p.search("http://google.com")
>>> print(m.group())
http
```
### 부정형 전방 탐색
- .*[.].*$ : 파일 이름 + . + 확장자를 나타내는 정규식
```python
# bat인 파일은 제외
.*[.](?!bat$).*$
```

### 문자열 바꾸기
- sub 메서드 : 정규식과 매치되는 부분 다른 문자로 바꾸기
- subn 메서드 : sub 와 기능은 동일하지만 결과를 튜플로 반환
- 문자열 대신 첫번째 매개변수로 함수 사용도 가능함 ! 
```python
>>> p = re.compile('(blue|white|red)')
>>> p.sub('colour', 'blue socks and red shoes')
# 바꿀 문자열 , 대상 문자열
'colour socks and colour shoes'

# 바꾸기 횟수 제어 -> count 변수 추가
>>> p.sub('colour', 'blue socks and red shoes', count=1)
'colour socks and red shoes'
```

### sub 메서드 사용 시 참조 구문 사용
-  sub의 바꿀 문자열 부분에 \g<그룹이름>을 사용하면 정규식의 그룹 이름을 참조할 수 있게 된다.
- \g<1>, \g<2> 처럼 참조 번호를 사용해도 됨.
```python
>>> p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
>>> print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
010-1234-1234 park
```

### Greedy vs Non-Greedy
```python
>>> s = '<html><head><title>Title</title>'
>>> len(s)
32
>>> print(re.match('<.*>', s).span())
(0, 32)
>>> print(re.match('<.*>', s).group())
<html><head><title>Title</title>
# 매치할 수 있는 최대한의 문자열 모두 소비
```
- <html> 문자열까지만 소비하도록 막는 법
- non-greedy 문자 "?" 사용
- 가능한 한 가장 최소한의 반복 수행하도록 도와줌.
ex ) *?, +?, ??, {m,n}?
```python
>>> print(re.match('<.*?>', s).group())
<html>
```