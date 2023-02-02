# 거스름돈 액수
x = int(input());

#동전 갯수
num1 = (x//5);
num2 = 0;

# 2로 나눠지는지 체크하는 함수
def check_2(x):
    if(x%2==0):
        return True;
    else:
        return False;

while True :
    if(num1<0):
        print("-1")
        break;

    if(check_2(x-(num1*5))==True):
        num2 = (x - (num1 * 5))//2
        print(num1+num2);
        break;
    else:
        num1=num1-1;