#!/bin/python3

import sys

def queensAttack(n, k, r_q, c_q, obstacles):
    result = 0
    left_max, right_max = (0, 0), (0, 0)
    left_min, right_min = (n, n), (n, n)
    #find the obstacles near queue most in each direction
    new_obstacles = []
    left_up_near, left_down_near = [], []
    vertical_up_near, vertical_down_near = [], []
    right_up_near, right_down_near = [], []
    horizon_left_near, horizon_right_near =[], []
    for each_obstacle in obstacles:
        if (each_obstacle[0] + each_obstacle[1]) == (r_q + c_q):
            if each_obstacle[0] > r_q:
                left_up_near.append(each_obstacle)
            elif each_obstacle[0] < r_q:
                left_down_near.append(each_obstacle)
        
        elif each_obstacle[1] == c_q:
            if each_obstacle[0] > r_q:
                vertical_up_near.append(each_obstacle)
            elif each_obstacle[0] < r_q:
                vertical_down_near.append(each_obstacle)

        elif (each_obstacle[0] - r_q) == (each_obstacle[1] - c_q):
            if each_obstacle[0] > r_q:
                right_up_near.append(each_obstacle)
            elif each_obstacle[0] < r_q:
                right_down_near.append(each_obstacle)
        
        elif each_obstacle[0] == r_q:
            if each_obstacle[1] < c_q:
                horizon_left_near.append(each_obstacle)
            elif each_obstacle[1] > c_q:
                horizon_right_near.append(each_obstacle)
    if left_up_near:
        new_obstacles.append(min([each for each in left_up_near if each[0] > r_q], key = lambda x : x[0]))
    if left_down_near:
        new_obstacles.append(max([each for each in left_down_near if each[0] < r_q], key = lambda x : x[0]))
    if vertical_up_near:
        new_obstacles.append(min([each for each in vertical_up_near if each[0] > r_q], key = lambda x : x[0]))
    if vertical_down_near:
        new_obstacles.append(max([each for each in vertical_down_near if each[0] < r_q], key = lambda x : x[0]))
    if right_up_near:
        new_obstacles.append(min([each for each in right_up_near if each[0] > r_q], key = lambda x : x[0]))
    if right_down_near:
        new_obstacles.append(max([each for each in right_down_near if each[0] < r_q], key = lambda x : x[0]))
    if horizon_left_near:
        new_obstacles.append(max([each for each in horizon_left_near if each[1] < c_q], key = lambda x : x[1]))
    if horizon_right_near:
        new_obstacles.append(min([each for each in horizon_right_near if each[1] > c_q], key = lambda x : x[1]))
    '''
    left_up_nearest = min([each for each in left_up_near if each[0] > r_q], key = lambda x : x[0])
    left_down_nearest = max([each for each in left_down_near if each[0] < r_q], key = lambda x : x[0])
    vertical_up_nearest = min([each for each in vertical_up_near if each[0] > r_q], key = lambda x : x[0])
    vertical_down_nearest = max([each for each in vertical_down_near if each[0] < r_q], key = lambda x : x[0])
    right_up_nearest = min([each for each in right_up_near if each[0] > r_q], key = lambda x : x[0])
    right_down_nearest = max([each for each in right_down_near if each[0] < r_q], key = lambda x : x[0])
    horizon_left_nearest = max([each for each in horizon_left_near if each[1] < c_q], key = lambda x : x[1])
    horizon_right_nearest =  min([each for each in horizon_right_near if each[1] > c_q], key = lambda x : x[1])
    print(left_up_nearest)
    print(left_down_nearest)
    print(vertical_up_nearest)
    print(vertical_down_nearest)
    print(right_up_nearest)
    print(right_down_nearest)
    print(horizon_left_nearest)
    print(horizon_right_nearest)
    '''
    #find all result  
    for i in range(n, 0, -1):
        for j in range(1, n + 1):
            if i == r_q and j == c_q:
                continue
            if (i + j) == (r_q + c_q):
                result += 1
                if i >= left_max[0]:
                    left_max = (i , j)
                if i <= left_min[0]:
                    left_min = (i, j)
            elif j == c_q:
                result += 1
            elif (i - r_q) == (j - c_q):
                result += 1
                if i >= right_max[0]:
                    right_max = (i , j)
                if i <= right_min[0]:
                    right_min = (i, j)
            elif i == r_q:
                result += 1

    #subtract obstacles from all-result
    for each_obstacle in new_obstacles:
        #vertical
        if each_obstacle[1] == c_q:
            if each_obstacle[0] > r_q:
                result -= (n - each_obstacle[0] + 1)
            else:
                result -= each_obstacle[0]
        #horizonal
        elif each_obstacle[0] == r_q:
            if each_obstacle[1] > c_q:
                result -= (n - each_obstacle[1] + 1)
            else:
                result -= each_obstacle[1]
        #left diagonal
        elif (each_obstacle[0] + each_obstacle[1]) == (r_q + c_q):
            if each_obstacle[0] > r_q:
                result -= (left_max[0] - each_obstacle[0])
            elif each_obstacle[0] < r_q:
                result -= (each_obstacle[0] - left_min[0])
        #right diagonal
        elif (each_obstacle[0] - r_q ) == (each_obstacle[1] - c_q):
            if each_obstacle[0] > r_q:
                result -= (right_max[0] - each_obstacle[0])
            elif each_obstacle[0] < r_q:
                result -= (each_obstacle[0] - right_min[0])
        
    return result
if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    r_q, c_q = input().strip().split(' ')
    r_q, c_q = [int(r_q), int(c_q)]
    obstacles = []
    for obstacles_i in range(k):
       obstacles_t = [int(obstacles_temp) for obstacles_temp in input().strip().split(' ')]
       obstacles.append(obstacles_t)
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
