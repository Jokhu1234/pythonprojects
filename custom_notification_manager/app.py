import json
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

NOTIFICATIONS_FILE = 'notifications.json'

# Notification class
class Notification:
    def __init__(self, message, notify_time):
        self.message = message
        self.notify_time = notify_time

    def __str__(self):
        return f"Reminder: {self.message} at {self.notify_time}"

    def to_dict(self):
        return {
            'message': self.message,
            'notify_time': self.notify_time.strftime("%Y-%m-%d %H:%M")
        }

    @classmethod
    def from_dict(cls, data):
        notify_time = datetime.strptime(data['notify_time'], "%Y-%m-%d %H:%M")
        return cls(data['message'], notify_time)

def load_notifications():
    try:
        with open(NOTIFICATIONS_FILE, 'r') as f:
            data = json.load(f)
            return [Notification.from_dict(item) for item in data]
    except FileNotFoundError:
        return []

def save_notifications(notifications):
    with open(NOTIFICATIONS_FILE, 'w') as f:
        json.dump([n.to_dict() for n in notifications], f)

notifications = load_notifications()

@app.route('/')
def index():
    current_time = datetime.now()
    triggered_notifications = []

    for notification in notifications:
        if notification.notify_time <= current_time:
            triggered_notifications.append(notification)

    for notification in triggered_notifications:
        notifications.remove(notification)
    
    save_notifications(notifications)

    return render_template('index.html', notifications=notifications, triggered_notifications=triggered_notifications)

@app.route('/add', methods=['POST'])
def add_notification():
    message = request.form['message']
    notify_time = request.form['notify_time']
    notify_time = datetime.strptime(notify_time, "%Y-%m-%d %H:%M")
    notifications.append(Notification(message, notify_time))
    save_notifications(notifications)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)