def line_input():
    lines = []
    print("Enter your text (press Enter twice to finish):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return  lines

def splitter(lines):
    joined=[]
    left=[]
    right=[]
    for i in lines:
        temp=''
        for idx, x in enumerate(i):
            if x.isdigit():
                temp+=str(x)
                if idx==len(i)-1:
                    joined.append(temp)
                    continue
            if i[idx-1].isdigit() and idx!=0 and not x.isdigit():
                joined.append(temp)
                temp=''
    for idx, el in enumerate(joined):
        if idx%2==0:
            left.append(el)
        else:
            right.append(el)
    return left,right


left,right=splitter(line_input())
print(left)
print(right)
