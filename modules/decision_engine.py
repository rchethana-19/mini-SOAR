def check_blacklist(indicator):
    with open("blacklist.txt") as f:
        blocked = f.read().splitlines()

    return indicator in blocked