n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
s_sequence = sorted(sequence)
index_list = [i*0 for i in range(n)]

for i in range(len(sequence)):
    for j in range(len(s_sequence)):
        if s_sequence[j] == 0:
            continue
        if sequence[i] == s_sequence[j]:
            index_list[i] = s_sequence.index(s_sequence[j]) + 1
            s_sequence[j] = 0
            break

for i in index_list:
    print(i, end=" ")