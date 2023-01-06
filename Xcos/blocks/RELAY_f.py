def RELAY_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'RELAY_f'
    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'c',
                      dependsOnU=1,
                      dependsOnT=1,
        simulationFunctionName='relay',
                      simulationFunctionType='TYPE_2',
                      style=func_name
                      )
    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=2,
                       width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    

    return outnode
