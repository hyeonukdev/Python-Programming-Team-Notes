n = 1260
count = 0

# 큰 단위 확인
coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += n
    n %= coin

print(count)