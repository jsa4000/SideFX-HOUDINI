# Python Snippets

https://houdinitricks.com/adding-parameters-to-the-interface-via-python/

node = hou.node(“/obj”).createNode(“geo”)
parm_group = node.parmTemplateGroup()
parm_folder = hou.FolderParmTemplate(“folder”, “Extras”)
parm_folder.addParmTemplate(hou.FloatParmTemplate(“noise”, “Noise”, 1))
parm_folder.addParmTemplate(hou.FloatParmTemplate(“amp”, “Amp”, 2))
parm_folder.addParmTemplate(hou.FloatParmTemplate(“cat_treats”, “Cat Treats”, 3))
parm_group.append(parm_folder)
node.setParmTemplateGroup(parm_group)

>>> node = hou.node("/obj").createNode("geo")
>>> group = node.parmTemplateGroup()
>>> folder = hou.FolderParmTemplate("folder","My Parms")
>>> folder.addParmTemplate(hou.FloatParmTemplate("myparm", "My Parm", 1))
>>> group.append(folder)
>>> node.setParmTemplateGroup(group)
 
 
 
 
//Adding parameters to an existing one

https://www.sidefx.com/forum/topic/20361/?page=1#post-95571
 
 n = hou.node('/out/renderNode3')
parm_group = n.parmTemplateGroup()
hou_parm_template2 = …
hou_parm_template3 = …
parm_group.appendTolFolder((“Passes”, ), hou_parm_template2)
parm_group.appendTolFolder((“Passes”, ), hou_parm_template3)
n.setParmTemplateGroup(parm_group)


Alternatively you can find the folder and append directly to it.

n = hou.node('/out/renderNode3')
parm_group = n.parmTemplateGroup()
target_folder = parm_group.findFolder((“Passes”,))
hou_parm_template2 = …
hou_parm_template3 = …
target_folder.addParmTemplate(hou_parm_template2)
target_folder.addParmTemplate(hou_parm_template3)
n.setParmTemplateGroup(parm_group)


// Some more operations
http://sidefx.jp/doc/hom/hou/ParmTemplateGroup.html

// To add  a buttom with a callback

1. This will be placed in the Button Python Script Callback on paramter interface. 

	hou.pwd().hdaModule().paintIt(kwargs)
	
	-> hou.pwd().hdaModule().createCurve(kwargs)

2. In Node, in editable nodes. Place "Paint" in the "Editable Node". This is the node you are goinf to modify.
		
3. In the section scripts. Create a new Script base on a Python module  and add the following function.

	import toolutils

	def paintIt(scriptargs):
		sopnode = scriptargs['node']
		viewer = toolutils.sceneViewer()
		
		paint = sopnode.node("paint")

		paint.setCurrent(True, True)
		viewer.enterCurrentNodeState()
		
		
		

