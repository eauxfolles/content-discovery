#!/usr/bin/env python3
# ==============================================================================
# Name: condisc.py (Content Discovery)
# Version: v3 (alpha)
# Author: eauxfolles
# Date: 19.04.2020
# Description: Script to support discovery of hidden content (folders and files)
# Usage: "condisc.py -option <url> [dictionary]"
# ==============================================================================

from os import system, name
import sys
import requests

condisc_parameter = ""			# sys.argv[1]
condisc_url = ""			# sys.argv[2]
condisc_dictionary = ""			# sys.argv[3]
dictionary_list = []			# list of files or folders to be discovered
brute_list = []				# list joining url and file or folder

# function to validate input provided with command line (has to be 2 or 3 parameters)
def validate_command_line():

	# validate correct use of calling an options or parameter and set variable
	if len(sys.argv) < 2:
		print_header(exit_code = "error: no parameters provided")
	elif len(sys.argv) > 4:
		print_header(exit_code = "error: too many parameters provided")
	elif sys.argv[1] == "-help" or sys.argv[1] == "--help":
		print_header(exit_code = "usage: condisc.py -option <url> [dictionary]")
	elif sys.argv[1] == "-files":
		condisc_parameter = "files"
	elif sys.argv[1] == "-folders":
		condisc_parameter = "folders"
	else:
		print_header(exit_code = "error: option unknown")

	# validate correct url is used and set variable
	if len(sys.argv) > 2:
		if sys.argv[2].startswith("http://") or sys.argv[2].startswith("https://"):
			if "." in sys.argv[2]:
				condisc_url = sys.argv[2]
			else:
				print_header(exit_code = "error: url not including tld")
		else:
			print_header(exit_code = "error: url not including protocol (http or https)")
	else:
		print_header(exit_code = "error: no url provided")

	# validate dictionary exists and set variable
	if len(sys.argv) == 4:
		condisc_dictionary = sys.argv[3]
	elif condisc_parameter == "files":
		condisc_dictionary = "default_files.dic"
	else:
		condisc_dictionary = "default_folders.dic"		
	
	try:
		dictionary_file = open(condisc_dictionary)
		dictionary_file.close()
	except FileNotFoundError:
	    print_header(exit_code = "error: dictionary not found")

	return condisc_parameter, condisc_url, condisc_dictionary

# function to load entries (possible files or folders) from external file into variable
def load_dictionary():

	with open(condisc_dictionary) as f: 
		dictionary_list = [line.rstrip() for line in f.readlines()]

	return dictionary_list	

# function generating list for later brute forcing (combination of url and files/folders)
def generate_list():

	for n in range(len(dictionary_list)):
		brute_list.append(sys.argv[2]+dictionary_list[n])

	return brute_list

# function using request-module to call url-file/folder-combination and discplay response
def conduct_discovery():
	
	print_header()

	for n in range(len(brute_list)):
		brute_response = requests.get(brute_list[n])
		print_response(brute_list[n], brute_response)

	print("\n")

# function to print header and error/help-messages
def print_header(exit_code = "no"):

	if name == "nt":
		system("cls")
	else: 
		system("clear")

	print("condisc.py - v3", "\n")

	if exit_code != "no":
		print(exit_code, "\n")
		sys.exit()

# function to print responses in formated manner
def print_response(brute_element, brute_response):

	print(brute_element, brute_response)

# main call of functions
condisc_parameter, condisc_url, condisc_dictionary = validate_command_line()
dictionary_list = load_dictionary()
brute_list = generate_list()
conduct_discovery()
