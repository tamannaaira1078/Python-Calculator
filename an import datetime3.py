
name = input("Enter Event Name: ")
e_event = input("Enter Event Date(YYYY-MM-DD): ")
print("===== EVENT COUNTDOWN =====")
print("-"*35)
import datetime
today = datetime.date.today()
event = datetime.date.strptime(
    e_event,
    "%Y-%m-%d"
)
remaining = event - today
if remaining.days>0:
    status = "Upcoming"
elif remaining.days<0:
    status = "Event is over" 
else:
    status = "Event is Today"       
print("===== EVENT COUNTDOWN =====")
print("-"*40)
print(f"{'Event':<15}:{name}")
print(f"{'Event Date':<15}:{e_event}")
print(f"{'Today':<15}:{today}")
print(f"{'Days Left':<15}:{remaining.days}")
print(f"{'Status':<15}:{status}")
print("-"*40)