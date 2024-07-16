t = int(input())

answers = []

for _ in range(t):
    n = int(input())
    coin_str = input()
    coins = [c for c in coin_str]

    length = len(coins)
    d_count = coins.count('D')

    if (length-d_count) % 2:
        answers.append('YES')
    else:
        answers.append('NO')

for ans in answers:
    print(ans)
