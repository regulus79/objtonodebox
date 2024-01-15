import sys

assert len(sys.argv)>1, "Please put the path to the obj file as the first command line argument"

scalar=1
if len(sys.argv)>=3:
    try:
        scalar=float(sys.argv[2])
    except ValueError:
        print("WARNING, the scalar you entered is not a float.")

points=[]
faces=[]
with open(sys.argv[1],"r") as file:
    for i in file.readlines():
        line_split=i.split()
        if line_split[0]=="v":
            points.append([float(line_split[i])*scalar for i in range(1,len(line_split))])
        elif line_split[0]=="f":
            # Minus one, since according to wikipeadia, the .obj indexes start at 1, not 0
            faces.append([int(line_split[i].split("/")[0])-1 for i in range(1,len(line_split))])

# Initialize point groups to unique numbers
point_groups=[i for i in range(len(points))]

# Group the points into unique groups based on if there are faces which unite the points
# (i.e, if there is a path of faces connecting two points, those two points will be given the same group id)

for face in faces:
    first_vert_group=point_groups[face[0]]
    for vert in face:
        point_groups[vert]=first_vert_group

# Nice, now all of the points are organized into contiguous sections. Each section has a unique id, probably corresponding to its first vertex
# We just have to go through the groups and make bounding box for each one!

# Organize points into key=group id, value=array of points
points_organized_by_group={}
for vert_index,group in enumerate(point_groups):
    if not group in points_organized_by_group:
        points_organized_by_group[group]=[]
    points_organized_by_group[group].append(points[vert_index])

# Now make those bounding boxes and print them!
print("fixed = {")
for group in points_organized_by_group:
    verts=points_organized_by_group[group]
    min_point=verts[0].copy()
    max_point=verts[0].copy()
    for point in verts:
        if point[0]>max_point[0]:
            max_point[0]=point[0]
        if point[1]>max_point[1]:
            max_point[1]=point[1]
        if point[2]>max_point[2]:
            max_point[2]=point[2]


        if point[0]<min_point[0]:
            min_point[0]=point[0]
        if point[1]<min_point[1]:
            min_point[1]=point[1]
        if point[2]<min_point[2]:
            min_point[2]=point[2]
    
    print("\t{"+str(min_point[0])+","+str(min_point[1])+","+str(min_point[2])+","+str(max_point[0])+","+str(max_point[1])+","+str(max_point[2])+"},")

print("}")
# Done! That was fun!