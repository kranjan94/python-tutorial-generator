Python Tutorial Generator
=========================

This is a simple script that takes specially formatted text files and turns them into interactive Python tutorials. Run with:

    python generator.py <input filename> <output filename>

<output filename> is the name of the python file that will be generated, and should thus (ideally) end in .py.
<input filename> can be anything. The file should be formatted like so:
* Regular text lines (i.e. lines that should appear as plaintext) can be written as plain text. No special treatment is required.
* Any line that begins with ">>> " (note the space) will be treated as an interactive code segment. The tutorial will prompt the user to enter the line and will not proceed until he or she does (whitespacing and Python in-line comments are ignored). Python exec and eval statements are used to execute the lines once they are entered correctly.
NOTE: All quotation marks (including in plaintext lines) must be double quotes,as the tutorials use single quotes to delimit Python strings.

You can launch the created tutorial with:

    python <output filename>

The tutorial file will also take an optional command-line argument:

    python <output filename> bypass

will run through the tutorial without waiting for user input.

The example file, exampleTutorial.txt, is a very short introduction to the Python language meant to demonstrate the usage of this script. You can use it with:

    python generator.py exampleTutorial.txt pythonIntro.py
    python pythonIntro.py
