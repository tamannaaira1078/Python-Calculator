print("TXT FILE REPORT")
print("-"*30)
import datetime
today = datetime.date.today()
Year = today.year
Month = today.month
Day = today.day
Days = datetime.timedelta(days=30)
after = today+Days
print(f"{'Today\'s Date':<18}:{today}")
print(f"{'Current Year':<18}:{Year}")
print(f"{'Current Month':<18}:{Month}")
print(f"{'Current Day':<18}:{Day}")
print(f"{'After 30 days':<18}:{after}")
