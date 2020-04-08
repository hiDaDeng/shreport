from pathlib import Path
from shreport import SH

cookies = {"Cookie": '您的cookies'}
sh = SH(cookies)
#获取当前代码所在的文件夹路径
cwd = Path().cwd()
#以浦发银行为例股票代码600000
sh.download(code='600000', savepath=cwd)