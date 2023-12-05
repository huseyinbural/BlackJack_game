import random
all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def buyukluk_checker(a, b):
    if a > b:
        print("Youuuu winnn")
    if b > a:
        print("youuuuu loooose")
    if a == b:
        print("draw")


def checker(total_comp_hand, total_player_hand):
    if total_comp_hand == 21:
        print("You loose, comp made a bj")
    elif total_player_hand == 21:
        print("You winnnnn")
    elif total_player_hand > 21:
        print("you loso")
    elif total_comp_hand > 21:
        print("yu winn")
def toplatıcı(z):
    add_player_hand = 0
    for i in z:
        add_player_hand += i
    return add_player_hand

def kontrol_as(player_hand, computer_hand):
    if all_cards[0] in player_hand:
        for i in player_hand:
            add_player_hand = 0
            add_player_hand += i
            if add_player_hand > 21:
                player_hand[player_hand.index(all_cards[0])] = 1
    if all_cards[0] in computer_hand:
        for i in computer_hand:
            add_comp_hand = 0
            add_comp_hand += i
            if add_comp_hand > 21:
                computer_hand[computer_hand.index(all_cards[0])] = 1


cond = False
while not cond:
    choice = input("do you like to play bjtype 'y ' or 'n'")
    if choice == "y":
        player_hand = [random.choice(all_cards), random.choice(all_cards)]
        computer_hand = [random.choice(all_cards), random.choice(all_cards)]
        print(f"your cards :{player_hand},current score:{toplatıcı(player_hand)}")
        print(f"computers first card:{computer_hand[0]}")
        kontrol_as(player_hand, computer_hand)

        toplam_bilgisayar_eli = toplatıcı(computer_hand)
        toplam_player_eli = toplatıcı(player_hand)
        checker(toplam_player_eli, toplam_bilgisayar_eli)
        print(cond)
        if toplam_player_eli < 21:
            devammı = input("Devam mı koç 'y',,'n'")
            toplam_bilgisayar_eli = toplatıcı(computer_hand)
            toplam_player_eli = toplatıcı(player_hand)

            if devammı == "n":
                checker(toplam_bilgisayar_eli, toplam_player_eli)
                buyukluk_checker(toplam_bilgisayar_eli, toplam_player_eli)
                cond = True
            elif devammı == "y":
                kontrol_as(player_hand, computer_hand)
                player_hand.append(random.choice(all_cards))
                computer_hand.append(random.choice(all_cards))
                toplam_bilgisayar_eli = toplatıcı(computer_hand)
                toplam_player_eli = toplatıcı(player_hand)
                checker(toplam_bilgisayar_eli, toplam_player_eli)
                print(f"your cards :{player_hand},current score:{toplatıcı(player_hand)}")
                print(f"computers first card:{computer_hand[0]},score{toplatıcı(computer_hand)}")
    if choice=="n"