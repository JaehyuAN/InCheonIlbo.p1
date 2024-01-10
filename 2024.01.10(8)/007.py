# 1~10까지의 합계

# x=0
# for a in range(1,11):
#     x=x+a
# print(x)

# 1~10까지의 3의 배수 출력
# continue = skip 무시하고 계속 진행한다.

# for x in range(1,11):
#     if x%3!=0:
#         continue 
#     print(x)

# 1~10사이의 3의 배수의 합계

# a=0
# for x in range(1,11):
#     if x%3==0:
#         a=a+x
# print(a)

# 1~100사이의 5와 7의 공배수를 출력
# for x in range(1,101):
#     if x%5==0 and x%7==0:
#         print(x)

# 1~100사이의 3과 5의 최소공배수를 출력
# for x in range(1,101):
#     if x%3==0 and x%5==0:
#         print(x)
#         break
    
# 1~100사이의 75와 50의 공약수를 출력
# for x in range(1,101):
#     if 75%x==0 and 50%x==0:
#         print(x)

# 1~100사이의 5와 7의 배수 출력하되 공배수 제외
# for x in range(1,101):    
#     if x%5==0 and x%7!=0:
#         print(x)
#     if x%7==0 and x%5!=0:
#         print(x)

# 1~100사이의 5와 7의 배수 출력하되 공배수 제외
for x in range(1,101):
    if x%5==0 and x%7==0:
        continue
    elif x%5==0 or x%7==0:
        print(x)