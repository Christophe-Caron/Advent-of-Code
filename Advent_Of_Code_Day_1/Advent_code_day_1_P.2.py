
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

def check_mult(left,right):
    res_list=[]
    for el in left:
        mult=0
        result=0
        for idx,j in enumerate(right):
            if j==el:
                mult+=1
        result=el*mult
        res_list.append(result)
    return res_list

lines = line_input()
left,right=splitter(lines)
res_list=check_mult(left,right)
print(sum(res_list))