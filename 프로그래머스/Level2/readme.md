1. list 내 string -> int 등 type 변환 **list(map()) 사용**
- num_list = list(map(int, num_list))

2. String 내장함수 upper(), lower()

3. split() , join()
- split( )은 공백이 1개이건 2개이건 n개이건 상관없이 무조건 1개로 보고 처리
- split(" ")은 공백 1개, 1개를 각각의 공백으로 따로따로 처리합니다.
-- 추가적으로 split( )은 공백만 처리하는 것이 아니라 "\t" ( 탭 ), "\n" ( 엔터 ) 도 처리해줍니다.

~~~
#word1 뒤에 공백 1개, word2 뒤에 공백 2개, word3 뒤에 공백 3개, word4 뒤에 공백 4개
string = "word1 word2  word3    word4     "

print(string.split())
> ['word1', 'word2', 'word3', 'word4']
print(string.split(" "))
> ['word1', 'word2', '', 'word3', '', '', 'word4', '', '', '', '']
~~~
