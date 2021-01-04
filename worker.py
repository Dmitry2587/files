import argparse


def ping_ip_adress(ip, count):
    pass


parser = argparse.ArgumentParser(description='ping test')

parser.add_argument('-a', action='store', dest='ip')
parser.add_argument('-c', action='store', dest='count', default=3, type=int)

args = parser.parse_args()

print(args.ip, args.count)
