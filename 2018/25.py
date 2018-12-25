def dist(p1, p2):
    return sum(abs(p1[i] - p2[i]) for i in range(len(p1)))


points = []

with open("25.input") as f:
    for l in map(lambda s: s.strip(), f):
        if l:
            points.append(tuple(map(int, l.split(','))))

clusters = []
min_dist = 3

for point in points:
    appended = []
    for i, cluster in enumerate(clusters):
        if min(dist(point, pc) for pc in cluster) <= min_dist:
            cluster.add(point)
            appended.append(i)
    if len(appended) == 0:
        clusters.append({point})
    for ia in appended[:0:-1]:
        clusters[appended[0]] |= clusters[ia]
        clusters.pop(ia)

print(len(clusters))
