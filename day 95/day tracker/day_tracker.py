import os
from datetime import date

def log_activity(activity, duration):
    today = date.today()
    filename = f'logs/{today}.txt'
    log_entry = f'{today} - {activity}: {duration} hours\n'
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'a') as file:
        file.write(log_entry)
    
    print(f'Logged: {activity} - {duration} hours')

def view_logs():
    today = date.today()
    filename = f'logs/{today}.txt'
    
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            print(file.read())
    else:
        print(f'No logs found for {today}')

if __name__ == '__main__':
    print("Welcome to Day Tracker!")

    while True:
        print("\nMenu:")
        print("1. Log Activity")
        print("2. View Logs")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            activity = input("Enter the activity: ")
            duration = float(input("Enter the duration (in hours): "))
            log_activity(activity, duration)
        elif choice == '2':
            view_logs()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")



'''
import datetime
import json

def track_activity(activity, start_time, end_time):
  """Tracks an activity and saves it to the JSON file."""

  with open("data.json", "r+") as f:
    data = json.load(f)
    data["activities"].append({
      "activity": activity,
      "start_time": start_time.isoformat(),
      "end_time": end_time.isoformat(),
    })
    json.dump(data, f, indent=4)

def get_tracked_activities(date_filter=None):
  """Returns a list of all tracked activities, filtered by date if provided."""

  with open("data.json", "r") as f:
    data = json.load(f)
    activities = data["activities"]

    if date_filter:
      activities = [activity for activity in activities if activity["start_time"][:10] == date_filter]

    return activities

def main():
  """The main function of the app."""

  # Get the current time.
  now = datetime.datetime.now()

  # Start tracking the current activity.
  current_activity = input("What are you doing right now? ")
  start_time = now

  # Wait for the user to press enter to stop tracking the current activity.
  input("Press enter to stop tracking your activity. ")

  # End tracking the current activity.
  end_time = now

  # Save the tracked activity.
  track_activity(current_activity, start_time, end_time)

  # Get a list of all tracked activities.
  tracked_activities = get_tracked_activities()

  # Print the tracked activities.
  for activity in tracked_activities:
    print(f"{activity['activity']} ({activity['start_time']} - {activity['end_time']})")

if __name__ == "__main__":
  main()

'''