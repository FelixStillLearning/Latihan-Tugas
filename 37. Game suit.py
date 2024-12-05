
import random as rdm

while True:
    pilihan = ["gunting", "batu", "kertas"]
    computer = rdm.choice(pilihan)
    player = None

    while player not in pilihan:
        player = input("masukkan pilihan : ").lower()

    if player == computer:
        print("computer memilih : ", computer)
        print("player memilih : ", player)
        print("Draw")
    elif player == "batu":
        if computer == "kertas":
            print("computer memilih : ", computer)
            print("player memilih : ", player)
            print("player kalah")
        if computer == "gunting":
            print("computer memilih : ", computer)
            print("player memilih : ", player)
            print("player menang")
    elif player == "kertas":
        if computer == "batu":
            print("computer memilih : ", computer)
            print("player memilih : ", player)
            print("player menang")
        if computer == "gunting":
            print("computer memilih : ", computer)
            print("player memilih : ", player)
            print("player kalah")
    elif player == "gunting":
        if computer == "batu":
            print("computer memilih : ", computer)
            print("player memilih : ", player)
            print("player kalah")
        if computer == "kertas":
            print("computer memilih : ", computer)
            print("player memilih : ", player)
            print("player menang")

    play_again = input("apakah ingin mengulang? (ya/tidak): ").lower()

    if play_again != "ya":
        break

print("terimakasih")