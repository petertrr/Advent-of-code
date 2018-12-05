task = open('05.input').readlines()[0].strip()

def react(polymer):
    i = 0
    while i < len(polymer):
        if i < len(polymer) - 1 and polymer[i].swapcase() == polymer[i+1]:
            polymer = polymer[:i] + polymer[i+2:]
            i = max(0, i - 1)
        else:
            i += 1
    return polymer

result = react(task)
print(len(result))

lens = {}
for letter in map(chr, range(ord('a'), ord('z') + 1)):
    cur = ''.join(s for s in task if s.lower() != letter)
    lens.update({letter: len(react(cur))})

min_letter = min(lens, key=lambda key: lens[key])
print(min_letter, lens[min_letter])
