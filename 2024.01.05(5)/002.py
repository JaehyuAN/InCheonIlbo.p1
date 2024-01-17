# jumin='980112-1111314'
# gender=jumin[7]

# 남자인지 여자인지 출력
# if gender=='1'or gender=='3':
#     print('남자')
# elif gender=='2' or gender=='4':
#     print('여자')

# # 둘 중의 하나 if문을 한줄로 바꾸는 식 >> 삼항연산자
# print('남자' if gender=='1' else "여자")

# # 복잡한 삼항연산자는 스파게티코드가 만들어진다.

# # gender가 1,3,5면 남자, 2또는4또는6이면 여자
# print('남자' if gender in ('1','3','5') else '여자')

# 주민번호로 나이 출력하기
jumin=input('주민번호를 - 양식으로 입력하시오')
THIS_YEAR=2024
born_year_jumin=jumin[0:2]
generation=jumin[7]

if generation in ('1','2'):
    generation_year=1900
elif generation in ('3','4'):
    generation_year=2000
else:
    print('다시 입력해주세요.')

born_year=generation_year+int(born_year_jumin)
nai=THIS_YEAR-born_year
print(nai)