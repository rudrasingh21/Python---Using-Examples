import os

os.chdir('D:\Mom medical bill new1040-20190312T171540Z-001\Copy')
print(os.getcwd())

counter = 1

for f in os.listdir():
    #print(f)                   #print all file/folders of file
    #print(os.path.splitext(f))
    file_name, file_ext = os.path.splitext(f)
    #print(file_name)           #will print filename only
    #print(file_name.split('-')) #will split file name with space
    #print(file_ext)
    ext = file_ext
    #print(file_name.strip()[:3])
    filename = file_name.strip()[:3]
    new_name = '{}-{}{}'.format(filename, counter, ext)
    counter = counter + 1
    #print(new_name)
    os.rename(f, new_name)

