import os

base = 'D:/'
i = 1
for j in range(10):
    file_name = base +str(i)+'/'
    os.mkdir(file_name)
    i += 1