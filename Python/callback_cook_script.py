import toolutils

# hou.pwd().hdaModule().Cook(kwargs)
def Cook(scriptargs):
    sopnode = scriptargs['node']
    foreach = sopnode.node("foreach_end1")
    foreach.cook(True)