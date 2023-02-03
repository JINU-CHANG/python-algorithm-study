# 에너지 드링크 갯수
N = int(input());

# 에너지 드링크 공백으로 받기
drinks = list(map(int, input().split()))
drinks.sort(reverse=True)

# 에너지 드링크 합치기
total_drinks = drinks[0];

for i in range(1,N):
    total_drinks = total_drinks + (drinks[i]/2);

print(total_drinks);









