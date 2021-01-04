import argparse


def make_pie_chart(elements):
    pass


parser = argparse.ArgumentParser(description='draw a chart')

parser.add_argument('-a', action='store', dest='elements')
# parser.add_argument('-c', action='store', dest='count', default=3, type=int)

args = parser.parse_args()

print(args.elements)
