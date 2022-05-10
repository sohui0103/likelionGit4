import random
import time

menu = ["된장찌개", "피자", "제육볶음", "짜장면"]

while True:
    print(menu)
    item = input("음식을 추가해주세요 : ")
    if (item == "q"):
        break
    else:
        menu.append(item)

print(menu)
set_menu = set(menu)

while True:
    print(set_menu)
    item = input("음식을 삭제해주세요 : ")
    if (item == "q"):
        break
    else:
        set_menu = set_menu - set([item])

# 음식 선택하기
print(set_menu, "중에서 선택합니다")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

print(random.choice(list(set_menu)))
