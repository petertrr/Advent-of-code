import re

RESP_VAL1 = 61
RESP_VAL2 = 17
task = open('advent10', 'r')
eof = False
bots = {}
bins = {}
while True:
    if not eof:
        line = task.readline()
    if len(line) == 0:
        eof = True

    if line[:3] == 'val':
        nums = re.findall(r'\d+', line)
        nums = [int(i) for i in nums]
        if nums[1] not in bots:
            bots.update({nums[1]: [[], []]})
        bots[nums[1]][0].append(nums[0])
#    print(bots)
    if line[:3] == 'bot':
        aims = re.findall(r'((?:bot|output) \d+)', line)
#        print(aims)
        num = int(aims[0][aims[0].index('t')+2:])
        if num not in bots:
            bots.update({num: [[], []]})
        bots[num][1].append('l' + aims[1][0] + aims[1][aims[1].index(' ')+1:])
        bots[num][1].append('h' + aims[2][0] + aims[2][aims[2].index(' ')+1:])

    temp = {i for i in bots}
    for i in temp:
        if len(bots[i][0]) == 2 and len(bots[i][1]) != 0:
            if bots[i][0][0] == RESP_VAL1 and bots[i][0][1] == RESP_VAL2:
                print('bot ' + str(i) + ' is responsible')
            if bots[i][0][1] == RESP_VAL1 and bots[i][0][0] == RESP_VAL2:
                print('bot ' + str(i) + ' is responsible')
#            print('ready')
            for j in range(0,2):
                if bots[i][1][j][0] == 'h':
                    val = max(bots[i][0])
                elif bots[i][1][j][0] == 'l':
                    val = min(bots[i][0])
                aim = int(bots[i][1][j][2:])
#                print(val, aim)
                if bots[i][1][j][1] == 'b':
                    if aim not in bots:
                        bots.update({aim: [[], []]})
                    bots[aim][0].append(val)
                    bots[i][0].remove(val)
                elif bots[i][1][j][1] == 'o':
                    if aim not in bins:
                        bins.update({aim: []})
                    bins[aim].append(val)
                    bots[i][0].remove(val)
#    print(bots)
    if eof:
        end = True
        for i in bots:
            if len(bots[i][0]) != 0:
             end = False 
        if end:
            break
#print(bots)
print(bins)
answer = bins[0][0] * bins[1][0] * bins[2][0]
print(answer)