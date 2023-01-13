def RAMP(outroot, attribid, ordering, geometry, parameters):
    func_name = 'RAMP'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'ramp', 'C_OR_FORTRAN',
                         func_name, 'c',
                         dependsOnT=1)

    addExprsNode(outnode, TYPE_STRING, 3, parameters)

    return outnode


def get_from_RAMP(cell):
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
