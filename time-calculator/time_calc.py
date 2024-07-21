def start_time(start):
    parts = start.split()
    time_part = parts[0]
    period_part = parts[1]
    hour, minutes = map(int, time_part.split(':'))
    return hour, minutes, period_part

def duration_time(duration):
    
    hour, minutes = map(int, duration.split(':'))
    return hour, minutes

def to_24_format(hour, period):
    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0
    return hour

def add_time_and_duration(start_hour, start_minutes, duration_hour, duration_minutes):
    add_hours = start_hour + duration_hour
    add_minutes = start_minutes + duration_minutes

    # if overflow of minutes 
    if add_minutes >= 60:
        add_hours += add_minutes // 60
        add_minutes = add_minutes % 60
    
    #  calculate days later
    days_later = add_hours // 24
    add_hours = add_hours % 24

    return add_hours, add_minutes, days_later 

def back_to_12_hour(hour):
    period = 'AM'
    if hour >= 12:
        period = 'PM'
    if hour > 12:
        hour -= 12
    if hour == 0:
        hour = 12
    return hour, period

def formatted_output(hour, minutes, period, days_later, starting_day=None):
    result = f"{hour}:{minutes:02d} {period}"
    if starting_day:
        result += f", {starting_day}"
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"
    return result


def add_time(start, duration, starting_day=None):
    
    start_hour, start_minutes, start_period = start_time(start)
    
    duration_hour, duration_minutes = duration_time(duration)
    
    start_hour = to_24_format(start_hour, start_period)
    
    new_hour, new_minutes, days_later = add_time_and_duration(start_hour, start_minutes, duration_hour, duration_minutes)
    
    new_hour, new_period = back_to_12_hour(new_hour)
    
    if starting_day:
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_index = weekdays.index(starting_day.capitalize())
        new_day_index = (start_day_index + days_later) % 7
        new_day = weekdays[new_day_index]
    else:
        new_day = None
    return print(formatted_output(new_hour, new_minutes, new_period, days_later, new_day))

add_time('3:30 PM', '2:12')