import sys

"""This is a simple script that takes specially formatted text files and turns
them into interactive Python tutorials. Run with
    python generator.py <input filename> <output filename>
<output filename> is the name of the python file that will be generated, and
should thus (ideally) end in .py.
<input filename> can be anything. The file should be formatted like so:
    -   Regular text lines (i.e. lines that should appear as plaintext) can be
        written as plain text. No special treatment is required.
    -   Any line that begins with ">>> " (note the space) will be treated as an
        interactive code segment. The tutorial will prompt the user to enter
        the line and will not proceed until he or she does (whitespacing and
        Python in-line comments are ignored). Python exec and eval statements
        are used to execute the lines once they are entered correctly.
NOTE: All quotation marks (including in plaintext lines) must be double quotes,
as the tutorials use single quotes to delimit Python strings.

You can launch the tutorial with
    python <output filename>
The tutorial file will also take an optional command-line argument:
    python <output filename> bypass
will run through the tutorial without waiting for user input.
"""

def checkArguments(args):
    if len(args) != 3:
        print("Incorrect number of arguments: " + str(len(args) - 1) + ", 2 "
            + " expected.")
        return None
    return args[1], args[2]

def processCodeBlock(codeLines):
    lines = [line[4:] for line in codeLines]
    indentedLines = ['print("\\t' + line + '")\n' for line in lines]
    instructions = ''.join(indentedLines)
    interactive = 'print("")\n'
    for line in lines:
        interactive += 'userLine = getCodeLine("' + line + '")\n'
        interactive += 'try:\n\tprint(eval(userLine))\n'
        interactive += 'except SyntaxError:\n\texec(userLine)\n'
    conclusion = 'if not bypass:\n\tprint("Good!")\n'
    return instructions + interactive + conclusion + '\n'

# IO setup
args = checkArguments(sys.argv)
if args is None:
    exit(-1)
srcFilepath, dstFilepath = args
inFile, outFile = None, None
try:
    inFile = open(srcFilepath, 'r')
    outFile = open(dstFilepath, 'w')
except IOError as e:
    print(e)
    exit(-2)

# basicHeader.txt contains utility methods for all tutorials
headerLines = open('basicHeader.txt').readlines()
outFile.write("".join(headerLines))

# Prepare lines from input file
lines = inFile.readlines()
lines = [line[:-1] if line[-1] == '\n' else line for line in lines]
lines = [''] + lines + ['']  # Buffer lines at top and bottom

inCodeBlock = False  # True iff the last line was a code line
codeLines = []
for line in lines:
    if len(line) < 4 or line[:4] != '>>> ':
        if inCodeBlock:  # Was in code block, now out of block
            inCodeBlock = False
            outFile.write(processCodeBlock(codeLines))
        outFile.write('print("' + line + '")\n')
    else:
        if not inCodeBlock:
            inCodeBlock = True
            codeLines = []  # Reset code block
        codeLines.append(line)

outFile.close()
