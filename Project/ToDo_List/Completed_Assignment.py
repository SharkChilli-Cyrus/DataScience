#-*- coding: utf-8 -*-

__Author__ = 'zx'

"""
Todo:
1. Rename this file, Replace X with your seminar number,
and change YourStudentID to your ID, for example U1418412A.

2. You can start with using the below todo string for data processing.
Try to convert the todo string to list or other data types for display
and editing the content.
After you have learnt File input output in week 5, then add in the
relevant part for reading and writing of text file.
"""

import os

def open_file(file_path):
    with open(file_path) as f:
        rows = f.read().split('\n')

        value_dict = {}
        for index, value in enumerate(rows):
            if len(value) > 1:
                value_dict[index] = value.split(',')
    
    return value_dict


def show_menu():
    print('')
    print('Welcome To My TODO Wonderful App')
    print('='*30,
          '\n1. View Todo List', 
          '\n2. Add in Todo Item',
          '\n3. Completed an Item',
          '\n4. Exit')
    print('='*30)


def status(key_word):
    if key_word == 'Yes':
        key_word = ''
        return key_word
    else:
        key_word = 'not '
        return key_word


def show_list(value_dict):
    print('Todo List.')
    for key, row in value_dict.items():
        if key > 0:
            # Name 
            name_word = row[0]
            
            # Important status
            important_word = row[1]
            important_status = status(important_word)
                
            # Urgent status
            urgent_word = row[2]
            urgent_status = status(urgent_word)
            
            # Completed status
            completed_word = row[3]
            completed_status = status(completed_word)
            
            print(key, ': {0} is {1}important and is {2}urgent, it has {3}been completed.'.format(name_word, important_status, urgent_status, completed_status))
    
    print('-'*25, 'All Todo Items', '-'*25)



def save(file_path, value_dict):
    with open(file_path, 'w') as f:
        for value in value_dict.values():
            row = ','.join(value)+'\n'
            f.write(row)
    
    print('Saved')


def main():
    # todo.txt file path
    dirpath = os.path.dirname(os.path.abspath(__file__))
    filename = 'todo.txt'
    file_path = os.path.join(dirpath, filename)

    value_dict = open_file(file_path)

    continue_key = 1
    while continue_key == 1:
        show_menu()
        # convert the user input from string to integer
        user_input = int(input('Enter your option: '))

        # if user input 1
        if user_input == 1:
            show_list(value_dict)

        # if user input 2
        if user_input == 2:
            print('Add Item.')
            print('-'*15)

            # Name
            input_name = input('Enter the name of the new item: ').title()

            # Important status
            input_important = input('Is it important? [Yes/No] ').title()
            important_status = status(input_important)

            # Urgent status
            input_urgent = input('Is it urgent? [Yes/No] ').title()
            urgent_status = status(input_urgent)

            # Completed status
            input_completed = 'No'
            completed_status = status(input_completed)

            print('-'*10, 'Add Finished', '-'*10)
            print('The item has been added as follows:')
            print('{0} is {1}important and is {2}urgent, it has {3}been completed.'.format(input_name, important_status, urgent_status, completed_status))

            # Auto Save
            new_row = len(value_dict.keys())
            value_dict[new_row] = [input_name, input_important, input_urgent, input_completed]

            # save(file_path, value_dict) 

        # if user input 3
        if user_input == 3:
            # Show Todo List
            show_list(value_dict)

            mark_index = int(input('Enter item number you have completed: '))
            if mark_index >= len(value_dict.keys()):
                print('This item cannot be found.')
            else:
                # Name 
                name_word = value_dict[mark_index][0]

                # Important status
                important_word = value_dict[mark_index][1]
                important_status = status(important_word)

                # Urgent status
                urgent_word = value_dict[mark_index][2]
                urgent_status = status(urgent_word)

                # Completed status
                completed_word = value_dict[mark_index][3]
                if completed_word == 'Yes':
                    print('This item has been completed, please choose another one.')
                else:
                    print('The item has been marked completed:')
                    print('{0} is {1}important and is {2}urgent, it has been completed.'.format(name_word, important_status, urgent_status))

                # Auto Save
                value_dict[mark_index][3] = 'Yes'
                # save(file_path, value_dict)

        # If user input 4
        if user_input == 4:
            save(file_path, value_dict)
            print('Good bye!')
            continue_key = 0
        
        if user_input not in [1, 2, 3, 4]:
            print('Warning: Invalid input! Please enter 1-4')
        

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(err)
        raise