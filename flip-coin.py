# lets solve the famous problem ion large data on flip coin

import random

# Number of coin flips
flips = 10

# Store all results
results = []

for i in range(flips):
    coin = random.choice(["Head", "Tail"])
    results.append(coin)

# Count heads and tails
heads = results.count("Head")
tails = results.count("Tail")

# Calculate percentages
head_percent = (heads / flips) * 100
tail_percent = (tails / flips) * 100

print("Total flips:", flips)
print("Heads:", heads)
print("Tails:", tails)
print(f"Head percentage: {head_percent:.2f}%")
print(f"Tail percentage: {tail_percent:.2f}%")



import random

def flip_coin(n):
    heads = 0

    for i in range(n):
        coin = random.choice(["Head", "Tail"])

        if coin == "Head":
            heads += 1

    percentage = (heads / n) * 100

    return percentage


# Test with different numbers of flips
experiments = [10, 100, 1000, 10000, 100000, 1000000]

for n in experiments:
    result = flip_coin(n)
    print(f"{n:>8} flips → Heads: {result:.2f}%")
