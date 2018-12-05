task = open('05.input').readlines()[0].strip()


def react(polymer):
    stack = []
    for s in polymer:
        if stack and stack[-1].swapcase() == s:
            stack.pop()
        else:
            stack.append(s)
    return ''.join(stack)


result = react(task)
print(len(result))

lens = {letter: len(react(''.join(s for s in task if s.lower() != letter)))
        for letter in map(chr, range(ord('a'), ord('z') + 1))}
min_letter = min(lens, key=lambda key: lens[key])
print(min_letter, lens[min_letter])
