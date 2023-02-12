#회의의 수
N = int(input());

#회의실 수 받기
room_list = [[0 for j in range(2)] for i in range(N)];

for i in range(N):
    room_list[i] = list(map(int, input().split()));

#회의실 정렬
room_list.sort(key=lambda x:x[0])

choose = room_list[0];
room_list2 = [];
room_list2.append(choose);

for i in range(1,N):
    if(choose[1] > room_list[i][0] and choose[1] > room_list[i][1]): # 포함되어 있다면
        room_list2.remove(choose);
        choose = room_list[i];
        room_list2.append(choose);
        continue;

    if(choose[0]==room_list[i][0]): #앞시간이 같다면
        if(choose[1]>room_list[i][1]):
            room_list2.remove(choose);
            choose = room_list[i];
            room_list2.append(choose);
        if(choose[1]==room_list[i][1]): # 완전히 같다면
            room_list2.append(choose);
        continue;

    if(choose[1] == room_list[i][0] or choose[1] < room_list[i][0]): #겹치지 않는다면
        choose = room_list[i];
        room_list2.append(choose);
        continue;

print(room_list2)
print(len(room_list2));