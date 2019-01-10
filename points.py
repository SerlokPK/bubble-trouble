def increase_points(queue, returnQueue):
    player1_points = 0
    player2_points = 0
    while True:
        message = queue.get()

        if message == 1:
            player1_points += 10
        elif message == 2:
            player2_points += 10
        elif message == 'quit':
            break
        else:
            returnQueue.put((player1_points, player2_points))

