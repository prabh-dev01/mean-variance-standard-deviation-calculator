import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(list).reshape(3, 3)

    mean_axis1 = arr.mean(axis=0).tolist()
    mean_axis2 = arr.mean(axis=1).tolist()
    mean_flat = arr.mean().item()

    var_axis1 = arr.var(axis=0).tolist()
    var_axis2 = arr.var(axis=1).tolist()
    var_flat = arr.var().item()

    std_axis1 = arr.std(axis=0).tolist()
    std_axis2 = arr.std(axis=1).tolist()
    std_flat = arr.std().item()

    max_axis1 = arr.max(axis=0).tolist()
    max_axis2 = arr.max(axis=1).tolist()
    max_flat = arr.max().item()

    min_axis1 = arr.min(axis=0).tolist()
    min_axis2 = arr.min(axis=1).tolist()
    min_flat = arr.min().item()

    sum_axis1 = arr.sum(axis=0).tolist()
    sum_axis2 = arr.sum(axis=1).tolist()
    sum_flat = arr.sum().item()

    return {
        'mean': [mean_axis1, mean_axis2, mean_flat],
        'variance': [var_axis1, var_axis2, var_flat],
        'standard deviation': [std_axis1, std_axis2, std_flat],
        'max': [max_axis1, max_axis2, max_flat],
        'min': [min_axis1, min_axis2, min_flat],
        'sum': [sum_axis1, sum_axis2, sum_flat]
    }