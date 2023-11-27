import numpy as np
import cupy as cp



def transfering(element, node):
    x = cp.float64(node[0])
    y = cp.float64(node[1])
    x1 = cp.float64(element.n1.x)
    y1 = cp.float64(element.n1.y)
    x2 = cp.float64(element.n2.x)
    y2 = cp.float64(element.n2.y)
    x3 = cp.float64(element.n3.x)
    y3 = cp.float64(element.n3.y)
    area = cp.linalg.det(cp.array([[1, x1, y1], [1, x2, y2], [1, x3, y3]], dtype=cp.float64))
    N1 = cp.float64(cp.linalg.det(cp.array([[1, x, y], [1, x2, y2], [1, x3, y3]], dtype=cp.float64)) / area)
    N2 = cp.float64(cp.linalg.det(cp.array([[1, x1, y1], [1, x, y], [1, x3, y3]], dtype=cp.float64)) / area)
    N3 = cp.float64(cp.linalg.det(cp.array([[1, x1, y1], [1, x2, y2], [1, x, y]], dtype=cp.float64)) / area)
    N = cp.array([[N1, 0, N2, 0, N3, 0], [0, N1, 0, N2, 0, N3]])
    D = cp.transpose(cp.array([element.n1.U1, element.n1.U2, element.n2.U1, element.n2.U2, element.n3.U1, element.n3.U2], dtype=cp.float64))
    Us = cp.matmul(N, D)
    Us_np = cp.asnumpy(Us)
    return Us_np

