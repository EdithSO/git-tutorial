from datetime import datetime

def print_day(d):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    days_dict = dict(zip(range(7), days))
    
    print(days_dict[d])
    pass

def weekend_or_not(d):
    if 4 < d < 7:
        print("weekend")
    else:
	pass


current = datetime.now()
print_day(current.weekend())
if current.weekday() == 4:
    print("TGIF!!!")
weekend_or_not(current.weekday())
elif current.weekday()==0:
	print ("Monday")
else:
    days_till_weekend = 5 - current.weekday()
    print(f"{dats_till_weekend} left to weekend...")

    
