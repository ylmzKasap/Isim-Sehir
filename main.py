import os

from tablemaker import table_it
import playerclass

players = []
gameCategories = []
playerNumber, categoryNumber = 1, 1
letters = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't',
           'u', 'ü', 'v', 'y', 'z']


print('\nİsim şehir oyununa hoş geldiniz.\n', end=' ')

"""
while True:
    print(f"\n{playerNumber}. oyuncunun ismini yazın."
          + " | '-' son kişiyi siler. 'q' isim sorgusunu bitirir.")
    name = input().title()

    if name in players:
        os.system('cls')
        print('\nBu isimde bir oyuncu zaten var. Başka bir isim girin.')
        continue

    if name == 'Q':
        if len(players) >= 2:
            break
        else:
            os.system('cls')
            print('\nOyunun başlaması için en az iki kişi olmalı. Bir oyuncu ismi girin.')
            continue

    try:
        os.system('cls')
        if name == '-':
            players.pop()
            playerNumber -= 1
            print(f"\nMevcut Oyuncular: {', '.join(players)}")
            continue

    except IndexError:
        os.system('cls')
        print('\nOlmayan şeyi nasıl sileyim yahu ?!')
        continue

    players.append(name)
    playerNumber += 1
    print(f"\nMevcut Oyuncular: {', '.join(players)}")

obj = {}
for player in players:
    obj[player] = playerclass.Contender(player, gameCategories)

os.system('cls')

while True:
    print(f"\n{categoryNumber}. kategorinin ismini yazın."
          + " | '-' son kategoriyi siler. 'q' kategori sorgusunu bitirir.")
    category = input().title()

    if category in gameCategories:
        os.system('cls')
        print('\nBu isimde bir kategori zaten var. Başka bir kategori girin.')
        continue

    if category == 'Q':
        if len(gameCategories) >= 2:
            break
        else:
            os.system('cls')
            print('\nOyunun başlaması için en az iki kategori olmalı. Bir kategori ismi girin.')
            continue

    try:
        os.system('cls')
        if category == '-':
            gameCategories.pop()
            categoryNumber -= 1
            print(f"\nMevcut Kategoriler: {', '.join(gameCategories)}")
            continue

    except IndexError:
        os.system('cls')
        print('\nOlmayan şeyi nasıl sileyim yahu ?!')
        continue

    gameCategories.append(category)
    categoryNumber += 1
    print(f"\nMevcut Kategoriler: {', '.join(gameCategories)}")

categoryNumbers = {category: index for index, category in enumerate(gameCategories)}
"""

# --- Remove after testing ---


players = ['Nisa', 'Mahmut', 'Yılmaz']
gameCategories = ['İsim', 'Şehir']

obj = {}
for player in players:
    obj[player] = playerclass.Contender(player, gameCategories)


# --- Remove after testing ---

tour = 1
while True:
    # TODO Harf seç | Süre ekle

    print('\nOyun başladı! Tur sona erdiğinde enter\'a basın.')
    input()

    categoryIndex = playerIndex = 0
    categoryAnswers = [
        [[player] for player in players] for category in gameCategories]  # To make a table for each category
    goingBack = 0

    while categoryIndex < len(gameCategories):
        category = gameCategories[categoryIndex]

        if goingBack == 0:  # Player index should give the last player while going back
            playerIndex = 0
        elif goingBack == 1:
            goingBack = 0

        while playerIndex < len(players):
            player = players[playerIndex]
            print(f"\n{player} {category} için ne diyor?")
            playerAnswer = input().lower()

            if playerAnswer == '-':
                try:
                    obj[players[playerIndex-1]].remove_answer(category, tour)
                    if goingBack == 0 and len(categoryAnswers[categoryIndex][playerIndex-1]) > 1:
                        categoryAnswers[categoryIndex][playerIndex-1].pop()
                        playerIndex -= 1
                    os.system('cls')
                    table_it(categoryAnswers[categoryIndex])
                    continue
                except AttributeError:
                    if categoryIndex > 0:
                        goingBack = 1
                        break
                    elif categoryIndex == 0:
                        os.system('cls')
                        continue

            obj[player].answer(category, playerAnswer)

            os.system('cls')
            categoryAnswers[categoryIndex][playerIndex].append(playerAnswer)
            table_it(categoryAnswers[categoryIndex])
            playerIndex += 1

        if goingBack == 1:
            categoryIndex -= 1
            playerIndex = len(players) - 1
            categoryAnswers[categoryIndex][playerIndex].pop()
            os.system('cls')
            table_it(categoryAnswers[categoryIndex])
            continue
        categoryIndex += 1

    while True:
        code = input()
        try:
            print(eval(code))
        except:
            continue
