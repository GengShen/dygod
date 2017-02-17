l = []
with open("dygod.csv", "r") as f:
    l = f.readlines()[1:]
    l = list(set(l))
    l = [i.strip().split(",") for i in l]
    l = [i for i in l if len(i) == 2]
    l = sorted(l[1:], key=lambda x: int(x[1]), reverse=True)
for i in l[:50]:
    print(",点击数".join(i))
