def selMinNum(list):
    small = list[0]
    for i in range(1,len(list)):
        if small > list[i]:
            small = list[i]
    return small

selMinNum([22,33,44,5])



