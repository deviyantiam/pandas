## melt
## pivot dan pivot_table
## concat
## crosstab
## merge

#import pandas as pd
#import numpy as np
# asean=[
#     {'negara':'Indonesia','kota':'Jakarta','suhu':34},
#     {'negara':'Malaysia','kota':'Kuala Lumpur','suhu':35},
#     {'negara':'Singapura','kota':'Singapura','suhu':32},
#     {'negara':'Thailand','kota':'Bangkok','suhu':35}]
# dfAsean=pd.DataFrame(asean)
# print(dfAsean)
#eropa=[
#     {'negara':'Inggris','kota':'London','suhu':27},
#     {'negara':'Italia','kota':'Roma','suhu':23},
#     {'negara':'Perancis','kota':'Paris','suhu':22},
#     {'negara':'Spanyol','kota':'Madrid','suhu':29}
# ]
# dfEropa=pd.DataFrame(eropa)
# print(dfEropa)

# eropa1=[
#     {'negara':'Inggris','kota':'London','angin':9},
#     {'negara':'Italia','kota':'Roma','suhu':11}
# ]
# dfEropa1=pd.DataFrame(eropa1)
# print(dfEropa)

##concatenating=merge 2 data frames
#dfAseanEropa=pd.concat([dfAsean,dfEropa],ignore_index=True) #index urut
#print(dfAseanEropa.iloc[0:2])
# dfAseanEropa=pd.concat([dfAsean,dfEropa],keys=['asia tenggara','europe'],
#     #ignore_index=True #ngga ada keys
#     )
# print(dfAseanEropa)
#print(dfAseanEropa.loc['asia tenggara'])
#print(dfAseanEropa.loc['europe'])

##concat dimensi sama, kolom beda
#dfAE=pd.concat([dfEropa1,dfAsean],keys=['europe','asia tenggara'])
#print(dfAE)
'''
                 angin          kota     negara  suhu
europe        0    9.0        London    Inggris   NaN
              1    NaN          Roma     Italia  11.0
asia tenggara 0    NaN       Jakarta  Indonesia  34.0
              1    NaN  Kuala Lumpur   Malaysia  35.0
              2    NaN     Singapura  Singapura  32.0
              3    NaN       Bangkok   Thailand  35.0
'''

#dfAE=pd.concat([dfEropa1,dfAsean],axis=1,keys=['europe','asia tenggara'])
#print(dfAE)
#print(dfAE.iloc[2])
'''
  europe                        asia tenggara                
   angin    kota   negara  suhu          kota     negara suhu
0    9.0  London  Inggris   NaN       Jakarta  Indonesia   34
1    NaN    Roma   Italia  11.0  Kuala Lumpur   Malaysia   35
2    NaN     NaN      NaN   NaN     Singapura  Singapura   32
3    NaN     NaN      NaN   NaN       Bangkok   Thailand   35
europe         angin           NaN
               kota            NaN
               negara          NaN
               suhu            NaN
asia tenggara  kota      Singapura
               negara    Singapura
               suhu             32
Name: 2, dtype: object
'''
# dfAE=pd.concat([dfEropa1,dfAsean],axis=0,keys=['europe','asia tenggara'])
# print(dfAE.iloc[4])
'''
            angin          kota     negara  suhu
europe        0    9.0        London    Inggris   NaN
              1    NaN          Roma     Italia  11.0
asia tenggara 0    NaN       Jakarta  Indonesia  34.0
              1    NaN  Kuala Lumpur   Malaysia  35.0
              2    NaN     Singapura  Singapura  32.0
              3    NaN       Bangkok   Thailand  35.0
angin           NaN
kota      Singapura
negara    Singapura
suhu             32
Name: (asia tenggara, 2), dtype: object
'''


#####
## concate 2 data yang memiliki salah satu properti yang sama
# import pandas as pd
# import numpy as np

# usiaSiswa={
#     'nama':['Andi','Budi','Cici','Deni'],
#     'usia':[20,21,22,23]
# }
# kotaSiswa={
#     'nama':['Budi','Cici'],
#     'kota':["Jakarta","Bandung"]
# }
# dfUsia=pd.DataFrame(usiaSiswa)
# dfKota=pd.DataFrame(kotaSiswa)
# dfSiswa=pd.concat([dfUsia,dfKota])
# print(dfSiswa)
'''
      kota  nama  usia
0      NaN  Andi  20.0
1      NaN  Budi  21.0
2      NaN  Cici  22.0
3      NaN  Deni  23.0
0  Jakarta  Budi   NaN
1  Bandung  Cici   NaN
'''
# dfSiswa=pd.concat([dfUsia,dfKota],axis=1)
# print(dfSiswa)
'''
   nama  usia  nama     kota
0  Andi    20  Budi  Jakarta
1  Budi    21  Cici  Bandung
2  Cici    22   NaN      NaN
3  Deni    23   NaN      NaN
'''
# dfUsia=pd.DataFrame(usiaSiswa,index=[0,1,2,3])
# dfKota=pd.DataFrame(kotaSiswa,index=[1,2])
# dfSiswa=pd.concat([dfUsia,dfKota],axis=1)
# print(dfSiswa)
'''
   nama  usia  nama     kota
0  Andi    20   NaN      NaN
1  Budi    21  Budi  Jakarta
2  Cici    22  Cici  Bandung
3  Deni    23   NaN      NaN
'''
##inner join by default
# dfUsia=pd.DataFrame(usiaSiswa)
# dfKota=pd.DataFrame(kotaSiswa)
# dfSiswa=pd.merge(dfUsia,dfKota,on='nama')
# print(dfSiswa)
'''
   nama  usia     kota
0  Budi    21  Jakarta
1  Cici    22  Bandung
'''
# kotaSiswa1={
#     'nama':['Budi','Cici','Deni','Andi'],
#     'kota':["Jakarta","Bandung","Sorong","Aceh"]
# }
# dfUsia=pd.DataFrame(usiaSiswa)
# dfKota1=pd.DataFrame(kotaSiswa1)
# dfSiswa=pd.merge(dfUsia,dfKota1,on='nama')
# print(dfSiswa)
'''
   nama  usia     kota
0  Andi    20     Aceh
1  Budi    21  Jakarta
2  Cici    22  Bandung
3  Deni    23   Sorong
'''
##outer join tampilkan semua
# dfUsia=pd.DataFrame(usiaSiswa)
# dfKota=pd.DataFrame(kotaSiswa)
# dfSiswa=pd.merge(dfUsia,dfKota,on='nama',how='outer')
# print(dfSiswa)
'''
   nama  usia     kota
0  Andi    20      NaN
1  Budi    21  Jakarta
2  Cici    22  Bandung
3  Deni    23      NaN
'''
##right join tampilkan semua yang kanan
# dfUsia=pd.DataFrame(usiaSiswa)
# dfKota=pd.DataFrame(kotaSiswa)
# dfSiswa=pd.merge(dfUsia,dfKota,on='nama',how='right')
# print(dfSiswa)
'''
   nama  usia     kota
0  Budi    21  Jakarta
1  Cici    22  Bandung
'''
##left join tampilkan semua yang left
# dfUsia=pd.DataFrame(usiaSiswa)
# dfKota=pd.DataFrame(kotaSiswa)
# dfSiswa=pd.merge(dfUsia,dfKota,on='nama',how='left')
# print(dfSiswa)
'''
   nama  usia     kota
0  Andi    20      NaN
1  Budi    21  Jakarta
2  Cici    22  Bandung
3  Deni    23      NaN
'''
usiaSiswa0={
    'nama':['Andi','Budi','Cici','Deni'],
    'usia':[11,12,13,14]
}
usiaSiswa1={
    'nama':['Andi','Budi','Cici','Deni'],
    'usia':[19,20,21,22]
}
# dfUsia0=pd.DataFrame(usiaSiswa0)
# dfUsia1=pd.DataFrame(usiaSiswa1)
# dfUsia=pd.merge(dfUsia0,dfUsia1,on='nama')
# print(dfUsia)
'''
   nama  usia_x  usia_y
0  Andi      11      19
1  Budi      12      20
2  Cici      13      21
3  Deni      14      22
'''
# dfUsia0=pd.DataFrame(usiaSiswa0)
# dfUsia1=pd.DataFrame(usiaSiswa1)
# dfUsia=pd.merge(dfUsia0,dfUsia1,on='nama',suffixes=['_sebelum','_sesudah'])
# print(dfUsia)
'''
   nama  usia_sebelum  usia_sesudah
0  Andi            11            19
1  Budi            12            20
2  Cici            13            21
3  Deni            14            22
'''

#####
##pivot
# import pandas as pd
# import numpy as np
# bmkg=[{'tanggal':'01-02-2019','kota':'Jakarta','suhu':32,'angin':9},
#     {'tanggal':'02-02-2019','kota':'Jakarta','suhu':34,'angin':11},
#     {'tanggal':'03-02-2019','kota':'Jakarta','suhu':31,'angin':8},
#     {'tanggal':'01-02-2019','kota':'Bandung','suhu':22,'angin':12},
#     {'tanggal':'02-02-2019','kota':'Bandung','suhu':20,'angin':14},
#     {'tanggal':'03-02-2019','kota':'Bandung','suhu':21,'angin':13}]
# dfBmkg=pd.DataFrame(bmkg)
#print(dfBmkg)
'''
    angin     kota  suhu     tanggal
0      9  Jakarta    32  01-02-2019
1     11  Jakarta    34  02-02-2019
2      8  Jakarta    31  03-02-2019
3     12  Bandung    22  01-02-2019
4     14  Bandung    20  02-02-2019
5     13  Bandung    21  03-02-2019
'''
# x=dfBmkg.pivot(index='tanggal',columns='kota')
# print(x)
# print(x.loc['03-02-2019','angin'])
'''
             angin            suhu        
kota       Bandung Jakarta Bandung Jakarta
tanggal                                   
01-02-2019      12       9      22      32
02-02-2019      14      11      20      34
03-02-2019      13       8      21      31
kota
Bandung    13
Jakarta     8
Name: 03-02-2019, dtype: int64
'''
# x=dfBmkg.pivot(index='tanggal',columns='kota')['suhu']
# print(x)
'''
kota        Bandung  Jakarta
tanggal                     
01-02-2019       22       32
02-02-2019       20       34
03-02-2019       21       31
'''
# grup=dfBmkg.groupby('kota')
# djkt=grup.get_group('Jakarta')
# print(djkt)
'''
   angin     kota  suhu     tanggal
0      9  Jakarta    32  01-02-2019
1     11  Jakarta    34  02-02-2019
2      8  Jakarta    31  03-02-2019
'''
## Hitung mean, sum, count
# x=dfBmkg.pivot_table(index='kota',columns='tanggal',aggfunc='sum')['angin'] #ga tampil 'All'
# print(x)
# x=dfBmkg.pivot_table(index='kota',columns='tanggal',aggfunc='sum',margins=True)['angin']
# print(x)
# y=dfBmkg.pivot_table(index='kota',columns='tanggal',aggfunc='mean',margins=True)['angin']
# print(y)
# z=dfBmkg.pivot_table(index='kota',columns='tanggal',aggfunc='count',margins=True)['angin']
# print(z)
# xx=dfBmkg.pivot_table(index='kota',columns='tanggal',aggfunc=['count','mean'],margins=True) #gabisa pake angin aja
# print(xx)

#####
##melt
import pandas as pd
import numpy as np
bmkg=[{'tanggal':'01-02-2019','Jakarta':32,"Bandung":21},
    {'tanggal':'02-02-2019','Jakarta':31,"Bandung":22},
    {'tanggal':'03-02-2019','Jakarta':33,"Bandung":21},
    {'tanggal':'04-02-2019','Jakarta':31,"Bandung":20},
    {'tanggal':'05-02-2019','Jakarta':32,"Bandung":23},
    {'tanggal':'06-02-2019','Jakarta':34,"Bandung":24}]
# dfBmkg=pd.DataFrame(bmkg)
#print(dfBmkg)
# x=pd.melt(dfBmkg,id_vars=['tanggal'],var_name='kota',value_name='suhu')
#print(x)
'''
       tanggal     kota  suhu
0   01-02-2019  Bandung    21
1   02-02-2019  Bandung    22
2   03-02-2019  Bandung    21
3   04-02-2019  Bandung    20
4   05-02-2019  Bandung    23
5   06-02-2019  Bandung    24
6   01-02-2019  Jakarta    32
7   02-02-2019  Jakarta    31
8   03-02-2019  Jakarta    33
9   04-02-2019  Jakarta    31
10  05-02-2019  Jakarta    32
11  06-02-2019  Jakarta    34
'''
#print(x[x['kota']=='Jakarta'])
'''
tanggal     kota  suhu
6   01-02-2019  Jakarta    32
7   02-02-2019  Jakarta    31
8   03-02-2019  Jakarta    33
9   04-02-2019  Jakarta    31
10  05-02-2019  Jakarta    32
11  06-02-2019  Jakarta    34
'''
## tunjukin frekuensi datanya ada berapa
# x=pd.crosstab(dfBmkg['tanggal'],dfBmkg['Bandung'])
# print(x)
'''
Bandung     20  21  22  23  24
tanggal                       
01-02-2019   0   1   0   0   0
02-02-2019   0   0   1   0   0
03-02-2019   0   1   0   0   0
04-02-2019   1   0   0   0   0
05-02-2019   0   0   0   1   0
06-02-2019   0   0   0   0   1
'''
bmkg1=[
    {'nama':"Andi","usia":20,"status":"Nikah","kota":"Jakarta","gender":"L"},
    {'nama':"Budi","usia":21,"status":"Belum","kota":"Bandung","gender":"L"},
    {'nama':"Caca","usia":21,"status":"Belum","kota":"Jakarta","gender":"P"},
    {'nama':"Deni","usia":23,"status":"Belum","kota":"Denpasar","gender":"L"},
    {'nama':"Euis","usia":24,"status":"Nikah","kota":"Denpasar","gender":"P"},
    {'nama':"Fafa","usia":25,"status":"Nikah","kota":"Bandung","gender":"P"}]
dfBmkg1=pd.DataFrame(bmkg1)
# x=pd.crosstab(dfBmkg1.kota,dfBmkg1['status'],margins=True) #margins tampilkan all
# print(x)
'''
status    Belum  Nikah  All
kota                       
Bandung       1      1    2
Denpasar      1      0    1
Jakarta       0      3    3
All           2      4    6
'''
# x=pd.crosstab(dfBmkg1.gender,[dfBmkg1['status'],dfBmkg1['kota']],margins=True) #margins tampilkan all
# print(x)
'''
status   Belum                    Nikah                  All
kota   Bandung Denpasar Jakarta Bandung Denpasar Jakarta    
gender                                                      
L            1        1       0       0        0       1   3
P            0        0       1       1        1       0   3
All          1        1       1       1        1       1   6
'''
# x=pd.crosstab(dfBmkg1.gender,dfBmkg1['kota'],normalize='index',margins=True) #tampilkan rata2 persen 0-1 perbaris
# print(x)
# x=pd.crosstab(dfBmkg1.gender,dfBmkg1['kota'],normalize='columns',margins=True) #perkolom
# print(x)
'''
kota     Bandung  Denpasar   Jakarta
gender                              
L       0.333333  0.333333  0.333333 total kesamping 1
P       0.333333  0.333333  0.333333 total kesamping 1
All     0.333333  0.333333  0.333333 total kesamping 1
kota    Bandung  Denpasar  Jakarta  All
gender                                 
L           0.5       0.5      0.5  0.5 kebawah 1
P           0.5       0.5      0.5  0.5 kebawah 1
'''
##Rata-rata usia yang belum/nikah berdasarkan gender
x=pd.crosstab(dfBmkg1.gender,dfBmkg1['status'],values=dfBmkg1.usia,aggfunc='mean')
print(x)
'''
status  Belum  Nikah
gender              
L        22.0   20.0
P        21.0   24.5
'''

