import sys
import statistics

files = sorted(sys.argv[1:])
medians = []

for filename in files:
    with open(filename) as f:
        numbers = [int(x) for x in f.read().split()]
        medians.append(statistics.median(numbers))

with open('face.txt', 'w') as f:
    for filename in files:
        with open(filename) as f:
            numbers = [int(x) for x in f.read().split()]
            f.write(' '.join(str(x) for x in numbers if x < min(medians)) + '\n')
