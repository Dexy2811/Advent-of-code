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
        # print(lengths)
        return lengths

    def total_lenght(self,lis):
        total=0
        for i in lis:
            total+=i

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

# Print the resulting lists for verification
# print("Column 1:", column1)
# print("Column 2:", column2)


test=List_managing(column1,column2)
liste_lengder =test.len_list()
total_lenght=test.total_lenght(liste_lengder)
print(total_lenght)
