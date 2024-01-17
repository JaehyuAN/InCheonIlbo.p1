lang='python'
# slicing
print(lang[0])  #p
print(lang[5])  #n
print('a' in lang) #false
print('p' in lang) #true
print('P' in lang) #false

#뒤에서 slicing

print(lang[-5]) #y

string = '123456789'
# 구간 자르기        문자열[시작위치:끝위치+1]
print(lang[1:3])

# 간격을 두고 자르기 문자열[시작위치:끝위치+1:간격]
print(string[1::5])

# 짝수만 출력
print(string[1::2])