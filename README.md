
## 一、简介

```
上海证券交易所上市公司定期报告下载,项目地址 https://github.com/thunderhit/shreport
```

- github地址 https://github.com/thunderhit/shreport
-  pypi地址 https://pypi.org/project/shreport



能：

1. 获取上证交易所所有公司目录
2. 上市公司历年报告(季报、半年报、年报)

**使用演示视频**
[B站:如何用Python批量下载上交所上市公司的年报pdf文件](https://www.bilibili.com/video/BV15A411h7RJ)


## 二、安装

```
pip install shreport
```

## 三、功能说明

```
companys()
  上证所有上市公司名录，公司名及股票代码
  :return: 返回DataFrame

download(code, savepath)
  下载上市公司的所有季度报告、半年报、年报pdf文件
  :param code:  上市公司股票代码
  :param savepath:  存储的路径，建议使用相对路径
  :return:
 
pdfurls(code)
  获取年报文件下载链接
  :param code:  股票代码
  :return: 年报pdf链接
```



## 四、快速入门

一定要先获得cookies后才能使用下面的所有代码，这里先直接看代码使用情况，cookies获取可见文档    **五、获取cookies**

### 4.1  获取上证交易所上市公司目录



```python
from shreport import SH

cookies = {"Cookie": '您的cookies'}
sh = SH(cookies)
df = sh.companys()
df.head(10)
```

Run

```
-  --------  ------
     name     code
0  浦发银行  600000
1  白云机场  600004
2  东风汽车  600006
3  中国国贸  600007
4  首创股份  600008
-  --------  ------
```

代码中的sh.companys()获取的是DataFrame数据类型，所以大家还可以自己存储成excel

```
df.to_excel('上证交易所上市公司名录.xlsx')
```



### 4.2下载某公司所有定期报告文件

绝大多数报告文件名格式

| 文件   | 文件名             | 例子                                 |
| ------ | ------------------ | ------------------------------------ |
| 季度报 | 公司代码-年份-数字 | 600000-2000-1.pdf、600000-2000-3.pdf |
| 半年报 | 公司代码-年份-z    | 600000-2000-z.pdf                    |
| 年报   | 公司代码-年份-n    | 600000-2000-n.pdf                    |

代码

```python
from pathlib import Path
from shreport import SH

cookies = {"Cookie": '您的cookies'}
sh = SH(cookies)
#获取当前代码所在的文件夹路径
cwd = Path().cwd() 
#以浦发银行为例股票代码600000
sh.download(code='600000', savepath=cwd)
```

Run

```
=======请耐心等待，正在获取600000数据
=======准备获取600000年报文件链接========
=======年报文件链接已获取完毕=============
已成功下载600000_2000_1.pdf
已成功下载600000_2000_z.pdf
已成功下载600000_2000_3.pdf
已成功下载600000_2000_n.pdf
......
已成功下载600000_2019_1.pdf
已成功下载600000_2019_z.pdf
已成功下载600000_2019_3.pdf
已成功下载600000_2000_n.pdf
```



### 4.3 获取某公司的所有定期报告url

如果暂时不想下载定期报告pdf文件，可以只得到该公司所有的报告文件链接



```python
from shreport import SH

cookies = {"Cookie": '您的cookies'}
sh = SH(cookies)
#以浦发银行为例股票代码600000
urls = sh.pdfurls(code='600000')
urls
```

Run 

```
=======准备获取600000年报文件链接========
=======年报文件链接已获取完毕=============
['http://www.sse.com.cn/disclosure/listedinfo/announcement/c/600000_2000_1.pdf',
 'http://www.sse.com.cn/disclosure/listedinfo/announcement/c/2002-10-30/600000_2002_3.pdf',
 'http://www.sse.com.cn/disclosure/listedinfo/announcement/c/2002-08-17/600000_2002_z.pdf',
 .......
 'http://www.sse.com.cn/disclosure/listedinfo/announcement/c/600000_2002_1.pdf',

 'http://www.sse.com.cn/disclosure/listedinfo/announcement/c/2019-03-26/600000_2018_n.pdf',
 'http://www.sse.com.cn/disclosure/listedinfo/announcement/c/2018-10-31/600000_2018_3.pdf',
 'http://www.sse.com.cn/disclosure/listedinfo/announcement/c/2018-08-30/600000_2018_z.pdf',
 'http://www.sse.com.cn/disclosure/listedinfo/announcement/c/2018-04-28/600000_2017_n.pdf',
 'http://www.sse.com.cn/disclosure/listedinfo/announcement/c/2018-04-28/600000_2018_1.pdf']

```



## 五、获取cookies

一定要先获得cookies后才能使用所有的代码，获取方法

1. 浏览器访问http://www.sse.com.cn/disclosure/overview/
2. 按F12（mac按option+command+I)打开开发者工具的Network
3. 刷新网页，耐心寻找与www.sse.com.cn有关的任意网址，找到cookies

![](/Users/thunderhit/Desktop/shreport/img/cookies.gif)

## 如果

如果您是经管人文社科专业背景，编程小白，面临海量文本数据采集和处理分析艰巨任务，个人建议学习[《python网络爬虫与文本数据分析》](https://ke.qq.com/course/482241?tuin=163164df)视频课。作为文科生，一样也是从两眼一抹黑开始，这门课程是用五年时间凝缩出来的。自认为讲的很通俗易懂o(*￣︶￣*)o，

- python入门
- 网络爬虫
- 数据读取
- 文本分析入门
- 机器学习与文本分析
- 文本分析在经管研究中的应用

感兴趣的童鞋不妨 戳一下[《python网络爬虫与文本数据分析》](https://ke.qq.com/course/482241?tuin=163164df)进来看看~



## 更多

- [B站:大邓和他的python](https://space.bilibili.com/122592901/channel/detail?cid=66008)

- 公众号：大邓和他的python

- [知乎专栏：数据科学家](https://zhuanlan.zhihu.com/dadeng)

      

## 支持一下

![](img/my_zanshang_qrcode.jpg)
