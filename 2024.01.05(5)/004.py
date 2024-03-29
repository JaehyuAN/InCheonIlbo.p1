# set : 중복 불가능, 순서가 없는 list
# 정렬된것 처럼 보여도 우연
set={1,2,3,4}

# list나 tuple은 중복이 가능하고 순서가 있다.
# list는 순서 변경이 가능하고 tuple은 순서 변경이 불가능하다
# set이 처리 속도가 #(해시태그)를 사용하기에 미세하게 더 빠르다.
# 일반적으로 set은 중복을 지우기 위하여 사용
# ex)
# list=(1,2,1,3,1,4)
# set= set(list) > list=list(set) 
# list=(1,2,3,4) > 중복된 1들은 삭제된다.