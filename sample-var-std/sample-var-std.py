import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x=np.asarray(x,dtype=float)
    center=x-np.mean(x)
    s_2=float(np.sum(center**2)/(x.size-1))
    sd=float(np.sqrt(s_2))
    return{
        "variance":s_2,
        "standard_deviation":sd
    }
    