# 다른 파일에 정의한 함수 불러오기.
import e005
from e005 import py
e005.py()

# 함수는 동시에 실행되지 않고 순서대로 실행된다 (하나씩 진행.)
# 병렬 프로그래밍 : 함수를 동시에 실행하는 것
# await fetch : 병렬 프로그래밍 명령어
def message():
    print("A")
    print("B")

message()
print("C")
message()