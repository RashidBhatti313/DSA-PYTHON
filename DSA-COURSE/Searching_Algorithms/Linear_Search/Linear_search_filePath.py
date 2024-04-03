
# def linear_search_text_file(file_path, target):
#     found = False
#     with open(file_path, 'r') as file:
#         line_number = 1
#         for line in file:
#             if target in line:
#                 print(f"Found '{target}' in line {line_number}: {line.strip()}")
#                 found = True
#             line_number += 1

#     if not found:
#         print(f"'{target}' not found in the file.")

# # Usage
# file_path = ""  # Replace with your file path

# target_word = 'I'  # Replace with the word or phrase you want to search for
# linear_search_text_file(file_path, target_word)



def Linear_search_text_file(file_path, target):
    found = False
    with open(file_path, 'r') as file:
        line_number = 1
        for line in file:
            if target in line:
                print(f"Found '{target}' in Line {line_number}: {line.strip()}")
                found = True
            line_number += 1
    
    if not found:
        print(f"'{target}' not found in the file.")

file_path = ""

target_word = 'I'
Linear_search_text_file(file_path, target_word)