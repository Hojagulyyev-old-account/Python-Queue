'''

Welcom to request post Machine-Py

'''

def machine(*args, **kwargs):
    machine_dict = {}

    if kwargs['rq_file']:
        for i in kwargs['rq_file']:
            machine_dict[f"{i}"] = kwargs['rq_file'].get(f"{i}", "")
    else:
        print('MyNone')

    for i in kwargs['rq_post']:
        machine_dict[f"{i}"] = kwargs['rq_post'].get(f"{i}", "")

    return machine_dict
