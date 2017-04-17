node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.

# In this graph we are going to loop over all nodes until get a
# nodes that host a node inside called "IO_IMPORT"

def getOutput(node, i):
    if (len(node.outputs())>i):
        return node.outputs()[i]
    else:
        return None

# Get the parent node
parentNode = node.parent();
# Get the node to hook the current import 
node_name = parentNode.parm("generator_node").eval()
       
#Get the node to find insde the outputs
result = getOutput(parentNode,0)
while (result is not None):
    if (result.node(node_name) is not None):
        break
    else:
        result = getOutput(result,0)
                
# Set the relative path obtained
if (result is not None):
    parentNode.parm("generator_path").set(result.path())
else:
    parentNode.parm("generator_path").set("Select or Connect to Generator")