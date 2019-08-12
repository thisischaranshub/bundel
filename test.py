import os


files = os.listdir('destination')

print(files)

print(type(files))

for i in range(len(files)):
    os.remove('destination/'+files[i])