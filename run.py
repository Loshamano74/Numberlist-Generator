import os

def generate_sequence(start, final, folder_name, file_name):
    # Create a folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_path = os.path.join(folder_name, file_name + '.txt')

    with open(file_path, 'w') as arq:
        for i in range(start, final+1):
            temp = str(i)
            arq.write(temp + '\n')

    print(f"Number sequence saved in '{file_path}'")

if __name__ == "__main__":
    folder_name = input('Enter the folder name: ')
    
    while True:
        start = int(input('Start number: '))
        final = int(input('End number: '))
        file_name = input('Insert a name for your number sequence file (or type "exit" to quit): ')
        
        if file_name.lower() == 'exit':
            break
        
        generate_sequence(start, final, folder_name, file_name)
