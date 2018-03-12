#IF YOU FOUND THIS USEFUL, Please Donate some Bitcoin .... 1FWt366i5PdrxCC6ydyhD8iywUHQ2C7BWC

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import matplotlib
if os.name != 'nt': # if not windows
  matplotlib.use('Agg')

from datetime import datetime, time
from time import sleep
import sys
import random
#import numpy as np
from numpy import arange,array,ones#,random,linalg
from pylab import plot,show
from scipy import stats
#Scikit's LinearRegression model
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.ticker as ptick
import matplotlib.dates as mdates
import operator
import configparser

sys.path.insert(0, '../FAIG')

from igclient import IGClient

config = configparser.ConfigParser()
config.read("../FAIG/default.conf")
config.read("../FAIG/config.conf")

igclient = IGClient(config=config)
 
d = igclient.session()

###################################################################################
Client_Sentiment_Check = 61 # fetch from config
cautious_trader = 1.2 #Like the greed value but opposite
greedy_trader = float(0.4) #Don't be too greedy (1 = Full 100% trade)
#PROGRAMMABLE VALUES
#SET INITIAL VARIABLES, Hacky for now! 
orderType_value = "MARKET"
size_value = "1"
expiry_value = "DFB"
guaranteedStop_value = True
currencyCode_value = "GBP"
forceOpen_value = True
draw_graphs = False

epic_ids = ["CS.D.AUDUSD.TODAY.IP", "CS.D.EURCHF.TODAY.IP", "CS.D.EURGBP.TODAY.IP", "CS.D.EURJPY.TODAY.IP", "CS.D.EURUSD.TODAY.IP", "CS.D.GBPEUR.TODAY.IP", "CS.D.GBPUSD.TODAY.IP", "CS.D.USDCAD.TODAY.IP", "CS.D.USDCHF.TODAY.IP", "CS.D.USDJPY.TODAY.IP", "CS.D.CADCHF.TODAY.IP", "CS.D.CADJPY.TODAY.IP", "CS.D.CHFJPY.TODAY.IP", "CS.D.EURCAD.TODAY.IP", "CS.D.EURSGD.TODAY.IP", "CS.D.EURZAR.TODAY.IP", "CS.D.GBPCAD.TODAY.IP", "CS.D.GBPCHF.TODAY.IP", "CS.D.GBPJPY.TODAY.IP", "CS.D.GBPSGD.TODAY.IP", "CS.D.GBPZAR.TODAY.IP", "CS.D.MXNJPY.TODAY.IP", "CS.D.NOKJPY.TODAY.IP", "CS.D.PLNJPY.TODAY.IP", "CS.D.SEKJPY.TODAY.IP", "CS.D.SGDJPY.TODAY.IP", "CS.D.USDSGD.TODAY.IP", "CS.D.USDZAR.TODAY.IP", "CS.D.AUDCAD.TODAY.IP", "CS.D.AUDCHF.TODAY.IP", "CS.D.AUDEUR.TODAY.IP", "CS.D.AUDGBP.TODAY.IP", "CS.D.AUDJPY.TODAY.IP", "CS.D.AUDNZD.TODAY.IP", "CS.D.AUDSGD.TODAY.IP", "CS.D.EURAUD.TODAY.IP", "CS.D.EURNZD.TODAY.IP", "CS.D.GBPAUD.TODAY.IP", "CS.D.GBPNZD.TODAY.IP", "CS.D.NZDAUD.TODAY.IP", "CS.D.NZDCAD.TODAY.IP", "CS.D.NZDCHF.TODAY.IP", "CS.D.NZDEUR.TODAY.IP", "CS.D.NZDGBP.TODAY.IP", "CS.D.NZDJPY.TODAY.IP", "CS.D.NZDUSD.TODAY.IP", "CS.D.CHFHUF.TODAY.IP", "CS.D.EURCZK.TODAY.IP", "CS.D.EURHUF.TODAY.IP", "CS.D.EURILS.TODAY.IP", "CS.D.EURMXN.TODAY.IP", "CS.D.EURPLN.TODAY.IP", "CS.D.EURTRY.TODAY.IP", "CS.D.GBPCZK.TODAY.IP", "CS.D.GBPHUF.TODAY.IP", "CS.D.GBPILS.TODAY.IP", "CS.D.GBPMXN.TODAY.IP", "CS.D.GBPPLN.TODAY.IP", "CS.D.GBPTRY.TODAY.IP", "CS.D.TRYJPY.TODAY.IP", "CS.D.USDCZK.TODAY.IP", "CS.D.USDHUF.TODAY.IP", "CS.D.USDILS.TODAY.IP", "CS.D.USDMXN.TODAY.IP", "CS.D.USDPLN.TODAY.IP", "CS.D.USDTRY.TODAY.IP", "CS.D.CADNOK.TODAY.IP", "CS.D.CHFNOK.TODAY.IP", "CS.D.EURDKK.TODAY.IP", "CS.D.EURNOK.TODAY.IP", "CS.D.EURSEK.TODAY.IP", "CS.D.GBPDKK.TODAY.IP", "CS.D.GBPNOK.TODAY.IP", "CS.D.GBPSEK.TODAY.IP", "CS.D.NOKSEK.TODAY.IP", "CS.D.USDDKK.TODAY.IP", "CS.D.USDNOK.TODAY.IP", "CS.D.USDSEK.TODAY.IP", "CS.D.AUDCNH.TODAY.IP", "CS.D.CADCNH.TODAY.IP", "CS.D.CNHJPY.TODAY.IP", "CS.D.BRLJPY.TODAY.IP", "CS.D.GBPINR.TODAY.IP", "CS.D.USDBRL.TODAY.IP", "CS.D.USDIDR.TODAY.IP", "CS.D.USDINR.TODAY.IP", "CS.D.USDKRW.TODAY.IP", "CS.D.USDMYR.TODAY.IP", "CS.D.USDPHP.TODAY.IP", "CS.D.USDTWD.TODAY.IP", "CS.D.EURCNH.TODAY.IP", "CS.D.sp_EURRUB.TODAY.IP", "CS.D.GBPCNH.TODAY.IP", "CS.D.NZDCNH.TODAY.IP", "CS.D.USDCNH.TODAY.IP", "CS.D.sp_USDRUB.TODAY.IP"]
#ALL EPICS


def calculate_stop_loss():
    d = igclient.prices(epic_id, 'HOUR/5')
    
    closing_prices = []
    TR_prices = []
    type = "bid"
 
    for count, i in enumerate(d['prices']):
        closing_prices.append(i['closePrice'][type])
        low_price = i['lowPrice'][type]
        high_price = i['highPrice'][type]
        price_range = float(high_price - i['closePrice'][type])
        if count > 0:
            prev_close = closing_prices[-2]
            TR = max(high_price-low_price, abs(high_price-prev_close), abs(low_price-prev_close))
            TR_prices.append(TR)

    return str(int(max(TR_prices)))

def humanize_time(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d:%02d:%02d' % (hours, mins, secs)  
        
def place_order(pred_ict, vol_slope):
    d = igclient.markets(epic_id)
    
    CURRENT_PRICE_bid = float(d['snapshot']['bid'])
    CURRENT_PRICE_offer = float(d['snapshot']['offer'])
    MARKET_ID = d['instrument']['marketId']
    price_diff = float(CURRENT_PRICE_bid) - float(pred_ict)
    
    #Reserved for Future use? .... 
    #net_change_day = float(d['snapshot']['netChange'])
   
    if float(std_err) > -2 and float(std_err) < 2:
        #print ("!!DEBUG!! Standard Deviation is GOOD!!")
        if price_diff > 0 and vol_slope > 1 and longPositionPercentage >= Client_Sentiment_Check:
            limitDistance_value = str(int(price_diff * greedy_trader))
            DIRECTION_TO_TRADE = "BUY"
        elif price_diff < 0 and vol_slope > 1 and longPositionPercentage >= Client_Sentiment_Check:
            DIRECTION_TO_TRADE = "BUY"
            limitDistance_value = str(int(price_diff * greedy_trader))
            limitDistance_value = str(int(limitDistance_value) * -1) 
        elif price_diff < 0 and vol_slope < 1 and shortPositionPercentage >= Client_Sentiment_Check:
            limitDistance_value = str(int(price_diff * greedy_trader))
            limitDistance_value = str(int(limitDistance_value) * -1) 
            DIRECTION_TO_TRADE = "SELL"
        elif price_diff > 0 and vol_slope < 1 and shortPositionPercentage >= Client_Sentiment_Check:
            limitDistance_value = str(int(price_diff * greedy_trader))
            limitDistance_value = str(int(limitDistance_value) * -1) 
            DIRECTION_TO_TRADE = "SELL"
        else:
            print ("!!DEBUG!! No trade, No Conditions Met!")
            return None
    
    else:
        print ("!!DEBUG!! No trade, std_err is WRONG!!")
        return None
    

    stopDistance_value = stop_loss_TR
    stopDistance_value = float(stopDistance_value) * cautious_trader
    stopDistance_value = str(int(stopDistance_value))

    #~~~~~~~Cautious Trader~~~~~~~~~~~~(stopDistance_value)
    if float(stopDistance_value) <= float(limitDistance_value):
        stopDistance_value = float(stopDistance_value) * cautious_trader
        stopDistance_value = str(int(stopDistance_value))

    if int(stopDistance_value) > 31: # Not at these high stop losses
        print ("!!DEBUG!! stopDistance too high")
        return None
    
    now = datetime.now()
    now_time = now.time()

    if now_time >= time(8,30) and now_time <= time(16,30):
        print ("!!DEBUG!!...LSE OPEN/Decent Volume ... continue on as you are")
    elif now_time >= time(14,30) and now_time <= time(20,59):
        print ("NY OPEN/Decent Volume")
    elif now_time >= time(23,30) and now_time <= time(3,30):
        print ("!!DEBUG!!...Overnight/Late Trading .... using slope")
        if float(slope) < greedy_trader:
            limitDistance_value = int(limitDistance_value) * float(slope)
            limitDistance_value = str(int(limitDistance_value))
            ###################################################
            stopDistance_value = int(stopDistance_value) * float(slope)
            stopDistance_value = str(int(stopDistance_value))
        else:
            return None #No trade early hours!!
    elif now_time >= time(3,30) and now_time <= time(8,29):
        print ("!!DEBUG!!...No early trading Zzzzzzzzzz!")
        return None #No trade early hours!!
        
    if int(limitDistance_value) <= 1 or int(stopDistance_value) <= 1:
        print ("!!DEBUG!!...Bailing Ooooot, Limit Distance/Stop Loss Below 1, Risk/Reward Not worth a trade")
        return None
        #Really don't bother!

    ###############################################################################################################
    print ("Order will be a " + str(DIRECTION_TO_TRADE) + " Order, With a limit of: " + str(limitDistance_value))
    print ("stopDistance_value for " + str(epic_id) + " will bet set at " + str(stopDistance_value))
    ###############################################################################################################
    #MAKE AN ORDER
    data = {"direction":DIRECTION_TO_TRADE,"epic": epic_id, "limitDistance":limitDistance_value, "orderType":orderType_value, "size":size_value,"expiry":expiry_value,"guaranteedStop":guaranteedStop_value,"currencyCode":currencyCode_value,"forceOpen":forceOpen_value,"stopDistance":stopDistance_value}
    igclient.setdebug(True)
    d = igclient.positions_otc(data)
    igclient.setdebug(False)
    
    deal_ref = d['dealReference']
    sleep(1)
    #CONFIRM MARKET ORDER
    d = igclient.confirms(deal_ref)
    DEAL_ID = d['dealId']
    print("DEAL ID : " + str(d['dealId']))
    print(d['dealStatus'])
    print(d['reason'])
    
    if str(d['reason']) == "INSUFFICIENT_FUNDS":
        print ("!!DEBUG!!...!!ERROR!! Wait for some funds to clear!!!....")
        sleep(1800)
        print ("-----------------DEBUG-----------------")
        print ("#################DEBUG#################")
        print ("!!DEBUG!! Resuming...")
        print ("-----------------DEBUG-----------------")
        print ("#################DEBUG#################")
        
    if str(d['reason']) != "SUCCESS":
        print ("-----------------DEBUG-----------------")
        print ("#################DEBUG#################")
        print ("!!DEBUG!!...!!ERROR!! Do something about this")
        print ("-----------------DEBUG-----------------")
        print ("#################DEBUG#################")
    else:
        print ("!!DEBUG!! ORDER OPEN")        

for x in range(0, 9999):
    
    OK_to_Trade = False
    
    while not OK_to_Trade:
        random.shuffle(epic_ids)
        epic_id = random.choice(epic_ids)
        now = datetime.now()
        now_time = now.time()
        
        if not now_time >= time(9,17) and now_time <= time(23,59):
            print ("!!DEBUG!!...Shouldn't be trading, Should be fast asleep")
            sleep(1800)
            continue
        else:
            # print ("!!DEBUG!! In time picking epic ....")
            pass

        print("!!DEBUG : Random epic_id is : " + str(epic_id), end='')
        d = igclient.markets(epic_id)

        bid_price = d['snapshot']['bid']
        ask_price = d['snapshot']['offer']
        MARKET_ID = d['instrument']['marketId']
        
        spread = float(bid_price) - float(ask_price)
        print (" spread : " + str(spread), end='')

        #if spread is less than -2, It's too big
        if float(spread) > -2:  # many forex will NEVER be below -2 - ig has minimum spreads
          OK_to_Trade = True
          #sleep(2)
        else:
          print (" - SPREAD TOO LARGE")
          OK_to_Trade = False
          sleep(2)
          continue #No point checking sentiment and wasting an API call!!
         
        d = igclient.clientsentiment(MARKET_ID)

        longPositionPercentage = float(d['longPositionPercentage'])
        shortPositionPercentage = float(d['shortPositionPercentage'])
        MarketID = str(d['marketId'])
    
        if shortPositionPercentage >= Client_Sentiment_Check or longPositionPercentage >= Client_Sentiment_Check:
            OK_to_Trade = True
        else:
            OK_to_Trade = False
            print("!!DEBUG!! Sentiment Check Failed!!")
            
    ###############################################
    #USING HISTORICAL
    ###############################################

    sleep(random.randint(1, 5)) #Wait to stop IG error
    
    y = [] # linearly generated sequence
    last_traded_volume = []
    
    d = igclient.prices(epic_id, 'MINUTE_30/8')

    for i in d['prices']:
        if i['lastTradedVolume'] is not None:
            last_traded_volume.append(i['lastTradedVolume'])
        y.append(float(i['highPrice']['bid']))

    d = igclient.prices(epic_id, 'HOUR/2')    

    for i in d['prices']:
        y.append(float(i['highPrice']['bid']))

    d = igclient.prices(epic_id, 'HOUR_4/1')    

    for i in d['prices']:
        y.append(float(i['highPrice']['bid']))
    
    xi = arange(0,len(last_traded_volume))
    A = array([ xi, ones((len(last_traded_volume)))])
    vol_slope, vol_intercept, vol_r_value, vol_p_value, vol_std_err = stats.linregress(xi,last_traded_volume)
    print ("#######LIN REG OF VOLUME##########")
    print (stats.linregress(xi,last_traded_volume))
 
    # Enable this on Windows to put some graphs in the directory, Doesnt work currently on Linux. 
    if draw_graphs:
        line = vol_slope*xi+vol_intercept
        now_file = datetime.now()
        plt.plot(xi,line,'r--',xi,last_traded_volume,'g--')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        plt.title(str(now_file) + " " + "(" + str(MarketID) + ")")
        plt.grid(True)
        graph_file_name = str(x) + "_" + str(MarketID) + ".png"
        plt.savefig(str(graph_file_name))
        show()
        plt.clf()
     
    xi = arange(0,len(y))
    A = array([ xi, ones((len(y)))])
    slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)
    
    print (stats.linregress(xi,y))
        
    remaining_allowance = d['allowance']['remainingAllowance']
    reset_time = humanize_time(int(d['allowance']['allowanceExpiry']))
    print ("-----------------DEBUG-----------------")
    print ("#################DEBUG#################")
    print ("Remaining API Calls left: " + str(remaining_allowance))
    print ("Time to API Key reset: " + str(reset_time))
    print ("-----------------DEBUG-----------------")
    print ("#################DEBUG#################")
    
    stop_loss_TR = calculate_stop_loss()
    print ("!!DEBUG!!...result from calculate_stop_loss() is ... " + str(stop_loss_TR))
    predicted_value = float(intercept)
    place_order(predicted_value,float(vol_slope))
