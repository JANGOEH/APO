import pandas as pd 
import numpy as np
data = pd.read_csv('C:/Users/jango/Downloads/订单.csv')
data2 = data.loc[:,['订单编号','商品规格','收件人','收件人手机号','详细地址','实收款（到付按此收费）','数量']]
data2 = data2.replace({'商品规格':'手推式扫地机 蓝色 99元'},'蓝色')
data2 = data2.replace({'商品规格':'手推式扫地机 粉色 99元'},'粉色')
data2['订单编号'] = data2['订单编号'].str[1:20]
data2['订单编号'] = data2['订单编号'].astype('str')
data3 = pd.read_excel('C:/Users/jango/Downloads/运单上传模板.xlsx',usecols='A:Y',header=2)
print (data3)
data3['收件人姓名'] = data2['收件人']
data3['商家订单号'] = data2['订单编号']
data3['收件人地址'] = data2['详细地址']
data3['收件人手机'] = data2['收件人手机号']
data3['包裹数量'] = data2['数量']
data3['代收货款金额（元）'] = data2['实收款（到付按此收费）']
data3['备注'] = data2['商品规格']
data3.to_excel('运单上传信息.xlsx',index=False,encoding='utf_8_sig')
wait = input('wait')