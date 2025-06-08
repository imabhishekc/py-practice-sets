result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

count = 0

for i in result:
    if i == 'heads':
        count += 1

print(f"Head appeared {count} times.")


result2 = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]    

count_tails = 0

for i in result2:
    if i == 'tails':
        count_tails += 1

print(f"Tails appeared {count_tails} times.")