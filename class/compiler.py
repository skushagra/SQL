"""
This is a Python Script File
Automatically Generated from /home/kali/Templates
"""

import sys

keywords = ["Silicon", "create", "class", "Classes", "declare", "set", "recieve", "send", "use", "excuse"]

path = "./ini"
exit_code = 0
with open(path, "r") as script:
	s = script.read()
	code = list(s.split("\n"))
	code = list(filter(("").__ne__, code))
	for i in code:
		i = i.replace("\t", "")
	# print(code)
	
	'''
	if code[0] != "#! Silicon/SQL/Classes":
		print(f"""\nError found in {script.name} Line 0
		Syntax Error: SQL Script Initializer not found. The initiliazer should be the first lie of the program. (Exit code {exit_code})""")
	'''
	for i in range(len(code)):
		if "use" in code[i] or "excuse use" in code[i]:
			use_info = list(code[i].split(" "))
			if len(use_info) > 3:
				exit_code = 0
				print(f"""\nError found in {script.name} Line {i+1}
				Syntax Error: use statement takes exactly 2 arguments, declaration-type and class-name. (Exit code {exit_code})""")
			else:
				if use_info[1] == "class":
					class_name = use_info[2]
					if class_name in keywords:
						exit_code = 0
						print(f"""\nError found in {script.name} Line {i+1}
		Keyword Error: Keyword used as class name {class_name}. Set class name to a non reserved word. (Exit code {exit_code})
						""")
					else:
						for i in code:
							if "create" in i:
								class_data = list(i.split(" "))
								if len(class_data) > 3:
									exit_code = 0
									print(f"""Error found in {script.name} Line {i+1)}
		Syntax Error: create takes two positional arguments, given were {len(class_data) - 1}. (Exit code {exit_code})""")
								else:
									if class_data[2] != class_name:
										exit_code = 0
										print(f"""Error in {script.name} Line {i+1}
	Class {class_data[2]} not used or declared as {class_name}. (Exit code {exit_code})""")
			exit_code = 1
		else:
			if i == len(code)-1:
				exit_code = 0
				print(f"""\nError found in {script.name}
				Syntax Error:  SQL class never called or excused. (Exit code {exit_code})""")
	
	'''
	else:
		exit_code = 1
		print(f"\nExecution success | No Errors found. (Exit code {exit_code})")
	'''