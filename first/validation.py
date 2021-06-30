'''

Welcom to validation Py

Here:
    - Validation List - VL ( vl )
    - Validation Context - VC ( vc )

'''
def genericV(request, *args, **kwargs):
    vl = []
    for rs in args:
        print(rs['bool'])
        if rs['bool'] == False:
            vl.append(rs)

    print('Len vc ', len(vl))
    if len(vl) > 0:
        vc = {}
        for dict in vl:
            vc[f"{dict['name']}"] = dict['content']
            vc[f"{dict['name']}value"] = dict['value']

        return vc

    print("NONE WoRKS")
    return None

def lenghtV(request, *args, **kwargs):
    result = {
                'value':kwargs['e'],
                'bool':True,
                'content':None,
                'name':None,
             }

    if len(kwargs['e']) < kwargs['l']:
        result['bool'] = False
        result['content'] = kwargs['content']
        result['name'] = kwargs['name']

    return result
