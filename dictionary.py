dic = {
    "cat": "mèo",
    "dog": "chó",
    "bird": "chim"
}

while True:
    print("""
===== TỪ ĐIỂN ANH VIỆT =====
    1 - Tra từ điển
    2 - Thêm từ điển
    3 - Xóa từ điển
    4 - Thoát chương trình
""")
    
    select = input("Hãy nhập số từ (1-4) để bắt đầu chương trình: ")
    if select.isdigit():
        select = int(select)
        if select == 1:
            while True:
                word = input("Hãy nhập từ cần tra: ").lower()
                print(f"từ {word} nghĩa là {dic.get(word)}")
                ques = input("bạn có muốn tiếp tục hay không(Y/N)? ").lower()
                if ques != "y":
                    break
        elif select == 2:
            while True:
                word = input("Nhập từ mà bạn muốn thêm: ")
                if word in dic:
                    print("từ này đã có trong từ điển")
                else:
                    meaning = input("nghĩa của từ: ")
                    dic[word] = meaning
                ques = input("bạn có muốn tiếp tục hay không(Y/N)? ").lower()
                if ques != "y":
                    break
        elif select == 3:
            while True:
                wordord = input("Nhập từ mà bạn muốn xóa: ")
                if word in dic:
                    del dic[word]
                ques = input("bạn có muốn tiếp tục hay không(Y/N)? ").lower()
                if ques != "y":
                    break
        elif select ==4:
            print("Đang thoát khỏi chương trình vui lòng chờ")
            exit()
                



