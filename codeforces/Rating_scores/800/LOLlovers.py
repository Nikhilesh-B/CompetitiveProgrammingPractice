n = int(input())
bo = input()

br = bo.count('L')
on = bo.count('O')


o_ct = 0
b_ct = 0

for i in range(n-1):
    if bo[i] == 'O':
        o_ct += 1
    else:
        b_ct += 1

    if br-b_ct != b_ct and on-o_ct != o_ct:
        print(i+1)
        exit()

print(-1)