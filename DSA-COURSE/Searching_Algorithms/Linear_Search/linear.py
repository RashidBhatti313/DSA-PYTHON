# def linear_search(user_list, user ):
#     for i in range(len(user_list)):
#         if user_list[i] == user:
#             return i
#     return -1

# user_list = ["ali", 'usman', "sufiyan", "kareem"]
# a = input("enter user name")
# x = linear_search(user_list,a)
# if x != -1:
#     print(f"this {a} found in the user_list")
# else:
#     print(f"{a} is not found in the user list")



def Linear_search(user_list, user):
    for i in range(len(user_list)):
        if user_list[i] == user:
            return i
    return -1

user_list = ["Ali", "Usman", "Rashid", "Samad", "Haris", "Sami"]
a = input("Enter The User Name: ")
x = Linear_search(user_list, a)
if x != -1:
    print(f"This {a} found in the user_list")
else:
    print(f"{a} si not found in the user_list")