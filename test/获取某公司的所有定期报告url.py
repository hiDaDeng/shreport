from shreport import SH

cookies = {"Cookie": '您的cookies'}
sh = SH(cookies)
#以浦发银行为例股票代码600000
urls = sh.pdfurls(code='600000')


print(urls)