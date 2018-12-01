from collections import Counter

def update_freq_and_check(df):
    global frequency, frequencies
    frequency += df
    frequencies[frequency] +=1
    if frequencies[frequency] == 2:
        print("First frequency to be reached twice: {}".format(frequency))
        return True
    return False


frequency = 0
frequencies = Counter()
df = []
with open("01.input") as f:
    for line in f.readlines():
        try:
            df.append(int(line.strip()))
            update_freq_and_check(df[-1])
        except:
            break

print("Final frequency is {}".format(frequency))

i = 0
while True:
    if update_freq_and_check(df[i]):
        break
    i = (i + 1) % len(df)
