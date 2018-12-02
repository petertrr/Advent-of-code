from itertools import count

with open("06.txt") as f:
    config = list(map(int, f.readline().strip().split('\t')))


def update_config(config):
    m, i = max(((v, i) for i, v in enumerate(config)), key=lambda p: (p[0], -p[1]))
    config[i] = 0
    for _ in range(m, 0, -1):
        i = (i + 1) % len(config)
        config[i] += 1
    return config


# config = [0, 2, 7, 0]  # for test, should give 5 and 4
configs = [config.copy()]

for i in count(1):
    config = update_config(config)
    if config in configs:
        print("On step {} configuration {} was repeated, {} iterations from "
              "previous time".format(i, config, i - configs.index(config)))
        break
    else:
        configs.append(config.copy())
