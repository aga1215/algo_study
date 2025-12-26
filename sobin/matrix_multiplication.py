import numpy as np

def solution(arr1, arr2):
    A = np.array(arr1)
    B = np.array(arr2)
   
    return (A @ B).tolist()
