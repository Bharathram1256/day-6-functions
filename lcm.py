def findLcm(a,b):
    if a>b:
        greater=a
    else:
        greater=b
    while True:
        if((greater % a==0) and (greater % b)==0):
            lcm=greater
            break
        greater+=1
    return lcm
print(findLcm(39,33))