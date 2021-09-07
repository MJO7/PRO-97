f=open('/Users/rachanajoshi/Desktop/pythonProject/sample1.txt' , 'w+')
data_a = f.read()
f=open('/Users/rachanajoshi/Desktop/pythonProject/sample2.txt')
data_b = f.read()
def swapFileData():
    file1 = input("Enter the original file:")
    file2 = input("Enter the file to be swapped:")
    with open(file1 , 'r') as a:
        data_a = a.read()
    with open(file2 , 'r') as b:
        data_b = b.read()

    with open(file1 , 'w+') as a:
       a.write(data_b)
    with open(file2 , 'w+') as b:
        a.write(data_a)
      
swapFileData()

