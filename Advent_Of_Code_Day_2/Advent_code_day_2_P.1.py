def line_input():
    lines = []
    print("Enter your text (press Enter twice to finish):")
    while True:
        line = input()
        line_list=line.split()
        if line == "":
            break
        lines.append(line_list)
    return  lines
#non
#non
#non
#non
#non
#non
#non
#non
#non
#non
#non
def inc_or_dec(lines):
    status='None'
    count=0
    for line in lines:
        skip=False
        if status == 'Down' or status == 'Up':
            count += 1
        status='None'
        for idx, i in enumerate(line[0:len(line)]):
            skip=False
            i=int(i)
            if status == 'NO':
                break
            for j in line[idx+1:len(line)+1]:
                if not skip:
                    skip=False
                    j=int(j)
                    if i>j:
                        if status=='Down' or status=='None':
                            if abs(i-j)<=3 and abs(i-j)>=1:
                                status='Down'
                                skip=True
                                break
                            else:
                                status='NO'
                                break
                        else:
                            status='NO'
                            break
                    elif i<j:
                        if status=='Up' or status=='None':
                            if abs(i-j)<=3 and abs(i-j)>=1:
                                status='Up'
                                skip=True
                                break
                            else:
                                status='NO'
                                break
                        else:
                            status='NO'
                            break
                    elif i==j:
                        status='NO'
                        continue
                else:
                    break
        if status == 'Down' or status == 'Up':
            count += 1
        status='None'
    return(count)
count=inc_or_dec(line_input())
print(count)