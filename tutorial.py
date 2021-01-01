from datetime import datetime

def print_day(d):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    days_dict = dict(zip(range(7), days))
    
    print(f" today is {days_dict[d]}")

def is_weekend(d):
    if d == 4:
        print("TGIF!!!")
    elif current.weekday() in [5,6]:
        print("WEEKEND!")
    else:
        days_till_weekend = 5 - current.weekday()
        print(f"{days_till_weekend} left to weekend...")
        

if __name__ == "__main__":
    
    current = datetime.now()
    print_day(current.weekend())
    is_weekend(current.weekend())

