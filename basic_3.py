#Testing String generator for CSCI 570 Analysis of Algorithms Final Project

#Step 1: Read the input and gather the indicies to concatenate with the previous_string and cummulative string

import time
import sys
from resource import *
import psutil


def main():
    print("Basic Sequence Alignment Algorithm")

    str1_num = []
    str2_num = []

    base_str1 = ""
    base_str2 = ""

    count_str = 0

    #open the file: filename to read the input parameters
    with open(sys.argv[1]) as open_file:
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
    str2 = str_generator(str2_num, base_str2)


    gap_penalty = 30
    match_score = 0

#function: returning mis-match penalty
    def mis_match_score(char1, char2, seq=['A', 'C', 'G', 'T'], alpha_matrix=[[0,110,48,94], [110, 0, 118, 48], [48, 118, 0, 110], [94, 48, 110, 0]]):
        i = seq.index(char1)
        j = seq.index(char2)
        return alpha_matrix[i][j]
    
    #function: initializing the matrix
    def initial_matrix(r, c):
        score_matrix = []
        for i in range(r):
            score_matrix.append([])
            for j in range(c):
                score_matrix[-1].append(0)
    
        return score_matrix
    
    #function: returning match score or mis-match score
    def align_score(x, y):
        #the character match
        if x == y:
            return 0

        #gap penalty
        elif x == '-' or y == '-':
            return gap_penalty

        else:
            mis_penalty = mis_match_score(x,y)
            return mis_penalty
        

    def cost_generator(str1, str2):
    #len of string 1
        l1 = len(str1)

    #len of string 2
        l2 = len(str2)

    #initializing the zero-matrix and checking the bounds for sequence
        
        if ((l1 >= 1 and l1 <= 2000) and (l2 >=1 and l2<= 2000 )):
            score = initial_matrix((len(str1)+1), (len(str2)+1))
            vertical_penalty = 0
            horizontal_penalty = 0

    #base-case: for each row initialize to i-incremental
        for i in range(1, l1+1):
            vertical_penalty += gap_penalty
            score[i][0] = vertical_penalty

    #for each column initialize to j-incremental
        for j in range(1, l2+1):
            horizontal_penalty += gap_penalty
            score[0][j] = horizontal_penalty
    
    #go-through each row and column and find which character can be picked to give us the min-penalty
        for i in range(1, l1+1):
            for j in range(1, l2+1):
            #checking is the lengths are not equal
                mis_matchPenalty = align_score(str1[i-1], str2[j-1])
            
                score[i][j] = min(score[i-1][j-1]+mis_matchPenalty, score[i-1][j]+gap_penalty, score[i][j-1]+gap_penalty)
    
        align_str1  = ""
        align_str2  = ""

        indexI = l2
        indexJ = l1

        while indexI > 0 and indexJ > 0:
            curr_score = score[indexJ][indexI]
            left_score = score[indexJ-1][indexI]
            up_score = score[indexJ][indexI-1]
            diagonal_score = score[indexJ-1][indexI-1]

    
            value = align_score(str1[indexJ - 1], str2[indexI - 1])

            if curr_score == diagonal_score + value:
                align_str1 += str1[indexJ-1]
                align_str2 += str2[indexI-1]
                indexI -= 1
                indexJ -= 1

            elif curr_score == up_score + gap_penalty:
                align_str1 += str1[indexJ-1]
                align_str2 += '-'
                indexJ -= 1

            elif curr_score == left_score + gap_penalty:
                align_str2 += str2[indexI-1]
                align_str1 += '-'
                indexI -= 1

        while indexJ > 0:
            align_str1 += str1[indexJ-1]
            align_str2 += '-'
            indexJ -= 1

        while indexI > 0:
            align_str2 += str2[indexI-1]
            align_str1 += '-'
            indexI -= 1

        final_str1 = align_str1 + "\n"
        final_str2 = align_str2 + "\n"

        #open output file 
        outputFile = open(sys.argv[2], "w")

        outputFile.write(final_str1)
        outputFile.write(final_str2)

        outputFile.close()

        return score[i][j]

    #Memory
    def memory_consumed():
        process = psutil.Process()
        memory_info = process.memory_info()
        memory_consumed = int(memory_info.rss/1024)
        return memory_consumed
    
    start_time = time.time()

    outputFile = open("output.txt", "w")
    min_cost = cost_generator(str1, str2)
    outputFile.write(str(min_cost))
    outputFile.write("\n")
    
    print("Min-Cost: ", cost_generator(str1, str2))

    
    end_time = time.time()

    #CPU-time
    cpu_time_taken = (end_time-start_time)*1000
    print("CPU Time: ", cpu_time_taken)

    

    outputFile.write(str(cpu_time_taken))
    outputFile.write("\n")

    memory_val = memory_consumed()

    outputFile.write(str(memory_val))
    outputFile.write("\n")

    print("Memory: ", memory_consumed())


if __name__ == "__main__":
    main()
