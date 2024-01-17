# 두 숫자를 입력받아 큰 수를 가리는 함수
def big_num(a:int,b:int):
    if a>b:
        return a
    else:
        return b
    
# 숫자를 입력받아 절대값을 계산하는 함수
def absolute(a):
    if a>0:
        return a
    else:
        return -a
    

print(absolute(0))
    