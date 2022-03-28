# knapsack_hc
01 knapsack problem dealing with hill climbing algorith

pseudocode
def hc(f,x):
    x = 隨意設定一個解
    while(x有鄰居y比x更高):
        x = y
    return x
    
1. 隨機一個重量<=capacity的解
2. 將此解輸出成01 bitstring, 0:物品有拿 1:物品沒拿
    ex: 10個物品,只有物品3有拿
        bitstring為0010000000
3. while(迭代500次):
     隨機改變一個物品狀態從0->1
     if 重量<=capacity:
       紀錄是否是最大值
     else:
       改回來
       if 所有物品都不能再拿:
         迭代結束
