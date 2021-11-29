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
#str1 = "ATTACA"
print(str1)
str2 = str_generator(str2_num, base_str2)
#str2 = "ATGCT"
print(str2)

gap_penalty = 30
match_score = 0
#mis_match_score = 0

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

    elif x == '-' or y == '-':
        return gap_penalty

    else:
        mis_penalty = mis_match_score(x,y)
        return mis_penalty


def cost_generator(str1, str2):
    #length of string 1
    l1 = len(str1)

    #length of string 2
    l2 = len(str2)

    #initializing the zero-matrix 
    score = initial_matrix((len(str1)+1), (len(str2)+1))
    vertical_penalty = 0
    horizontal_penalty = 0
    
    #base-case: for each row initialize to i-incremental
    for i in range(1, l1+1):
        vertical_penalty += gap_penalty
        score[i][0] += vertical_penalty

    #for each column initialize to j-incremental
    for j in range(1, l2+1):
        horizontal_penalty += gap_penalty
        score[0][j] += horizontal_penalty

    for line in score:
        print(line)
    
    #go-through each row and column and find which character can be picked to give us the min-penalty
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            #checking is the lengths are not equal
            mis_matchPenalty = align_score(str1[i-1], str2[j-1])
            
            score[i][j] = min(score[i-1][j-1]+mis_matchPenalty, score[i-1][j]+gap_penalty, score[i][j-1]+gap_penalty)
    
    for line in score:
        print(line)
    
    align_str1  = ""
    align_str2  = ""

    indexI = l2
    indexJ = l1

    print("the index values are...", indexI, '....', indexJ)

    print("the string first is ", str1[indexJ - 1], '....', str2[indexI - 1])

    #value = align_score(str1[indexJ - 1], str2[indexI - 1])
    #print("the returned value is ...", value)

    total_score = 0

    while indexI > 0 and indexJ > 0:
        curr_score = score[indexJ][indexI]
        left_score = score[indexJ-1][indexI]
        up_score = score[indexJ][indexI-1]
        diagonal_score = score[indexJ-1][indexI-1]

    
        value = align_score(str1[indexJ - 1], str2[indexI - 1])
    
        if curr_score == diagonal_score + value:
            align_str1 += str1[indexJ-1]
            align_str2 += str2[indexI-1]
            total_score += value
            indexI -= 1
            indexJ -= 1

        elif curr_score == up_score + gap_penalty:
            align_str1 += str1[indexJ-1]
            align_str2 += '-'
            total_score += up_score
            indexJ -= 1

        elif curr_score == left_score + gap_penalty:
            align_str2 += str2[indexI-1]
            align_str1 += '-'
            total_score += left_score
            indexI -= 1

    while indexJ > 0:
        align_str1 += str1[indexJ-1]
        align_str2 += '-'
        total_score += gap_penalty
        indexJ -= 1

    while indexI > 0:
        align_str2 += str2[indexI-1]
        align_str1 += '-'
        total_score += gap_penalty
        indexI -= 1

    align_str1 = align_str1[::-1]
    align_str2 = align_str2[::-1]

    res_str = align_str1 + align_str2

    print("the final string is .....", res_str[:51], '...', res_str[-50:])

    print("the first string alignment path is ", align_str1)

    print("the second string alignment path is", align_str2)

    print("The total score....", total_score)

    return score[i][j]

#Implementing the back_tracking algorithm and adding the score... 
print(cost_generator(str1, str2))


'''def OPT_cost(score, l1, l2):
    if l1 == 0 or l2 == 0:
        return

    left_gap = score[l1][l2-1] + gap_penalty
    mis_match = score[l1-1][l2-1] + align_score(str1[l1-1], str2[l2-1])
    bottom_gap = score[l1-1][l2] + gap_penalty

    OPT_score = min(left_gap, mis_match, bottom_gap)

    if OPT_score == left_gap:
        return OPT_cost(score[:l1+1][l2], l1, l2-1)
    
    elif OPT_score == mis_match:
        return OPT_cost(score[:l1][:l2], l1-1, l2-1)

    elif OPT_score == bottom_gap:
        return OPT_cost(score[:l1-2][:l2], l1-1, l2)
'''
'''
for i in range(r):
score_matrix.append([])
for j in range(c):
score_matrix[-1].append(0)
'''

    
    
    


