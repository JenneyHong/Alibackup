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

def food_all_cost(argument):
	switcher = {
		0: [180,190,210],
		1: [150,170,190],
		2: [180,200,230,250],
		3: [150,180,200,220]
	}
	org = switcher.get(argument)[0]
	star1 = switcher.get(argument)[1]
	star2 = switcher.get(argument)[2]
	if argument == 0 or argument ==1:
		stars = [org, star1, star2]
	else:
		star3 = switcher.get(argument)[3]
		stars = [org, star1, star2,star3]
	return stars


def total_for_chose(chose_food,chose_func,org_money,food_all_cost):
	org_cost = food_all_cost(chose_food)[0]
	food_to_buy = org_money/org_cost
	org_money_rel = food_to_buy * org_cost

	#star 1
	total_star_1 = food_to_buy * food_all_cost(chose_food)[1]
	net_earn_1 = food_to_buy * (food_all_cost(chose_food)[1]-org_cost)
	rate_star_1 = float(net_earn_1)/float(org_money_rel)

	#star 2
	total_star_2 = food_to_buy * food_all_cost(chose_food)[2]
	net_earn_2 = food_to_buy * (food_all_cost(chose_food)[2]-org_cost)
	rate_star_2 = float(net_earn_2)/float(org_money_rel)	

	#star 3
	total_star_3 = food_to_buy * food_all_cost(chose_food)[2]
	net_earn_3 = food_to_buy * (food_all_cost(chose_food)[2]-org_cost)
	rate_star_3 = float(net_earn_3)/float(org_money_rel)


	if (chose_food == 0 and chose_func == 0):
		print "Cooking : MiFan"
		print "Origin Money is %d" % org_money_rel
		print "MiFan of Star 2.0: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_1, net_earn_1, rate_star_1)
		print "MiFan of Star 2.5: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_2, net_earn_2, rate_star_2)
	elif (chose_food ==1 and chose_func ==0):
		print "Cooking : MianBao"
		print "Origin Money is %d" % org_money_rel
		print "MianBao of Star 2.0: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_1, net_earn_1, rate_star_1)
		print "MianBao of Star 2.5: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_2, net_earn_2, rate_star_2)
	elif (chose_food ==2 and chose_func ==0):
		print "Cooking: Zhou"
		print "Origin Money is %d" % org_money_rel
		print "Zhou of Star 2.5: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_1, net_earn_1, rate_star_1)
		print "Zhou of Star 3.0: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_2, net_earn_2, rate_star_2)
		print "Zhou of Star 3.5: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_3, net_earn_3, rate_star_3)
	elif (chose_food ==3 and chose_func ==1):
		print "Cooking: Tusi"
		print "Origin Money is %d" % org_money_rel		
		print "Tusi of Star 2.5: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_1, net_earn_1, rate_star_1)
		print "Tusi of Star 3.0: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_2, net_earn_2, rate_star_2)
		print "Tusi of Star 3.5: tatal money is %d, net earnings %d, and rate is %.2f%%" % (total_star_3, net_earn_3, rate_star_3)
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
total_for_chose(chose_food,chose_func,org_money,food_all_cost)