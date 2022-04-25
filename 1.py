import sys

sim = input()
data = list(map(str.strip, sys.stdin))
# data = [
# 'RPZZ']
max_string = ''
max_counter = 0
for i in data:
    counter = 0
    for j in i:
        if j == sim:
            counter += 1
    if counter > max_counter:
        max_string = i
        max_counter = counter
podstroks = []
this_string = ''
max_string_counter = 0
for i in max_string:
    if i != sim:
        this_string += i
    else:
        if not max_string_counter:
            podstroks.append(this_string)
            max_string_counter = len(this_string)
            this_string = ''
        elif len(this_string) == max_string_counter:
            podstroks.append(this_string)
            this_string = ''
        elif len(this_string) > max_string_counter:
            max_string_counter = len(this_string)
            podstroks = []
            podstroks.append(this_string)
            this_string = ''
if not max_string_counter:
    podstroks.append(this_string)
    max_string_counter = len(this_string)
    this_string = ''
elif len(this_string) == max_string_counter:
    podstroks.append(this_string)
    this_string = ''
elif len(this_string) > max_string_counter:
    max_string_counter = len(this_string)
    podstroks = []
    podstroks.append(this_string)
    this_string = ''
podstroks.sort()
this_podstrok = None
for i in podstroks:
    if not this_podstrok:
        this_podstrok = i
    elif i < this_podstrok:
        this_podstrok = i
print(this_podstrok)