#Testing String generator for CSCI 570 Analysis of Algorithms Final Project

#Step 1: Read the input and gather the indicies to concatenate with the previous_string and cummulative string

print("Sequence Alignment Algorithm")

print("Generating 2 String from Base String 1 and 2... ")

str1_num = []
str2_num = []

base_str1 = ""
base_str2 = ""

count_str = 0

#open the file
with open('input.txt') as open_file:
    line = open_file.readline()
    while line:
        line = line.rstrip() 
        if line.isalpha() and count_str == 0:
            base_str1 += line
            count_str += 1

        elif line.isalpha() and count_str == 1:
            base_str2 += line
            count_str += 1

        if line.isdigit() and count_str == 1:
            
            str1_num.append(int(line))

        elif line.isdigit() and count_str == 2:
            
            str2_num.append(int(line))

        line = open_file.readline()

print(str1_num, base_str1)
print(str2_num, base_str2)

def str_generator(arr, base_str):
    prev_str = base_str
    for i in range(len(arr)):
        val = arr[i]
        slice_str = prev_str[:val+1]
        remain_len = len(prev_str) - len(slice_str)

        if remain_len == 0:
            remain_str = ""
        else:
            remain_str = prev_str[-remain_len:]

        result_str = slice_str + prev_str + remain_str
        prev_str = result_str

    return prev_str


str1 = str_generator(str1_num, base_str1)
print(str1)
str2 = str_generator(str2_num, base_str2)
print(str2)

        
    
    
    


