

import curses
import ssl
import time
import psutil
import csv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule


# Function to show system information
def show_system_info(window):
    window.clear()
    window.addstr(1, 1, "System Information", curses.color_pair(1) | curses.A_BOLD)
    window.addstr(3, 1, f"Current Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}", curses.color_pair(2))
    window.addstr(5, 1, "Press any key to return to the menu.", curses.A_NORMAL)
    window.refresh()
    window.getch()


# Function to show metrics and collect them into a dictionary
def show_metrics(window):
    window.clear()
    window.addstr(1, 1, "Metrics", curses.color_pair(1) | curses.A_BOLD)

    # CPU usage
    cpu_percent = psutil.cpu_percent()
    window.addstr(3, 1, f"CPU Usage: {cpu_percent}%", curses.color_pair(2))

    # Memory usage
    mem = psutil.virtual_memory()
    mem_used_percent = mem.percent
    mem_total = round(mem.total / (1024 * 1024 * 1024), 2)  # Convert bytes to GB
    mem_used = round(mem.used / (1024 * 1024 * 1024), 2)
    window.addstr(4, 1, f"Memory Usage: {mem_used_percent}% ({mem_used}GB / {mem_total}GB)", curses.color_pair(2))

    # Disk usage
    disk = psutil.disk_usage('/')
    disk_used_percent = disk.percent
    disk_total = round(disk.total / (1024 * 1024 * 1024), 2)  # Convert bytes to GB
    disk_used = round(disk.used / (1024 * 1024 * 1024), 2)
    window.addstr(5, 1, f"Disk Usage: {disk_used_percent}% ({disk_used}GB / {disk_total}GB)", curses.color_pair(2))

    # Logged-in users
    users = len(psutil.users())
    window.addstr(6, 1, f"Logged-in Users: {users}", curses.color_pair(2))

    window.addstr(8, 1, "Press any key to return to the menu.", curses.A_NORMAL)
    window.refresh()
    window.getch()

    # Check if RAM usage exceeds a threshold (e.g., 90%)
    if mem_used_percent > 90:
        send_email(f"WARNING: RAM usage is critical ({mem_used_percent}%).")

    
    # Collect metrics into a dictionary
    metrics = {
        'CPU Usage (%)': cpu_percent,
        'Memory Usage (%)': mem_used_percent,
        'Memory Total (GB)': mem_total,
        'Memory Used (GB)': mem_used,
        'Disk Usage (%)': disk_used_percent,
        'Disk Total (GB)': disk_total,
        'Disk Used (GB)': disk_used,
        'Logged-in Users': users
    }


    return metrics


# Function to write metrics to CSV file

# Function to send email
def send_email(ram_usage):
    sender_email = "m.elsaleh88@gmail.com"
    receiver_email = "m.elsaleh88@gmail.com"
    password = "kuizqsnaoxedndsn"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Critical RAM Usage Alert"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = f"WARNING: RAM usage is critical ({ram_usage}%)."
    part1 = MIMEText(text, "plain")

    message.attach(part1)

    context=ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# Function to send the weekly system report via email
def send_weekly_report():
    # Function to send email
    def send_email(ram_usage):
        sender_email = "m.elsaleh88@gmail.com"
        receiver_email = "m.elsaleh88@gmail.com"
        password = "kuizqsnaoxedndsn"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Weekly System Report"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = f"Weekly System Report:\n\n"
        # Add system metrics to the email body
        text += f"CPU Usage: {psutil.cpu_percent()}%\n"
        mem = psutil.virtual_memory()
        text += f"Memory Usage: {mem.percent}%\n"
        text += f"Disk Usage: {psutil.disk_usage('/').percent}%\n"
        text += f"Logged-in Users: {len(psutil.users())}\n"

        part1 = MIMEText(text, "plain")
        message.attach(part1)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

    # Call the send_email function to send the report
    send_email(psutil.virtual_memory().percent)

# Schedule sending the weekly report every Monday at 9:00 AM
schedule.every().monday.at("09:00").do(send_weekly_report)


# Function to write metrics to CSV file
def write_metrics_to_csv(metrics):
    with open('metrics.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for metric, value in metrics.items():
            writer.writerow([metric, value])


# Main menu function
def main_menu(window):
    window.clear()
    window.addstr(1, 1, "Main Menu", curses.color_pair(1) | curses.A_BOLD)
    window.addstr(3, 1, "1. Show System Information", curses.A_NORMAL)
    window.addstr(4, 1, "2. Show Metrics", curses.A_NORMAL)
    window.addstr(5, 1, "3. Quit", curses.A_NORMAL)
    window.addstr(7, 1, "Enter your choice: ")
    window.refresh()
    choice = window.getch()
    if choice == ord('1'):
        show_system_info(window)
    elif choice == ord('2'):
        metrics = show_metrics(window)
        write_metrics_to_csv(metrics)
    elif choice == ord('3'):
        return False
    return True

# Main function
def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLUE)  # Color pair for titles (yellow on blue)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)    # Color pair for content (cyan on black)

    # Get screen dimensions
    screen_height, screen_width = stdscr.getmaxyx()

    # Create a window with blue background and white borders
    window_height = 25
    window_width = 100
    window_y = (screen_height - window_height) // 2
    window_x = (screen_width - window_width) // 2
    window = curses.newwin(window_height, window_width, window_y, window_x)
    window.bkgd(' ', curses.color_pair(1))  # Set background color
    window.box()  # Draw a border around the window
    window.refresh()

    while True:
        if not main_menu(window):
            break

# Run the main function
curses.wrapper(main)
