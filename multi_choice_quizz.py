from quizz import quiz
Questions = [
    "Câu 1. Trong hệ tọa độ Oxyz, góc giữa đường thẳng Ox và đường thẳng Oy là:\nA. 0\nB. 90\nC. 45\nD. 30",
    "Câu 2. Trong hệ tọa độ Oxyz, góc giữa đường thẳng Ox và mặt phẳng (Oxyz) là:\nA. 0\nB. 90\nC. 45\nD. 30",
    "Câu 3. Trong hệ tọa độ Oxyz, cho mặt phẳng (P): 2x - y - z = 0 và (Q): x - z - 2 = 0. Góc giữa 2 mặt phẳng (P) và (Q) là:\nA. 0\nB. 90\nC. 45\n.D 30"
]

quizzes = [
    quiz(Questions[0], "B"),
    quiz(Questions[1], "A"),
    quiz(Questions[2], "D"),
]
def run_quizzes(quizzes):
    score = 0
    for quiz in quizzes:
        print(quiz.question)
        user_input = input("Hãy nhập câu trả lời: ")
        if user_input.lower() == quiz.answers.lower():
            score += 1
            print("Bạn đã trả lời đúng rồi")
        else:
            score += 0
            print("Bạn đã trả lời sai rồi.")
       
    print(f"\n ---> KẾT QUẢ: Bạn đã trả lời đúng {score}/{len(quizzes)} câu ")

run_quizzes(quizzes)