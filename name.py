# Following function "reverse" takes two strins as input (first name and last name)
# and reverse the whole string including the space between first and last name.
def reverse(first_name: str, last_name: str):
    name = first_name.capitalize() + " " + last_name.capitalize()
    rev_name = name[::-1].lower()
    return f"\nName is: {name}.\nReverse of above name is: {rev_name}."
