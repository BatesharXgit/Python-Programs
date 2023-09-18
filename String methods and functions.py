str = "Hello there how are you"

# String methods
print(str.capitalize())  # Output: "Hello there how are you"
print(str.upper())       # Output: "HELLO THERE HOW ARE YOU"
print(str.lower())       # Output: "hello there how are you"
print(str.title())       # Output: "Hello There How Are You"
print(str.strip())       # Output: "Hello there how are you"
print(str.startswith("Hello"))  # Output: True
print(str.endswith("you"))      # Output: True
print(str.replace("Hello", "Hi"))  # Output: "Hi there how are you"
print(str.split())       # Output: ['Hello', 'there', 'how', 'are', 'you']
print('-'.join(str.split()))    # Output: "Hello-there-how-are-you"
print(str.find("there"))        # Output: 6
print(str.count("e"))           # Output: 4
print(str.isalpha())            # Output: False
print(str.islower())            # Output: False

# String functions
print(len(str))      # Output: 23
print(max(str))      # Output: 'y'
print(min(str))      # Output: ' '
print(ord('H'))      # Output: 72
print(chr(72))       # Output: 'H'
