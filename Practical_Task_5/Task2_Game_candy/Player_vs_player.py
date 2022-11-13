from random import randint

def p_v_p(max_candy, max_candy_round):
    name_first_player = input('Введите имя первого игрока: ')
    name_second_player = input('Введите имя второго игрока: ')

    first_move = randint(1, 2)
    while max_candy > 0:
        player = name_first_player   
        if first_move == 1:
            print(f'Ход игрока {player}.')
            count = 1
            while count != 2:
                player_move = int(input('Введите количество конфет которое хотите забрать: '))
                if player_move >= 1 and player_move <= max_candy_round:
                    count = 2
                    max_candy -= player_move

            print(f'Осталось {max_candy} конфет.')
            if max_candy <= 0:
                break

            player = name_second_player 
            print(f'Ход игрока {player}.')           
            count = 1
            while count != 2:
                player_move = int(input('Введите количество конфет которое хотите забрать: '))
                if player_move >= 1 and player_move <= max_candy_round:
                    count = 2
                    max_candy -= player_move
                
            print(f'Осталось {max_candy} конфет.')
            if max_candy <= 0:
                break  

        else:
            player = name_second_player 
            print(f'Ход игрока {player}.')           
            count = 1
            while count != 2:
                player_move = int(input('Введите количество конфет которое хотите забрать: '))
                if player_move >= 1 and player_move <= max_candy_round:
                    count = 2
                    max_candy -= player_move

            print(f'Осталось {max_candy} конфет.')
            if max_candy <= 0:
                break

            player = name_first_player 
            print(f'Ход игрока {player}.')
            count = 1
            while count != 2:
                player_move = int(input('Введите количество конфет которое хотите забрать: '))
                if player_move >= 1 and player_move <= max_candy_round:
                    count = 2
                    max_candy -= player_move
            print(f'Осталось {max_candy} конфет.')

    print(f'Победил {player}')
