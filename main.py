import os
import traceback

from tablemaker import table_it
import playerclass

players = []
gameCategories = []
playerNumber, categoryNumber = 1, 1
letters = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't',
           'u', 'ü', 'v', 'y', 'z']


def calculate_score(category, gameTour):
    answerToScore = []
    for gamePlayer in players:
        answerToScore.append(getattr(obj[gamePlayer], f'{category}_{gameTour}'))
    for gamePlayer in players:
        playerCategoryAnswer = getattr(obj[gamePlayer], f'{category}_{gameTour}')
        if playerCategoryAnswer == '':
            obj[gamePlayer].score_response(category, gameTour, 0)
        elif answerToScore.count('') == len(players) - 1:
            obj[gamePlayer].score_response(category, gameTour, 20)
        elif answerToScore.count(playerCategoryAnswer) > 1:
            obj[gamePlayer].score_response(category, gameTour, 5)
        else:
            obj[gamePlayer].score_response(category, gameTour, 10)


def get_answer_score_for_table(gameTour):
    for gamePlayer in players:
        for i in range(len(gameCategories)):
            obj[gamePlayer].table[i][gameTour] = (
                getattr(obj[gamePlayer], f'{gameCategories[i]}_{gameTour}')
                + ': '
                + str(getattr(obj[gamePlayer], f'{gameCategories[i]}_{gameTour}_score'))
                 )


def sum_tour_score(gameTour):
    for player in players:
        playerRoundScore = 0
        for i in range(len(gameCategories)):
            playerRoundScore += getattr(obj[player], f'{gameCategories[i]}_{gameTour}_score')
        try:
            obj[player].table[-1][gameTour] = playerRoundScore
        except IndexError:
            obj[player].table[-1].append(playerRoundScore)
        obj[player].sum_tour(gameTour, playerRoundScore)


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
gameCategories = ['İsim', 'Şehir', 'Hayvan']

obj = {}
for player in players:
    obj[player] = playerclass.Contender(player, gameCategories)


# --- Remove after testing ---

tour = 1

while True:
    # TODO Harf seç | Süre ekle

    print('\nOyun başladı! Tur sona erdiğinde enter\'a basın.')
    a = input()
    os.system('cls')

    if a == 'q':  # For testing
        break

    categoryIndex = playerIndex = 0
    categoryAnswers = [
        [[player] for player in players] for category in gameCategories]
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
                    deleteOnAnswersList = categoryAnswers[categoryIndex][playerIndex-1]
                    if goingBack == 0 and len(deleteOnAnswersList) > 1:
                        deleteOnAnswersList.pop()
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
            obj[players[playerIndex]].remove_answer(gameCategories[categoryIndex], tour)
            os.system('cls')
            table_it(categoryAnswers[categoryIndex])
            continue
        calculate_score(category, tour)
        categoryIndex += 1

    for category in gameCategories:
        for player in players:
            obj[player].score += getattr(obj[player], f'{category}_{tour}_score')  # Add to total score

    totalScores = {player: obj[player].score for player in players}
    sortedTotalScores = {
        k: v for k, v in sorted(totalScores.items(), reverse=True, key=lambda item: item[1])}
    scoresList = [[], []]
    for name, score in sortedTotalScores.items():
        scoresList[0].append(name)
        scoresList[1].append(score)

    os.system('cls')
    print('\nPuan tablosu: \n ')
    table_it(scoresList)

    get_answer_score_for_table(tour)
    sum_tour_score(tour)

    while True:
        print('\nOyuncu ismi yazarak puan tablosunu görüntüleyebilirsiniz.')
        decision = input().title()
        if decision == '':
            break

        elif decision == '-':
            while decision != 'Q':
                print('\nDüzeltme modu. Cevabını düzenlemek istediğiniz kişinin ismini yazın.')
                print('Düzeltme modundan çıkmak için \'q\' tuşuna basın.')
                playerNameToEdit = input().title()
                os.system('cls')

                if playerNameToEdit == 'Q':
                    decision = ' '
                    break

                while playerNameToEdit not in players:
                    print(f"\nBöyle bir oyuncu yok. Mevcut oyuncular: {', '.join(players)}")
                    playerNameToEdit = input().title()
                    os.system('cls')

                print(f'Oyuncu adı: {playerNameToEdit}')
                table_it(obj[playerNameToEdit].table)
                print('\nHangi kategorideki cevap değiştirilsin?')
                categoryToEdit = input().title()
                os.system('cls')

                while categoryToEdit not in gameCategories:
                    table_it(obj[playerNameToEdit].table)
                    print(f"\nBöyle bir kategori yok. Mevcut kategoriler: {', '.join(gameCategories)}")
                    categoryToEdit = input().title()
                    os.system('cls')

                valueError = indexError = 0
                while True:
                    try:
                        print(f'Oyuncu adı: {playerNameToEdit}')
                        print(f'Kategori: {categoryToEdit}')
                        table_it(obj[playerNameToEdit].table)
                        print('\nHangi turdaki cevap değiştirilsin?')

                        if valueError == 1:
                            print('\nBir sayı girin.')
                            valueError = 0

                        if indexError == 1:
                            print(f'\nGeçerli bir tur sayısı girin. Şu anda {tour}. turdayız.')
                            indexError = 0

                        tourToEdit = int(input())

                    except ValueError:
                        valueError = 1
                        os.system('cls')
                        continue

                    if tourToEdit < 1 or tourToEdit > tour:
                        indexError = 1
                        os.system('cls')
                        continue
                    break

                print(f'Oyuncu adı: {playerNameToEdit}')
                table_it(obj[playerNameToEdit].table)
                print('\n' + getattr(
                    obj[playerNameToEdit], f'{categoryToEdit}_{tourToEdit}')
                      + ' yerine ne yazılsın?')

                newAnswer = input()

                obj[playerNameToEdit].change_answer(categoryToEdit, tourToEdit, newAnswer)
                calculate_score(categoryToEdit, tourToEdit)
                get_answer_score_for_table(tourToEdit)

                for player in players:
                    obj[player].score -= getattr(obj[player], f'sum_{tourToEdit}')

                sum_tour_score(tourToEdit)

                for player in players:
                    obj[player].score += getattr(obj[player], f'sum_{tourToEdit}')

                totalScores = {player: obj[player].score for player in players}
                sortedTotalScores = {
                    k: v for k, v in sorted(totalScores.items(), reverse=True, key=lambda item: item[1])}
                scoresList = [[], []]
                for name, score in sortedTotalScores.items():
                    scoresList[0].append(name)
                    scoresList[1].append(score)
                break

            os.system('cls')
            continue

        elif decision not in players:
            os.system('cls')
            table_it(scoresList)
            print(f'\n{decision} adında bir oyuncu yok.')
            continue

        os.system('cls')
        print(f'\n{decision} Puan Tablosu:')
        table_it(obj[decision].table)

    os.system('cls')
    tour += 1


while True:
    code = input()
    try:
        eval(code)
    except:
        print(traceback.format_exc())
