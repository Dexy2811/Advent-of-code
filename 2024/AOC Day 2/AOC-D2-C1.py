class SafetyCheck:
    def __init__(self,l):
        self.l=l

    def indifferences(self):
        difference=[]

        for i in self.l:
            num=[i[j]-i[j+1] for j in range(len(i)-1)]
            difference.append(num)

        return difference
    
    def dec_inc(self,lis):
        count=0
        check_list1=[]
        for i in lis:
            count+=1
            all_pos=all(num >0 for num in i)
            all_neg=all(num<0 for num in i)
            if all_pos or all_neg:
                print(f"line {count} does only incline or decline")
                check_list1.append(True)
            else: 
                print(f"WARNING DANGER OH GOD OH NO line{count} is BAD")
                check_list1.append(False)
        return check_list1
    def safe_dist(self,lis):
        check_list2=[]
        for i in lis:
            for j in i:
                if abs(j)>3:
                    check_list2.append(False)
                    break
            else:

                check_list2.append(True)

        return check_list2 
    def double_check(self,a,b):
        save_unsave_list=[]
        counts=0
        countf=0
        final_count=[counts,countf]
        for i in range(len(a)):
            if a[i] and b[i]:
                print( "safe")
                counts+=1
            else: 
                print( "unsafe")
                countf+=1
        final_count=[counts,countf]
        return final_count



l=[]
l2=[]
with open("D2-input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    value=line.strip().split()
    l.append(value)

for i in l:
    num=tuple(int(j) for j in i)
    l2.append(num)


test=SafetyCheck(l2)
lists=test.indifferences()
print(lists)
print()
dec_inc_check=test.dec_inc(lists)
print(dec_inc_check)
print()
dist_chec=test.safe_dist(lists)
print()
CHECK=test.double_check(dec_inc_check,dist_chec)
print(CHECK)

