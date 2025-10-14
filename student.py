class student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def get_id(self):
        return self.id
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def show(self):
        print(f"nhập ID của bạn: {self.id}")
        print(f"Nhập tên của bạn: {self.name}")
        
        