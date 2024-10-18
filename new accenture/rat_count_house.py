def house_count(r, unit, arr):
    food_needed = r * unit
    house_counts = 0
    
    if len(arr) == 0:
        return -1
    
    total_food = 0
    
    for i in arr:
        total_food += i
        house_counts += 1
        if total_food >= food_needed:
            return house_counts
    
    return 0 

r = 5
unit = 2            
arr = [4, 2, 5, 3]
print(house_count(r, unit, arr))
