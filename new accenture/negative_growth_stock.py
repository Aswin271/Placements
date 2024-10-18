def negative_growth(arr):
    count = 0
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            count += 1    
    return count
stock1 = [3, 5, 6, -7, 9, 10, -12]   
stock2 = [-5, -8, -12]

print(negative_growth(stock1))
print(negative_growth(stock2))     