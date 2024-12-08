# Name: Greyson Barber
# email:  barbergn@mail.uc.edu
# Assignment Number: Final Project
# Due Date:   12/10/2024
# Course #/Section:   IS 4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Decode encrypted information for photograph

# Brief Description of what this module does. This is the main that insntiates classes
# Citations: Professor Nicholson, W3 Schools, ChatGPT
# Anything else that's relevant: none

# movie.py

# Part 3 and 4
import json
from cryptography.fernet import Fernet

class TeamMessageDecryptor:
    def __init__(self, key: str):
        self.fernet = Fernet(key)

    def decrypt_message(self, encrypted_message: str) -> str:
        decrypted_bytes = self.fernet.decrypt(encrypted_message.encode('utf-8'))
        return decrypted_bytes.decode('utf-8')

    def decrypt_team_messages(self, filepath: str, group_name: str) -> str:
        with open(filepath, "r") as file:
            data = json.load(file)
    
        if group_name in data:
            encrypted_message = data[group_name][0]  # Assuming the first message in the list
            return self.decrypt_message(encrypted_message)
        else:
            raise ValueError(f"Team '{group_name}' not found in the file.")
# End Part 3 and 4



