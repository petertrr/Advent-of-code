import re

task = open('advent7.txt', 'r')
count = 0
total = 0
while True:
    possible = True
    line = task.readline()
    if len(line) == 0:
        break
    total += 1
    pattern = r"\[\w*((\w)(\w)\3{1}\2)\w*\]"
    exceptions = re.findall(pattern, line)
    if len(exceptions) != 0:
        for e in exceptions:
            if e[0][0] != e[0][1]:
                possible = False
                break
    if possible:
        pattern = r'((?P<first>\w)(?P<letter>\w)(?P=letter){1}(?P=first))'
        candidates = re.findall(pattern, line)
    #    print(candidates)
        for l in candidates:
            if l[0][0] != l[0][1]:
                count += 1
                break
print("From %d IPs" % total + " %d support TLS" % count)

task = open('advent7.txt', 'r')
count = 0
total = 0
while True:
    line = task.readline()
    if len(line) == 0:
        break
    total += 1
    pattern = r"^\w*(?:\[\w*\]\w*)*(?P<l1>\w)(?P<l2>\w)(?P=l1).*\[\w*(?P=l2)(?P=l1)(?P=l2)"
    variants1 = re.findall(pattern, line)
    pattern = r"\[\w*(?P<l1>\w)(?P<l2>\w)(?P=l1)\w*\]\w*(?:\[\w*\]\w*)*(?P=l2)(?P=l1)(?P=l2)"
    variants2 = re.findall(pattern, line)
    if len(variants1) != 0 or len(variants2) != 0:
        count += 1
print("From %d IPs" % total + " %d support SSL" % count)
