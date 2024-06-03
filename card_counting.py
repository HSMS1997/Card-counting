CARD_POINTS = {
        'Z': 1,
        'X': 0,
        'C': -1,
}

DECKS = 8
player_count = 0


def main():

    count = 0
    cards = 0
    user_input = True

    while user_input:
        user_input = input("Cards:")
        cards += len(user_input)

        for card in user_input:
            count += CARD_POINTS[card.upper()]

        print('Count: {}'.format(count))

        decks_played = cards / 52.0
        t_count = count / (DECKS - decks_played)

        if t_count >= 2:
            print('True Count: {}'.format(t_count))
            print("Count: Double down")
        elif t_count == 1:
            print('True Count: {}'.format(t_count))
            print("Count: Hit")
        else:
            print('True Count: {}'.format(t_count))
            print("Count: Stand")


if __name__ == '__main__':
    main()
