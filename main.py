
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