def add_time(start, duration, day = None):
    hh, mm, nn = start.replace(':', ' ').split()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    time_start = 0
    if hh == '12' and nn == 'AM': time_start = int(mm)
    elif nn == 'AM': time_start = int(hh) * 60 + int(mm)
    elif hh == '12' and nn == 'PM': time_start = 720 + int(mm)
    else: time_start = 720 + int(hh) * 60 + int(mm)

    hh, mm = duration.split(':')
    time_add = int(hh) * 60 + int(mm)

    whole_min = time_start + time_add
    new_day = whole_min // 1440
    new_min = whole_min % 1440

    new_hour = new_min // 60
    hour_string = str(new_hour if new_hour <= 12 and new_hour > 0 else 12 if new_hour == 0 else new_hour - 12)
    minute_string = ':{0:02d}'.format(new_min % 60)
    nn_string = ' AM' if new_min // 60 < 12 else ' PM'

    day_string = ''
    if day is not None:
        day_string = ', ' + days[(days.index(day.lower()) + new_day) % 7].capitalize()
    
    if new_day == 1: day_string += ' (next day)'
    if new_day > 1: day_string += ' (' + str(new_day) + ' days later)'

    return hour_string + minute_string + nn_string + day_string