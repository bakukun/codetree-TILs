arr_1 = list(map(int,input().split()))
arr_2 = list(map(int,input().split()))
arr_x = [arr_1[0],arr_1[2],arr_2[0],arr_2[2]]
arr_y = [arr_1[1],arr_1[3],arr_2[1],arr_2[3]]

min_x = min(arr_x)
max_x = max(arr_x)

min_y = min(arr_y)
max_y = max(arr_y)

print( (max_y-min_y) *(max_x-min_x))