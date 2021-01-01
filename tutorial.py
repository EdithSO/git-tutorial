from datetime import datetime

def print_day(d):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    days_dict = dict(zip(range(7), days))
    
    print(days_dict[d])


current = datetime.now()
print_day(current.weekend())
if current.weekday() == 4:
    print("TGIF!!!")
elif current.weekday() in [5,6]:
    print("WEEKEND!")
else:
    days_till_weekend = 5 - current.weekday()
    print(f"{dats_till_weekend} left to weekend...")

    