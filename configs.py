import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Crawling of microblog information')

    # cookie
    # parser.add_argument('--cookie', default='_T_WM=94796105813;SSOLoginState=1606958688;SCF=AvVZU6NdvvJKYK9hgFD4KWxit2nGXCEqTc7xzZsgUFz0BP1LyOdUjiSzi_W1wVVn-Z4X8i4WIgx6IIZlq5wFvNg.;SUB=_2A25yzE4wDeRhGeFP7VAT9SzLwzyIHXVuT1J4rDV6PUJbktANLU3FkW1NQQEe34KAm-AAMK0buil5x3vwHg6nDS5A;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWQAsHE1AUUms8uI4c4k8F05JpX5KzhUgL.FoMpSozESKzN1h52dJLoIp7LxKnL1K2LBKeLxK-L1h5LBK.LxK-L1h5LBKLx')

    # user
    """
    user_id: the id of user, such as 1669879400(迪丽热巴)  3566865465  5527986069  5264532649  1159768381
    user_url: the url of user's information
    """
    parser.add_argument('--user_id', default=1669879400)
    parser.add_argument('--user_url', default='https://weibo.cn/')

    # information
    """
    filter: 0 or 1 (0: 原创微博 + 转发微博; 1:原创微博)
    pic_download: 0 or 1 (0: 不下载原始微博图片; 1: 下载微博原始图片)
    """
    parser.add_argument('--filter', default=1)
    parser.add_argument('--pic_download', default=1)
    # parser.add_argument('--file_dir', default='E:/py_project/Crawling of microblog information/user_information/')

    return parser.parse_args()