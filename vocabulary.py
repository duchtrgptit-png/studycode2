class vocabulary:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def get_word(self):
        return self.word
    def set_meaning(self, meaning):
        self.meaning = meaning
    def get_meaning(self):
        return self.meaning
    
    def show(self):
        print(f"Hãy nhập tên từ: {self.word}")
        print(f"Hãy nhập nghĩa của từ:{self.meaning}")