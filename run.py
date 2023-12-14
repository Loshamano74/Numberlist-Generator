#!/usr/bin/env python3

import os

def generate_sequence(start, final, folder_name, file_name):
    # Create a folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_path = os.path.join(folder_name, file_name + '.txt')

    with open(file_path, 'w') as arq:
        for i in range(start, final + 1):
            temp = str(i)
            arq.write(temp + '\n')

    print(f"Number sequence saved in '{file_path}'")

def get_input(prompt):
    while True:
        user_input = input(prompt + " (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            return None
        return user_input

if __name__ == "__main__":
    print('''
     _______                .__  .__          __      ________                                   __                
     \      \  __ __  _____ |  | |__| _______/  |_   /  _____/  ____   ____   ________________ _/  |_  ___________ 
     /   |   \|  |  \/     \|  | |  |/  ___/\   __\ /   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
    /    |    \  |  /  Y Y  \  |_|  |\___ \  |  |   \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
    \____|__  /____/|__|_|  /____/__/____  > |__|    \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|   
            \/            \/             \/                 \/     \/     \/     \/           \/                   
    ''')

    folder_name = get_input('Enter the folder name')

    while folder_name is not None:
        start = get_input('Start number')
        if start is None:
            break
        start = int(start)

        final = get_input('End number')
        if final is None:
            break
        final = int(final)

        file_name = get_input('Insert a name for your number sequence file')
        if file_name is None:
            break

        generate_sequence(start, final, folder_name, file_name)
