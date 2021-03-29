import os
import shutil

file_1_name = input("Swap :- ")
file_2_name = input("with :- ")

with open(file_1_name, "r") as a:
    data_a = a.read()

with open(file_2_name, "r") as b:
    data_b = b.read()


def swappingdata(): 
    print("Swapping Data From "+file_1_name+" to "+file_2_name)

    with open(file_1_name, "w") as a:
        a.write(data_b)
    
    with open(file_2_name, "w") as b:
        b.write(data_a)

swappingdata()