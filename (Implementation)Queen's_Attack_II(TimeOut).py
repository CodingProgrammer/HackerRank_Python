'''
Iterate from the most inner level 
each level has 8 possible steps, update each position and judge whether is in obstacles
if the position is not in the chessboard ,make it None
if the position is in obstacles, each_level_points -= 1, and make this position None
'''
#!/bin/python3
import sys

def queensAttack(n, k, r_q, c_q, obstacles):
    result = 0

    left_up = (r_q + 1, c_q - 1) if ((r_q + 1) <= n) and ((c_q - 1) >= 1) else None
    
    vertical_up = (r_q + 1, c_q) if (r_q + 1) <= n else None
    
    right_up = (r_q + 1, c_q + 1) if ((r_q + 1) <= n) and ((c_q + 1) <= n) else None

    horizon_left = (r_q, c_q - 1) if (c_q - 1) >= 1 else None

    horizon_right = (r_q, c_q + 1) if (c_q + 1) <= n else None

    right_down = (r_q - 1, c_q - 1) if (r_q - 1) >= 1 and (c_q - 1) >= 1 else None

    vertical_down = (r_q - 1, c_q) if (r_q - 1) >= 1 else None

    left_down = (r_q - 1, c_q + 1) if (r_q - 1) >= 1 and (c_q + 1) <= n else None

    level = 0
    max_level = max(n-r_q, n-c_q, r_q-1, c_q-1)
    while level < max_level:
        each_level_add = 8

        if left_up:
            if left_up in obstacles:
                each_level_add -= 1
                left_up = None
            else:
                #update 
                if (left_up[0] + 1) <= n and (left_up[1] - 1) >= 1:
                    left_up = (left_up[0] + 1, left_up[1] - 1)
                else:
                    left_up = None
        else:
            each_level_add -= 1

        if left_down:
            if left_down in obstacles:
                each_level_add -= 1
                left_down = None
            else:
                #update 
                if (left_down[0] - 1) >= 1 and (left_down[1] + 1) <= n:
                    left_down = (left_down[0] - 1, left_down[1] + 1)
                else:
                    left_down = None
        else:
            each_level_add -= 1

        if vertical_up:
            if vertical_up in obstacles:
                each_level_add -= 1
                vertical_up = None
            else:
                #update 
                if (vertical_up[0] + 1) <= n:
                    vertical_up = (vertical_up[0] + 1, vertical_up[1])
                else:
                    vertical_up = None
        else:
            each_level_add -= 1

        if vertical_down:
            if vertical_down in obstacles:
                each_level_add -= 1
                vertical_down = None
            else:
                #update 
                if (vertical_down[0] - 1) >= 1:
                    vertical_down = (vertical_down[0] - 1, vertical_down[1])
                else:
                    vertical_down = None
        else:
            each_level_add -= 1

        if right_up:
            if right_up in obstacles:
                each_level_add -= 1
                right_up = None
            else:
                #update 
                if (right_up[0] + 1) <= n and (right_up[1] + 1) <= n:
                    right_up = (right_up[0] + 1, right_up[1] + 1)
                else:
                    right_up = None
        else:
            each_level_add -= 1

        if right_down:
            if right_down in obstacles:
                each_level_add -= 1
                right_down = None
            else:
                #update 
                if (right_down[0] - 1) >= 1 and (right_down[1] - 1) >= 1:
                    right_down = (right_down[0] - 1, right_down[1] - 1)
                else:
                    right_down = None
        else:
            each_level_add -= 1

        if horizon_left:
            if horizon_left in obstacles:
                each_level_add -= 1
                horizon_left = None
            else:
                #update 
                if (horizon_left[1] - 1) >= 1:
                    horizon_left = (horizon_left[0], horizon_left[1] - 1)
                else:
                    horizon_left = None
        else:
            each_level_add -= 1

        if horizon_right:
            if horizon_right in obstacles:
                each_level_add -= 1
                horizon_right = None
            else:
                #update 
                if (horizon_right[1] + 1) <= n:
                    horizon_right = (horizon_right[0], horizon_right[1] + 1)
                else:
                    horizon_right = None
        else:
            each_level_add -= 1

        result += each_level_add  
        level += 1
    return result
            




if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    r_q, c_q = input().strip().split(' ')
    r_q, c_q = [int(r_q), int(c_q)]
    obstacles = []
    for obstacles_i in range(k):
       obstacles_t = [int(obstacles_temp) for obstacles_temp in input().strip().split(' ')]
       obstacles.append(tuple(obstacles_t))
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    r_q, c_q = input().strip().split(' ')
    r_q, c_q = [int(r_q), int(c_q)]
    obstacles = []
    for obstacles_i in range(k):
       obstacles_t = (int(obstacles_temp) for obstacles_temp in input().strip().split(' '))
       obstacles.append(obstacles_t)
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
