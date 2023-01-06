def VanneReglante(outroot, attribid, ordering, geometry, parameters):
    func_name = 'VanneReglante'

    outnode = addNode(outroot,
                      'BasicBlock',
                      **{'id': attribid},
                      parent=1,
        interfaceFunctionName=func_name,
                      ordering=ordering,
                      blockType = 'c',
                      dependsOnU=1,
        simulationFunctionName='VanneReglante',
                      simulationFunctionType='DEFAULT',
                      style=func_name
                      )

    node = addDataNode(outnode, 'ScilabString',
                       **{'as': 'exprs'},
                       height=2,
                       width=1)
    addDataData(node, parameters[0])
    addDataData(node, parameters[1])
    

    return outnode
