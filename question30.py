## Password Masking (Basic): Prompt the user for a password and print a masked version (e.g., ****** for 6 characters).

import getpass

password = getpass.getpass("Enter a password: ")
print("*" * len(password))