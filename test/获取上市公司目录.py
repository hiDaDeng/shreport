from shreport import SH

cookies = {"Cookie": '您的cookies'}
sh = SH(cookies)
df = sh.companys()
print(df.head(10))