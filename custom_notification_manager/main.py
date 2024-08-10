# Start with basic libraries
import time
from datetime import datetime

# Create a basic notification class
class Notification:
    def __init__(self, message, notify_time):
        self.message = message
        self.notify_time = notify_time

    def __str__(self):
        return f"Reminder: {self.message} at {self.notify_time}"
    
# Add Notifications
    
def add_notification(notifications):
    message = input("Enter the notification message: ")
    notify_time = input("Enter the time for the notification (YYYY-MM-DD HH:MM): ")
    notify_time = datetime.strptime(notify_time, "%Y-%m-%d %H:%M")
    notifications.append(Notification(message, notify_time))
    print("Notification added successfully!")
        
# Check and trigger notifications

def check_notifications(notifications):
    current_time = datetime.now()
    triggered_notifications = []
    
    for notification in notifications:
        if notification.notify_time <= current_time:
            print(f"ALERT: {notification.message}")
            triggered_notifications.append(notification)
            
            
# Remove triggered notifications from the list
    for notification in triggered_notifications:
        notifications.remove(notification)
    
    if not triggered_notifications:
        print("No notifications to display at this time.")
         
            
# Main Program Loop:
def main():
    notifications = []
    while True:
        print("\n1. Add Notification\n2. Check Notifications\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_notification(notifications)
        elif choice == '2':
            check_notifications(notifications)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
        
        time.sleep(1)  # Wait a bit before the next loop iteration

if __name__ == "__main__":
    main() 