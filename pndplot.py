import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_excel('https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx',sheet_name='Canada by Citizenship',skiprows=range(20),skipfooter=2)
# print(df.head())
years=list(map(int,range(1980,2014))) #applies a given function to each element and return the result
# print(list(df))
# print(df[df['OdName']=='Australia'].index.item())
dfc=df.set_index('OdName')
# print(dfc.head())

##LINE CHART
# dfc.loc['Australia',years].plot(kind='line')
# plt.title('Immigration from Australia')
# plt.ylabel('Number of Immigrants')
# plt.xlabel('Years')
# plt.show()

##STACKED AREA CHART
dfc['Total']=dfc[years].sum(axis=1)
dfc.sort_values(['Total'],ascending=False,inplace=True) #inplace=True no assign, False assign to var
dfc_top5=dfc.head()
# dfc_top5=dfc_top5[years].transpose()
# print(dfc_top5)
# dfc_top5.plot(kind='area') 
# plt.title('Immigration trend of top 5 countries')
# plt.ylabel('Number of Immigrants')
# plt.xlabel('Years')
# plt.show()

##HISTOGRAM CANADA
# print(list(dfc))
# count,bin_edges=np.histogram(dfc[2013])
# dfc[2013].plot(kind='hist',xticks=bin_edges)
# plt.title('Histogram of immigration from {} countries in 2013'.format(len(dfc)))
# plt.ylabel('Number of Countries')
# plt.xlabel('Number of Immigrants')
# plt.show()

##BAR ICELAND
dfi=dfc.loc['Iceland',years]
# #plt.bar(years,dfi[years])
# #plt.xlim(1980,2013)
# #plt.xticks(np.arange(1980,2013,1))
# dfi.plot(kind='bar') #'barh' horizontal
# plt.title('Icelandic imigrants to Canada')
# plt.xlabel('year')
# plt.ylabel('number of immigrants')
# plt.show()

##PIE BY CONTINENT
# df_con=dfc.groupby('AreaName',axis=0).sum()
# df_con['Total'].plot(kind='pie')
# plt.title('Immigration to Canda by continent')
# plt.show()

##BOX 
# dfj=dfc.loc[['Japan'],years].transpose()
# dfj.plot(kind='box')
# plt.title('Box plot of Japanase Immigrants')
# plt.ylabel('Number of Immigrants')
# plt.show()

##SCATTER
# dfc_new=df[years].transpose()
# dfc_new['Totalc']=dfc_new[0:194].sum(axis=1)
# dfc_new['year']=np.arange(1980,2014)
# dfc_new=dfc_new.loc[:,['year','Totalc']]
# print(dfc_new.head())
# dfc_new.plot(kind='scatter',x='year',y='Totalc')
# plt.title('Total Immigrant population to Canada')
# plt.xlabel('Year')
# plt.ylabel('Total',fontsize=10)
# plt.tick_params(axis = 'y', color = 'black', colors = 'black', labelsize = 'small')
# plt.show()







