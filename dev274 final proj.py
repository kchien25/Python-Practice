# import elements file
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt

# open file with 20 elements
elements_file = open('elements1_20.txt', 'r+')

# read one line at a time to get element names
elements_line = elements_file.readline().strip() 
elements = ""

while elements_line:
    elements = elements_line + "," + elements
    elements_line = elements_file.readline().strip()

# remove whitespace and save each element name as lowercase into a list
elements = elements.lower()

element_list = elements.split(',')
del element_list[-1]
check_list = element_list

# create get_names() fxn with no arguments and returns list of 5 input strings
def get_names():
    element_inputs = []
    while len(element_inputs) < 5:
        guess = input("enter the name of an element: ")
        if guess.isalpha() == True:
            if guess.lower() in element_inputs:
                print("no duplicates allowed.")
                pass
            elif guess == "":
                pass
            else:
                element_inputs.append(guess.lower())
                pass
        else:
            print("no numbers or empty inputs allowed.")
            pass
    return element_inputs

# call get_names() to get return value
print("list any 5 of the first 20 elements in the periodic table")

element_inputs = get_names()

# iterate through return value and compare to list of 20 elements
correct = 0
correct_list = []
incorrect_list = []
    
for element in element_inputs:
    if element in element_list:
        correct += 1
        correct_list.append(element)
    else:
        incorrect_list.append(element)
        
# calculate % correct then print % correct as well as list of correct+incorrect responses
correct_list = " ".join(correct_list)
incorrect_list = " ".join(incorrect_list)

print(str(correct * 20) + "% correct")
print("correct responses:", correct_list)
print("incorrect responses:", incorrect_list)

elements_file.close()