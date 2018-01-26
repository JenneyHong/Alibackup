#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import math

# Set script submit value
reload(sys)
# Set coding
sys.setdefaultencoding('utf-8')

def food_to_chose(argument):
	switcher = {
		0: "DaMI",
		1: "XiaoMF",
		2: "MiFan",
		3: "MianBao"
	}
	return switcher.get(argument, "nothing")

def func_to_chose(argument):
	switcher = {
		0: "Guo",
		1: "PingDG"
	}
	return switcher.get(argument, "worng")

def total_for_chose(chose_food,chose_func,org_money):
	if (chose_food == 0 and chose_func == 0):
		print "Cooking : MiFan"
		food_to_buy = org_money/180
		org_money_rel = food_to_buy*180
		print "Origin Money is %d" % org_money_rel
		total_star_2_0 =(food_to_buy)*190
		net_earn_2_0 = (food_to_buy)*(190-180)
		rate_star_2_0 = float(net_earn_2_0)/float(org_money_rel)
		total_star_2_5 =(food_to_buy)*210
		net_earn_2_5 = (food_to_buy)*(210-180)
		rate_star_2_5 = float(net_earn_2_5)/float(org_money_rel)
		print "MiFan of Star 2.0: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_2_0, net_earn_2_0, rate_star_2_0)
		print "MiFan of Star 2.5: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_2_5, net_earn_2_5, rate_star_2_5)
	elif (chose_food ==1 and chose_func ==0):
		print "Cooking : MianBao"
		food_to_buy = org_money/150
		org_money_rel = food_to_buy * 150
		print "Origin Money is %d" % org_money_rel
		total_star_2_0 =(food_to_buy)*170
		net_earn_2_0 = (food_to_buy)*(170-150)
		rate_star_2_0 = float(net_earn_2_0)/float(org_money_rel)
		total_star_2_5 =(food_to_buy)*190
		net_earn_2_5 = (food_to_buy)*(190-150)
		rate_star_2_5 = float(net_earn_2_5)/float(org_money_rel)
		print "MianBao of Star 2.0: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_2_0, net_earn_2_0, rate_star_2_0)
		print "MianBao of Star 2.5: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_2_5, net_earn_2_5, rate_star_2_5)
	elif (chose_food ==2 and chose_func ==0):
		print "Cooking: Zhou"
		food_to_buy = org_money/180
		org_money_rel = food_to_buy * 180
		print "Origin Money is %d" % org_money_rel
		total_star_2_5 =(food_to_buy)*200
		net_earn_2_5 = (food_to_buy)*(200-180)
		rate_star_2_5 = float(net_earn_2_5)/float(org_money_rel)
		total_star_3_0 =(food_to_buy)*230
		net_earn_3_0 = (food_to_buy)*(230-180)
		rate_star_3_0 = float(net_earn_3_0)/float(org_money_rel)
		total_star_3_5 =(food_to_buy)*250
		net_earn_3_5 = (food_to_buy)*(250-180)
		rate_star_3_5 = float(net_earn_3_5)/float(org_money_rel)
		print "Zhou of Star 2.5: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_2_5, net_earn_2_5, rate_star_2_5)
		print "Zhou of Star 3.0: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_3_0, net_earn_3_0, rate_star_3_0)
		print "Zhou of Star 3.5: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_3_5, net_earn_3_5, rate_star_3_5)
	elif (chose_food ==3 and chose_func ==1):
		print "Cooking: Tusi"
		food_to_buy = org_money/150
		org_money_rel = food_to_buy * 150
		print "Origin Money is %d" % org_money_rel
		total_star_2_5 =(food_to_buy)*180
		net_earn_2_5 = (food_to_buy)*(180-150)
		rate_star_2_5 = float(net_earn_2_5)/float(org_money_rel)
		total_star_3_0 =(food_to_buy)*200
		net_earn_3_0 = (food_to_buy)*(200-150)
		rate_star_3_0 = float(net_earn_3_0)/float(org_money_rel)
		total_star_3_5 =(food_to_buy)*220
		net_earn_3_5 = (food_to_buy)*(220-150)
		rate_star_3_5 = float(net_earn_3_5)/float(org_money_rel)		
		print "Tusi of Star 2.5: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_2_5, net_earn_2_5, rate_star_2_5)
		print "Tusi of Star 3.0: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_3_0, net_earn_3_0, rate_star_3_0)
		print "Tusi of Star 3.5: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_3_5, net_earn_3_5, rate_star_3_5)
	else:
		print "worng couple"
	return


org_money = (int)(raw_input(u"请输入初始本金:\n"))
chose_food = (int)(raw_input("please input your choice of food(0:大米, 1:小麦粉, 2:粥, 3:面包):\n"))
food_to_cook = food_to_chose(chose_food)
print "You chose food %s" % food_to_cook
chose_func = (int)(raw_input("please input your choice of cooking function(0:锅, 1:平底锅): \n"))
func_to_cook = func_to_chose(chose_func)
print "You chose Cooking Function %s" % func_to_cook
print "======Final================================"
print "Your Origin Money is %d" % org_money
print "Your Cooking Food is %s" % food_to_cook
print "Your Cooking Function is %s" % func_to_cook
total_for_chose(chose_food,chose_func,org_money)
