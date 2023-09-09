#!/usr/bin/env python3

x = [795, 795 + 80, 795 + 80*2, 795 + 80*3, 795 + 80*4]
y = [335, 335 + 80, 335 + 80*2, 335 + 80*3, 335 + 80*4, 335 + 80*5]

CMD_POS = []
print(CMD_POS)

for i in range(6):
    CMD_POS.append([])
    for j in range(5):
        CMD_POS[i].append((x[j],y[i]))

print(CMD_POS)
