birthdate = input("Enter Birthday(YYYY-MM-DD): ")
import datetime
print("BIRTHDAY COUNTDOWN")
print("-"*30)
today = datetime.date.today()
birthday = datetime.date.strptime(
    birthdate,
    "%Y-%m-%d"
)
remaining = birthday - today
print(f"{'Birthday':<18}:{today}")
print(f"{'Days Remaining':<18}:{remaining.days}")
