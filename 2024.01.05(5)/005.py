list1=[1,3,5]
for item in list1:
    print(item)

# list1의 원소를 하나씩 꺼내 item에 담는 반복문
# for x in list:
    # print(x)

# index=0
# while index<3:
#     print(list1[index])
#     index+=1

# break : 반복문을 중단한다
# while True:
#     a= int(input('값을 입력하세요.(999면 종료)'))
#     if a==999:
#         break
#     print(f'입력한 값 : {a}')
num1=[]
while True:
    print('1. 값 추가')
    print('2. 리스트 출력')
    print('3. 리스트 합계 출력')
    print('4. 리스트 평균 출력')
    print('999. 종료')
    
    select = input('번호 입력:')
    
    if select=='1':
        num=int(input('숫자 입력:'))
        num1.append(num)
    elif select=='2':
        print(num1)
    elif select=='3':
        print(sum(num1))
    elif select=='4':
        print(sum(num1)/len(num1))
    elif select=='999':
        print("감사합니다.")
        break
    else:
        print('정확한 메뉴를 선택하시요.')
