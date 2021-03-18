def add_time(start, duration, day=''):
    data = parse_input(start, duration, day)
    answer_data = calculate_time(data)
    return format_answer(answer_data)


def parse_input(start, duration, day=''):
    start = start.split(":")
    start_hours = start[0]
    start = start[1].split()
    start_minutes = start[0]
    am_pm = start[1]
    duration = duration.split(":")
    duration_hours = duration[0]
    duration_minutes = duration[1]
    day = day
    data = {
        "start_hours": int(start_hours),
        "start_minutes": int(start_minutes),
        "am_pm": am_pm.upper(),
        "duration_hours": int(duration_hours),
        "duration_minutes": int(duration_minutes),
        "day": day.lower()
    }
    return data


def calculate_time(data):
    days_later = 0
    minutes = data["start_minutes"] + data["duration_minutes"]
    if minutes >= 60:
        data["duration_hours"] += 1
        minutes -= 60
    if len(str(minutes)) < 2:
        minutes = f'{0}{minutes}'
    hours = data["start_hours"] + data["duration_hours"]
    while hours > 12:
        hours -= 12
        if data["am_pm"] == 'AM':
            data["am_pm"] = 'PM'
        else:
            data["am_pm"] = 'AM'
            days_later += 1
    if hours == 12:
        if data["am_pm"] == 'AM':
            data["am_pm"] = 'PM'
        else:
            data["am_pm"] = 'AM'
            days_later += 1
    am_pm = data['am_pm']
    answer_data = {
        "hours": hours,
        "minutes": minutes,
        "am_pm": am_pm.upper(),
        "days_later": days_later,
        "day": data["day"]
    }
    answer_data = determine_day(answer_data)
    return answer_data


def determine_day(answer_data):
    days_later = answer_data["days_later"]
    day = answer_data["day"]
    while days_later >= 7:
        days_later -= 7
    if day == "sunday":
        days_of_the_week = ['Sunday', 'Monday', 'Tuesday',
                            'Wednesday', 'Thursday', 'Friday', 'Saturday']
        new_day = days_of_the_week[days_later]
    elif day == "monday":
        days_of_the_week = ['Monday', 'Tuesday',
                            'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        new_day = days_of_the_week[days_later]
    elif day == "tuesday":
        days_of_the_week = ['Tuesday',
                            'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday']
        new_day = days_of_the_week[days_later]
    elif day == "wednesday":
        days_of_the_week = ['Wednesday', 'Thursday', 'Friday',
                            'Saturday',  'Sunday', 'Monday', 'Tuesday']
        new_day = days_of_the_week[days_later]
    elif day == "thursday":
        days_of_the_week = ['Thursday', 'Friday', 'Saturday',
                            'Sunday', 'Monday', 'Tuesday', 'Wednesday']
        new_day = days_of_the_week[days_later]
    elif day == "friday":
        days_of_the_week = ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday',
                            'Wednesday', 'Thursday']
        new_day = days_of_the_week[days_later]
    elif day == "saturday":
        days_of_the_week = ['Saturday', 'Sunday', 'Monday', 'Tuesday',
                            'Wednesday', 'Thursday', 'Friday']
        new_day = days_of_the_week[days_later]
    else:
        new_day = ''
    answer_data['day'] = new_day
    return answer_data


def format_answer(answer_data):
    hours = answer_data['hours']
    minutes = answer_data['minutes']
    am_pm = answer_data['am_pm']
    days_later = answer_data['days_later']
    day = answer_data['day']
    if day == '':
        if days_later > 1:
            return f'{hours}:{minutes} {am_pm} ({days_later} days later)'
        elif days_later == 1:
            return f'{hours}:{minutes} {am_pm} (next day)'
        else:
            return f'{hours}:{minutes} {am_pm}'
    else:
        if days_later > 1:
            return f'{hours}:{minutes} {am_pm}, {day} ({days_later} days later)'
        elif days_later == 1:
            return f'{hours}:{minutes} {am_pm}, {day} (next day)'
        else:
            return f'{hours}:{minutes} {am_pm}, {day}'


print(add_time('3:00 am', '546:47', 'MoNDay'))
print(add_time('3:00 am', '546:47'))
print(add_time('3:00 am', '24:47', 'friDay'))
print(add_time('3:00 am', '26:47'))
print(add_time('3:00 am', '13:47', 'MoNDay'))
print(add_time('11:55 am', '3:12'))
print(add_time("11:59 PM", "24:05"))
