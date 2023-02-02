#N,M,K 공백으로
N, K = map(int,input().split())

count = 0

while True:
    if((N%K)==0 or N==1):
        break;
    N=N-1;
    count=count+1;

while True:
    if(N==1):
        break;
    N = (int)(N/K)
    count=count+1;

print(count);
