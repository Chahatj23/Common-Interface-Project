def ENDBLK(outroot, attribid, ordering, geometry, parameters):
    func_name = 'ENDBLK'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      blockType='h',
                      ordering=ordering, parent=1,
                      simulationFunctionName='csuper',
                      simulationFunctionType='DEFAULT',
                      style=func_name)

    addExprsNode(outnode, TYPE_DOUBLE, 0, parameters)

    return outnode


def get_from_ENDBLK(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_DOUBLE)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
