from student import student
sv = []
while True:
    print("""
    Hãy chọn 1 trong các số sau đây:
    0: Thoát khỏi chương trình
    1: Xem danh sách sinh viên
    2: thêm sinh viên vào danh sách
    3: sửa danh sách sinh viên 
    4: xóa sinh viên khỏi danh sách
    """)

    select = input("Hãy nhập số ở đây: ")
    if select.isdigit():
        select = int(select)
        if select == 0:
            print("Đang thoát khỏi chương trình vui lòng đợi")
            break
        elif select == 1:
            print("Đây là danh sách sinh viên hiện có: ")
            for i in sv:
                i.show()

        elif select == 2:
            id = int(input("Hãy nhập ID của sinh viên: "))
            name = input("Hãy nhập tên của sinh viên: ")
            sv.append(student(id, name))
        elif select == 3:
            id = int(input("Nhập ID của sinh viên cần sửa: "))
            for i in sv:
                i.set_name(input(" hãy sửa tên: "))
        elif select == 4:
            id = int(input("Nhập ID của sinh viên cần xóa: "))
            for i in sv:
                if i.id == id:
                    sv.remove(i)

    
    

    else:
        print("Không hợp lệ vui lòng chọn lại")

        
            
       
           

