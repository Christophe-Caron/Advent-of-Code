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
            left.append(int(el))
        else:
            right.append(int(el))
    return left,right

def pairing(left,right):
    difflist=[]
    print(left)
    print(right)
    while left!=[] and right!=[]:
        small1=min(left)
        small2=min(right)
        left.remove(small1)
        right.remove(small2)
        diff=abs(small2-small1)
        difflist.append(diff)
    return difflist
lines = line_input()
left,right=splitter(lines)
difflist=pairing(left,right)
print(sum(difflist))