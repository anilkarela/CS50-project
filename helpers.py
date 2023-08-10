from datetime import datetime, timedelta


def time_ago(timestamp):
    current_time = datetime.now()
    time_difference = current_time - datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

    if time_difference < timedelta(minutes=1):
        seconds = time_difference.seconds
        return f"{seconds} seconds ago"
    elif time_difference < timedelta(hours=1):
        minutes = time_difference.seconds // 60
        return f"{minutes} minutes ago"
    elif time_difference < timedelta(days=1):
        hours = time_difference.seconds // 3600
        return f"{hours} hours ago"
    else:
        days = time_difference.days
        return f"{days} days ago"