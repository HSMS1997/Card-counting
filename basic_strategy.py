CARD_VALUES = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11,
}


def main():
    play = 1
    while play > 0:
        player_count = 0
        player = input("Player hand:")
        dealer = input("Dealer hand:")

        for card in player:
            player_count += CARD_VALUES[card.upper()]

        for card in dealer:
            dealer_count = CARD_VALUES[card.upper()]

            if player_count <= 8:
                print('Hit')
            elif player_count == 9:
                if dealer_count in [2, 7, 8, 9, 10, 11]:
                    print('Hit')
                else:
                    print('Double')
            elif player_count == 10:
                if dealer_count in [10, 11]:
                    print('Hit')
                else:
                    print('Double')
            elif player_count == 11:
                print('Double')
            elif player_count in [12]:
                if dealer_count in [4, 5, 6]:
                    print('Stand')
                else:
                    print('Hit')

            elif player_count in [13, 14, 15, 16]:
                if dealer_count in [2, 3, 4, 5, 6]:
                    print('Stand')
                else:
                    print('Hit')

            elif player_count in [17, 18, 19, 20]:
                print('Stand')

            elif player_count == 22:
                print('Split')

            else:
                pass


if __name__ == '__main__':
    main()

