import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection

#99年開始變成新北市 index變動
#整理出90-109年出生人口資料

born90to98 = []  #裝90-98年出生人口
born99to109 = []  #裝99-109年出生人口
def Born90(born):
    with open(born,encoding='utf8') as file:
        fn = csv.reader(file)
        info =list(fn)
    return info[26][1]

def Born99(born):
    with open(born,encoding='utf8') as file:
        fn = csv.reader(file)
        info =list(fn)
    return info[23][1]

born = [r'C:\Users\Siou\Desktop\專題\出生人口\出生人口90.csv',
        r'C:\Users\Siou\Desktop\專題\出生人口\出生人口91.csv',
        r'C:\Users\Siou\Desktop\專題\出生人口\出生人口92.csv',
        r'C:\Users\Siou\Desktop\專題\出生人口\出生人口93.csv',
        r'C:\Users\Siou\Desktop\專題\出生人口\出生人口94.csv',
        r'C:\Users\Siou\Desktop\專題\出生人口\出生人口95.csv',
        r'C:\Users\Siou\Desktop\專題\出生人口\出生人口96.csv',
        r'C:\Users\Siou\Desktop\專題\出生人口\出生人口97.csv',
        r'C:\Users\Siou\Desktop\專題\出生人口\出生人口98.csv'
        ]
born1 = [r'C:\Users\Siou\Desktop\專題\出生人口\出生人口99.csv',
         r'C:\Users\Siou\Desktop\專題\出生人口\出生人口100.csv',
         r'C:\Users\Siou\Desktop\專題\出生人口\出生人口101.csv',
         r'C:\Users\Siou\Desktop\專題\出生人口\出生人口102.csv',
         r'C:\Users\Siou\Desktop\專題\出生人口\出生人口103.csv',
         r'C:\Users\Siou\Desktop\專題\出生人口\出生人口104.csv',
         r'C:\Users\Siou\Desktop\專題\出生人口\出生人口105.csv',
         r'C:\Users\Siou\Desktop\專題\出生人口\出生人口106.csv',
         r'C:\Users\Siou\Desktop\專題\出生人口\出生人口107.csv',
         r'C:\Users\Siou\Desktop\專題\出生人口\出生人口108.csv',
         r'C:\Users\Siou\Desktop\專題\出生人口\出生人口109.csv'
         ]
for i in range(9):
    x = Born90(born[i])
    z = x.replace(',','')
    born90to98.append(z)
for i in range(11):
    x = Born99(born1[i])
    z = x.replace(',','')
    born99to109.append(z)
    
#90-109出生人口 list型態
born90to109 = born90to98 + born99to109    

#-----------------------------------------------

#整理出90-109年死亡人口資料

dead90to98 = []  #裝90-98年死亡人口
dead99to109 = []  #裝99-109年死亡人口
def Dead90(dead):
    with open(dead,encoding='utf8') as file:
        fn = csv.reader(file)
        info = list(fn)
        return info[26][1]
def Dead99(dead):
    with open(dead,encoding='utf8') as file:
        fn = csv.reader(file)
        info =list(fn)
    return info[23][1]
   
dead = [r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口90.csv',
        r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口91.csv',
        r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口92.csv',
        r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口93.csv',
        r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口94.csv',
        r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口95.csv',
        r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口96.csv',
        r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口97.csv',
        r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口98.csv'
        ]  
dead1 = [r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口99.csv',
         r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口100.csv',
         r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口101.csv',
         r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口102.csv',
         r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口103.csv',
         r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口104.csv',
         r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口105.csv',
         r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口106.csv',
         r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口107.csv',
         r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口108.csv',
         r'C:\Users\Siou\Desktop\專題\死亡人口\死亡人口109.csv'
        ]  
for i in range(9):
    x = Dead90(dead[i])
    z =x.replace(',','')
    dead90to98.append(z)
for i in range(11):
    x = Dead99(dead1[i])
    z =x.replace(',','')
    dead99to109.append(z)
    
#90-109死亡人口 list型態
dead90to109 = dead90to98 + dead99to109

#-----------------------------------------------

#100年開始變成新北市 Index變動
#整理出90-109年65歲以上人口資料

old90to99man = [] #90-99年 男
old90to99women = [] #90-99年 女
old100to109man = [] #100-109年 男
old100to109women = [] #100-109年 女

def Old(old,old1):
    with open(old,encoding='utf8') as file:
        fn = csv.reader(file)
        info = list(fn)
    with open(old1,encoding='utf8') as file1:
        fn1 = csv.reader(file1)
        info1 = list(fn1)
    return info[26][1],info[26][2],info1[23][1],info1[23][2]

old = [r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料90.csv',
       r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料91.csv',
       r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料92.csv',
       r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料93.csv',
       r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料94.csv',
       r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料95.csv',
       r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料96.csv',
       r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料97.csv',
       r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料98.csv',
       r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料99.csv'
       ]
old1 = [r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料100.csv',
        r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料101.csv',
        r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料102.csv',
        r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料103.csv',
        r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料104.csv',
        r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料105.csv',
        r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料106.csv',
        r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料107.csv',
        r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料108.csv',
        r'C:\Users\Siou\Desktop\專題\65歲以上人口\人口資料109.csv'
        ]
old2 = [r'C:\Users\Siou\Desktop\專題\65upTotal\65up90.csv',
       r'C:\Users\Siou\Desktop\專題\65upTotal\65up91.csv',
       r'C:\Users\Siou\Desktop\專題\65upTotal\65up92.csv',
       r'C:\Users\Siou\Desktop\專題\65upTotal\65up93.csv',
       r'C:\Users\Siou\Desktop\專題\65upTotal\65up94.csv',
       r'C:\Users\Siou\Desktop\專題\65upTotal\65up95.csv',
       r'C:\Users\Siou\Desktop\專題\65upTotal\65up96.csv',
       r'C:\Users\Siou\Desktop\專題\65upTotal\65up97.csv',
       r'C:\Users\Siou\Desktop\專題\65upTotal\65up98.csv',
       r'C:\Users\Siou\Desktop\專題\65upTotal\65up99.csv',
       ]
old3 = [r'C:\Users\Siou\Desktop\專題\65upTotal\65up100.csv',
        r'C:\Users\Siou\Desktop\專題\65upTotal\65up101.csv',
        r'C:\Users\Siou\Desktop\專題\65upTotal\65up102.csv',
        r'C:\Users\Siou\Desktop\專題\65upTotal\65up103.csv',
        r'C:\Users\Siou\Desktop\專題\65upTotal\65up104.csv',
        r'C:\Users\Siou\Desktop\專題\65upTotal\65up105.csv',
        r'C:\Users\Siou\Desktop\專題\65upTotal\65up106.csv',
        r'C:\Users\Siou\Desktop\專題\65upTotal\65up107.csv',
        r'C:\Users\Siou\Desktop\專題\65upTotal\65up108.csv',
        r'C:\Users\Siou\Desktop\專題\65upTotal\65up109.csv',
        ]

for n in range(10):
    x,y,i,j = Old(old[n],old1[n])
    a =x.replace(',','')
    b =y.replace(',','')
    c =i.replace(',','')
    d =j.replace(',','')
    old90to99man.append(a)
    old90to99women.append(b)
    old100to109man.append(c)
    old100to109women.append(d)
    
#各地老年人口分布
up65North90 = [] 
up65Mid90 = [] 
up65South90 = [] 
up65East90 = [] 
up65Out90 = [] 

up65North100 = [] 
up65Mid100 = [] 
up65South100 = [] 
up65East100 = [] 
up65Out100 = [] 

up65North104 = [] 
up65Mid104 = [] 
up65South104 = [] 
up65East104 = [] 
up65Out104 = [] 

# 裝加起來的int
UP65North90 = [0,0,0,0,0,0,0,0,0,0] 
UP65Mid90 = [0,0,0,0,0,0,0,0,0,0] 
UP65South90 = [0,0,0,0,0,0,0,0,0,0] 
UP65East90 = [0,0,0,0,0,0,0,0,0,0] 
UP65Out90 = [0,0,0,0,0,0,0,0,0,0] 
    
UP65North100 = [0,0,0,0] 
UP65Mid100 = [0,0,0,0] 
UP65South100 = [0,0,0,0] 
UP65East100 = [0,0,0,0] 
UP65Out100 = [0,0,0,0] 

UP65North104 = [0,0,0,0,0,0] 
UP65Mid104 = [0,0,0,0,0,0] 
UP65South104 = [0,0,0,0,0,0] 
UP65East104 = [0,0,0,0,0,0] 
UP65Out104 = [0,0,0,0,0,0] 

# 90-99年的地區區分
north3 = [0,2,4,5,18,19]
mid3 = [6,7,8,9,10,20]
south3 = [1,11,12,13,14,21,22]
east3 = [3,15,16]
out3 = [17,23,24]

#100-103年的地區區分
north4 = [0,1,6,7,17,18]
mid4 = [2,8,9,10,11]
south4 = [3,4,12,13,19]
east4 = [5,14,15]
out4 = [16,20,21]

#104-109年的地區區分
north5 = [0,1,2,7,17,18]
mid5 = [3,8,9,10,11]
south5 = [4,5,12,13,19]
east5 = [6,14,15]
out5 = [16,20,21]

for i in range(10):
    file = pd.read_csv(old2[i])
    data1 = file['65歲以上總計'][north3]
    data2 = file['65歲以上總計'][mid3]
    data3 = file['65歲以上總計'][south3]
    data4 = file['65歲以上總計'][east3]
    data5 = file['65歲以上總計'][out3]
    up65North90.append(data1)
    up65Mid90.append(data2)
    up65South90.append(data3)
    up65East90.append(data4)
    up65Out90.append(data5)

for i in range(4):
    file = pd.read_csv(old3[i])
    data1 = file['65歲以上總計'][north4]
    data2 = file['65歲以上總計'][mid4]
    data3 = file['65歲以上總計'][south4]
    data4 = file['65歲以上總計'][east4]
    data5 = file['65歲以上總計'][out4]
    up65North100.append(data1)
    up65Mid100.append(data2)
    up65South100.append(data3)
    up65East100.append(data4)
    up65Out100.append(data5)
    
for i in range(4,10):
    file = pd.read_csv(old3[i])
    data1 = file['65歲以上總計'][north5]
    data2 = file['65歲以上總計'][mid5]
    data3 = file['65歲以上總計'][south5]
    data4 = file['65歲以上總計'][east5]
    data5 = file['65歲以上總計'][out5]
    up65North104.append(data1)
    up65Mid104.append(data2)
    up65South104.append(data3)
    up65East104.append(data4)
    up65Out104.append(data5)

#90年
def N65(a,b,c):
    for x in range(10):
        for i in a:
            z = b[x][i]
            z = z.replace(',','')
            z = int(z)
            c[x]+=z
N65(north3,up65North90,UP65North90)
N65(mid3,up65Mid90,UP65Mid90)
N65(south3,up65South90,UP65South90)
N65(east3,up65East90,UP65East90)
N65(out3,up65Out90,UP65Out90)

#100年
def N66(a,b,c):
    for x in range(4):
        for i in a:
            z = b[x][i]
            z = z.replace(',','')
            z = int(z)
            c[x]+=z
N66(north4,up65North100,UP65North100)
N66(mid4,up65Mid100,UP65Mid100)
N66(south4,up65South100,UP65South100)
N66(east4,up65East100,UP65East100)
N66(out4,up65Out100,UP65Out100)

#104年 
def N67(a,b,c):
    for x in range(6):
        for i in a:
            z = b[x][i]
            z = z.replace(',','')
            z = int(z)
            c[x]+=z 
N67(north5,up65North104,UP65North104)
N67(mid5,up65Mid104,UP65Mid104)
N67(south5,up65South104,UP65South104)
N67(east5,up65East104,UP65East104)
N67(out5,up65Out104,UP65Out104)

UP65NORTH = UP65North90 + UP65North100 + UP65North104
UP65MID = UP65Mid90 + UP65Mid100 + UP65Mid104
UP65SOUTH = UP65South90 + UP65South100 + UP65South104
UP65EAST = UP65East90 + UP65East100 + UP65East104
UP65OUT = UP65Out90 + UP65Out100 + UP65Out104


#90-109年65歲以上人口 男女 list型態
old90to109man = old90to99man + old100to109man
old90to109women = old90to99women + old100to109women

#-----------------------------------------------

#100年開始變成新北市 Index變動
#整理出90-109年全國人口

totalPerson90to99 = [] #  90-99年總人數
totalPerson100to109 = [] # 100-109年總人數

def Total(person,person1):
    file = pd.read_csv(person)
    data = file['總計'][25]
    file1 = pd.read_csv(person1)
    data1 = file1['總計'][22]
    return data,data1
    
Person = [r'C:\Users\Siou\Desktop\專題\全國人口\全國人口90.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口91.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口92.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口93.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口94.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口95.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口96.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口97.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口98.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口99.csv'
    ]
Person1 = [r'C:\Users\Siou\Desktop\專題\全國人口\全國人口100.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口101.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口102.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口103.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口104.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口105.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口106.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口107.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口108.csv',
         r'C:\Users\Siou\Desktop\專題\全國人口\全國人口109.csv'
    ] 
for i in range(10):
    Info,Info1 = Total(Person[i],Person1[i])
    z = Info.replace(',','')
    z1 = Info1.replace(',','')
    totalPerson90to99.append(z)
    totalPerson100to109.append(z1)

    
#裝還沒加起來的 str  
totalpersonNorth90 = [] 
totalpersonMid90 = [] 
totalpersonSouth90 = [] 
totalpersonEast90 = [] 
totalpersonOut90 = [] 

totalpersonNorth100 = [] 
totalpersonMid100 = [] 
totalpersonSouth100 = [] 
totalpersonEast100 = [] 
totalpersonOut100 = [] 

totalpersonNorth104 = [] 
totalpersonMid104 = [] 
totalpersonSouth104 = [] 
totalpersonEast104 = [] 
totalpersonOut104 = [] 

# 裝加起來的int
TotalpersonNorth90 = [0,0,0,0,0,0,0,0,0,0] 
TotalpersonMid90 = [0,0,0,0,0,0,0,0,0,0] 
TotalpersonSouth90 = [0,0,0,0,0,0,0,0,0,0] 
TotalpersonEast90 = [0,0,0,0,0,0,0,0,0,0] 
TotalpersonOut90 = [0,0,0,0,0,0,0,0,0,0] 

TotalpersonNorth100 = [0,0,0,0] 
TotalpersonMid100 = [0,0,0,0] 
TotalpersonSouth100 = [0,0,0,0] 
TotalpersonEast100 = [0,0,0,0] 
TotalpersonOut100 = [0,0,0,0] 

TotalpersonNorth104 = [0,0,0,0,0,0] 
TotalpersonMid104 = [0,0,0,0,0,0] 
TotalpersonSouth104 = [0,0,0,0,0,0] 
TotalpersonEast104 = [0,0,0,0,0,0] 
TotalpersonOut104 = [0,0,0,0,0,0] 

# 90-99年的地區區分
north = [0,2,4,5,18,19]
mid = [6,7,8,9,10,20]
south = [1,11,12,13,14,21,22]
east = [3,15,16]
out = [17,23,24]

#100-103年的地區區分
north1 = [0,1,6,7,17,18]
mid1 = [2,8,9,10,11]
south1 = [3,4,12,13,19]
east1 = [5,14,15]
out1 = [16,20,21]

#104-109年的地區區分
north2 = [0,1,2,7,17,18]
mid2 = [3,8,9,10,11]
south2 = [4,5,12,13,19]
east2 = [6,14,15]
out2 = [16,20,21]

for i in range(10):
    file = pd.read_csv(Person[i])
    data1 = file['總計'][north]
    data2 = file['總計'][mid]
    data3 = file['總計'][south]
    data4 = file['總計'][east]
    data5 = file['總計'][out]
    totalpersonNorth90.append(data1)
    totalpersonMid90.append(data2)
    totalpersonSouth90.append(data3)
    totalpersonEast90.append(data4)
    totalpersonOut90.append(data5)

for i in range(4):
    file = pd.read_csv(Person1[i])
    data1 = file['總計'][north1]
    data2 = file['總計'][mid1]
    data3 = file['總計'][south1]
    data4 = file['總計'][east1]
    data5 = file['總計'][out1]
    totalpersonNorth100.append(data1)
    totalpersonMid100.append(data2)
    totalpersonSouth100.append(data3)
    totalpersonEast100.append(data4)
    totalpersonOut100.append(data5)
for i in range(4,10):
    file = pd.read_csv(Person1[i])
    data1 = file['總計'][north2]
    data2 = file['總計'][mid2]
    data3 = file['總計'][south2]
    data4 = file['總計'][east2]
    data5 = file['總計'][out2]
    totalpersonNorth104.append(data1)
    totalpersonMid104.append(data2)
    totalpersonSouth104.append(data3)
    totalpersonEast104.append(data4)
    totalpersonOut104.append(data5)

#90年
def NT1(a,b,c):
    for x in range(10):
        for i in a:
            z = b[x][i]
            z = z.replace(',','')
            z = int(z)
            c[x]+=z
NT1(north,totalpersonNorth90,TotalpersonNorth90)
NT1(mid,totalpersonMid90,TotalpersonMid90)
NT1(south,totalpersonSouth90,TotalpersonSouth90)
NT1(east,totalpersonEast90,TotalpersonEast90)
NT1(out,totalpersonOut90,TotalpersonOut90)

#100年
def NT2(a,b,c):
    for x in range(4):
        for i in a:
            z = b[x][i]
            z = z.replace(',','')
            z = int(z)
            c[x]+=z
NT2(north1,totalpersonNorth100,TotalpersonNorth100)
NT2(mid1,totalpersonMid100,TotalpersonMid100)
NT2(south1,totalpersonSouth100,TotalpersonSouth100)
NT2(east1,totalpersonEast100,TotalpersonEast100)
NT2(out1,totalpersonOut100,TotalpersonOut100)

#104年
def NT3(a,b,c):
    for x in range(6):
        for i in a:
            z = b[x][i]
            z = z.replace(',','')
            z = int(z)
            c[x]+=z
NT3(north2,totalpersonNorth104,TotalpersonNorth104)
NT3(mid2,totalpersonMid104,TotalpersonMid104)
NT3(south2,totalpersonSouth104,TotalpersonSouth104)
NT3(east2,totalpersonEast104,TotalpersonEast104)
NT3(out2,totalpersonOut104,TotalpersonOut104)


#90-109全國總人數 list型態
totalPerson90to109 = totalPerson90to99 + totalPerson100to109

#90-109全國人口分布圖
TotalpersonNORTH = TotalpersonNorth90 + TotalpersonNorth100 + TotalpersonNorth104
TotalpersonMID = TotalpersonMid90 + TotalpersonMid100 + TotalpersonMid104
TotalpersonSOUTH = TotalpersonSouth90 + TotalpersonSouth100 + TotalpersonSouth104
TotalpersonEAST = TotalpersonEast90 + TotalpersonEast100 + TotalpersonEast104
TotalpersonOUT = TotalpersonOut90 + TotalpersonOut100 + TotalpersonOut104

#-----------------------------------------------

'''
出生: born90to109
死亡: dead90to109
全國: totalPerson90to109

65歲以上男: old90to109man
65歲以上女: old90to109women
自然增加: Nature
'''

nature = [] 
Num = []
for i in range(20):
    x = int(born90to109[i])-int(dead90to109[i])
    nature.append(str(x))
for i in range(1,21):
    Num.append(i)

#自然增加=出生-死亡
Nature = list(map(int,nature))

NN = ['%d年'%i for i in range(90,110)]

DEAD = list(map(int,dead90to109))
BORN = list(map(int,born90to109))
Old65man = list(map(int,old90to109man))
Old65women = list(map(int,old90to109women))

#----------------------------------------------

# 安養院資料
# NH = nursing home
nh = []
NH = []
nhname = []  #各縣市名
nhname1 = [] #空的
nhplacetotal = [] #總計
nhplace1 = []  #長期照護型機構
nhplace2 = []  #養護型機構
nhplace3 = []  #失智照顧型機構
nhplace4 = []  #安養機構

for i in range(2015,2021):
    years = '%d年'%i
    data = pd.read_excel(r'C:\Users\Siou\Desktop\專題\安養機構資料.xls',
                     sheet_name= years,usecols='A:G')
    totaldata = pd.read_excel(r'C:\Users\Siou\Desktop\專題\安養機構資料.xls',
                     sheet_name= years,usecols='A:AA')
    information = data.iloc[9,:7]
    infoPlace = totaldata.iloc[10:34,2:7]
    infoPlace1 = totaldata.iloc[10:34,7:12]
    infoPlace2 = totaldata.iloc[10:34,12:17]
    infoPlace3 = totaldata.iloc[10:34,17:22]
    infoPlace4 = totaldata.iloc[10:34,22:27]
    nh.append(information)
    nhplacetotal.append(infoPlace)
    nhplace1.append(infoPlace1)
    nhplace2.append(infoPlace2)
    nhplace3.append(infoPlace3)
    nhplace4.append(infoPlace4)
    if nhname ==nhname1:
        infoname = totaldata.iloc[10:34,:1]
        nhname.append(infoname)
for z in range(6):
    NH.append(nh[z][1:7].values)

#----------------------------------------------

Old65=[] 

TotalPerson = list(map(int,totalPerson90to109))

count=0 
while count<len(Old65man):
    x = Old65man[count]+Old65women[count]
    Old65.append(str(x))
    count+=1

olD65 = list(map(int,Old65))
  
# Aging Society高齡化社會
AgingSociety = []
for countnumber in range(20):
    j = olD65[countnumber] / TotalPerson[countnumber]
    j*=100
    AgingSociety.append(str('%.3f'%j))

#-----------------------------------------------

N1 = ['%d'%i for i in range(90,110)]
N2 = list(map(int,N1))
#出生&死亡 圖表

# plot the data
fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot(1,1,1)
ax.plot(N1, BORN, color='tab:blue')
ax.plot(N1, DEAD, color='tab:orange')

#加入中文字
plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['font.size'] = 12

# create the events marking the x data points
xevents1 = EventCollection(N1, color='blue', linelength=0.05)
xevents2 = EventCollection(N1, color='orange', linelength=0.05)

# create the events marking the y data points
yevents1 = EventCollection(BORN, color='blue', linelength=0.05,
                           orientation='vertical')
yevents2 = EventCollection(DEAD, color='orange', linelength=0.05,
                           orientation='vertical')

# add the events to the axis
ax.add_collection(xevents1)
ax.add_collection(xevents2)
ax.add_collection(yevents1)
ax.add_collection(yevents2)

# display the plot
plt.show()

#-----------------------------------------------

#自然增加 圖表

x = ['%d'%i for i in range(90,110)]
y = Nature

fig, ax = plt.subplots()

# Using set_dashes() to modify dashing of an existing line
line1, = ax.plot(x, y, label='自然增加人數')
line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break

plt.minorticks_on()

plt.xlabel('年份', size=16)
plt.ylabel('人數', size=16,rotation=0,ha='right')
ax.legend()
plt.show()

#-----------------------------------------------

#65歲以上老人 圖表

fig = plt.figure(figsize=(12,6),facecolor='skyblue')

ax1 = fig.add_subplot(1,1,1)
ax1.bar([i-0.17 for i in range(90,110)], Old65man, color='brown',width=0.3,label='男')
ax1.bar([i+0.17 for i in range(90,110)], Old65women, color='orange',width=0.3,label='女')

plt.title('65歲以上人口 90-109年')
plt.xlabel('年份',size=16)
plt.ylabel('人口/百萬',size=16,rotation=0,ha='right')
plt.ylim(200000,2000000)
plt.xticks([i for i in range(90,110)])
plt.legend()
plt.show()

#-----------------------------------------------

# Aging Society高齡化社會 圖表

fig = plt.figure(figsize=(12,6),facecolor='orange')
plt.bar([i for i in range(90,110)],AgingSociety,
         color='lightgreen',label='%')

plt.title('老年人口 占總比例')
plt.xlabel('年')
plt.ylabel('%數',rotation=0,ha='right')
plt.minorticks_on()
plt.xticks([i for i in range(90,110)])

plt.legend()
plt.show()

#----------------------------------------------------

# 把安養中心資料分類

NHouse = [] #安養院數量
NHousePerson = [] #安養院可容納人數
NHtotalperson = [] #安養院已容納人數
NHouseMan = [] #安養院 男
NHouseWomen = [] #安養院 女

for among in NH:
    fn1 = among[1]
    fn2 = among[2]
    fn3 = among[3]
    fn4 = among[4]
    fn5 = among[5]
    NHouse.append(fn1)
    NHousePerson.append(fn2)
    NHtotalperson.append(fn3)
    NHouseMan.append(fn4)
    NHouseWomen.append(fn5)

x = list(map(int,NHousePerson)) #安養院容納人數 轉成int
y = list(map(int,NHtotalperson)) #安養院已容納人數 轉乘int

NHfullpercent = []
for i in range(6):
    z = y[i]/x[i]
    c = z*100   
    NHfullpercent.append(str('%.2f'%(c)))

#---------------------------------------------------------

#安養院統計圖

years = [i for i in range(2015,2021)]

fig,ax1 = plt.subplots()
plt.xlabel('年份')
ax2 = ax1.twinx()

ax1.set_ylabel('人數', color='skyblue',rotation=0,ha='right')
ax1.plot(years,NHousePerson, color='skyblue',label='安養院容納數量')
ax1.tick_params(axis='y', labelcolor='skyblue')
ax1.plot(years,NHtotalperson, color='red',label='總人數')

ax2.set_ylabel('%', color='black',rotation=0,ha='left')
ax2.plot(years,NHfullpercent, color='black')
ax2.tick_params(axis='y', labelcolor='black')

ax1.legend()
plt.show()

#---------------------------------------------------------

#全國&65歲以上人口 圖表

fig,ax1 = plt.subplots()
plt.xlabel('年份')
ax2 = ax1.twinx()

ax1.set_ylabel('人數/千萬', color='green',rotation=0,ha='right')
ax1.plot(N2,TotalPerson, color='green',label='全國人口')

ax2.set_ylabel('人數/百萬', color='red',rotation=0,ha='left')
ax2.plot(N2,olD65, color='red',label='65歲以上人口')
ax2.tick_params(axis='y', labelcolor='black')
plt.xticks([i for i in range(90,110)])
ax1.legend()
ax2.legend(loc='lower right')

plt.show()

#---------------------------------------------------------
#65歲以上老人各地分布圖

T = [i for i in range(90,110)]
plt.figure(figsize=(9,6))
plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['font.size'] = 12

plt.title('歷年老人人口')
plt.ylabel('人口/百萬',rotation=0,ha='right')
plt.plot(T,UP65NORTH,color='b',label='北部')
plt.plot(T,UP65MID,color='g',label='中部')
plt.plot(T,UP65SOUTH,color='r',label='南部')

plt.ylim(400000,1750000)
plt.xticks([i for i in range(90,110)])

plt.legend()
plt.show()

plt.figure(figsize=(9,6))
plt.title('歷年老人人口')
plt.ylabel('人口',rotation=0,ha='right')
plt.plot(T,UP65EAST,color='b',label='東部')
plt.plot(T,UP65OUT,color='g',label='外島')
plt.ylim(10000,500000)
plt.xticks([i for i in range(90,110)])

plt.legend()
plt.show()

#---------------------------------------------------
#全國人口 北中南東 外島 分布

plt.figure(figsize=(9,6))
plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['font.size'] = 12

plt.title('全國人口 北中南分布')
plt.ylabel('人口/千萬',rotation=0,ha='right')
plt.plot(T,TotalpersonNORTH,color='b',label='北部')
plt.plot(T,TotalpersonMID,color='g',label='中部')
plt.plot(T,TotalpersonSOUTH,color='r',label='南部')

plt.ylim(5000000,12000000)
plt.xticks([i for i in range(90,110)])

plt.legend()
plt.show()

plt.figure(figsize=(9,6))
plt.title('全國人口 東 外島 分布')
plt.ylabel('人口/百萬',rotation=0,ha='right')
plt.plot(T,TotalpersonEAST,color='b',label='東部')
plt.plot(T,TotalpersonOUT,color='g',label='外島')
plt.ylim(15000,1500000)
plt.xticks([i for i in range(90,110)])

plt.legend()
plt.show()

#----------------------------------------------------

#90-109 老年人口比例分布
NORTH90to109 = []
MID90to109 = []
SOUTH90to109 = []
EAST90to109 = []
OUT90to109 = []
for k in range(20):
    D1 = UP65NORTH[k] / TotalpersonNORTH[k] * 100
    D2 = UP65MID[k] / TotalpersonMID[k] * 100
    D3 = UP65SOUTH[k] / TotalpersonSOUTH[k] * 100
    D4 = UP65EAST[k] / TotalpersonEAST[k] * 100
    D5 = UP65OUT[k] / TotalpersonOUT[k] * 100
    D6 = str('%.2f'%(D1))
    D7 = str('%.2f'%(D2))
    D8 = str('%.2f'%(D3))
    D9 = str('%.2f'%(D4))
    D10 = str('%.2f'%(D5))
    NORTH90to109.append(D6)
    MID90to109.append(D7)
    SOUTH90to109.append(D8)
    EAST90to109.append(D9)
    OUT90to109.append(D10)
North90to109 = list(map(float,NORTH90to109))
Mid90to109 = list(map(float,MID90to109))
South90to109 = list(map(float,SOUTH90to109))
East90to109 = list(map(float,EAST90to109))
Out90to109 = list(map(float,OUT90to109))

#----------------------------------------------------

#高齡化 北中南東外島 比例

T = [i for i in range(90,110)]
plt.figure(figsize=(9,6))
plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['font.size'] = 12

plt.title('高齡化 北中南東外島 比例')
plt.ylabel('比例',rotation=0,ha='right')
plt.plot(T,North90to109,color='b',label='北部')
plt.plot(T,Mid90to109,color='g',label='中部')
plt.plot(T,South90to109,color='r',label='南部')
plt.plot(T,East90to109,color='black',label='東部')
plt.plot(T,Out90to109,color='purple',label='外島')

plt.ylim(5,18)
plt.xticks([i for i in range(90,110)])

plt.legend()
plt.show()
    
#---------------------------------------------------

# 2015-2020 年 各地區安養院分布

nhNorth = [0,0,0,0,0,0]
nhMid = [0,0,0,0,0,0]
nhSouth = [0,0,0,0,0,0]
nhEast = [0,0,0,0,0,0]
nhOut = [0,0,0,0,0,0]

def YEAR(year): 
    ap = []
    data = pd.read_excel(r'C:\Users\Siou\Desktop\專題\安養機構資料.xls',
                     sheet_name= year,usecols='A:G')
    INFO1 = data.iloc[11:33,2:3]
    r = INFO1.values
    for a in range(22):
        key = r[a][0]
        ap.append(key)
    return ap
    
year2015 = YEAR('2015年')        
year2016 = YEAR('2016年') 
year2017 = YEAR('2017年') 
year2018 = YEAR('2018年') 
year2019 = YEAR('2019年') 
year2020 = YEAR('2020年') 
def ASD(k,j):
    for z in k:
        data1 = year2015[z]
        data2 = year2016[z]
        data3 = year2017[z]
        data4 = year2018[z]
        data5 = year2019[z]
        data6 = year2020[z]
        j[0]+= data1
        j[1]+= data2
        j[2]+= data3
        j[3]+= data4
        j[4]+= data5
        j[5]+= data6
ASD(north2,nhNorth)
ASD(mid2,nhMid)
ASD(south2,nhSouth)
ASD(east2,nhEast)
ASD(out2,nhOut)

#2014
a = ['Unnamed: 3','Unnamed: 12','Unnamed: 21','Unnamed: 30','Unnamed: 39','Unnamed: 42']
a1 = [36,51,66,81,96,111,126,141,156,171,
     186,201,216,231,246,261,276,291,306,321,336,351]
FA = []
FB = []
FC = []
FD = []
FE = []
FF = []
data = pd.read_excel(r'C:\Users\Siou\Desktop\專題\安養機構資料.xls',
                     sheet_name= '2014',usecols='A:AW')
data.fillna('0')
for j in a1:
    A = data[a[0]][j]
    B = data[a[1]][j]
    C = data[a[2]][j]
    D = data[a[3]][j]
    E = data[a[4]][j]
    F = data[a[5]][j]
    FA.append(A)
    FB.append(B)
    FC.append(C)
    FD.append(D)
    FE.append(E)
    FF.append(F)
FFF = []    
for i in range(22):
    BB = FA[i] + FB[i] + FC[i] + FD[i] + FE[i] + FF[i]   
    FFF.append(BB)
    
#2014年北中南東外島分布 
NORTH2014 = [0]
MID2014 = [0]
SOUTH2014 = [0]
EAST2014 = [0]
OUT2014 = [0]

north1 = [0,1,6,7,17,18]
mid1 = [2,8,9,10,11]
south1 = [3,4,12,13,19]
east1 = [5,14,15]
out1 = [16,20,21]

def NNN(ya,na):
    for i in ya:
        D = FFF[i]
        na[0] +=D
NNN(north1,NORTH2014)
NNN(mid1,MID2014)
NNN(south1,SOUTH2014)
NNN(east1,EAST2014)
NNN(out1,OUT2014)

nhNorth.insert(0,NORTH2014[0])
nhMid.insert(0,MID2014[0])
nhSouth.insert(0,SOUTH2014[0])
nhEast.insert(0,EAST2014[0])
nhOut.insert(0,OUT2014[0])

#--------------------------------------------------

#安養院及老人比例

nnnNorth = []
nnnMid = []
nnnSouth = []
nnnEast = []
nnnOut = []

a = 0
b = [14,15,16,17,18,19,20]

def KK(m,n):
      z = '%.4f'%(nhNorth[m] / UP65NORTH[n]*100)
      x = '%.4f'%(nhMid[m] / UP65MID[n]*100)
      c = '%.4f'%(nhSouth[m] / UP65SOUTH[n]*100)
      v = '%.4f'%(nhEast[m] / UP65EAST[n]*100)
      b = '%.4f'%(nhOut[m] / UP65OUT[n]*100)
      nnnNorth.append(z)
      nnnMid.append(x)
      nnnSouth.append(c)
      nnnEast.append(v)
      nnnOut.append(b)
KK(0,13)
KK(1,14)
KK(2,15)
KK(3,16)
KK(4,17)
KK(5,18)
KK(6,19)

NNNNorth = list(map(float,nnnNorth))
NNNMid = list(map(float,nnnMid))
NNNSouth = list(map(float,nnnSouth))
NNNEast = list(map(float,nnnEast))
NNNOut = list(map(float,nnnOut))

H = [i for i in range(103,110)]
plt.figure(figsize=(9,6))
plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['font.size'] = 12

plt.title('安養院及老人比例 北中南')
plt.ylabel('百分比',rotation=0,ha='right')
plt.plot(H,NNNNorth,color='b',label='北部')
plt.plot(H,NNNMid,color='g',label='中部')
plt.plot(H,NNNSouth,color='r',label='南部')

plt.ylim(0,0.05)
plt.xticks([i for i in range(103,110)])

plt.legend()
plt.show()

plt.figure(figsize=(9,6))
plt.title('安養院及老人比例 東 外島')
plt.ylabel('百分比',rotation=0,ha='right')
plt.plot(H,NNNEast,color='b',label='東部')
plt.plot(H,NNNOut,color='g',label='外島')
plt.ylim(0,0.05)
plt.xticks([i for i in range(103,110)])

plt.legend()
plt.show()