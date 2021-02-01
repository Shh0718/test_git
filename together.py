import datetime

#now = datetime.datetime.now().strftime("%Y-%m-%d")
current_year = datetime.datetime.now().strftime("%Y")
current_month = datetime.datetime.now().strftime("%m")
current_day = datetime.datetime.now().strftime("%d")

d1 = datetime.date(int(current_year),int(current_month),int(current_day))
d2 = datetime.date(2020,7,18)
d3 = datetime.date(2020,6,8)
print("We've been together for {} days !!!".format((d1-d2).days+1))
print("We've been kown each other for {} days !!!".format((d1-d3).days+1))
