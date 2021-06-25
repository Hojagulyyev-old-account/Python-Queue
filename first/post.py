'''

Welcom to request post Machine-Py

'''

def machine(*args, **kwargs):
    # machine_list = []
    # for i in args:
    #     machine_list.append(i)
    #
    machine_dict = {}
    if kwargs['rq_file']:
        for i in kwargs['rq_file']:
            machine_dict[f"{i}"] = kwargs['rq_file'].get(f"{i}", "")
    else:
        print('MyNone')

    for i in kwargs['rq_post']:
        machine_dict[f"{i}"] = kwargs['rq_post'].get(f"{i}", "")

    return f"""This is my: {machine_dict}"""
            # Machine List: {machine_list}
            # Machine Dictionary: {machine_dict}
