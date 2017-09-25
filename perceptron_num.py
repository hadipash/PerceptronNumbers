import random
import numpy as np
from data import in_num, out_num

eta = 0     # learning rate
w = []      # matrix of weights


def init():
    # generating random weights
    # output layer consists of 4 nodes, therefore the matrix has 4 rows
    # because numbers are saved in 9 x 7 grid, the matrix has 9 x 7 = 63 elements in each row
    temp = list(range(10)) * 7
    w.append(random.sample(temp, 63))
    w.append(random.sample(temp, 63))
    w.append(random.sample(temp, 63))
    w.append(random.sample(temp, 63))

    # set a learning rate
    global eta
    while eta == 0:
        try:
            eta = float(input('Input a learning rate: '))
            if eta <= 0 or eta > 1:
                print("Learning rate should be within 0 and 1!")
                eta = 0
        except ValueError:
            print('Not a number')


def train():
    print("Training...")
    done = False    # training is finished
    iteration = 0

    while not done:
        iteration += 1
        print("Iteration #%d" % iteration)
        done = True

        for i in range(len(in_num)):
            # multiply input data by weights
            product = np.dot(in_num[i], np.transpose(w))

            for j in range(len(product)):
                # apply a threshold function
                if product[j] >= 0:
                    product[j] = 1
                else:
                    product[j] = -1

                # adjust weights if an output value not equals the target value
                if not product[j] == out_num[i][j]:
                    done = False
                    # w(t+1) = w(t) + eta * [d(t) - y(t)] * x(t)
                    # where d(t) - target value, y(t) - output value, x(t) - input value
                    temp = np.dot(eta * (out_num[i][j] - product[j]), in_num[i])
                    for k in range(len(w[j])):
                        w[j][k] += temp[k]


def findNum(num):
    # generate output values
    product = np.dot(num, np.transpose(w))
    temp = []

    # apply the threshold function
    for j in range(len(product)):
        if product[j] >= 0:
            product[j] = 1
        else:
            product[j] = 0
        temp.append(int(product[j]))

    # convert the output value into decimal representation
    n = int(str(temp[0])+str(temp[1])+str(temp[2])+str(temp[3]), 2)
    if 0 <= n <= 9:
        return n
    else:
        return None
