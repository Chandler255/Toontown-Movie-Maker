from datetime import datetime

date = datetime.today()
month = date.month
day = date.day

isHalloween = False
isWinter = False

if month == 10 and day >= 20 and day <= 31:
	isHalloween = True
	
if month == 12 and day >= 7 and day <= 31:
	isWinter = True
