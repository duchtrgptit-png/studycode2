#🔹 Cú pháp:
def info(name, age):
    print(f'Tôi tên là {name}, tôi {age} tuổi.')
info("Đức", 18)

def sum_all(*numbers):
    total = sum(numbers)
    print(f'Tổng = {total}')
sum_all(1,3,5)