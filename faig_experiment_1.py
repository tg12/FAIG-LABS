'''THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

# Bitcoin Cash (BCH)   qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
# Ether (ETH) -        0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
# Litecoin (LTC) -     Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
# Bitcoin (BTC) -      34L8qWiQyKr8k4TnHDacfjbaSqQASbBtTd

# contact :- github@jamessawyer.co.uk



#IF YOU FOUND THIS USEFUL, Please Donate some Bitcoin .... 1FWt366i5PdrxCC6ydyhD8iywUHQ2C7BWC

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time, sleep
from datetime import datetime, time
import datetime
import requests
import json
import logging
import sys
import urllib
import random
from random import randint
import numpy as np
from numpy import arange,array,ones#,random,linalg
from pylab import plot,show
from scipy import stats
#Scikit's LinearRegression model
from sklearn.linear_model import LinearRegression
##################################################
import sys, os
import csv
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ptick
import matplotlib.dates as mdates
import operator


########################################################################################################################
REAL_OR_NO_REAL = 'https://demo-api.ig.com/gateway/deal'
API_ENDPOINT = "https://demo-api.ig.com/gateway/deal/session"
#API_KEY = '**********************' 
API_KEY = '***********************'
##############################################################
#API_KEY = 'e8ac2586a8bb7ff31d2717665425be5332985eed' #<- DO NOT USE!!
data = {"identifier":"*****************","password": "*************"}
########################################################################################################################
########################################################################################################################
########################################################################################################################
# FOR REAL....
########################################################################################################################
########################################################################################################################
########################################################################################################################
# REAL_OR_NO_REAL = 'https://api.ig.com/gateway/deal'
# API_ENDPOINT = "https://api.ig.com/gateway/deal/session"
# API_KEY = '**********************'
# #####################################################
# #API_KEY = '*************************' #<- DO NOT USE
# data = {"identifier":"***************","password": "****************"}

headers = {'Content-Type':'application/json; charset=utf-8',
        'Accept':'application/json; charset=utf-8',
        'X-IG-API-KEY':API_KEY,
        'Version':'2'
        }

r = requests.post(API_ENDPOINT, data=json.dumps(data), headers=headers)
 
headers_json = dict(r.headers)
CST_token = headers_json["CST"]
print (R"CST : " + CST_token)
x_sec_token = headers_json["X-SECURITY-TOKEN"]
print (R"X-SECURITY-TOKEN : " + x_sec_token)

#GET ACCOUNTS
base_url = REAL_OR_NO_REAL + '/accounts'
authenticated_headers = {'Content-Type':'application/json; charset=utf-8',
        'Accept':'application/json; charset=utf-8',
        'X-IG-API-KEY':API_KEY,
        'CST':CST_token,
        'X-SECURITY-TOKEN':x_sec_token}

auth_r = requests.get(base_url, headers=authenticated_headers)
d = json.loads(auth_r.text)

# print(auth_r.status_code)
# print(auth_r.reason)
# print (auth_r.text)

for i in d['accounts']:
    if str(i['accountType']) == "SPREADBET":
        print ("Spreadbet Account ID is : " + str(i['accountId']))
        spreadbet_acc_id = str(i['accountId'])

#SET SPREAD BET ACCOUNT AS DEFAULT
base_url = REAL_OR_NO_REAL + '/session'
data = {"accountId":spreadbet_acc_id,"defaultAccount": "True"}
auth_r = requests.put(base_url, data=json.dumps(data), headers=authenticated_headers)

# print(auth_r.status_code)
# print(auth_r.reason)
# print (auth_r.text)
#ERROR about account ID been the same, Ignore! 

###################################################################################
##########################END OF LOGIN CODE########################################
##########################END OF LOGIN CODE########################################
##########################END OF LOGIN CODE########################################
##########################END OF LOGIN CODE########################################
###################################################################################
high_a = np.empty((0)) #Init this
low_a = np.empty((0)) #Init this
snapshotTime_a = np.empty((0)) #Init this
##########################################
bid_a = np.empty((0))
offer_a = np.empty((0))
updateTime_a = np.empty((0))
##########################################
price_prediction = 0 #Init this
Client_Sentiment_Check = 69

epic_ids = ["CS.D.AUDUSD.TODAY.IP", "CS.D.EURCHF.TODAY.IP", "CS.D.EURGBP.TODAY.IP", "CS.D.EURJPY.TODAY.IP", "CS.D.EURUSD.TODAY.IP", "CS.D.GBPEUR.TODAY.IP", "CS.D.GBPUSD.TODAY.IP", "CS.D.USDCAD.TODAY.IP", "CS.D.USDCHF.TODAY.IP", "CS.D.USDJPY.TODAY.IP", "CS.D.CADCHF.TODAY.IP", "CS.D.CADJPY.TODAY.IP", "CS.D.CHFJPY.TODAY.IP", "CS.D.EURCAD.TODAY.IP", "CS.D.EURSGD.TODAY.IP", "CS.D.EURZAR.TODAY.IP", "CS.D.GBPCAD.TODAY.IP", "CS.D.GBPCHF.TODAY.IP", "CS.D.GBPJPY.TODAY.IP", "CS.D.GBPSGD.TODAY.IP", "CS.D.GBPZAR.TODAY.IP", "CS.D.MXNJPY.TODAY.IP", "CS.D.NOKJPY.TODAY.IP", "CS.D.PLNJPY.TODAY.IP", "CS.D.SEKJPY.TODAY.IP", "CS.D.SGDJPY.TODAY.IP", "CS.D.USDSGD.TODAY.IP", "CS.D.USDZAR.TODAY.IP", "CS.D.AUDCAD.TODAY.IP", "CS.D.AUDCHF.TODAY.IP", "CS.D.AUDEUR.TODAY.IP", "CS.D.AUDGBP.TODAY.IP", "CS.D.AUDJPY.TODAY.IP", "CS.D.AUDNZD.TODAY.IP", "CS.D.AUDSGD.TODAY.IP", "CS.D.EURAUD.TODAY.IP", "CS.D.EURNZD.TODAY.IP", "CS.D.GBPAUD.TODAY.IP", "CS.D.GBPNZD.TODAY.IP", "CS.D.NZDAUD.TODAY.IP", "CS.D.NZDCAD.TODAY.IP", "CS.D.NZDCHF.TODAY.IP", "CS.D.NZDEUR.TODAY.IP", "CS.D.NZDGBP.TODAY.IP", "CS.D.NZDJPY.TODAY.IP", "CS.D.NZDUSD.TODAY.IP", "CS.D.CHFHUF.TODAY.IP", "CS.D.EURCZK.TODAY.IP", "CS.D.EURHUF.TODAY.IP", "CS.D.EURILS.TODAY.IP", "CS.D.EURMXN.TODAY.IP", "CS.D.EURPLN.TODAY.IP", "CS.D.EURTRY.TODAY.IP", "CS.D.GBPCZK.TODAY.IP", "CS.D.GBPHUF.TODAY.IP", "CS.D.GBPILS.TODAY.IP", "CS.D.GBPMXN.TODAY.IP", "CS.D.GBPPLN.TODAY.IP", "CS.D.GBPTRY.TODAY.IP", "CS.D.TRYJPY.TODAY.IP", "CS.D.USDCZK.TODAY.IP", "CS.D.USDHUF.TODAY.IP", "CS.D.USDILS.TODAY.IP", "CS.D.USDMXN.TODAY.IP", "CS.D.USDPLN.TODAY.IP", "CS.D.USDTRY.TODAY.IP", "CS.D.CADNOK.TODAY.IP", "CS.D.CHFNOK.TODAY.IP", "CS.D.EURDKK.TODAY.IP", "CS.D.EURNOK.TODAY.IP", "CS.D.EURSEK.TODAY.IP", "CS.D.GBPDKK.TODAY.IP", "CS.D.GBPNOK.TODAY.IP", "CS.D.GBPSEK.TODAY.IP", "CS.D.NOKSEK.TODAY.IP", "CS.D.USDDKK.TODAY.IP", "CS.D.USDNOK.TODAY.IP", "CS.D.USDSEK.TODAY.IP", "CS.D.AUDCNH.TODAY.IP", "CS.D.CADCNH.TODAY.IP", "CS.D.CNHJPY.TODAY.IP", "CS.D.BRLJPY.TODAY.IP", "CS.D.GBPINR.TODAY.IP", "CS.D.USDBRL.TODAY.IP", "CS.D.USDIDR.TODAY.IP", "CS.D.USDINR.TODAY.IP", "CS.D.USDKRW.TODAY.IP", "CS.D.USDMYR.TODAY.IP", "CS.D.USDPHP.TODAY.IP", "CS.D.USDTWD.TODAY.IP", "CS.D.EURCNH.TODAY.IP", "CS.D.sp_EURRUB.TODAY.IP", "CS.D.GBPCNH.TODAY.IP", "CS.D.NZDCNH.TODAY.IP", "CS.D.USDCNH.TODAY.IP", "CS.D.sp_USDRUB.TODAY.IP"]
#ALL EPICS

# def runningSums(lst):
    # res = [lst[0]]
    # for elem in lst[1:]:
        # res.append(res[-1] + elem)
    # return res
# def antiRunningSums(lst):
    # res = [lst[0]]
    # for i in range(1,len(lst)):
        # res.append(lst[i] - lst[i-1])
    # return res

# def predict(lst):
    # deriv = 0
    # while True:
        # nxt = antiRunningSums(lst)
        # if sum(map(abs, nxt)) > sum(map(abs, lst)):
            # break
        # lst = nxt
        # deriv += 1
    # lst.append(lst[-1])
    # for i in range(deriv):
        # lst = runningSums(lst)
    # return lst
        
def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
       return (abs(current - previous)/ previous * 100.0)
    except ZeroDivisionError:
        return 0
        
def place_order(pred_ict):
    base_url = REAL_OR_NO_REAL + '/markets/'+ epic_id
    auth_r = requests.get(base_url, headers=authenticated_headers)
    d = json.loads(auth_r.text)
    
    CURRENT_PRICE_bid = float(d['snapshot']['bid'])
    CURRENT_PRICE_offer = float(d['snapshot']['offer'])
    MARKET_ID = d['instrument']['marketId']
    price_diff = float(CURRENT_PRICE_bid) - float(pred_ict)
    ################################################################
    print ("!!DEBUG!! Max Value During this time: " + str(max_value))
    ################################################################
    percent_check = get_change(CURRENT_PRICE_bid, max_value)
    print ("!!DEBUG!! Percent Check: " + str(percent_check))
    ################################################################
         
    if price_diff > 0 and float(shortPositionPercentage) > float(longPositionPercentage) and float(shortPositionPercentage) > Client_Sentiment_Check:
        DIRECTION_TO_TRADE = "SELL"
        limitDistance_value = str(int(price_diff))
    elif price_diff < 0 and float(longPositionPercentage) > float(shortPositionPercentage) and float(longPositionPercentage) > Client_Sentiment_Check:
        DIRECTION_TO_TRADE = "BUY"
        limitDistance_value = str(int(price_diff * -1))
    else:
        print ("!!DEBUG!! No trade")
        print (price_diff)
        print (float(longPositionPercentage))
        print (float(shortPositionPercentage))
        return None
    
    #PROGRAMMABLE VALUES
    #SET INITIAL VARIABLES, Hacky for now! 
    orderType_value = "MARKET"
    size_value = "1"
    expiry_value = "DFB"
    guaranteedStop_value = True
    currencyCode_value = "GBP"
    forceOpen_value = True
    stopDistance_value = stop_loss_TR
    cautious_trader = 1.5 #Like the greed value but opposite
    greedy_trader = 0.3 #Don't be too greedy (1 = Full 100% trade)
    
    if str(limitDistance_value) == "0":
        print ("!!DEBUG!! Bailing Ooooot")
        return None
        #Really don't bother! 
        
    #~~~~~~~Cautious Trader~~~~~~~~~~~~
    if float(stopDistance_value) < float(limitDistance_value):
        stopDistance_value = float(stopDistance_value) * cautious_trader
        stopDistance_value = str(int(limitDistance_value))
 
    now = datetime.datetime.now()
    now_time = now.time()
    if now_time >= time(8,30) and now_time <= time(16,30):
        print ("LONDON MARKET OPEN")
        #~~~~~~~~~~~Greedy Trader~~~~~~~~~~~~~~~~~
        limitDistance_value = float(limitDistance_value) * greedy_trader
        limitDistance_value = str(int(limitDistance_value))
    elif now_time >= time(14,30) and now_time <= time(21,00):
        print ("NEW YORK MARKET OPEN")
        #~~~~~~~~~~~Greedy Trader~~~~~~~~~~~~~~~~~
        limitDistance_value = float(limitDistance_value) * greedy_trader
        limitDistance_value = str(int(limitDistance_value))
    else:
        print ("OVERNIGHT/LATE TRADING")
        limitDistance_value = "1"

    ###############################################################################################################
    print ("Order will be a " + str(DIRECTION_TO_TRADE) + " Order, With a limit of: " + str(limitDistance_value))
    print ("stopDistance_value for " + str(epic_id) + " will bet set at " + str(stop_loss_TR))
    ###############################################################################################################
    base_url = REAL_OR_NO_REAL + '/positions/otc'         
    data = {"direction":DIRECTION_TO_TRADE,"epic": epic_id, "limitDistance":limitDistance_value, "orderType":orderType_value, "size":size_value,"expiry":expiry_value,"guaranteedStop":guaranteedStop_value,"currencyCode":currencyCode_value,"forceOpen":forceOpen_value,"stopDistance":stopDistance_value}
    r = requests.post(base_url, data=json.dumps(data), headers=authenticated_headers)
    
    print ("-----------------DEBUG-----------------")
    print(r.status_code)
    print(r.reason)
    print (r.text)
    print ("-----------------DEBUG-----------------")

    d = json.loads(r.text)
    deal_ref = d['dealReference']
    sleep(2)
    #MAKE AN ORDER
    #CONFIRM MARKET ORDER
    base_url = REAL_OR_NO_REAL + '/confirms/'+ deal_ref
    auth_r = requests.get(base_url, headers=authenticated_headers)
    d = json.loads(auth_r.text)
    DEAL_ID = d['dealId']
    print("DEAL ID : " + str(d['dealId']))
    print(d['dealStatus'])
    print(d['reason'])
        
    if str(d['reason']) != "SUCCESS":
        print ("!!DEBUG!! !!ERROR!! Do something about this")
    else:
        print ("!!DEBUG!! ORDER OPEN")


##################################################
##################################################
##################################################
# spreads_and_epics = []

# for epic_id in epic_ids:
    # tmp_lst = []
    # base_url = REAL_OR_NO_REAL + '/markets/'+ epic_id
    # auth_r = requests.get(base_url, headers=authenticated_headers)
    # d = json.loads(auth_r.text)
    # # print(auth_r.status_code)
    # # print(auth_r.reason)
    # # print (auth_r.text)
    # # print (epic_id)
    
    # try:
        # tmp_lst.append(epic_id)

        # bid_price = d['snapshot']['bid']
        # ask_price = d['snapshot']['offer']
        # spread = float(bid_price) - float(ask_price)
        # # print ("bid : " + str(bid_price))
        # # print ("ask : " + str(ask_price))
        # # print ("-------------------------")
        # # print ("spread : " + str(spread))
        # # print ("-------------------------")
        # tmp_lst.append(spread)
        # spreads_and_epics.append(tmp_lst)
        # sleep(1)
    # except Exception:
        # pass
    

# sorted_list = sorted(spreads_and_epics, key=operator.itemgetter(1))

# # for i in range(len(sorted_list)):
    # # print(sorted_list[i])
    
# # print (max(sorted_list, key=lambda x: x[1]))
# lowest_epic = max(sorted_list, key=lambda x: x[1])
# epic_id = lowest_epic[0]

#DEBUGGING, Really should better pick an epic! 
#EPIC OF YOUR CHOOSING! Code above just picks lowest spread. Whatever way you want to do it is up to you! 
#epic_id = "CS.D.GBPUSD.TODAY.IP"

for x in range(0, 9999):
    
    OK_to_Trade = False
    
    while not OK_to_Trade:
        random.shuffle(epic_ids)
        epic_id = random.choice(epic_ids)

        print ("-----------------------------------------")
        print("!!DEBUG : Random epic_id is : " + str(epic_id))
        base_url = REAL_OR_NO_REAL + '/markets/' + epic_id
        auth_r = requests.get(base_url, headers=authenticated_headers)
        d = json.loads(auth_r.text)
        sleep(2)

        # print ("-----------------DEBUG-----------------")
        # print(auth_r.status_code)
        # print(auth_r.reason)
        # print (auth_r.text)
        # print ("-----------------DEBUG-----------------")
        bid_price = d['snapshot']['bid']
        ask_price = d['snapshot']['offer']
        MARKET_ID = d['instrument']['marketId']
                   
        # print ("bid : " + str(bid_price))
        # print ("ask : " + str(ask_price))
        # print ("-------------------------")
        
        spread = float(bid_price) - float(ask_price)
        print ("spread : " + str(spread))

        #if spread is less than -2, It's too big
        if float(spread) < -2:
         print ("!!DEBUG!! :- SPREAD NOT OK")
         OK_to_Trade = False
         sleep(2)
         continue #No point checking sentiment and wasting an API call!!
        elif float(spread) > -2:
         OK_to_Trade = True
         
        #Good ol "Crowd-sourcing" check.....
        base_url = REAL_OR_NO_REAL + '/clientsentiment/'+ MARKET_ID
        auth_r = requests.get(base_url, headers=authenticated_headers)
        d = json.loads(auth_r.text)
        
        print ("-----------------DEBUG-----------------")
        print(auth_r.status_code)
        print(auth_r.reason)
        print (auth_r.text)
        print ("-----------------DEBUG-----------------")

        longPositionPercentage = float(d['longPositionPercentage'])
        shortPositionPercentage = float(d['shortPositionPercentage'])
    
        if float(shortPositionPercentage) > Client_Sentiment_Check or float(longPositionPercentage) > Client_Sentiment_Check:
            OK_to_Trade = True
        else:
            OK_to_Trade = False
            print("!!DEBUG!! Sentiment Check Failed!!")
            
    ###############################################
    ###############################################
    ###############################################
    ###############################################
    #USING HISTORICAL
    ###############################################
    ###############################################
    ###############################################
    ###############################################
    
    time_series_int = str(randint(30, 60))
    sleep(3) #Wait 3s to stop IG error
    
    y = [] # linearly generated sequence
    base_url = REAL_OR_NO_REAL + '/prices/'+ epic_id + '/MINUTE_15/' + time_series_int
    # Price resolution (MINUTE, MINUTE_2, MINUTE_3, MINUTE_5, MINUTE_10, MINUTE_15, MINUTE_30, HOUR, HOUR_2, HOUR_3, HOUR_4, DAY, WEEK, MONTH)
    auth_r = requests.get(base_url, headers=authenticated_headers)
    d = json.loads(auth_r.text)

    # print(auth_r.status_code)
    # print(auth_r.reason)
    # print (auth_r.text)

    for i in d['prices']:
        snapshotTime = i['snapshotTime']
        lowPrice = i['lowPrice']['bid']
        highPrice = i['highPrice']['bid']
        closePrice = i['closePrice']['bid']
        #####################################################################
        dt_obj = datetime.datetime.strptime(snapshotTime,'%Y:%m:%d-%H:%M:%S')
        snapshotTime = datetime.datetime.strftime(dt_obj, '%H:%M')  
        high_a = np.append(high_a, highPrice)
        high_a = np.append(high_a, highPrice)
        low_a = np.append(low_a, lowPrice)
        snapshotTime_a = np.append(snapshotTime_a, snapshotTime)
        ###########################################################
        y.append(float(closePrice))
        
    max_value = np.amax(high_a)
    price_ranges = []
    closing_prices = []
    first_time_round_loop = True
    TR_prices = []
    price_compare = "bid"

    for i in d['prices']:
        if first_time_round_loop == True:
            #First time round loop cannot get previous
            closePrice = i['closePrice'][price_compare]
            closing_prices.append(closePrice)
            high_price = i['highPrice'][price_compare]
            low_price = i['lowPrice'][price_compare]
            price_range = float(high_price - closePrice)
            price_ranges.append(price_range)
            first_time_round_loop = False
        else:
            prev_close = closing_prices[-1]
            ###############################
            closePrice = i['closePrice'][price_compare]
            closing_prices.append(closePrice)
            high_price = i['highPrice'][price_compare]
            low_price = i['lowPrice'][price_compare]
            price_range = float(high_price - closePrice)
            price_ranges.append(price_range)
            TR = max(high_price-low_price, abs(high_price-prev_close), abs(low_price-prev_close))
            #print (TR)
            TR_prices.append(TR)
            
    stop_loss_TR = str(int(max(TR_prices)))
    
    xi = arange(0,len(y))
    A = array([ xi, ones((len(y)))])
    slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)
    
    # print (stats.linregress(xi,y))
    # print ('r value ' +  str(r_value))
    # print  ('p_value ' + str(p_value))
    # print ('standard deviation ' + str(std_err))
    
    line = slope*xi+intercept
    plot(xi,line,'r-',xi,y,'o')
    graph_file_name = str(x) + "_" + str(epic_id) + ".png"
    plt.savefig(str(graph_file_name))
    print ("Slope: " + str(slope))
    print ("Intercept: " + str(intercept))
    #show()
    
    if float(slope) > 3:
        print("!!DEBUG!! Strong Trend UP")
    elif float(slope) < -3:
        print("!!DEBUG!! Strong Trend DOWN")
    
    predicted_value = float(intercept)
    print ("!!DEBUG!! Passing .... " + str(predicted_value))
    place_order(predicted_value)

