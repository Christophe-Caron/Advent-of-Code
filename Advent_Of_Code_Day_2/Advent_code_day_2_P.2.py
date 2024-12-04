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

def inc_or_dec(lines):
    count=0
    run=False
    status='None'
    times=0
    for line in lines:
        fail=0
        status='None'
        while True:
            if run:
                run = False
                continue
            if fail>1:
                fail=0
                run=False
                status='None'
                break
            for idx, i in enumerate(line[0:len(line)]):
                if run:
                    break
                i=int(i)
                for j in line[idx+1:len(line)+1]:
                        j=int(j)
                        if i>j:
                            if status=='Down' or status=='None':
                                if abs(i-j)<=3 and abs(i-j)>=1:
                                    status='Down'
                                    break
                                else:
                                    del line[idx]
                                    run=True
                                    fail+=1
                                    break
                            else:
                                fail+=1
                                break
                        elif i<j:
                            if status=='Up' or status=='None':
                                if abs(i-j)<=3 and abs(i-j)>=1:
                                    status='Up'
                                    skip=True
                                    break
                                else:
                                    del line[idx]
                                    run = True
                                    fail+=1
                                    break
                            else:
                                del line[idx]
                                run = True
                                fail+=1
                                break
                        elif i==j:
                            del line[idx]
                            run = True
                            fail+=1
                            continue
            break
        if status == 'Down' or status == 'Up' and fail<=1:
            count += 1
        status='None'
        continue
    return(count)
count=inc_or_dec(line_input())
print(count)