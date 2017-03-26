import toolutils

# hou.pwd().hdaModule().createCurve(kwargs)
def createCurve(kwargs):
    # select the current SOP node from the args
    parentNode = kwargs['node'].parent()
    node = kwargs['node']
    # Select the current viewer to toogle the controsl
    viewer = toolutils.sceneViewer()
  
    # LINK: http://sidefx.jp/doc/hom/assetscripts.html
    # hou.ui.displayMessage("You created " + kwargs['script_multiparm_index'])
    
    # Check for midify curve if exist
    curve_node_name = 'curve_create' + kwargs['script_multiparm_index']
    curve_node = parentNode.node(curve_node_name)
    if (curve_node is None):
        # Create a curve node if not exist
        curve_node = parentNode.createNode('curve',curve_node_name)
        # Create a curve node if not exist
        group_node = parentNode.createNode('group',"group_" + curve_node_name)
        group_node.setNextInput(curve_node )
        
        # Add this group into the custom group tag
        node.setParms({"group"+ kwargs['script_multiparm_index']:"group_" + curve_node_name,
        "name"+ kwargs['script_multiparm_index']:"curve_created_" + kwargs['script_multiparm_index']})
        
        # Select the merge curves nodes to connect the node created
        merge_curves = parentNode.node("merge_curves")
        if (merge_curves is None):
            # If merge node doesn't exist create a new one
            merge_curves = parentNode.createNode("merge","merge_curves")
            # Get the input connected to the first input and set to this one
            if (len(node.inputs()) ):
                merge_curves.setNextInput(node.inputs()[0])
            # Connect the merge node into the current Sop
            node.setInput(0, merge_curves) 
        
        # Append this new curve into the merge node    
        merge_curves.setNextInput(group_node)
        
    
    # Enter into curve to edit
    curve_node.setCurrent(True, True)
    viewer.enterCurrentNodeState()
