
if __name__ == '__main__':
    #print("Welcome to Sequence Alignment!")
    """
    Step 1: Reading input strings
    """
    output_list = []
    with open('input.txt') as f:
        stringForProcessing = f.readline().strip()
        for line in f:
            try:
                idx = int(line)
                stringForProcessing = stringForProcessing[:idx+1] + stringForProcessing + stringForProcessing[idx+1:]
                """
                Step 2: String generation based on input
                """
            except ValueError:
                output_list.append(stringForProcessing)
                stringForProcessing = line.strip()

        output_list.append(stringForProcessing)

    print(output_list)
    """
    Step 3: Matching steps
    """

    def get_from_matrix(i, j, seq=['A', 'C', 'G', 'T'], matrix=[[0, 110, 48, 94], [110, 0, 118, 48], [48, 118, 0, 110], [94, 48, 110, 0]]):
        indexI = seq.index(i)
        indexJ = seq.index(j)
        return matrix[indexI][indexJ]


    string1= output_list[0]
    string2= output_list[1]


    """
    Step 4: Cost generation
    """
    def get_cost(match_list, delta=30):

        seqA = match_list[0]
        seqB = match_list[1]

        cost = 0
        for i in range(len(seqA)):

            if seqA[i] == seqB[i]:
                cost += 0
            elif seqA[i] == '1':
                cost += delta
            elif seqB[i] == '1':
                cost += delta
            else:

                cost += get_from_matrix(seqA[i], seqB[i], ['A', 'C', 'G', 'T'],
                                        [[0, 110, 48, 94], [110, 0, 118, 48], [48, 118, 0, 110], [94, 48, 110, 0]])

        return cost

        #get_cost(output_list, delta, alpha): 'ACC1GGTCG1','1CCAGGTGGC'=208
    print(get_cost(['ACC1GGTCG1','1CCAGGTGGC']),30)