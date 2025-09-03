
num = 25
if num >= 0 :
    print("양수입니다.")


num2 = 21
if num2%3 == 0 :
    print('3의 배수입니다.')

# 디버깅 : 프로그램을 한줄씩 실행
# 중단점(breaking point)선택
# -> F5 -> 파이썬 디버거 선택 ->
# 현재활성파일 디버그 선택
# F10 한줄씩 실행
# F5 한번에 실행
age = 28       
gender = 'F'
if age >= 8 and gender == 'F' :
    print('여학생입니다.')


var = 150
if var > 100 and var < 200 :
    print("var는 100보다 크고 200보다 작다")


# 파이썬은 연속 비교 가능
i = 10
print(100 < i < 200)
