# utils/auth.py
import csv
from datetime import datetime

# Sample user data
users = {
    "admin": {"password": "admin_pass", "role": "Admin"},
    "analyst": {"password": "analyst_pass", "role": "Security Analyst"},
    "operator": {"password": "operator_pass", "role": "Operator"},
}

def login(username, password):
    """Check if the username and password are correct."""
    if username in users and users[username]["password"] == password:
        # Log to audit trail
        with open('audit_trail.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f"{username} logged in."])
        return True
    return False

def check_role(username):
    """Return the role of the user."""
    return users[username]["role"] if username in users else None