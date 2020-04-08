from setuptools import setup
import setuptools
setup(
    name='shreport',     # 包名字
    version='0.0.2',   # 包版本
    description='上海证券交易所上市公司定期报告下载,项目地址 https://github.com/thunderhit/shreport',
    author='大邓',  # 作者
    author_email='thunderhit@qq.com',  # 邮箱
    url='https://github.com/thunderhit/shreport',      # 包的主页
    packages=setuptools.find_packages(),
    install_requires=['requests', 'grequests'],
    python_requires='>=3.5',
    license="MIT",
    keywords=['data collect', 'text analysis', 'pdf download', 'finance'],
    long_description=open('README.md').read(), # 读取的Readme文档内容
    long_description_content_type="text/markdown")  # 指定包文档格式为markdown
    #py_modules = ['eventextraction.py']
