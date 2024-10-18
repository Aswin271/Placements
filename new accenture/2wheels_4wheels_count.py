def four_wheels_two_wheels_count(vehicles,wheels):
    if wheels%2!=0 or vehicles>wheels:
        return "Invalid Inputs"
    else:
        fw=((wheels-2*vehicles)//2)
        print(fw)
        tw = vehicles - fw
        return fw,tw
print(four_wheels_two_wheels_count(200,540))   
print("this is trial branch")  

print("This is for trial branch and merge")



