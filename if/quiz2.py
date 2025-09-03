
# gender = 'F'

# if gender == 'F' :
#     print("여성입니다.")
# else :
#     print("남성입니다.")


# #
# age = 55
# if age >= 65 :
#     print("무료 승차")
# else :
#     print("유료 승차")

# #
# time = 21
# if time >= 22 :
#     print("심야 요금 적용")
# else :
#     print("일반 요금 적용")


# if~elif~else
# 여러 조건을 순차적으로 검사
# 나이에 따라 다른 문장을 출력
# 조건이 여러개일 때, 앞에 있는 조건식이 참이면
# 뒤에 있는 조건식은 판단하지 않는다.
age = 25
if age < 8 :
    print('아동입니다.')
elif age < 14 :
    print('초등학생입니다.')
elif age < 20 :
    print('중고등학생입니다.')
else :
    print('성인입니다.')
