def CANIMXY3D(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CANIMXY3D'

    outnode = addNode(outroot, 'BasicBlock', **{'id': attribid},
                      interfaceFunctionName=func_name,
                      ordering=ordering,
                      parent=1,
                      simulationFunctionName='canimxy3d',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='d')

    addExprsNode(outnode, TYPE_STRING, 11, parameters)

    return outnode


def get_from_CANIMXY3D(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
