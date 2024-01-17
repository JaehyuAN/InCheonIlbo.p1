 # 숫자를 입력받아 CR(합계, 평균)UD 하는 프로그램 만들기
 # 메뉴를 띄운다 (1: 숫자추가, 2:숫자출력, 3: 합계출력, 999: 종료)
members=[]
while True:
    print('========== 메뉴 ==========')
    print('(1: 추가, 2: 합계, 3: 평균, 4: 출력, 5: 삭제, 999: 종료)')
    select = input("번호 입력:")
    if select == '1':
        members1=int(input('숫자 입력:'))
        members.append(members1)
    elif select == '2':
        print(sum(members))
    elif select == '3':
        print(sum(members)/len(members))
    elif select == '4':
        print(members)
    elif select == '5':
        want_to_delete=(int(input('삭제할 숫자 입력:')))
        if want_to_delete in members:
            members.remove(want_to_delete)
        else:
            print('없는 값입니다. 초기메뉴로 돌아갑니다.')    
    elif select == '999':
        print('이용해주셔서 감사합니다.')
        break