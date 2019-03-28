## conditions

'''
## print(df['Column'][condition])
## eg. print(df['Name'][df['Age']==df['Age'].max()])
'''

import pandas as pd
df=pd.read_csv('data.csv')
# print(df.head()) #5 baris
# print(df.loc[0:5,['Name','Age','Nationality']])
# print(df['Age'].max())
# print(df['Age'].min())
# print(df.describe())
# print(df[df['Age']==df['Age'].max()])
# print(df[['Name','Age']][df['Age']==df['Age'].max()]) #atau kayak yang dibawah
# print(df[df['Age']==df['Age'].max()][['Name','Age']])
# print(df[['Name','Position','Club','Overall']][df['Overall']>=90][df['Club']=='Real Madrid'])

df2=df[['Name','Position','Club','Overall']][df['Overall']>=90]
df2=df2[df['Club']=='Real Madrid']
print(df2.iloc[0])

#==================================================================
import pandas as pd
df=pd.read_json('data21.json')
print(df['nama'][df['usia']==df['usia'].max()])

#==================================================================
## OPEN EXCEL AND CONVERT TO ANOTHER TYPE OF FILE
## pip install xlrd
## pip install openpyxl

import pandas as pd
df=pd.read_excel('data21.xlsx','Sheet1',header=2) #element ke 2 mau jd header, index 1
# df2=pd.read_excel('data21.xlsx','Sheet2')
# df=df.loc[:,['No','Nama','Usia','Kota']]
# df.to_csv('data21excel.csv')
# df.to_json('data21excel.json')
# df.to_excel('databaru.xls')
#print(df[df['Usia']==df['Usia'].max()])
#print(df[df['Usia']==22].index.items()) #dapet indexnya

#==================================================================
import pandas as pd
df=pd.read_json('data21excel.json')
df.to_json('data21excel.json',orient='index') #{col=val}
 