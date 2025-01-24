from random import randint as r
mod1: float = 1
mod2: float = 3


def dropping(v: list[float], prt: float) -> list[float]:
    result: list[float] = list(v)
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

