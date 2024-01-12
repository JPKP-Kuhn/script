def is_valid_IP(strng = False):
    if strng == '' or strng == None:
        return False
    elif strng == False:
        return False
    elif strng.count('.') == 3:
        for i in strng.split('.'):
            if i.isdigit() and 0 <= int(i) <= 255 and (len(i) == 1 or len(i) > 1 and i[0] != '0'):
                continue
            else:
                return False
        return True
    return None

print(is_valid_IP())