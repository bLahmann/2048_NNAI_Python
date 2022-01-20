import multiprocessing as mp
import time

from Board import Board
from NeuralNetwork import NeuralNetwork as nn
from AI import AI


def simulate_games(ai, num_games, return_value):

    score = 0.0
    for _ in range(0, num_games):
        board = Board()
        while ai.do_move(board):
            pass
        score += board.get_score()
    score /= num_games
    return_value.value = score


def simulate_games_multiprocess(ai, num_per_cpu):

    processes = []
    results = []
    for i in range(0, mp.cpu_count()):
        results.append(mp.Value("d", 0.0))
        process = mp.Process(target=simulate_games, args=(ai, num_per_cpu, results[i]))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    average_result = 0.0
    for result in results:
        average_result += result.value
        print(result.value)
    average_result /= mp.cpu_count()

    return average_result


nn1 = nn([16, 32, 32, 32, 4])
ai1 = AI(nn1)

nn2 = nn([16, 32, 32, 32, 4])
ai2 = AI(nn2)

ai1.breed(ai2)

#print(simulate_games_multiprocess(ai, 100))
