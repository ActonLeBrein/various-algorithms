def ip_val(ip):
    pi = ip.split('.')
    if len(pi) == 4:
        for i in pi:
            try:
                if int(i) and int(i) > 0 and int(i) < 256:
                    pass
                else:
                    return False
            except ValueError:
                return False
        return True
    else:
        return False

print ip_val('12.32.265.1')

print ip_val('12.-9.54.1')

print ip_val('12.a.54.1')

print ip_val('12.32.25')

print ip_val('12.32.1.255.54')

print ip_val('12.32.0.255')

print ip_val('12.32.1.255')