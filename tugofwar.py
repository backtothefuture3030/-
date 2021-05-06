from itertools import combinations

def TugWar(n, *args):
    k = n//2
    s = sum(args)/2  #전체 몸무게 합의 절반
    combs = combinations(args, k)  #k명으로 구성할 수 있는 모든 경우의 수
    diff = list(map(lambda x : abs(s - sum(x)), combs))  #k명의 몸무게 합과 전체 몸무게의 절반과의 차이
    return [int(s - min(diff)), int(s + min(diff))]  #차이가 최소가 되는 부분을 출력

print(TugWar(6, 45, 55, 70, 60, 50, 75))