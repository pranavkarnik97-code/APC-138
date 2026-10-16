f = open("source.py", "r")
lines = f.readlines()
f.close()

f = open("without_comments.py", "w")

for line in lines:
    if not line.lstrip().startswith("#"):
        f.write(line)

f.close()

print("Comments removed successfully")