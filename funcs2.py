from random import randint as r

mod1: float = 1
mod2: float = 3


def exp(u: float, d: float, x: float) -> float:
    if x != 0:
        return (abs(x) / x) * (abs(x) ** (u / d))
    else:
        return 0


def dexp(u: float, d: float, x: float) -> float:
    if x != 0:
        return 1 / x ** (d - u)
    else:
        return 0


def dropping(v: list[float], prt: float) -> list[float]:
    result: list[float] = list(v)
    for i in range(len(result)):
        s = r(0, 10 ** 6) / (10 ** 6)
        if s < prt:
            result[i] = 0
    return result


def dropping_m(m: list[list[float]], prt: float) -> list[list[float]]:
    result: list[list[float]] = list(m)
    for i in range(len(m)):
        for o in range(len(m[i])):
            s = r(0, 10 ** 6) / (10 ** 6)
            if s < prt:
                result[i][o] = 0
    return result


def conv(matrix: list[list[float]], kernel: list[list[float]]) -> list[list[float]]:
    rd: int = len(matrix) - len(kernel) + 1
    result: list[list[float]] = [[0 for __ in range(rd)] for _ in range(rd)]
    for i in range(len(kernel)):
        for o in range(len(kernel)):
            for p in range(i, len(matrix) + 1 - len(kernel) + i):
                for k in range(o, len(matrix) + 1 - len(kernel) + o):
                    if matrix[p][k] != 0:
                        result[p - i][k - o] += kernel[i][o] * matrix[p][k]
    return result


def act_m(matrix: list[list[float]]) -> list[list[float]]:
    result = list(matrix)
    for i in range(len(matrix)):
        for o in range(len(matrix)):
            result[i][o] = exp(mod1, mod2, result[i][o])
    return result


def act_v(v: list[float]) -> list[float]:
    result: list[float] = list(v)
    for i in range(len(v)):
        result[i] = exp(mod1, mod2, result[i])
    return result


def vm_mpx(vector: list[float], matrix: list[list[float]]) -> list[float]:
    result: list[float] = [0 for _ in range(len(matrix))]
    for i in range(len(vector)):
        if vector[i] != 0:
            for o in range(len(matrix)):
                result[o] += matrix[o][i] * vector[i]
    return result


def vv_sum(v1: list[float], v2: list[float]) -> list[float]:
    result: list[float] = [0 for _ in range(len(v1))]
    for i in range(len(v1)):
        result[i] = v1[i] + v2[i]
    return result


def mm_sum(m1: list[list[float]], m2: list[list[float]]) -> list[list[float]]:
    result: list[list[float]] = [[0 for __ in range(len(m1))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for o in range(len(m1)):
            result[i][o] = m1[i][o] + m2[i][o]
    return result


def vm_div(vector: list[float], matrix: list[list[float]], d: list[float]) -> list[float]:
    result: list[float] = [0 for _ in range(len(d))]
    for i in range(len(d)):
        if d[i] != 0:
            for o in range(len(vector)):
                if vector[o] != 0:
                    result[i] += vector[o] * matrix[o][i]
            result[i] *= dexp(mod1, mod2, d[i])
    return result


def mk_div(matrix: list[list[float]], kernel: list[list[float]], d: list[list[float]]) -> list[list[float]]:
    result = [[0 for __ in range(len(d))] for _ in range(len(d))]
    for i in range(len(matrix)):
        for o in range(len(matrix)):
            if matrix[i][o] != 0 and d[i][o] != 0:
                for p in range(len(kernel)):
                    for k in range(len(kernel)):
                        result[i + p][o + k] += matrix[i][o] * kernel[p][k]
                        result[i + p][o + k] *= dexp(mod1, mod2, d[i][o])
    return result


def mm_div(m1: list[list[float]], m2: list[list[float]]) -> list[list[float]]:
    k_size: int = len(m1) - len(m2) + 1
    result: list[list[float]] = [[0 for __ in range(k_size)] for __ in range(k_size)]
    for i in range(k_size):
        for o in range(k_size):
            for p in range(len(m2)):
                for k in range(len(m2)):
                    if m1[i + p][o + k] != 0 and m2[p][k] != 0:
                        result[i][o] += m1[i + p][o + k] * m2[p][k]
    return result

