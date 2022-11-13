from random import randint

def p_v_b(max_candy, max_candy_round):
    player = 0
    name_player = input('Введите имя: ')

    first_move = randint(1, 2)
    while max_candy > 0:
        if first_move == 1:
            player = name_player
            print(f'Ход игрока {name_player}.')
            count = 1
            while count != 2:
                player_move = int(input('Введите количество конфет которое хотите забрать: '))
                if player_move >= 1 and player_move <= max_candy_round:
                    count = 2
                    max_candy -= player_move

            print(f'Осталось {max_candy} конфет.')
            if max_candy <= 0:
                break
            
            player = 'бот'
            if max_candy <= max_candy_round:
                player_move = max_candy
            else:
                player_move = max_candy - max_candy_round * (max_candy // max_candy_round) - 1
                if player_move <= 0:
                    player_move += max_candy_round
            print(f'Бот забрал {player_move} конфет.')
            max_candy -= player_move
            print(f'Осталось {max_candy} конфет.')

        else:
            player = 'бот'
            if max_candy <= max_candy_round:
                player_move = max_candy
            else:
                    player_move = max_candy - max_candy_round * (max_candy // max_candy_round) - 1
                    if player_move <= 0:
                        player_move += max_candy_round
            print(f'Бот забрал {player_move} конфет.')
            max_candy -= player_move
            print(f'Осталось {max_candy} конфет.')
            if max_candy == 0:
                break

            player = name_player
            print(f'Ход игрока {player}.')
            count = 1
            while count != 2:
                player_move = int(input('Введите количество конфет которое хотите забрать: '))
                if player_move >= 1 and player_move <= max_candy_round:
                    count = 2
                    max_candy -= player_move
                    
    print(f'Победил(а) {player}')
