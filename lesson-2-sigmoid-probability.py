import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


point_list = [(1, 1), (2, 4), (5, -5), (-4, 5)]

for i in range(len(point_list)):
    score = 4*point_list[i][0] + 5*point_list[i][1] - 9
    probability = sigmoid(score)
    print('Point {} has probability of {:.2f} of being blue or red'.format(
        point_list[i], probability*100))
