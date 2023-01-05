import os
print(os.getcwd())
write_to_file="H:\\Mamta_python\\wri.txt"
read_to_file="H:\\Mamta_python\\rea.txt"         
file=open(read_to_file,"r")
data=file.read()
# file.close()
print(data)
# with open(write_to_file,"a") as file:
#    file.write(data)
print(int(data)+3)
  




