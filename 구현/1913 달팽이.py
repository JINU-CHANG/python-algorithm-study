N = int(input());
target = int(input());
snail_list = [[0 for j in range(N)] for i in range(N)];

value = N*N;
a = 0
b = N-1;
c = N-1;
d = 0;

while (value>0):
    #위에서 아래
    for i in range(N):
        if (snail_list[i][a] != 0):
            continue;
        if(target==value):
            target_ans = [i+1,a+1]
        snail_list[i][a]=value;
        value = value-1;
    a = a+1;

    #왼쪽에서 오른쪽
    for i in range(N):
        if(snail_list[b][i]!=0):
            continue;
        if (target == value):
            target_ans = [b+1, i+1];
        snail_list[b][i] = value;
        value = value-1;
    b = b-1;

    #아래에서 위
    for i in range(N):
        if (snail_list[(N-1)-i][c] != 0):
            continue;
        if (target == value):
            target_ans = [(N-1)-i+1,c+1];
        snail_list[(N-1)-i][c] = value;
        value = value-1;
    c = c-1;

    #오른쪽에서 왼쪽
    for i in range(N):
        if (snail_list[d][(N-1)-i] != 0):
            continue;
        if (target == value):
            target_ans = [d+1,(N-1)-i+1];
        snail_list[d][(N-1)-i] = value;
        value = value-1;
    d = d+1;

for i in snail_list:
    print(*i);

print(*target_ans);
