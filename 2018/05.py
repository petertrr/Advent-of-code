example = 'dabAcCaCBAcCcaDA'
task = open('05.input').readlines()[0].strip()

def react(polymer):
    i = 0
    cur = polymer
    iter = 0
    while i < len(cur):
        if i == len(cur) - 1:
            break

        if cur[i].lower() == cur[i+1].lower() and cur[i].islower() != cur[i+1].islower():
            cur = cur[:i] + cur[i+2:]
            i = max(0, i - 1)
        else:
            i += 1
        if iter > 100000:
            exit(-1)
    return cur

result = react(task)
print(len(result))

lens = {}
for letter in map(chr, range(ord('a'), ord('z') + 1)):
    print(letter)
    cur = ''.join(s for s in task if s.lower() != letter)
    lens.update({letter: len(react(cur))})
#    del cur

min_letter = min(lens, key=lambda key: lens[key])
print(min_letter, lens[min_letter])
