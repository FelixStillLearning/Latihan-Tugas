def new_game():
    """
    fungsi buat mulai game baru
    """
    tebakan = []
    tebakan_benar = 0 
    nomor_pertanyaan = 1

    for kunci in question:
        print("----------------------")
        print(kunci)
        for q in option[nomor_pertanyaan-1]:
            print(q)

        tebak = input("enter (A,B,C,D):")
        tebak = tebak.upper()
        tebakan.append(tebak)

        tebakan_benar += check_answer(question.get(kunci), tebak) # fungsi buat check answer 
        nomor_pertanyaan += 1 

    display_score(tebakan_benar, tebakan)

def check_answer(answer, tebak):
    """
    fungsi buat check jawabannya bener atau engga
    """
    if answer == tebak:
        print("correct")
        return 1
    else:
        print("wrong")
        return 0

def display_score(tebakan_benar, tebakan):
    """
    fungsi ini buat liatin score 
    """
    print("----------------------")
    print("RESULTS")
    print("----------------------")
    print("Answers: ", end="")
    for i in question:
        print(question.get(i), end=" ")
    print()

    print("tebakan: ", end="")
    for i in tebakan:
        if i == "":
            continue
        print((i), end=" ")
    print()

    score = (tebakan_benar / len(question)) * 100
    print("Your score is: " + str(score) + "%")

def play_again():
    """
    fungsi ini buat nanyain player mau main lagi atau engga
    """
    response = input("Do you want to play again? (yes or no): ")
    response = response.lower()
    if response == "yes":
        return True
    else:
        return False

question = {
    "what is the color of the sky?": "A",
    "what is the color of the sun?": "B",
    "what is the color of the grass?": "C",
    "what is the color of the moon?": "D"
}

option = [
    ["A. blue", "B. yellow", "C. green", "D.red"],
    ["A. blue", "B. yellow", "C. red", "D. green"],
    ["A. blue", "B. red", "C. green", "D. yellow"],
    ["A. red", "B. green", "C. yellow", "D. white"]
]

new_game()

while play_again():
    new_game()

print("Bye")