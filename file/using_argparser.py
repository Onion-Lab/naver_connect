import argparse

parser = argparse.ArgumentParser(description='Sum two integers.')

parser.add_argument('-a', "--a_value",dest="a",help="A integer", type=int, default=0)
parser.add_argument('-b', "--b_value",dest="b",help="B integer", type=int, default=0)

args = parser.parse_args()

print(args)
print(args.a)
print(args.b)