# 숫자 리스트 -추가, 목록, 합계, 변경, 삭제, 함수
numbers=[]
def print_menu():
    print('====##@@ 숫자만들기 CRUD @@##====')
    print('1. 추가, 2. 목록, 3. 합계, 4. 삭제, 999.종료')

def input_select():
    return input('원하시는 번호를 입력해주세요. ')

def add_value():
    val=int(input('추가하고자 하는 숫자를 입력해주세요. '))
    numbers.append(val)
    print('입력하신 숫자가 추가되었습니다.')

def list_number():
    print(f'숫자 목록은 {numbers} 입니다.')

def plus_number():
    print(f'숫자들의 총 합은{sum(numbers)}입니다.')

def delete_number():
    del_num=int(input('삭제하고 싶은 숫자를 입력해주세요. '))
    index = 0
    for num in numbers:
        if num==del_num:
            del numbers[index]
        index=index+1
    print('입력하신 숫자가 삭제되었습니다.')
    print(f'남은 숫자 목록은{numbers} 입니다.')
    
        


def finish():
    print('이용해주셔서 감사합니다.')
    

while True:
    print_menu()
    select = input_select()
    if select =='1':
        add_value()
    elif select =='2':
        list_number()
    elif select =='3':
        plus_number()
    elif select =='4':
        delete_number()
    elif select =='999':
        finish()
        break