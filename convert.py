
import sys

assert len(sys.argv)>1, "Please put the path to the obj file as the first command line argument"


points=[]
faces=[]
with open(sys.argv[1],"r") as file:
    for i in file.readlines():
        line_split=i.split()
        if line_split[0]=="v":
            points.append([line_split[1],line_split[2],line_split[3]])
        elif line_split[0]=="f":
            faces.append([line_split[1],line_split[2],line_split[3]])