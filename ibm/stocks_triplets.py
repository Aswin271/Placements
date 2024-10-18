s =[3,3,4,7,8]
sorted_s =sorted(s)
count = 0
i = 0
first,second,third = 0
while(i<len(sorted_s)-2):
    sum = sorted_s[first] + sorted_s[second] + sorted_s[third]
    if sum%5 !=0:
        third+=1
    else:
        count+=1