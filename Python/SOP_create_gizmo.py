node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.

attrib = geo.addAttrib(hou.attribType.Point,"Cd",(0,0,0))

# Vector X (Side)
sidevector = hou.Vector3((1.0,0.0,0.0))
sidevector.normalized()
attribSide = geo.addAttrib(hou.attribType.Point,"Side",sidevector)
# Vector Y (Up)
upvector = hou.Vector3((0.0,1.0,0.0))
upvector.normalized()
attribUp = geo.addAttrib(hou.attribType.Point,"Up",upvector)
# Vector Z (Aim)
aimvector = hou.Vector3((0.0,0.0,1.0))
aimvector.normalized()
attribAim = geo.addAttrib(hou.attribType.Point,"Aim",aimvector)

for i in range(0,3):
    initial_pos = (0,0,0)
    final_pos = [0,0,0]
    final_pos[i] = 3
    color = [0,0,0]
    color[i] = 1
       
    # Create the polygon
    poly = geo.createPolygon()
    positions = [initial_pos, final_pos ]

    # Create the points and the vertices
    for position in positions:
        point = geo.createPoint()
        point.setAttribValue(attrib, color)
        point.setPosition(position)
        poly.addVertex(point)
        
    # SEt the poly opened to display as an edge
    poly.setIsClosed(False)
	
	