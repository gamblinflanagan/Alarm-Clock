import os
import time
from datetime import datetime
from datetime import date
import calendar

time.sleep(1.0)

now = datetime.now()
today = date.today()

lst = []

cmin = now.strftime("%M")
chour = int(now.strftime("%H"))

if chour < 12:
    meridian = "A M"
    if chour == 0:
        chour = 12
else:
    meridian = "P M"
    if chour > 12:
        chour -=12
    
if meridian == "A M":
    st1 = "Good morning sir,"
elif chour < 5 or chour ==  12:
    st1 = "Good afternoon sir,"
else: 
    st1 = "Good evening sir,"

if cmin == "00":
    cmin = ""

st2 = "It is " + str(chour) + " "  + cmin + " " + meridian + ","

lst.append(st1)
lst.append(st2)


date = today.strftime("%B %d")
day = datetime.today().weekday()
nday = calendar.day_name[day]

st3 = nday + ", " + date + "th,"

lst.append(st3)




outf = open("morning_main1.txt", "w+")
outf.write(str(lst))
outf.close()

os.system("say -f morning_main1.txt")
os.system("say -f morning_main2.txt")
os.system("say -f custom.txt")
#os.system("say I hope you slept well sir,")


