# 리스트 형태
total_list = []

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문": question, "답변": ""})
        # 온전한 딕셔너리를 만든 뒤 total에 추가함


for i in total_list:
    print(i["질문"])
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer  # 변수 answer을 "답변"이라는 key에 value로 저장함
print(total_list)
