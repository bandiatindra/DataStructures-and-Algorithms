# python3

# Conditions to be printed - 
# 1. First unmatched closing bracket which dosent have an opening bracket before it eg - ] in  "]()"
# 2. Closes the wrong bracket like } in "()[}"
# 3. First unmatched opening bracket which does not have a corresponding closing bracket like ( in "{}([]"


from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    bracket_location = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            bracket_location.append(i+1)
            pass

        if next in ")]}":
            # Process closing bracket, write your code here

            # Check if there is no opening bracket. Return the index - 1st condition. 
            if len(opening_brackets_stack) == 0:                
                return i+1

            # Check if the opening bracket does not match with closing bracket, and return the index - 2nd condition
            top = opening_brackets_stack.pop()
            bracket_location.pop()
            if (top=='(' and next!=')') or (top=='[' and next!=']') or (top=='{' and next!='}'):
                return i+1  
            pass
    if len(opening_brackets_stack)==0:
        return "Success"
    else:
        return bracket_location.pop()


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
