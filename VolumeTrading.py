# IF YOU FOUND THIS USEFUL, Please Donate some Bitcoin ....
# 1FWt366i5PdrxCC6ydyhD8iywUHQ2C7BWC

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy
import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Scikit's LinearRegression model
from sklearn.linear_model import LinearRegression
from scipy import stats

import math
import os
import requests
import json
import time
import random
import uuid
from time import gmtime, strftime
import datetime as dt
from datetime import date
import calendar
import sys
import itertools
import operator

import sched

# ALL EPICS
main_epic_ids = [
    "CS.D.AUDUSD.TODAY.IP",
    "CS.D.EURCHF.TODAY.IP",
    "CS.D.EURGBP.TODAY.IP",
    "CS.D.EURJPY.TODAY.IP",
    "CS.D.EURUSD.TODAY.IP",
    "CS.D.GBPEUR.TODAY.IP",
    "CS.D.GBPUSD.TODAY.IP",
    "CS.D.USDCAD.TODAY.IP",
    "CS.D.USDCHF.TODAY.IP",
    "CS.D.USDJPY.TODAY.IP",
    "CS.D.CADCHF.TODAY.IP",
    "CS.D.CADJPY.TODAY.IP",
    "CS.D.CHFJPY.TODAY.IP",
    "CS.D.EURCAD.TODAY.IP",
    "CS.D.EURSGD.TODAY.IP",
    "CS.D.EURZAR.TODAY.IP",
    "CS.D.GBPCAD.TODAY.IP",
    "CS.D.GBPCHF.TODAY.IP",
    "CS.D.GBPJPY.TODAY.IP",
    "CS.D.GBPSGD.TODAY.IP",
    "CS.D.GBPZAR.TODAY.IP",
    "CS.D.MXNJPY.TODAY.IP",
    "CS.D.NOKJPY.TODAY.IP",
    "CS.D.PLNJPY.TODAY.IP",
    "CS.D.SEKJPY.TODAY.IP",
    "CS.D.SGDJPY.TODAY.IP",
    "CS.D.USDSGD.TODAY.IP",
    "CS.D.USDZAR.TODAY.IP",
    "CS.D.AUDCAD.TODAY.IP",
    "CS.D.AUDCHF.TODAY.IP",
    "CS.D.AUDEUR.TODAY.IP",
    "CS.D.AUDGBP.TODAY.IP",
    "CS.D.AUDJPY.TODAY.IP",
    "CS.D.AUDNZD.TODAY.IP",
    "CS.D.AUDSGD.TODAY.IP",
    "CS.D.EURAUD.TODAY.IP",
    "CS.D.EURNZD.TODAY.IP",
    "CS.D.GBPAUD.TODAY.IP",
    "CS.D.GBPNZD.TODAY.IP",
    "CS.D.NZDAUD.TODAY.IP",
    "CS.D.NZDCAD.TODAY.IP",
    "CS.D.NZDCHF.TODAY.IP",
    "CS.D.NZDEUR.TODAY.IP",
    "CS.D.NZDGBP.TODAY.IP",
    "CS.D.NZDJPY.TODAY.IP",
    "CS.D.NZDUSD.TODAY.IP",
    "CS.D.CHFHUF.TODAY.IP",
    "CS.D.EURCZK.TODAY.IP",
    "CS.D.EURHUF.TODAY.IP",
    "CS.D.EURILS.TODAY.IP",
    "CS.D.EURMXN.TODAY.IP",
    "CS.D.EURPLN.TODAY.IP",
    "CS.D.EURTRY.TODAY.IP",
    "CS.D.GBPCZK.TODAY.IP",
    "CS.D.GBPHUF.TODAY.IP",
    "CS.D.GBPILS.TODAY.IP",
    "CS.D.GBPMXN.TODAY.IP",
    "CS.D.GBPPLN.TODAY.IP",
    "CS.D.GBPTRY.TODAY.IP",
    "CS.D.TRYJPY.TODAY.IP",
    "CS.D.USDCZK.TODAY.IP",
    "CS.D.USDHUF.TODAY.IP",
    "CS.D.USDILS.TODAY.IP",
    "CS.D.USDMXN.TODAY.IP",
    "CS.D.USDPLN.TODAY.IP",
    "CS.D.USDTRY.TODAY.IP",
    "CS.D.CADNOK.TODAY.IP",
    "CS.D.CHFNOK.TODAY.IP",
    "CS.D.EURDKK.TODAY.IP",
    "CS.D.EURNOK.TODAY.IP",
    "CS.D.EURSEK.TODAY.IP",
    "CS.D.GBPDKK.TODAY.IP",
    "CS.D.GBPNOK.TODAY.IP",
    "CS.D.GBPSEK.TODAY.IP",
    "CS.D.NOKSEK.TODAY.IP",
    "CS.D.USDDKK.TODAY.IP",
    "CS.D.USDNOK.TODAY.IP",
    "CS.D.USDSEK.TODAY.IP",
    "CS.D.AUDCNH.TODAY.IP",
    "CS.D.CADCNH.TODAY.IP",
    "CS.D.CNHJPY.TODAY.IP",
    "CS.D.BRLJPY.TODAY.IP",
    "CS.D.GBPINR.TODAY.IP",
    "CS.D.USDBRL.TODAY.IP",
    "CS.D.USDIDR.TODAY.IP",
    "CS.D.USDINR.TODAY.IP",
    "CS.D.USDKRW.TODAY.IP",
    "CS.D.USDMYR.TODAY.IP",
    "CS.D.USDPHP.TODAY.IP",
    "CS.D.USDTWD.TODAY.IP",
    "CS.D.EURCNH.TODAY.IP",
    "CS.D.sp_EURRUB.TODAY.IP",
    "CS.D.GBPCNH.TODAY.IP",
    "CS.D.NZDCNH.TODAY.IP",
    "CS.D.USDCNH.TODAY.IP",
    "CS.D.sp_USDRUB.TODAY.IP"]
# ALL EPICS

# TESTINGs
#main_epic_ids = ['CS.D.AUDUSD.TODAY.IP', 'CS.D.EURGBP.TODAY.IP', 'CS.D.EURJPY.TODAY.IP', 'CS.D.EURUSD.TODAY.IP', 'CS.D.GBPUSD.TODAY.IP', 'CS.D.USDCAD.TODAY.IP', 'CS.D.USDCHF.TODAY.IP', 'CS.D.USDJPY.TODAY.IP', 'CS.D.AUDEUR.TODAY.IP', 'CS.D.AUDGBP.TODAY.IP', 'CS.D.AUDJPY.TODAY.IP', 'CS.D.EURAUD.TODAY.IP', 'CS.D.GBPAUD.TODAY.IP']
# TESTING


# TIME_FRAMES = ["MINUTE/1", "MINUTE_2/1", "MINUTE_3/1", "MINUTE_5/1", "MINUTE_10/1",
# "MINUTE_15/1", "MINUTE_30/1", "HOUR/1", "HOUR_2/1", "HOUR_3/1", "HOUR_4/1",
# "DAY/1", "WEEK/1", "MONTH/1"]

#####################################################################
#####################################################################
#####################################################################
#####################################################################
# REAL_OR_NO_REAL = 'https://demo-api.ig.com/gateway/deal'
# API_ENDPOINT = "https://demo-api.ig.com/gateway/deal/session"
# API_KEY = '***'
# #API_KEY = '***'
# #############################################################
# # API_KEY = '***' #<- DO NOT USE!!
# data = {"identifier": "***", "password": "***"}
#######################################################################
# FOR REAL....
#######################################################################
#######################################################################
#######################################################################
REAL_OR_NO_REAL = 'https://api.ig.com/gateway/deal'
API_ENDPOINT = "https://api.ig.com/gateway/deal/session"
API_KEY = '***'
###################################################
# API_KEY = '***' #<- DO NOT USE
data = {"identifier": "***", "password": "***"}

headers = {'Content-Type': 'application/json; charset=utf-8',
           'Accept': 'application/json; charset=utf-8',
           'X-IG-API-KEY': API_KEY,
           'Version': '2'
           }

r = requests.post(API_ENDPOINT, data=json.dumps(data), headers=headers)

headers_json = dict(r.headers)
CST_token = headers_json["CST"]
print(R"CST : " + CST_token)
x_sec_token = headers_json["X-SECURITY-TOKEN"]
print(R"X-SECURITY-TOKEN : " + x_sec_token)

# GET ACCOUNTS
base_url = REAL_OR_NO_REAL + '/accounts'
authenticated_headers = {'Content-Type': 'application/json; charset=utf-8',
                         'Accept': 'application/json; charset=utf-8',
                         'X-IG-API-KEY': API_KEY,
                         'CST': CST_token,
                         'X-SECURITY-TOKEN': x_sec_token}

auth_r = requests.get(base_url, headers=authenticated_headers)
d = json.loads(auth_r.text)

# print ("-----------------DEBUG-----------------")
# print ("#################DEBUG#################")
# print(auth_r.status_code)
# print(auth_r.reason)
# print (auth_r.text)
# print ("-----------------DEBUG-----------------")
# print ("#################DEBUG#################")

for i in d['accounts']:
    if str(i['accountType']) == "SPREADBET":
        print("Spreadbet Account ID is : " + str(i['accountId']))
        spreadbet_acc_id = str(i['accountId'])

# SET SPREAD BET ACCOUNT AS DEFAULT
base_url = REAL_OR_NO_REAL + '/session'
data = {"accountId": spreadbet_acc_id, "defaultAccount": "True"}
auth_r = requests.put(
    base_url,
    data=json.dumps(data),
    headers=authenticated_headers)

# print ("-----------------DEBUG-----------------")
# print ("#################DEBUG#################")
# print(auth_r.status_code)
# print(auth_r.reason)
# print (auth_r.text)
# print ("-----------------DEBUG-----------------")
# print ("#################DEBUG#################")
# ERROR about account ID been the same, Ignore!

##########################################################################
##########################END OF LOGIN CODE###############################
##########################END OF LOGIN CODE###############################
##########################END OF LOGIN CODE###############################
##########################END OF LOGIN CODE###############################
##########################################################################
# PROGRAMMABLE VALUES
# SET INITIAL VARIABLES, Hacky for now!
orderType_value = "MARKET"
size_value = "1"
expiry_value = "DFB"
guaranteedStop_value = True
currencyCode_value = "GBP"
forceOpen_value = True
stopDistance_value = "0"  # Make this a global variable for ease!


def percentage(part, whole):
    return 100 * float(part) / float(whole)


def humanize_time(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d:%02d:%02d' % (hours, mins, secs)


def lowest_spread_epic():
    spreads_and_epics = []
    i_count = 0
    pick_from_epics = []

    for epic_id in main_epic_ids:
        tmp_lst = []
        base_url = REAL_OR_NO_REAL + '/markets/' + epic_id
        auth_r = requests.get(base_url, headers=authenticated_headers)
        d = json.loads(auth_r.text)
        # print(auth_r.status_code)
        # print(auth_r.reason)
        # print (auth_r.text)
        # print (epic_id)

        try:
            i_count = i_count + 1
            if epic_id.find('MXN') != -1:
                print("!!DEBUG!!...skipping, FOUND MXN in..." + str(epic_id))
                time.sleep(1)
            elif epic_id.find('SEK') != -1:
                print("!!DEBUG!!...skipping, FOUND SEK in..." + str(epic_id))
                time.sleep(1)
            elif epic_id.find('NOK') != -1:
                print("!!DEBUG!!...skipping, FOUND NOK in..." + str(epic_id))
                time.sleep(1)
            elif epic_id.find('CNH') != -1:
                print("!!DEBUG!!...skipping, FOUND CNH in..." + str(epic_id))
                time.sleep(1)
            else:
                bid_price = d['snapshot']['bid']
                ask_price = d['snapshot']['offer']
                spread = float(bid_price) - float(ask_price)
                if float(spread) > -1:
                    # tmp_lst.append(epic_id)
                    # spreads_and_epics.append(tmp_lst)
                    pick_from_epics.append(epic_id)
                    # print ("bid : " + str(bid_price))
                    # print ("ask : " + str(ask_price))
                    # print ("-------------------------")
                    # print ("spread : " + str(spread))
                    # print ("-------------------------")
                    print("!!DEBUG!!...FOUND GOOD EPIC..." +
                          str(i_count) + "/" + str(len(main_epic_ids)))
                else:
                    print(
                        "!!DEBUG!!...skipping, NO GOOD EPIC....Checking next epic spreads..." +
                        str(i_count) +
                        "/" +
                        str(
                            len(main_epic_ids)))
                    time.sleep(1)
                    continue
        except Exception as e:
            print(e)
            pass

    # sorted_list = sorted(spreads_and_epics, key=operator.itemgetter(1))
    # for i in range(len(sorted_list)):
        # print(sorted_list[i])
    # print (max(sorted_list, key=lambda x: x[1]))

    # lowest_epic = max(sorted_list, key=lambda x: x[1])

    # return (str(lowest_epic[0]))
    return (pick_from_epics)


def calculate_stop_loss(d):

    price_ranges = []
    closing_prices = []
    first_time_round_loop = True
    TR_prices = []
    price_compare = "bid"

    for i in d['prices']:
        if first_time_round_loop:
            # First time round loop cannot get previous
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
            TR = max(high_price - low_price,
                     abs(high_price - prev_close),
                     abs(low_price - prev_close))
            #print (TR)
            TR_prices.append(TR)

    return str(int(float(max(TR_prices))))


def are_we_going_to_trade(epic_id, TRADE_DIRECTION):

    if TRADE_DIRECTION == "NONE":
        return None

    limitDistance_value = "16"
    DIRECTION_TO_TRADE = TRADE_DIRECTION

    ##########################################################################
    print(
        "Order will be a " +
        str(DIRECTION_TO_TRADE) +
        " Order, With a limit of: " +
        str(limitDistance_value))
    print(
        "stopDistance_value for " +
        str(epic_id) +
        " will bet set at " +
        str(stopDistance_value))
    ##########################################################################

    # MAKE AN ORDER
    base_url = REAL_OR_NO_REAL + '/positions/otc'
    data = {
        "direction": DIRECTION_TO_TRADE,
        "epic": epic_id,
        "limitDistance": limitDistance_value,
        "orderType": orderType_value,
        "size": size_value,
        "expiry": expiry_value,
        "guaranteedStop": guaranteedStop_value,
        "currencyCode": currencyCode_value,
        "forceOpen": forceOpen_value,
        "stopDistance": stopDistance_value}
    r = requests.post(
        base_url,
        data=json.dumps(data),
        headers=authenticated_headers)

    print("-----------------DEBUG-----------------")
    print("#################DEBUG#################")
    print(r.status_code)
    print(r.reason)
    print(r.text)
    print("-----------------DEBUG-----------------")
    print("#################DEBUG#################")

    d = json.loads(r.text)
    deal_ref = d['dealReference']
    time.sleep(1)
    # CONFIRM MARKET ORDER
    base_url = REAL_OR_NO_REAL + '/confirms/' + deal_ref
    auth_r = requests.get(base_url, headers=authenticated_headers)
    d = json.loads(auth_r.text)
    DEAL_ID = d['dealId']
    print("DEAL ID : " + str(d['dealId']))
    print(d['dealStatus'])
    print(d['reason'])

    if str(d['reason']) != "SUCCESS":
        print("!!DEBUG!!...!!some thing occurred ERROR!!")
        # TO DO :- Remove this and treat like a normal error...Eventually! But
        # for now acts as very basic rate limiting
        time.sleep(10)
        print("-----------------DEBUG-----------------")
        print("#################DEBUG#################")
        print("!!DEBUG!! Resuming...")
        print("-----------------DEBUG-----------------")
        print("#################DEBUG#################")
    else:
        print("-----------------DEBUG-----------------")
        print("#################DEBUG#################")
        print("!!DEBUG!!...Yay, ORDER OPEN")
        print("-----------------DEBUG-----------------")
        print("#################DEBUG#################")


def vol_price_action(time_frame, epic_id):

    all_prices = []  # MUST MUST CLEAR OUT THIS EACH TIME ROUND LOOP!!!
    low_prices = []
    high_prices = []
    ltv = []  # MUST MUST CLEAR OUT THIS EACH TIME ROUND LOOP!!!
    time.sleep(1)

    base_url = REAL_OR_NO_REAL + "/prices/" + epic_id + time_frame
    # Price resolution (MINUTE, MINUTE_2, MINUTE_3, MINUTE_5, MINUTE_10,
    # MINUTE_15, MINUTE_30, HOUR, HOUR_2, HOUR_3, HOUR_4, DAY, WEEK, MONTH)
    auth_r = requests.get(base_url, headers=authenticated_headers)
    d = json.loads(auth_r.text)

    # print ("-----------------DEBUG-----------------")
    # print ("#################DEBUG#################")
    # print(auth_r.status_code)
    # print(auth_r.reason)
    # print (auth_r.text)
    # print ("-----------------DEBUG-----------------")
    # print ("#################DEBUG#################")

    remaining_allowance = d['allowance']['remainingAllowance']
    reset_time = humanize_time(int(d['allowance']['allowanceExpiry']))
    print("-----------------DEBUG-----------------")
    print("#################DEBUG#################")
    print("Remaining API Calls left: " + str(remaining_allowance))
    print("Time to API Key reset: " + str(reset_time))
    print("-----------------DEBUG-----------------")
    print("#################DEBUG#################")

    for i in d['prices']:

        lastTradedVolume = i['lastTradedVolume']
        ltv.append(lastTradedVolume)
        #######################################
        if i['highPrice']['bid'] is not None:
            highPrice = i['highPrice']['bid']
            all_prices.append(highPrice)
        ########################################
        if i['lowPrice']['bid'] is not None:
            lowPrice = i['lowPrice']['bid']
            all_prices.append(lowPrice)

    ltv = numpy.asarray(ltv)
    xi = numpy.arange(0, len(ltv))
    A = numpy.array([xi, numpy.ones((len(ltv)))])
    ltv_slope, ltv_intercept, ltv_r_value, ltv_p_value, ltv_std_err = stats.linregress(
        xi, ltv)
    print("-----------------DEBUG-----------------")
    print("#################DEBUG#################")
    print(stats.linregress(xi, ltv))
    print("-----------------DEBUG-----------------")
    print("#################DEBUG#################")
    print("\n")
    print("\n")
    print("\n")
    # line = ltv_slope*xi+ltv_intercept
    # plt.plot(xi,line,'r--',xi,ltv,'g--')
    # plt.xlabel('X Axis')
    # plt.ylabel('Y Axis')
    # plt.show()
    # plt.clf()

    all_prices = numpy.asarray(all_prices)
    xi = numpy.arange(0, len(all_prices))
    A = numpy.array([xi, numpy.ones((len(all_prices)))])
    all_prices_slope, all_prices_intercept, all_prices_r_value, all_prices_p_value, all_prices_std_err = stats.linregress(
        xi, all_prices)
    print("-----------------DEBUG-----------------")
    print("#################DEBUG#################")
    print(stats.linregress(xi, all_prices))
    print("-----------------DEBUG-----------------")
    print("#################DEBUG#################")
    # line = all_prices_slope*xi+all_prices_intercept
    # plt.plot(xi,line,'r--',xi,all_prices,'g--')
    # plt.xlabel('X Axis')
    # plt.ylabel('Y Axis')
    # plt.show()
    # plt.clf()

    if ltv_slope > 0:  # 0.1 because, Well not strong enough i.e Noise!
        VOLUME_ACTION = "UP"
    elif ltv_slope <= 0:
        VOLUME_ACTION = "DOWN"

    if all_prices_slope > 0:
        PRICE_ACTION = "UP"
    elif all_prices_slope <= 0:
        PRICE_ACTION = "DOWN"

    print("-----------------DEBUG-----------------")
    print("#################DEBUG#################")
    print("VOLUME_ACTION IS ...." + str(VOLUME_ACTION))
    print("PRICE_ACTION IS ...." + str(PRICE_ACTION))
    print("-----------------DEBUG-----------------")
    print("#################DEBUG#################")

    return VOLUME_ACTION, PRICE_ACTION


def Chandelier_Exit_formula(TRADE_DIR, ATR, Price):
    # Chandelier Exit (long) = 22-day High - ATR(22) x 3
    # Chandelier Exit (short) = 22-day Low + ATR(22) x 3

    if TRADE_DIR == "BUY":

        return float(Price) - float(ATR) * 3

    elif TRADE_DIR == "SELL":

        return float(Price) + float(ATR) * 3


if __name__ == '__main__':

    while True:

        try:

            base_url = REAL_OR_NO_REAL + "/accounts"
            auth_r = requests.get(base_url, headers=authenticated_headers)
            d = json.loads(auth_r.text)

            # print ("-----------------DEBUG-----------------")
            # print ("#################DEBUG#################")
            # print(auth_r.status_code)
            # print(auth_r.reason)
            # print (auth_r.text)
            # print ("-----------------DEBUG-----------------")
            # print ("#################DEBUG#################")

            for i in d['accounts']:
                if str(i['accountType']) == "SPREADBET":
                    balance = i['balance']['balance']
                    deposit = i['balance']['deposit']

            percent_used = percentage(deposit, balance)

            print("-----------------DEBUG-----------------")
            print("#################DEBUG#################")
            print("Percent of account used ..." + str(percent_used))
            print("-----------------DEBUG-----------------")
            print("#################DEBUG#################")

            if float(percent_used) > 60:
                print("Don't trade, Too much margin used up already")
                time.sleep(60)
                continue
            else:
                print("OK to trade!!")

            tradeable_epic_ids = lowest_spread_epic()

        except Exception as e:
            print(e)
            print("No Suitable Epics...Yet!!, Try again!!")
            continue

        for epic_id in tradeable_epic_ids:

            print("!!DEBUG!!...chosen epic is ..." + str(epic_id))
            time.sleep(2)  # Generic Rate Limit for IG Index API....

            while True:
                print("Waiting..." + str(time.strftime("%S")))
                time.sleep(1)
                if str(time.strftime("%S")) == "59":
                    break

            VOLUME_4h, PRICE_4h = vol_price_action("/HOUR/4", epic_id)

            print("-----------------DEBUG-----------------")
            print("#################DEBUG#################")
            if PRICE_4h == "UP" and VOLUME_4h == "UP":
                print("Price up and volume up is the bullish signal for the market (or pair). It shows the market is in an uptrend and more and more traders want to enter in the pair.")
                TRADE_DIRECTION = "BUY"
            elif PRICE_4h == "UP" and VOLUME_4h == "DOWN":
                print("Price up and volume down is a dangerous situation for the market as well as for the inexperienced trader where the distribution is done by the smart investors who have some inside information about the market. Price and volume analysis is very helpful at this point which shows the clear divergence where price is moving up but volume is not supporting the up movement giving the early signal of smart money exit.")
                TRADE_DIRECTION = "NONE"
            elif PRICE_4h == "DOWN" and VOLUME_4h == "UP":
                print("This is the situation where nobody wants to continue with their long position and wants to exit from the pair. This is the divergence point where price moves down and the volume goes up.")
                TRADE_DIRECTION = "SELL"
            elif PRICE_4h == "DOWN" and VOLUME_4h == "DOWN":
                print(
                    "Price down and volume down is the market situation where the market is near its bottom.")
                TRADE_DIRECTION = "BUY"
            else:
                TRADE_DIRECTION = "NONE"
            print("-----------------DEBUG-----------------")
            print("#################DEBUG#################")

            base_url = REAL_OR_NO_REAL + "/markets/" + epic_id
            auth_r = requests.get(base_url, headers=authenticated_headers)
            d = json.loads(auth_r.text)

            bid_price = d['snapshot']['bid']

            try:
                base_url = REAL_OR_NO_REAL + "/prices/" + epic_id + "/HOUR/4"
                # Price resolution (MINUTE, MINUTE_2, MINUTE_3, MINUTE_5,
                # MINUTE_10, MINUTE_15, MINUTE_30, HOUR, HOUR_2, HOUR_3,
                # HOUR_4, DAY, WEEK, MONTH)
                auth_r = requests.get(base_url, headers=authenticated_headers)
                d = json.loads(auth_r.text)

                ATR = calculate_stop_loss(d)
                high_prices = []
                low_prices = []

                for i in d['prices']:

                    if i['highPrice']['bid'] is not None:
                        highPrice = i['highPrice']['bid']
                        high_prices.append(highPrice)
                    ########################################
                    if i['lowPrice']['bid'] is not None:
                        lowPrice = i['lowPrice']['bid']
                        low_prices.append(lowPrice)

                if TRADE_DIRECTION == "SELL":

                    ce_stop = Chandelier_Exit_formula(
                        TRADE_DIRECTION, ATR, min(low_prices))
                    tmp_stop = int(float(bid_price) - (ce_stop))

                    if tmp_stop < 0:
                        tmp_stop = int(tmp_stop * -1)  # Make Positive

                    if tmp_stop > 49:  # Final Check
                        TRADE_DIRECTION = "NONE"
                    else:
                        stopDistance_value = str(tmp_stop)

                elif TRADE_DIRECTION == "BUY":

                    ce_stop = Chandelier_Exit_formula(
                        TRADE_DIRECTION, ATR, max(high_prices))
                    tmp_stop = int(float(bid_price) - (ce_stop))

                    if tmp_stop < 0:
                        tmp_stop = int(tmp_stop * -1)  # Make Positive

                    if tmp_stop > 49:  # Final Check
                        TRADE_DIRECTION = "NONE"
                    else:
                        stopDistance_value = str(tmp_stop)

            except BaseException:
                print("Cannot reliably set Stop Loss, Bailing Out!")
                TRADE_DIRECTION = "NONE"

            ###################################################################
            ##########################END OF DATA CODE#########################
            ##########################END OF DATA CODE#########################
            ##########################END OF DATA CODE#########################
            ##########################END OF DATA CODE#########################
            ###################################################################
            try:
                are_we_going_to_trade(epic_id, TRADE_DIRECTION)
            except Exception as e:
                print(e)
                print("Something fucked up!!, Try again!!")
                continue
