# Overview
This exercise will test your understanding of python, coding practices in general, and how to effectively use python in Maya.

# Requirements
  - General Guidelines 
      - Use no external dependencies.
      	- Anything from the `standard library` is fair game.
      	- You will need to use the Maya python API.
      - You may organize your program's file structure however you feel most effectively meets your needs.
        - Feel free to create libraries, modules and/or packages as you see fit.
        - Do what makes sense.
  
  - Code
      - Use PEP8 formatting.
      - Make the code concise but readable.
      - Comment meaningfully, not excessively.

You will write a program that can read and write the data provided in the `data` directory.

The provided data lives in the `data` directory located next to this `README` file. There are multiple data sets, each
in their own subdirectory. The structure is defined in the `Data` section below

Before starting, read all documentation so you have a clear understanding of the expectations.

# Exercises
For each of the numbered sections, create a python file with that section's name.

	- All code for that section is to reside within that section's file.   

1) `core_functionality`
	- Write a class that can read and write the format defined by the files in the `data` directory.
	
		- Create any necessary accessor or convenience functions to streamline interaction with the class.
		- Include a test file that runs through the class's capabilities
		- Place the test file in a `test` directory.

2) `command_line_core`
	- Write a command line utility that uses the class you defined in step 1.
	
		- This utility takes arguments that allows the user to report various aspects of the files' content to stdout.
		- Select 3 or more meaningful statistics to report on.
			- example: node names
		- The reviewer of this test will be able to run the utility in a command prompt and observe its output. 

3) `batching_core`
	- Write a separate, small batching utility that can step through all of the `data` files.

		- Takes a directory as input and processes all contained files
		- Format all output to a single file, specified by the user.


4) `batching_1`
	- Extend the batching capability outlined in `batching_core` to allow selective modification of positions of nodes in the hierarchy.

		- Write a script that makes the hierarchy twice its current size without manipulating the scale components.
		- Write the changes to an output file specified on the command line.

5) `maya_core`
	- Using the functionality defined in `core_functionality`, write code that is capable of accurately reflecting the data defined in the accompanying files by building a hierarchy of transform nodes.

		- Use the Maya Python API

6) `maya_naming_core`
	- Add functionality that allows nodes in the Maya hierarchy to be renamed using the Python API.

7)	`maya_prefix`
	- Use the functionality defined in `maya_naming_core` to add a prefix to all of the nodes in the hierarchy.

8) `maya_output_core`
	- Write raw functionality that allows the user to specify a hierarchy to be writen to disk.
	- Write the necessary data required to reload output successfully in Maya. You need not include all data in original source format.

	- command can be run from maya script editor
	- user specified arguments:
		- hierarchy_root
		- output_filename