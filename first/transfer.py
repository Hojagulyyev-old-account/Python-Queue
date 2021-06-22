'''
    Welcome to already transfered functions [ def! ]
    # Here my library function to use...

    print ({
        # True:'a',
        # 1:'b',
        # 1.0:'c',
    })

'''

# first function's name - TimeTable
class TimeX():

    stepfuncs = {
            10:['00','10','20','30','40','50','60'],
            15:['00','15','30','45'],
            20:['00','20','40'],
            30:['00','30'],
        }

def create_time(*args, **kwargs):
    if kwargs['start'] >= kwargs['end']:
        kwargs['start'] = 8
        kwargs['end'] = 14
    else:
        if not kwargs['start'] in range(1, 24):
            kwargs['start'] = 8
        if not kwargs['end'] in range(1, 24):
            kwargs['end'] = 14
        kwargs['start']=round(kwargs['start'])
        kwargs['end']=round(kwargs['end'])

    timelist = []
    for hour in range(kwargs['start'], kwargs['end']):
        for min in TimeX.stepfuncs.get(round(kwargs['step']), TimeX.stepfuncs[20]):
            l = f'{hour}:{min}'
            timelist.append(l)
    timelist.append(f"{kwargs['end']}:00")

    return timelist
