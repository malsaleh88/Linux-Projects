# System Metrics Monitor

## Introduction
This Python script provides a simple system metrics monitor using the curses library. It displays system information such as CPU usage, memory usage, disk usage, and logged-in users. Users can navigate through the menu to view system information, metrics, and quit the program.

## Requirements
- Python 3.12 or higher
- [psutil](https://pypi.org/project/psutil/) library (for system monitoring)
- [curses](https://docs.python.org/3/library/curses.html) library (for terminal-based user interface)
- ssl module (for secure socket layer support)
- csv module (for reading and writing CSV files)
- os module (for operating system interaction)
- smtplib module (for sending email)
- email.mime.multipart module (for creating multipart email messages)
- email.mime.text module (for creating text email messages)

## Usage
1. Run the script using Python 3.12 or higher.
2. The main menu will be displayed.
3. Choose an option:
   - **1. Show System Information**: Displays current system information including the current time.
   - **2. Show Metrics**: Displays system metrics such as CPU usage, memory usage, disk usage, and logged-in users. Metrics are also saved to a CSV file named `metrics.csv`.
   - **3. Quit**: Exits the program.
4. Follow the on-screen instructions to navigate through the menu.

## CSV Metric Report
The script saves system metrics to a CSV file named `metrics.csv` in the same directory. The CSV file includes the following metrics:
- CPU Usage (%)
- Memory Usage (%)
- Memory Total (GB)
- Memory Used (GB)
- Disk Usage (%)
- Disk Total (GB)
- Disk Used (GB)
- Logged-in Users

## Email Notification

The system is configured to automatically send an email notification under the following circumstances:

### High RAM Usage Alert
The system monitors RAM usage, and if it exceeds 90%, an email notification is triggered. This feature serves as an alert mechanism to notify the user about the critical system state. When triggered, an email containing a warning message regarding the high RAM usage is sent to the user's email address.

### Weekly Report Notification
Additionally, the system is programmed to send a weekly report via email. The report is scheduled to be sent every Monday at 9:00 AM local time. The report contains essential system metrics and usage information for the previous week, providing insights into system performance and resource utilization.

These email notifications enhance system monitoring and provide timely alerts and reports to the user, facilitating proactive management and maintenance of the system.


## Example
To run the script:
```bash
python3 cur.py
```

## Test

![1](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/5f87c197-6af3-4650-9b94-70acb5562ccf)


![2](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/2597913b-0a85-4292-a87b-90fb70d58bd8)

![3](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/f78c9821-3e4b-4c29-a933-1a3508a09c0c)

![4](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/8945fd49-bafa-4575-aa6d-2c0f2c716562)


![email](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/125745ed-09fb-4a1b-b966-8787e3f52e2c)



## Test on remote machine


![6](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/dfe59a29-bbbf-4350-a4e0-f96320fab3a1)


![8](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/e142f725-94b8-4558-9939-7dbcc73b387d)


## Weekly Report Schedule

The weekly report is scheduled to be sent every Monday at 9:00 AM. However, during testing, the scheduling is set to occur at 4:22 PM to facilitate testing procedures.

To accommodate testing requirements, the scheduling time has been adjusted to 4:22 PM. Once testing is completed, the scheduling will revert to the regular time of 9:00 AM every Monday.


![111](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/3c9b2d62-0784-48e8-b358-af86695ab7f0)


![55](https://github.com/malsaleh88/BXL-k4MK4r-2/assets/141853984/7ef49cc9-c5d6-42da-826b-11813ce5737f)

