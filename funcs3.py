from random import randint as r
mod1: float = 1
mod2: float = 3


def dropping(v: list[float], prt: float | None) -> list[float]:
    result: list[float] = list(v)
    if prt != 0 or not prt:
        for i in range(len(result)):
            s = r(0, 10 ** 6) / (10 ** 6)
            if s < prt:
                result[i] = 0
    return result


def act(v: list[float]) -> list[float]:
    result: list[float] = list(v)
    for i in range(len(v)):
        if result[i] != 0:
            result[i] = (result[i] / abs(result[i]) * (abs(result[i]) ** (mod1 / mod2)))
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
    result: list[list[float]] = [[0 for __ in range(len(m1[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for o in range(len(m1[0])):
            result[i][o] = m1[i][o] + m2[i][o]
    return result


def vm_div(vector: list[float], matrix: list[list[float]], d: list[float]) -> list[float]:
    result: list[float] = [0 for _ in range(len(d))]
    for i in range(len(d)):
        if d[i] != 0:
            for o in range(len(vector)):
                if vector[o] != 0:
                    result[i] += vector[o] * matrix[o][i]
            if result[i] != 0:
                result[i] *= (abs(d[i] / d[i] * (abs(d[i]) ** ((mod1 - mod2) ** (1 / mod2)))))
    return result


def vm_div_p(vector: list[float], matrix: list[list[float]]) -> list[float]:
    result: list[float] = [0 for _ in range(len(matrix[0]))]
    for i in range(len(vector)):
        if vector[i] != 0:
            for o in range(len(matrix[0])):
                result[o] += vector[i] * matrix[i][o]
    return result


def vv_mpx(v1: list[float], v2: list[float]) -> float:
    result: float = 0
    for i in range(len(v1)):
        result += (v1[i] * v2[i])
    return result


def vv_div(v1: list[float], v2: list[float]) -> list[list[float]]:
    result: list[list[float]] = [[0 for __ in range(len(v2))] for _ in range(len(v1))]
    for i in range(len(v1)):
        if v1[i] != 0:
            for o in range(len(v2)):
                if v2[o] != 0:
                    result[i][o] = v1[i] * v2[o]
    return result


def vn_mpx(vector: list[float], n: float) -> list[float]:
    result: list[float] = [0 for _ in range(len(vector))]
    for i in range(len(vector)):
        if vector[i] != 0:
            result[i] = vector[i] * n
    return result



