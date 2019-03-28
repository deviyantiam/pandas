##parse date
##resample
##plot

# import pandas as pd
# import matplotlib.pyplot as plt
# dfTelkom=pd.read_csv('TLKM.JK.csv')
#print(dfTelkom)
#print(type(dfTelkom['Date'][0])) #<class str>
# dfXL=pd.read_csv('EXCL.JK.csv',parse_dates=['Date'],index_col='Date')
# dfIsat=pd.read_csv('ISAT.JK.csv',parse_dates=['Date'],index_col='Date')
# dfSfren=pd.read_csv('FREN.JK.csv',parse_dates=['Date'],index_col='Date')
# dfTelkom=pd.read_csv('TLKM.JK.csv',parse_dates=['Date'],index_col='Date') #ubah type jadi date, dan indexnya jadi date
#print(type(dfTelkom['Date'][0])) #<class 'pandas._libs.tslibs.timestamps.Timestamp'>
#print(dfTelkom)
#print(dfTelkom['2018-02']) #bisa diambil kalau timestamp, kalau string ga bisa
#print(dfTelkom['2019-02-08':'2019-02-12'])
#print(dfTelkom.loc['2019-02-18'])
'''
jangan pakai 29-01-2019, karena kalau 03-02-2019 kebaca bulan tanggal
print(dfTelkom['29-01-2019':'31-01-2019'])
'''
# print(dfTelkom['2018-11']['Close'].mean())
# print(dfTelkom['2018-11']['Close'].max())
# print(dfTelkom['2018-11']['Close'].min())
## M: month end; W: per week; D: per day
## tertinggi tiap bulan/ minggu
# print(dfTelkom['Close'].resample('W').max())
## menampilkan yang tidak ditampilkan, yaitu weekend 
#print(dfTelkom['Close'].resample('D').max())
## Isi yang NaN
# dfTelkom=dfTelkom['Close'].resample('W').max().fillna(method='ffill')
# print(dfTelkom)
# dfXL=dfXL['Close'].resample('W').max().fillna(method='ffill')
# dfIsat=dfIsat['Close'].resample('W').max().fillna(method='ffill')
# dfSfren=dfSfren['Close'].resample('W').max().fillna(method='ffill')

# plt.style.use('dark_background')
# plt.plot(dfTelkom,'w-')
# plt.plot(dfTelkom,'y*')
# plt.grid(True)
# plt.xlabel('Tanggal')
# plt.ylabel('Close')
# plt.title('PT. Telekomunikasi Indonesia Tbk')
# plt.plot(dfTelkom)
# plt.show()

# plt.style.use('seaborn')
# plt.plot(dfTelkom,'r-')
# plt.plot(dfXL,'b-')
# plt.plot(dfIsat,'g-')
# plt.plot(dfSfren,'y-')
# plt.plot(dfTelkom,'r*')
# plt.plot(dfXL,'b*')
# plt.plot(dfIsat,'g*')
# plt.plot(dfSfren,'y*')
# plt.grid(True)
# plt.xlabel('Tanggal')
# plt.ylabel('Close')
# plt.legend(['Telkom','Xl','Indosat','Smartfren'])
# plt.plot(dfTelkom)
# plt.show()

###PLOT DF jadi 2 garis
import matplotlib.pyplot as plt
import pandas as pd
b=[1,2]
c=[2,4]
d=[3,6]

x=pd.DataFrame([b,c,d],columns=['apa','siapa'])
x['Total']=x[['apa','siapa']].sum(axis=1)
print(x)
# x.plot(kind='line')
# plt.show()
