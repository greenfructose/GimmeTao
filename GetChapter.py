import os, random

if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(
            os.getcwd(), os.path.dirname(__file__)
            )
    )
    f = open(os.path.join(__location__, 'taoteching.txt'), 'r')
    lines = f.readlines()
    chapterNumber = random.randint(1, 81)
    chapterFound = False
    for line in lines:
        if str(chapterNumber) in line: 
            chapterFound = True
        if str(chapterNumber + 1) in line:
            chapterFound = False
        if chapterFound == True:
            print(line.strip('\n'))
    f.close()
