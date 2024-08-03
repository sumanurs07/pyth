def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_str = ''.join(s.split()).lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Example usage
input_str = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input_str):
    print(f'"{input_str}" is a palindrome.')
else:
    print(f'"{input_str}" is not a palindrome.')