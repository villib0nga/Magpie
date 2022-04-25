import sys

sim = input()
data = list(map(str.strip, sys.stdin))
max_len_strok = None
big = ''
for i in data:
    sim_kolvo = 0
    for j in i:
        if j == sim:
            sim_kolvo += 1
    if not max_len_strok:
        max_len_strok = sim_kolvo
        big = i
    elif sim_kolvo > max_len_strok:
        max_len_strok = sim_kolvo
        big = i
this = sorted(big.split(sim), key=len)
max_len = len(this[-1])
this_string = this[-1]
for j in this:
    if len(j) == max_len:
        if j < this_string:
            this_string = j
print(this_string)