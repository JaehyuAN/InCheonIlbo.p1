members=[]
while True:
    print('=====메뉴=====')
    print('1. 숫자 추가, 2. 숫자 출력, 3. 합계, 4. 삭제, 100. 종료')
    choice=(input('번호를 입력해주세요 : '))
    if choice == '1':
        while True:
            members1=(int(input('숫자를 입력해주세요 : ')))
            members.append(members1)
            print('입력 하신 숫자가 추가되었습니다.')
            print('1. 숫자 계속 추가, 2. 초기 메뉴')
            choice2=input('번호를 입력해주세요 : ')
            if choice2=='1':
                print('계속 추가하겠습니다.')
            else:
                print('초기 메뉴로 돌아갑니다.')
                break
    elif choice == '2':
        print(f'숫자 목록은 {members} 입니다.')
        print('초기 메뉴로 돌아갑니다.')
    elif choice == '3':
        print(f'숫자들의 총 합계는 {sum(members)} 입니다.')
        print('초기 메뉴로 돌아갑니다.')
    elif choice == '4':
        while True:
            print('원하지 않을 경우 -100을 입력해주세요.')
            remove_number=int(input('삭제하고 싶은 숫자를 입력해주세요 : '))
            if remove_number in members:
                members.remove(remove_number)
                print('입력하신 숫자는 삭제되었습니다.')
                print(f'남은 숫자 목록은 {members} 입니다.')
                print('1. 숫자 계속 삭제, 2. 초기 메뉴')
                choice2=input('번호를 입력해주세요 : ')
                if choice2=='1':
                    print('계속 삭제하겠습니다.')
                else:
                    print('초기 메뉴로 돌아갑니다.')
                    break
            elif remove_number==-100:
                break
            else:
                print('입력된 숫자는 없는 숫자입니다.')
    elif choice == '100':
        print('이용해주셔서 감사합니다.')
        break
    else:
        print('다시 입력해주세요.')


