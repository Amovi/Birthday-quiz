from datetime import datetime
from calendar import month_name
name = input ("what is your name?")
month_b = input ("what is the month you were born in?")
year = input ("what year were you born in?")
day = input ("on what day were you born?")
if year == [2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000]:
    yeargroup=two thousands
if year == [1999, 1998, 1997,1996,1995,1994,1993,1992,1991,1990]:
    yeargroup=nineties
if year == [1989,1989,1987,1986,1985,1984,1983,1982,1981,1980]:
    yeargroup=eighties
if month == "january":
    season=winter
if month == "february":
    season=winter
if month == "march":
    season=spring
if month == "April":
    season=spring
if month == "May":
    season=spring
if month == "June":
    season=summer
if month == "July":
    season=summer
if month == "august":
    season=summer
if month == "september":
    season=fall
if month == "october":
    season=fall
if month == "november":
    season=fall
if month == "december":
    season=winter
print (name "you are a" yeargroup "baby born in" season)