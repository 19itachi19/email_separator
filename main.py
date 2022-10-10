email = input("Enter the email please: ")
char = '@'
index = email.index(char)
# here we get the symbol of @ and then we will define some functions

def get_name():
    i = 0
    name = ""
    while (i < index):
        name += email[i]
        i += 1
    return name
# we're done with the functions that returns only the name second will return the domain
def get_domain():
    i = index + 1
    domain = ""
    while (i < len(email)):
        domain += email[i]
        i += 1
    return domain
# done, let's see the result
print(get_name())
print(get_domain())
# expected output: 
# name
# domain
# be mindful that it does not include the char in the output
