'''
1. Initialize the 8 directions with the longest distance.
2. Iterate the obstacles, if the obstacle in one of the 8 directions, update the distance in that direction
3. Sum the distances of 8 directions together.
Attention: The longest distance in the diagonal direction equals to min(vertical, horizonal)

'''
#!/bin/python3
import sys

def queensAttack(n, k, r_q, c_q, obstacles):
    
    vertical_up = n - r_q
    vertical_down = r_q - 1
    horizon_left = c_q - 1
    horizon_right = n - c_q

    left_up = min(vertical_up, horizon_left)
    left_down = min(vertical_down, horizon_right)
    right_up = min(vertical_up, horizon_right)
    right_down = min(horizon_left, vertical_down)

    
    for each_obstacle in obstacles:
        #left
        if (each_obstacle[0] + each_obstacle[1]) == (r_q + c_q):
            if each_obstacle[0] > r_q and (each_obstacle[0] - 1 - r_q) < left_up:
                left_up = each_obstacle[0] - 1 - r_q
            elif each_obstacle[0] < r_q and (r_q - 1 - each_obstacle[0]) < left_down:
                left_down = r_q - 1 - each_obstacle[0]

        #vertival
        elif each_obstacle[1] == c_q:
            if each_obstacle[0] > r_q and (each_obstacle[0] - 1 - r_q) < vertical_up:
                vertical_up = each_obstacle[0] - 1 - r_q
            elif each_obstacle[0] < r_q and (r_q - 1 - each_obstacle[0]) < vertical_down:
                vertical_down = r_q - 1 - each_obstacle[0]
        #right
        elif (each_obstacle[0] - r_q) == (each_obstacle[1] - c_q):
            if each_obstacle[0] > r_q and (each_obstacle[0] - 1 - r_q) <right_up:
                right_up = each_obstacle[0] - 1 - r_q
            elif each_obstacle[0] < r_q and (r_q - 1 - each_obstacle[0]) < right_down:
                right_down = r_q - 1 - each_obstacle[0]
        #horizon
        elif each_obstacle[0] == r_q:
            if each_obstacle[1] < c_q and (c_q - 1 - each_obstacle[1])  < horizon_left:
                horizon_left = c_q - 1 - each_obstacle[1]
            elif each_obstacle[1] > c_q and (each_obstacle[1] - 1 - c_q) < horizon_right:
                horizon_right = each_obstacle[1] - 1 - c_q

    
    return left_up+left_down+right_up+right_down+vertical_up+vertical_down+horizon_left+horizon_right

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