"""
Will copy contents of a file, removing all parts of a .tex file between 
"\begin{document}" and "\end{document}". 
Content on same line as key phrases is also copied over.

    use: python blanktex.py <oldfilename> <newfilename>

Brent Jacobs 2017-08-16
"""
import sys 

def main():
    try:
        oldfilename = sys.argv[1]
        newfilename = sys.argv[2]
    except IndexError:
        print "Error. Please provide file names."
        print "Use: python blanktex.py <oldfilename> <newfilename>"

    oldfile = file(oldfilename, 'r')
    newfile = file(newfilename, 'w')

    transfer = True 

    for line in oldfile.readlines():
        if transfer:
            newfile.write(line)
        if "begin{document}" in line:
            transfer = False
        if "end{document}" in line:
            newfile.write("\n")
            newfile.write(line)
            transfer = True

    oldfile.close()

    newfile.close()

if __name__ == "__main__":
    main()
            
