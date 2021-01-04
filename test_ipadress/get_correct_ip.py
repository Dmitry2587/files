from .check_ipadress import check_ip


def return_correct_ip_list(list_of_ip):
    return [ip for ip in list_of_ip if check_ip(ip)]


# def return_correct_ip_list_too(list_of_ip):
#    correct = []
#
#    for ip in list_of_ip:
#        if check_ip(ip):
#            correct.append(ip)
#
#    return correct


ip_list = ['8.8.8.8', '10', '1.1.1.1']
print(return_correct_ip_list(ip_list))
