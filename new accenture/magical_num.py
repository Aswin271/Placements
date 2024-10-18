def magical_num(num):
    """This is a function which will convert the number into binary and find the sum
    if the sum is even its not magical and if odd magical and while add if the bit is zero 
    it  becomes one and if its one it becomes 2"""
    if num == 0:
        return 0
    sum = 0
    binary_num = bin(num).replace("0b","")
    for i in range(len(binary_num)):
        if binary_num[i]=='1':
            sum = sum + 2
        elif binary_num[i]=='0':
            sum = sum + 1
    if sum % 2 == 0:
        return "Not Magical"
    else:
        return "Magical"            
answer = magical_num(4)
print(answer)               