#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
import json

def view_btc(okcoinSpot, okcoinFuture):
    print (u' 现货行情 btc_usd')
    print (okcoinSpot.ticker('btc_usd'))
    #print (u' 美元汇率 ')
    #print (okcoinFuture.exchange_rate())

    print (u' 现货深度 ')
    print (okcoinSpot.depth('btc_usd'))

    #print (u' 现货历史交易信息 ')
    #print (okcoinSpot.trades())

    #print (u' 用户现货账户信息 ')
    #print (okcoinSpot.userinfo())

# 返回现货/期货API
def read_key():
    okcoinRESTURL = 'www.okcoin.com'   #请求注意：国内账号需要 修改为 www.okcoin.cn
    with open('lijianhui', 'r') as apis:
        keys = json.loads(apis.read())
    #现货API
    okcoinSpot = OKCoinSpot(okcoinRESTURL, keys["api"], keys["secret"])
    #期货API
    okcoinFuture = OKCoinFuture(okcoinRESTURL,keys["api"], keys["secret"])

    return okcoinSpot, okcoinFuture



if __name__ == '__main__':
    okcoinSpot, okcoinFuture = read_key();
    #view_btc(okcoinSpot, okcoinFuture);
    print (okcoinSpot.ticker('btc_usd'))
    print (okcoinFuture.future_userinfo())
    print (okcoinFuture.exchange_rate())
