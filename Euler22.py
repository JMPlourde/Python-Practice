def stringlistfrom_file(filename):
    text_file = open(filename, "r")
    stringlist = text_file.readline()
    return stringlist

stringlist = sorted((str.lower(stringlistfrom_file('p022_names.txt')).replace('"','')).split(","))

letters={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

def sumofletters(name):
    namesum = 0
    for letter in name:
        namesum+=letters[letter]
    return namesum

def prodofnameandindex(names,name):
    prodofname=sumofletters(name)*(names.index(name)+1)
    print(name,sumofletters(name), names.index(name)+1,prodofname)
    return prodofname


        
def sumnamescore(listofnames):
    total = 0
    for name in listofnames:
        total+=prodofnameandindex(listofnames,name)
        print(total)
    print(total)

    
sumnamescore(stringlist)
