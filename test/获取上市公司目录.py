from shreport import SH

cookies = {"Cookie": '您的cookies'}
sh = SH(cookies)
df = sh.companys()

#显示前5条数据
print(df.head())

#将查询结果存储
#df.to_excel('上证交易所上市公司名录.xlsx')