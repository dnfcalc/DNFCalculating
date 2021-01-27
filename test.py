def faction(lis):
    for i in lis:
        if isinstance(i,list):
            faction(i)
        else:
            print(i)

lis = [1, 2, [4, [5, [6, [7], 8],9],0],3,9]
faction(lis)