malicious = []
with open('malicious_extensions.txt', 'r') as m:
    for line in m:
        malicious.append(str(line))
my_ext = []
with open('my_extensions.txt', 'r') as f:
    for line in f:
        my_line = line.strip().split(':')[0]
        my_ext.append(str(my_line))

for line in malicious:
    for ext in my_ext:
        if ext == line:
            print(line)
