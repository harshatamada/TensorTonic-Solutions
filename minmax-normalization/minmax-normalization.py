import numpy as np

def minmax_scale(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns a floating-point NumPy array matching the shape of X.
    """
    X = np.asarray(X,dtype=float)
    minimum=np.min(X,axis=axis,keepdims=True)
    maximum=np.max(X,axis=axis,keepdims=True)
    data_range=maximum-minimum
    safe_range=np.where(data_range > eps,data_range,1.0)
    return (X-minimum)/safe_range