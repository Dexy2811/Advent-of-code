
class List_managing:
    def __init__(self,l1,l2):
        self.l1=sorted(map(int,l1))
        self.l2=sorted(map(int,l2))


    def len_list(self):
        lengths=[]
        x=zip(self.l1,self.l2)
        for i in x:
            l1=abs(i[0]-i[1])
            lengths.append(l1)
        return lengths

    def total_lenght(self,lis):
        total=0
        for i in lis:
            total+=i

        return total
    
    def sim(self):
        comparisons1=[]
        comparisons2=[]
        
        unique1=set(self.l1)
        for i in unique1:
            count1=self.l1.count(i)
            comparisons1.append((i,count1))


        unique2=set(self.l2)
        for x in unique2:
            count2=self.l2.count(x)
            comparisons2.append((x,count2))

        comparisons1.sort()
        comparisons2.sort()
        
        return comparisons1, comparisons2

    def comp_sim(self,a,b):
        numbers=[]


        
        for k in a:
            for l in b:
                if k[0]==l[0]:
                    num=k[0]*l[1]
                    numbers.append(num)


        total=sum(numbers)
        return total



# Initialize two empty lists
column1 = []
column2 = []

# Read the file and process the lines
with open("D1-input.txt", "r") as file:
    lines = file.readlines()

# Loop through each line in the file
for line in lines:
    # Strip whitespace and split the line by spaces
    values = line.strip().split()
    if len(values) == 2:  # Ensure the line has exactly two columns
        try:
            # Append the values to their respective lists
            column1.append(int(values[0]))
            column2.append(int(values[1]))
        except ValueError:
            print(f"Skipping line due to non-numeric values: {line.strip()}")
    else:
        print(f"Skipping line due to invalid format: {line.strip()}")



test=List_managing(column1,column2)
liste_lengder =test.len_list()
total_lenght=test.total_lenght(liste_lengder)
comp=test.sim()
a,b=test.sim()
x=test.comp_sim(a,b)
print(x)
