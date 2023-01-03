def CSCOPXY(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CSCOPXY'
    
    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
        interfaceFunctionName=func_name,
        ordering=ordering,
        parent=1,
        blockType='d',
        simulationFunctionName='cscopxy',
        simulationFunctionType='C_OR_FORTRAN',
        style=func_name)

    node = addDataNode(outnode, 'ScilabString', **{'as': 'exprs'}, height=11, width=1)
   
    for i in range(11):
        addDataData(node, parameters[i])
    
    return outnode
