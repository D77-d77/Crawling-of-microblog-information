import traceback
import configs

from MicroBlog import MicroBlog

def main(args):
    """
    user_id: the id of user, such as 1669879400(迪丽热巴)
    filter: 0 or 1 (0: 原创微博 + 转发微博; 1:原创微博)
    pic_download: 0 or 1 (0: 不下载原始微博图片; 1: 下载微博原始图片)
    """
    try:

        cookie = {
            'Cookie':'_T_WM=94796105813; SCF=AvVZU6NdvvJKYK9hgFD4KWxit2nGXCEqTc7xzZsgUFz0ygsaRKVlUugfs3QJyhZXreU0M1pdtBcwcrd2CVTaRyk.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWQAsHE1AUUms8uI4c4k8F05JpX5K-hUgL.FoMpSozESKzN1h52dJLoIp7LxKnL1K2LBKeLxK-L1h5LBK.LxK-L1h5LBKLx; ALF=1610086071; SUB=_2A25y1B1rDeRhGeFP7VAT9SzLwzyIHXVuNqMjrDV6PUJbkdAKLXagkW1NQQEe31-lVcLmXI0dgtF2B2VKRqdGBPOg' }
        # 使用实例，输入一个用户id，所有信息都会存储在文件user_information中
        user_id = args.user_id
        user_url = args.user_url
        filter = args.filter
        pic_download = args.pic_download
        # print(user_id, filter, pic_download)

        # 调用MicroBlog类，创建微博实例MB
        MB = MicroBlog(cookie, user_id, user_url, filter, pic_download)
        # 爬取微博信息
        MB.start()

    except Exception as e:
        print('ERROR: ', e)
        traceback.print_exc() # 捕获并打印异常的方法

if __name__ == '__main__':
    args = configs.parse_args()
    main(args)
