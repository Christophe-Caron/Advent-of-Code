def line_input():
    lines = []
    print("Enter your text (press Enter twice to finish):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    multiline_input = "\n".join(lines)
    return multiline_input

def splitter(multiline_input):
    left=[]
    right=[]
    for idx, i in enumerate(multiline_input):
        if idx%2==0: #checks if it is even, if even, goes in left list
            left.append(i)
        else:
            right.append(i)
    print(left)
    print(right)
    return left,right

line_input()
splitter(line_input())
