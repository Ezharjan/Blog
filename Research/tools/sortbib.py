import re

# Function to extract the year from a BibTeX entry
def extract_year(entry):
    match = re.search(r'year\s*=\s*"?(\d+)"?', entry, re.IGNORECASE)
    if match:
        return int(match.group(1))
    else:
        return 0

# Function to order references by latest year
def order_references_by_year(input_file):
    # Read the input BibTeX file
    with open(input_file, 'r') as file:
        content = file.read()

    # Find all BibTeX entries
    entries = re.split(r'(@\w+{)', content)[1:]

    # Pair entry type with its content
    paired_entries = [(entries[i], entries[i + 1]) for i in range(0, len(entries), 2)]

    # Sort the entries by year in descending order
    sorted_entries = sorted(paired_entries, key=lambda x: extract_year(x[1]), reverse=True)

    # Construct the output BibTeX file
    output = ''
    for entry_type, entry_content in sorted_entries:
        output += entry_type + entry_content

    with open('output.bib', 'w') as file:
        file.write(output)

    print("The ordered reference file 'output.bib' is generated!")

# Function to get the reference count
def get_reference_count(input_file):
    with open(input_file, 'r') as file:
        content = file.read()

    # Find all BibTeX entries
    entries = re.split(r'@\w+{', content)
    reference_count = len(entries) - 1  # Subtract 1 to exclude the initial split part

    print(f"The total number of references is {reference_count}.")

# Main function
def main():
    print("1. Order references by latest year;\n2. Get reference count.\nSelect the function you want to use:\n")
    user_input = input("Enter 1 or 2: ")

    if user_input == '1':
        print("Please input your reference file name:")
        input_file = input()
        order_references_by_year(input_file)
    elif user_input == '2':
        print("Please input your reference file name:")
        input_file = input()
        get_reference_count(input_file)
    else:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
