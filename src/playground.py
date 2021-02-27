malist = ["1","2","3","4","5"]
neff = (len(malist))
i = 0
while (i < neff):
    print(i)
    if (malist[i]=="3"):
        del malist[i]
        print(malist)
    i+=1