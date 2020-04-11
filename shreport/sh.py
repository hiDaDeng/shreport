#!/usr/bin/env python3
# author： 大邓
# github： https://github.com/liuhuanyong/ComplexEventExtraction
# 【公众号:大邓和他的Python】

import re
import pandas as pd
import requests
import grequests
import datetime
import json
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

class SH(object):
    def __init__(self, cookies):
        """
        :param cookies:  您的cookies
        """
        self.cookies = cookies

    def date_ranges(self):
        begin = datetime.datetime(1990, 11, 26)
        now = datetime.datetime.today()
        interv = datetime.timedelta(days=900)
        dates = []
        date = begin
        while True:
            if (date < now) & (date + interv < now):
                date = date + interv
                dates.append(date.strftime('%Y-%m-%d'))
            else:
                dates.append(now.strftime('%Y-%m-%d'))
                break
        return [(d1, d2) for d1, d2 in zip(dates, dates[1:])]

    def companys(self):
        """
        上证所有上市公司名录，公司名及股票代码
        :return: 返回DataFrame
        """
        stocks = []
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
                   'Referer': 'http://www.sse.com.cn/assortment/stock/list/share/'}

        url = 'http://query.sse.com.cn/security/stock/getStockListData2.do?&jsonCallBack=jsonpCallback13284&isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage=1&pageHelp.pageSize=25&pageHelp.pageNo=2&pageHelp.endPage=21'
        resp = requests.get(url, headers=headers, cookies=self.cookies)
        raw_json = re.split('Callback\d+\(', resp.text)[-1][:-1]
        pages = json.loads(raw_json)['pageHelp']['pageCount']
        for page in range(1, pages + 1):
            base = 'http://query.sse.com.cn/security/stock/getStockListData2.do?&jsonCallBack=jsonpCallback13284&isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage={page}&pageHelp.pageSize=25&pageHelp.pageNo=2&pageHelp.endPage=21'
            pageurl = base.format(page=page)
            pageresp = requests.get(pageurl, headers=headers, cookies=self.cookies)
            page_raw_json = re.split('Callback\d+\(', pageresp.text)[-1][:-1]
            results = json.loads(page_raw_json)['result']
            results = [[r['COMPANY_ABBR'], r['COMPANY_CODE']] for r in results]
            stocks.extend(results)

        df = pd.DataFrame(stocks, columns=['name', 'code'])
        return df

    def pdfurls(self, code):
        """
        获取年报文件下载链接
        :param code:  股票代码
        :return: 年报pdf链接
        """
        print('=======准备获取{}年报文件链接========'.format(code))
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
                   'Referer': 'http://www.sse.com.cn/disclosure/listedinfo/regular/'}
        URLs = []
        base = 'http://query.sse.com.cn/security/stock/queryCompanyBulletin.do?isPagination=true&productId={code}&securityType=0101%2C120100%2C020100%2C020200%2C120200&reportType2=DQBG&reportType=&beginDate={beginDate}&endDate={endDate}&pageHelp.pageSize=25&pageHelp.pageCount=50&pageHelp.pageNo=1&pageHelp.beginPage=1&pageHelp.cacheSize=1&pageHelp.endPage=5'
        dateranges = self.date_ranges()
        for begin, end in dateranges:
            url = base.format(code=code, beginDate=begin, endDate=end)
            resp = requests.get(url, headers=headers, cookies=self.cookies)
            raw_data = json.loads(resp.text)
            results = raw_data['result']
            for result in results:
                URL = 'http://www.sse.com.cn' + result['URL']
                if '_n.pdf' in URL:
                    URLs.append(URL)
                elif '_3.pdf' in URL:
                    URLs.append(URL)
                elif '_1.pdf' in URL:
                    URLs.append(URL)
                elif '_z.pdf' in URL:
                    URLs.append(URL)
                else:
                    continue
        print('=======年报文件链接已获取完毕=============')
        return URLs

    def download(self, code, savepath):
        """
        下载上市公司的所有季度报告、半年报、年报pdf文件
        :param code:  上市公司股票代码
        :param savepath:  存储的路径，建议使用相对路径
        :return:
        """

        path = Path(savepath).joinpath(*('stocks', str(code)))
        Path(path).mkdir(parents=True, exist_ok=True)


        print('=======请耐心等待，正在获取{}数据'.format(code))
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
                   'Referer': 'http://www.sse.com.cn/disclosure/listedinfo/regular/'}

        urls = self.pdfurls(code=code)
        tasks = [grequests.request("GET", url=url, headers=headers, cookies=self.cookies) for url in urls]
        results = grequests.map(tasks)

        for result in results:
            pdfname = result.url.split('/')[-1]
            pdfpath = path.joinpath(pdfname)

            with open(pdfpath, 'wb') as f:
                f.write(result.content)
                print('已成功下载{}'.format(pdfname))










