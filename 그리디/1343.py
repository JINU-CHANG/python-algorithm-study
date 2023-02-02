#보드판 받아오기
board = input();
global p_board #폴리오미노 적용 보드판
p_board='';

#.까지 X 갯수세기
cnt = 0;

#변환하기
def change_board(cnt):
    global p_board;
    p_board = p_board + (cnt//4)*'AAAA' + (cnt%4//2)*'BB'

for i in list(board):
    if(i=='.'):
        if(cnt%2==0):
            #변환하기
            change_board(cnt);
            p_board=p_board+'.';
            cnt=0;
        else:
            break;
    else:
        cnt+=1;

#변환할 부분 남아있으면 변환하고, 남은 숫자가 홀수이면 -1
if(cnt%2==0):
    change_board(cnt);
    print(p_board)
else:
    print('-1');

