# Massad Raza
# Using stacks to convert a number into binary

from stack import Stack

def convert_int_to_bin(dec_num):

    if dec_num == 0:
        return 0

    a = Stack()

    while dec_num != 0:
        bin = dec_num % 2
        a.push(bin)
        dec_num = int(dec_num / 2)

    finalBin = ""

    while not a.is_empty():
        finalBin = finalBin + str(a.pop())

    return finalBin

print(convert_int_to_bin(37))
print(convert_int_to_bin(53))
print(convert_int_to_bin(36))
print(convert_int_to_bin(37))
