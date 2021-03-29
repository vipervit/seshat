def arr_transform_dates(arr):
    def get_mean_for_range(val):
        import numpy        
        return int(numpy.mean([int(n) for n in val.split('-')]))
    for i in range(len(arr)):
        if 'BCE' in arr[i]:
            arr[i]=-get_mean_for_range(arr[i].replace('BCE', ''))
    for i in range(len(arr)):
        if isinstance(arr[i], str):
            arr[i]=get_mean_for_range(arr[i].replace('CE', ''))
    return arr