import numpy as np

def adam_step(
    param: list,
    grad: list,
    m: list,
    v: list,
    t: int,
    lr: float = 1e-3,
    beta1: float = 0.9,
    beta2: float = 0.999,
    eps: float = 1e-8,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Returns (param_new, m_new, v_new) as NumPy arrays.
    """
    m=np.asarray(m,dtype=float)
    param=np.asarray(param,dtype=float)
    grad=np.asarray(grad,dtype=float)
    v=np.asarray(v,dtype=float)
    mt=beta1 * m + (1-beta1) * grad
    vt=beta2 * v +(1-beta2) * grad**2
    m_b=mt/(1-beta1**t)
    v_b=vt/(1-beta2**t)
    teta=param-lr*(m_b/((np.sqrt(v_b))+eps))
    return teta,mt,vt