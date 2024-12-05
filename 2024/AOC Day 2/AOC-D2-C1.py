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
                if j>3:
                    print("AAAAAAAAAAAAAAAAAAAAH")
                    check_list2.append(False)
                    break
            else:
                print("everything is fine :)")
                check_list2.append(True)

        return check_list2
    ############# this checks for all values in the list and does not stop once an danger is found            
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


#l=[(9,5,3),(7,5,6),(1,2,3)]
l=[]
l2=[]
with open("D2-input.txt", "r") as file:
    lines = file.readlines()
#    l.append(lines)

for line in lines:
    value=line.strip().split()
    l.append(value)

for i in l:
    num=tuple(int(j) for j in i)
    l2.append(num)

#print(l2[:5])
###########################

test_tuples = [
    (1, 2, 3),          # Safe (all positive differences ≤ 3, inclining)
    (5, 4, 3, 2, 1),    # Safe (all negative differences ≤ 3, declining)
    (10, 6, 2),         # Unsafe (difference > 3: 10 - 6 = 4)
    (3, 5, 7, 8),       # Safe (all positive differences ≤ 3, inclining)
    (20, 15, 10, 5, 0), # Safe (all negative differences ≤ 3, declining)
    (1, 5, 2),          # Unsafe (mixed differences: 5 - 1 = 4, 2 - 5 = -3)
    (8, 7, 6),          # Safe (all negative differences ≤ 3, declining)
    (4, 8, 4),          # Unsafe (mixed differences: 8 - 4 = 4, 4 - 8 = -4)
    (2, 2, 2, 2),       # Safe (all differences are 0)
    (1, 4, 8),          # Unsafe (difference > 3: 8 - 4 = 4)
    (15, 12, 9, 6),     # Safe (all negative differences ≤ 3, declining)
    (1, 1, 1, 1),       # Safe (all differences are 0)
    (9, 13, 14, 17),    # Unsafe (difference > 3: 13 - 9 = 4)
    (7, 7, 7, 7),       # Safe (all differences are 0)
    (30, 27, 23, 20),   # Safe (all negative differences ≤ 3, declining)
    (5, 2, 1, -1, -4),  # Safe (all negative differences ≤ 3, declining)
    (100, 97, 92),      # Unsafe (difference > 3: 97 - 100 = -3, 92 - 97 = -5)
    (0, 3, 6, 10),      # Unsafe (difference > 3: 10 - 6 = 4)
    (40, 37, 36, 32),   # Unsafe (difference > 3: 36 - 32 = 4)
    (1, 2, 3, 6),       # Unsafe (difference > 3: 6 - 3 = 3)
    (10, 10, 10, 10),   # Safe (all differences are 0)
    (25, 20, 15, 10, 5),# Safe (all negative differences ≤ 3, declining)
    (1, 4, 7, 8),       # Unsafe (difference > 3: 4 - 1 = 3, 7 - 4 = 3)
    (3, 6, 9),          # Unsafe (difference > 3: 6 - 3 = 3, 9 - 6 = 3)
    (20, 19, 18, 15),   # Unsafe (difference > 3: 15 - 18 = 3)
    (0, 1, 3, 6),       # Unsafe (difference > 3: 6 - 3 = 3)
    (10, 7, 4),         # Safe (all negative differences ≤ 3, declining)
    (100, 95, 90, 85),  # Unsafe (difference > 3: 95 - 100 = 5)
    (50, 48, 47),       # Safe (all negative differences ≤ 3, declining)
    (5, 8, 11, 14),     # Unsafe (difference > 3: 8 - 5 = 3, 11 - 8 = 3)
]

################################

test=SafetyCheck(test_tuples)
lists=test.indifferences()
print(lists)
print()
dec_inc_check=test.dec_inc(lists)
print(dec_inc_check)
print()
dist_chec=test.safe_dist(lists)
#print(dist_chec)
print()
CHECK=test.double_check(dec_inc_check,dist_chec)
print(CHECK)

