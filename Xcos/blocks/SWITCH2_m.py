def SWITCH2_m(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SWITCH2_m'

    outnode = addOutNode(outroot, BLOCK_BASIC,
                         attribid, ordering, 1,
                         func_name, 'switch2_m', 'C_OR_FORTRAN',
                         func_name, 'c',
                         dependsOnU=1)

    addExprsNode(outnode, TYPE_STRING, 4, parameters)

    return outnode


def get_from_SWITCH2_m(cell):
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
