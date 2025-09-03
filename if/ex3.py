# 조건문 만들기

# 조건은 날씨
weather = '비' # 맑음, 비, 눈

# 조건을 만족하면 if 블록을 수행
# if weather == '비' :
#     print("우산을 가져간다")

# if~else
# 조건을 만족하면 if 블록, 아니면 else 블록이 수행
# if weather == '비' :
#     print("우산을 가져간다")
# else :
#     print('우산을 가져가지 않는다.')


# if~elif~else
# 여러 조건을 순차적으로 검사
if weather == '비' :
    print("우산을 가져간다")
elif weather == '눈' :
    print('장화를 신는다.')
else :
    print('우산을 가져가지 않는다.')