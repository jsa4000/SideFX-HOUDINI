node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.

#In this graph we are going to loop over all the nodes until get a
# nodes that host a node inside called "IO_IMPORT"

def getOutput(node, i):
    if (len(node.outputs())>i):
        return node.outputs()[i]
    else:
        return None
        
node_name = "IO_IMPORT"
parentNode = node.parent();

result = parentNode.outputs()[0];
while (result is not None):
    if (result.node(node_name) is not None):
        break
    else:
        result = getOutput(result,0)
                
# Set the relative path obtained

   
if (result is not None):
    node.parent().parm("generator_path").set(result.path())