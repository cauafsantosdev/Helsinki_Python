# Write your solution here

def is_it_valid(pic: str):
    from datetime import datetime

    if len(pic) != 11:
        return False

    if "+" in pic:
        day = int(pic[:2])
        month = int(pic[2:4])
        year = int("18" + pic[4:6])
    elif "-" in pic:
        day = int(pic[:2])
        month = int(pic[2:4])
        year = int("19" + pic[4:6])
    elif "A" in pic[6]:
        day = int(pic[:2])
        month = int(pic[2:4])
        year = int("20" + pic[4:6])
    else:
        return False

    try:
        date = datetime(year, month, day)
    except:
        return False

    special = int(pic[:6] + pic[7:10]) % 31
    chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    if pic[10] != chars[special]:
        return False
    else:
        return True


if __name__ == "__main__":
    print(is_it_valid("120488+246L"))