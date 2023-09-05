# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/4 11:53
@Auth ： 陈不辣
@File ：ssl_check.py
@IDE ：PyCharm
@addres:kyfq

1. 此脚本为检测域名的SSL证书过期时间，距离当前时间还有多久。
2. 此脚本需要配合 dname_list 使用，dname_list 里面是以列表的形式写入需要检测的域名。
"""

import socket
import ssl
import datetime
import time
#import config
import logging

dname_list=[
'www.baidu.com',
'www.pathologycn.com',
'*.ai.pathologycn.com',
]
def get_domain_cert(domain):
        socket.setdefaulttimeout(5)

        cxt = ssl.create_default_context()
        skt = cxt.wrap_socket(socket.socket(),server_hostname=domain)

        skt.connect((domain,443))
        cert = skt.getpeercert()

        # 获取证书结束的GMT时间
        end_time = cert["notAfter"]

        # 关闭socket连接
        skt.close()

        # 返回证书过期时间，返回的是GMT时间
        return end_time


def get_end_time(end_time,domain):
        # 将证书到期时间转换常规可读的时间，还是GMT时间
        GMT_FORMAT = '%b %d %H:%M:%S %Y GMT'
        GMT_TIME = datetime.datetime.strptime(end_time, GMT_FORMAT)
        # 将证书到期转换成东 8 区的时间
        East_8th_District = GMT_TIME + datetime.timedelta(hours=8)
        print("域名：%s 的证书到期时间：%s" %(domain,East_8th_District))

        # 将结束时间转换成时间戳，预备以后做计算，小于多少天报警。
        end_time_stamp = time.mktime(East_8th_District.timetuple())
        now_time_stamp = time.time()

        # 算出证书过期的天数
        time_difference = end_time_stamp - now_time_stamp
        # 将时间戳转换成天数
        days = ("%.2f" % (time_difference / 60 / 60 / 24))
        return days

if __name__ == '__main__':
        print("检测时间：%s" % time.strftime('%Y-%m-%d %H:%M:%S'))
        for i in dname_list:
                try:
                        end_time = get_domain_cert(i)
                except:
                        logging.error("请检查域名：%s 是否正确。 该域名否使用SSL证书，或者域名填写错误。\n" % i)
                else:
                        days = get_end_time(end_time, i)
                        print("域名：%s 的证书过期离当前时间还有：%s 天。\n" %(i, days))
