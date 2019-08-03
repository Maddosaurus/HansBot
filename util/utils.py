def safely_calc_timeout(str_input):
    default_timeout = 5
    timeout = 0
    try:
        timeout = int(str_input)
    except (ValueError):
        timeout = default_timeout
    
    if (timeout < 1) or (timeout > 10):
        timeout = default_timeout
    return timeout


def find_target_room(room_name, channels):
    silence = None
    for channel in channels:
        if channel.name.startswith(room_name):
            silence = channel
            break
        else:
            pass
    return silence