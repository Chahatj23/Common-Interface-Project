def SCALAR2VECTOR(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SCALAR2VECTOR'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'c',
                      dependsOnU=1,
        simulationFunctionName='scalar2vector',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=1,
                       width=1)
    addDataData(node, parameters[0])
    return outnode
