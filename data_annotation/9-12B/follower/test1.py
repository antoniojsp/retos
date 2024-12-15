# Step 1: Get the number of students
no = int(input("Enter the number of students: "))

# Step 2: Open the file in write mode
file = open('output_data.txt', 'w')

# Step 3: Get student details and write to the file
for i in range(no):
    print(f"For student {i+1}")  # More readable f-string formatting
    name = input("Enter name: ")
    score = input("Enter the score: ")
    data_format = "Name:" + name + " Score: " + score  # No extra space needed after "Name:"
    file.write(data_format + "\n")

file.close()

# Step 4: Read and display the data from the file
read_file = open("output_data.txt", "r")
data = read_file.read()
print(data)
read_file.close()