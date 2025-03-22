# Create an empty list called my_list
my_list = []

# Append elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)

# Extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from my_list
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Print my_list to verify the elements have been added and sorted
print("my_list:", my_list)

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("The index of the value 30 in my_list is:", index_of_30)

# Find and print the index of the value 50 in my_list
index_of_50 = my_list.index(50)
print("The index of the value 50 in my_list is:", index_of_50)

# Create a tuple with the names of five favorite books
favorite_books = (
    "The River Between",
    "Chinua Achebe",
    "The River and the Source",
    "The Cat and the Dog",
    "My Life in Crime"
)

# Use a for loop to print each book name on a separate line
for book in favorite_books:
    print(book)
    
# Create an empty dictionary to store the person's information
person_info = {}

# Ask the user for input and store the information in the dictionary
person_info['name'] = input("Enter your name: ")
person_info['age'] = input("Enter your age: ")
person_info['favorite_color'] = input("Enter your favorite color: ")

# Print the dictionary to the console
print("\nPerson Information:")
for key, value in person_info.items():
    print(f"{key.capitalize()}: {value}")
    
def create_set(prompt):
    """
    Accepts user input to create a set of integers.
    """
    integer_set = set()
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'done':
            break
        try:
            integer_set.add(int(user_input))
        except ValueError:
            print("Invalid input. Please enter an integer or 'done'.")
    return integer_set

# Create two sets of integers
print("Enter integers for the first set (type 'done' to finish):")
set1 = create_set("Enter an integer: ")

print("Enter integers for the second set (type 'done' to finish):")
set2 = create_set("Enter an integer: ")

# Create a new set that contains only the elements that are common to both sets
common_elements = set1.intersection(set2)

# Print the common elements
print("\nCommon elements in both sets:")
print(common_elements)

# Store a list of words
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Use list comprehension to create a new list with words that have an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the new list
print("Words with an odd number of characters:")
print(odd_length_words)