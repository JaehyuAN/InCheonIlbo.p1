# for문

# for x in [1,2,3]:
#     print('hello') 

# 'hello' 3번 출력

# for x in range(3):
#     print('hello')

# range() : 범위를 정하는 함수 (똑같은 값을 반복해야하는 반복문에서 횟수의 범위를 지정 가능) 0부터 시작하며 (n-1)까지 n회

# for를 이용하여 0~10까지 출력

# for x in range(11):
#     print(x)

# for를 이용하여 0~10까지의 짝수를 출력

# for x in range(11):
#     if x%2==0 and x>0:
#         print(x)

# range(a,b) : a부터 시작해서 b-1까지 출력
# 1~5까지의 합
a=0
for x in range(1,6):
    a=a+x
print(a)