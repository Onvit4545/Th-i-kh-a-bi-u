import pandas as pd
import numpy as np
import random
detail_class = np.loadtxt('data\detail_class.csv', dtype = str, delimiter=',')
lop =  ' '.join(i[0] for i in detail_class).split()
monhoc = ' '.join(i[1] for i in detail_class).split()
s = pd.Series(monhoc, index=lop)
default_sllop =pd.Series([4,4,4,2,2,2,2,2,2,2], index=[1,2,3,4,5,6,7,8,9,10])
mang=[]
mang_kq2 = []

for i in range(len(s)):
    
    for ij in list(s[i]):
        for j in range(default_sllop[int(ij)]):
            mang.append(int(ij))
    mang_kq1 = []
    for i in range(len(mang)):
        sdc = random.choice(mang)
        mang_kq1.append(sdc)
        mang.remove(sdc)
    mang_kq2.append(mang_kq1)
print(mang_kq2)


    