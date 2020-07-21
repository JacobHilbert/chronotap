import sys
from time import time

times = []

input("Press Enter when you're ready")
start = time()
t = start
last = ""
while not last:
    last = input("> ")
    now = time()
    times.append(now-t)
    t = now
    print(f"lap {len(times):4}: {times[-1]:.3}\t\ttotal: {t-start:.3}\t\tmean: {sum(times)/len(times):.4}")

if len(sys.argv) > 1:
    with open(sys.argv[1],"w") as file:
        for i in times[-1]:
            file.write(str(i)+"\n")
else:
    print(*times[:-1],sep="\n")
