#sort_values
#fillna
#interpolate
#get_group
#dropna
#replace
#ffill


# import pandas as pd
# df=pd.read_csv('data22.csv',header=None, #atau bisa juga header=-1 untuk baris pertama tidak jadi header
#    names=['id','nama','usia','massa']) 
# print(df) #id bagian dari data
# df=df.set_index('id')#id udah jadi index
# print(df.loc[:,'nama']) 
# print(df['nama'])
# print(df.nama)
# print(df.sort_values(by='nama',ascending=False)[['nama','usia']]) #tampilin nama usia, urutin dari abjad bawah
# print(df.loc[2::2].sort_values(by='nama',ascending=False)[['nama','usia']]) #index yg genap
# print(df['massa'].mean())
'''
kalau ada '-' 'n.a' di data ubah => NaN
'''


import pandas as pd
df=pd.read_csv('data22.csv',header=None, #atau bisa juga header=-1 untuk baris pertama tidak jadi header
    names=['id','nama','usia','massa'],
    na_values=['-','n.a'])
df=df.set_index('id')
## HANDLING MISSING DATA
# df=df.fillna(0) #NaN jadi 0
# df=df.fillna({
#     'massa':0,
#     'usia':0,
#     'nama':'Tanpa Nama'
# })
# df=df.fillna(method='ffill') #forward filling buat ambil data atasnya
# df=df.fillna(method='bfill') #backward ambil dari data bawahnya
# df=df.fillna(method='ffill',axis='columns') #forward ambil dari data yg di kiri
# df=df.fillna(method='bfill',axis='columns') #forward ambil dari data yg di kanan
## Interpolate itu bagus kalau time series
# df=df.interpolate() #nilai tengah antara baris sebelum dan sesudah
# df=df.interpolate().fillna({'nama':'Tanpa Nama'})
# df=df.dropna() #yang ada Nan kehapus
# df=df.dropna(thresh=2) #masih ada 2 values dalam satu baris, ditampilkan
# df =df.dropna(axis='columns') #kalau ada NaN di kolom tertentu, hilang semua
# df =df.dropna(subset=['nama']) #tampilin yang punya nama
#df =df.dropna(subset=['nama','usia']) #tampilin yang ada nama dan usia
print(df)

#==================================================================
import pandas as pd
import numpy as np
df=pd.read_csv('data22.csv',header=None, #atau bisa juga header=-1 untuk baris pertama tidak jadi header
    names=['id','nama','usia','massa'])
df=df.set_index('id')
## SALAH df=df.replace(['-','n.a'],'NaN')
# df=df.replace(['-','n.a'],np.nan) #jangan string NaN, biar bisa di proses
# df=df.fillna('x')
# df=df.replace({
#     '-':0,
#     'n.a':np.nan
# })
# df=df.replace(to_replace=['-','n.a'],method='ffill')
## UBAH yg nama=anonim, usia=0, massa='ffill'
df=df.replace({'nama':['-','n.a'],
    'usia':'-'},{'nama':'Anonim','usia':0})
df['massa']=df['massa'].replace(to_replace=['-','n.a'],method='ffill')
print(df)


##Group by
import pandas as pd
import numpy as np
df=pd.read_csv('data221.csv',header=None,names=['id','nama','usia','massa','kota'])
df=df.set_index('id')
df=df.drop('nama',axis=1) #hapus kolom, hapus baris axis=0
grup=df.groupby('kota')
djkt=grup.get_group('Jakarta')
dbdg=grup.get_group('Bandung')
# print(grup.max()) #nilai maksimum pada informasi di setiap kota
# print(djkt['massa'].mean()) #rata-rata massa pada orang Jakarta
# print(djkt[djkt['massa']>djkt['massa'].mean()]) #orang yang massanya lebih dari mean massa
# print(grup.min())
print(dbdg)