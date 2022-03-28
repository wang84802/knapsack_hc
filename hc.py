# pseudocode
# def hc(f,x):
#     x = 隨意設定一個解
#     while(x有鄰居y比x更高):
#         x = y
#     return x

import numpy as np
import random
import matplotlib.pyplot as plt
import config

#get knapsack file data
file_empty = 0
with open(config.path_p07_c, mode="r") as file:
    capacity = np.loadtxt(file)
    if capacity.size == 0:
        file_empty = 1

with open(config.path_p07_w, mode="r") as file:
    weights = np.loadtxt(file)
    weights = weights.astype(np.int32)
    if weights.size == 0:
        file_empty = 1
with open(config.path_p07_p, mode="r") as file:
    profits = np.loadtxt(file)
    profits = profits.astype(np.int32)
    if profits.size == 0:
        file_empty = 1
with open(config.path_p07_s, mode="r") as file:
    selects = np.loadtxt(file)
    selects = selects.astype(np.int32)
    if selects.size == 0:
        file_empty = 1

if file_empty == 1:
    print('file is empty')
    exit()

# 計算string代表的value, weight
def count_values(keys):
    res_v = 0
    res_w = 0
    for idx, key in enumerate(keys):
        if int(key)==1:
            res_v += profits[int(idx)]
            res_w += weights[int(idx)]
    return res_v,res_w

# random 01 bitstring
def rand_key(count):
    while True:
        init_key = ""
        for i in range(count):
            temp = str(random.randint(0, 1))
            init_key += temp
        res_v, res_w = count_values(init_key)
        # 不能超過限重
        if res_w <= capacity: 
            break
    return res_v, init_key

# change a bit
def change_a_bit(key, position, bit):
    temp = list(key)
    temp[position] = str(bit)
    key = "".join(temp)
    return key

# 迭代次數
round = 10000

# 折線圖list
list_plot = [0 for x in range(0, round)]

# 最大值
max_v = 0

# 物品數量
items = np.size(weights)

# 迭代500次
for j in range(0, round):
    # 生成random bit string
    res_v, init_key = rand_key(items)
    take_step_key = init_key

    list_plot[j] = max_v

    # 隨機找一個物品
    i = random.randint(0, items-1)
    # 紀錄是否所有bit都檢查完
    k = 0

    while True:
        if take_step_key[i] == '0':
            # take a step by changing 1 bit
            take_step_key = change_a_bit(take_step_key, i, '1')

            # check the step is legel or not
            check_v, check_w = count_values(take_step_key)
            if check_w <= capacity:
                res_v = check_v
            else: # move back
                k += 1
                take_step_key = change_a_bit(take_step_key, i, '0')
                res_v, res_w = count_values(take_step_key)

                # 每個物品都不能再拿 => 此輪迭代結束
                if k == items:
                    break

        #檢查下個物品是否可拿
        i = (i + 1) % items

    # 紀錄最大值&最大值之string
    if max_v < res_v:
        max_v = res_v
        max_v_key = take_step_key

print('result max value: ' + str(max_v))
print('result knapsack: ' + str(max_v_key))
print('expected max value: ', end='')
expected_v = 0
for idx, select in enumerate(selects):
    if select == 1:
        expected_v += profits[int(idx)]
print(expected_v)
print('expected knapsack: ', end='')
s = [str(i) for i in selects]
res = int(''.join(s))
print(res)

# 折線圖
x = np.linspace(1, round, round)
y = np.linspace(1, capacity)
plt.plot(x, list_plot, 'r')
plt.show()

