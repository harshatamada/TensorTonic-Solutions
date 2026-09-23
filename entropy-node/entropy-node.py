import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    y=np.asarray(y,dtype=float)
    if len(y)==0:
        return 0.0
    names,counts=np.unique(y,return_counts=True)
    probabilities=counts/len(y)
    return -np.sum(probabilities*np.log2(probabilities))
    