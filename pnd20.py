# series
# data frame
# np.rand

#series
import pandas as pd
x=[1,2,3,4,5,6,7,8,9]
y=['Andi','Budi','Caca','Deni','Euis']
seriesku=pd.Series(x)
serieskuy=pd.Series(y,index=['a','b','c','d','e'])
##nama kolom di baris pertama
##indeks yang dikiri
##isi di kanan
# print(x)
# print(seriesku)
print(serieskuy['a'])
print(seriesku[0::2])

#==================================================================
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
# x=np.random.rand(1,10) #random 1 dimensi, 10 angka 0-1
# x=np.random.randint(10,size=10) # nilai max 10, size=(2,4)
y=np.random.randint(10,size=10) 
# z='abcdefghij'
# a=[('Andi',21,'S1'),('Budi',25,'S1'),
# ('Caca',22,'S2'),('Deni',24,'S1')]

# data={'id':[1,2,3,4],
# 'nama':["Andi","Budi",'Caca','Deni'],
# 'job':['Programmer','Designer','Insinyur','PNS']}
# dic=[{"nama":"Andi","usia":23},{"nama":"Budi","usia":21},{"nama":"Caca","usia":24}]
# s=pd.Series(x, index=np.arange(1,11,1))
# d=pd.DataFrame(x) # ada index diatas kolom
# dy=pd.DataFrame([x,y]) #x baris pertama, y baris kedua
# ds=pd.DataFrame([x,y,z])
# da=pd.DataFrame(a,index=['a','b','c','d'],columns=['Nama','Usia','Pendidikan'])
# db=pd.DataFrame(data)
# print(db)
# dc=pd.DataFrame(dic,index=['a','b','c'])
# print(dc)
# print(s)
# print(d)
# print(dy)
# print(ds)
# print(da['Nama'])
# print(da.loc['b'])

#==================================================================
coba={"satu":"hai","dua":np.arange(10),'tiga':pd.Series(y),"empat":pd.Timestamp('20190220'),"lima":pd.date_range('20190220',periods=10)}
# dk=pd.DataFrame(coba)#,index=list('abcdefghij'))
# for x in dk.values:
#     print(x[0])
# print(dk.head()) #lima line terakhir
# print(dk.tail(6)) #satu row terakhir
# print(dk.index)
# print(dk['satu'])
# print(dk[0:3])
# print(dk.columns)
# print(dk.values[0][0]) #kolom pertama ##index urutan bukan index nama
# print(dk.sort_index(axis=1)) #abjad kolom
# print(dk.sort_index(axis=0, ascending=False)) #baris
# print(dk.sort_values(by=['tiga','dua'],ascending=[False,True])) #urutin 'tiga' lalu 'dua'
# print(dk[2:3])
# print(dk[0:2]) #0-2 sama kyk loc dibawah
# print(df.describe())
# print(dk.loc[0:3]) #0-3 #loc=by index name, kalau indexnya alphabet, maka index yg dipanggil harus alphabet
# print (dk.iloc[:3,[0,2]]) #posisi 3 pertama, kolom 1,3
# print(dk.iloc[:3,[0:2]]) # kolom index 0,1
df=pd.DataFrame(coba,index=list('abcdefghij')) #pd.Series gabisa
print(df)
print(df.at['a','satu']) #yang ada a nya di key satu
print(df.iat[1,3]) #kolom index 3/ke 4, baris index 1 atau ke 2 isinya apa
# print(df.T) #Transpose baris jadi kolom
# print(dk.loc[0:3,['satu','tiga']])
# print(dk.loc[2]) #jabarin perkolom baris ke index 2
# i=plt.subplot2grid((1,1),(0,0))
# i.plot(dk["lima"],dk["tiga"])
# plt.xticks(rotation=90)
# i.tick_params(axis = 'both', color = 'black', colors = 'red', labelsize = 'small') #color = warna tick marker pada axis, colors = warna font axis 
# plt.show()

#==================================================================
# a=pd.Series(y)
# a=pd.Series([0,2,4,6,8])
# b=pd.Series([0,4,16,32,64])
# print(a)
# # plt.plot(a,a)
# plt.plot(a,b)
# plt.scatter(a,b,marker='o',s=200,color='green')
# plt.show()

#==================================================================
### GANTI ROW JADI NAMA KOLOM
df = pd.DataFrame([(1,2,3), ('foo','bar','baz'), (4,5,6)])
# df.columns = df.iloc[1]
# df=df.reindex(df.index.drop(1))
# print(df)

headers = df.loc[1]
new_df  = pd.DataFrame(df.values[0:], columns=headers)
# aja=np.arange(0,2)
# new_df=new_df.drop([1])
# new_df=new_df.reindex(aja)
##hasil row 1=NaN
print(new_df)

##DELETE COLUMN
# df=df.drop(['namacolum'],axis=1)