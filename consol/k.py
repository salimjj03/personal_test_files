#!/usr/bin/python3
def add(*kwargs):
    print(sum(kwargs))

if __name__ == "__main__":
    li = [2, 3, 5, 5, 2]
    add(*li)
