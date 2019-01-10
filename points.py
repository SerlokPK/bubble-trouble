from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=2)


def increase_points(queue, returnQueue):
    player1_points = 0
    player2_points = 0
    while True:
        message = queue.get()

        if message == 'player1':
            result = pool.apply_async(add_points)
            player1_points += result.get()
        elif message == 'player2':
            result = pool.apply_async(add_points)
            player2_points += result.get()
        elif message == 'all_players_died':
            returnQueue.put((player1_points, player2_points))
            player1_points = 0
            player2_points = 0
        elif message == 'quit':
            break


def add_points():
    return 10
