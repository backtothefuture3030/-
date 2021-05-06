import sys

def solution(morning, night, tree):
    if morning >= tree:
        return 1
    delta = morning-night
    day = (tree-morning)//delta
    if (tree-morning) % delta == 0 :
        return day +1
    else:
        return day +2 

if __name__ == "__main__":
    a,b,v = map(int,sys.stdin.readline().split())
    print(solution(a, b, v))