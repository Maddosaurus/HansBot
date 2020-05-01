def safely_calc_timeout(str_input):
    default_timeout = 5
    timeout = 0
    shenanigans = False
    try:
        timeout = int(str_input)
    except (ValueError):
        timeout = default_timeout
        shenanigans = True

    if (timeout < 1) or (timeout > 10):
        timeout = default_timeout
        shenanigans = True

    return (timeout, shenanigans)


def find_target_room(room_name, channels):
    silence = None
    for channel in channels:
        if channel.name.startswith(room_name):
            silence = channel
            return silence


def find_member(server, member_string):
    # Try the user_id first (right click on a user, select "Copy ID")
    member = None
    try:
        member_int = int(member_string)
    except ValueError:
        pass
    else:
        member = server.get_member(member_int)

    if member is None:
        # try the hooman friendly nickname
        member = server.get_member_named(member_string)
    return member
