from ipaddress import ip_address


def check_ip(ip):
    try:
        ip_address(ip)
        return True
    except ValueError as e:
        return False


if __name__ == "__main__":
    ip_1 = '8.8.8.8'
    ip_2 = '192.168.0.1'
    ip_3 = '192.168.0'

    print(check_ip(ip_1))
    print(check_ip(ip_2))
    print(check_ip(ip_3))
