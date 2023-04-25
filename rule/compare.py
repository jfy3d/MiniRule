def get_target_value(match, fields):
    _type = match["target_type"]
    if _type == 'field':
        return fields[match['target_value']]
    elif _type == 'array':
        return match['target_value'].split(',')
    elif _type == 'range':
        return [
            match['target_value'][0],
            match['target_value'][-1],
            match['target_value'][1:-1].split(',')[0],
            match['target_value'][1:-1].split(',')[1]
        ]
    else:
        return match['target_value']


def equal_compare(field_value, match, fields):
    return field_value == get_target_value(match, fields)


def notequal_compare(field_value, match, fields):
    return field_value != get_target_value(match, fields)


def contain_compare(field_value, match, fields):
    return field_value.find(get_target_value(match, fields)) > -1


def notcontain_compare(field_value, match, fields):
    return field_value.find(get_target_value(match, fields)) == -1


def gt_compare(field_value, match, fields):
    return field_value > get_target_value(match, fields)


def gte_compare(field_value, match, fields):
    return field_value > get_target_value(match, fields)


def lt_compare(field_value, match, fields):
    return field_value < get_target_value(match, fields)


def lte_compare(field_value, match, fields):
    return field_value <= get_target_value(match, fields)


def in_compare(field_value, match, fields):
    return field_value in get_target_value(match, fields)


def notin_compare(field_value, match, fields):
    return field_value not in get_target_value(match, fields)


def range_compare(field_value, match, fields):
    _target = get_target_value(match, fields)
    field_value = field_value * 1
    if '(' == _target[0]:
        if field_value <= eval('{}*1'.format(_target[2])):
            return False
    if '[' == _target[0]:

        if field_value < eval('{}*1'.format(_target[2])):
            return False

    if ')' == _target[1]:
        if field_value >= eval('{}*1'.format(_target[3])):
            return False
    if ']' == _target[1]:
        if field_value > eval('{}*1'.format(_target[3])):
            return False
    return True


compare_map = {
    'equal': equal_compare,
    'notequal': notequal_compare,
    'contain': contain_compare,
    'notcontain': notcontain_compare,
    'gt': gt_compare,
    'gte': gte_compare,
    'lt': lt_compare,
    'lte': lte_compare,
    'in': in_compare,
    'notin': notin_compare,
    'range': range_compare,
}
