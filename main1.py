import dict
import funcs

DA: str = 'C:/Users/tatar/TTPuKoJIbI/basicai32/'
ContentSize: int = 64
EmDim: int = 16
npL: list[int] = [ContentSize, 32, 12, 1]
drop_prt: float = 0.1

vocab = dict.d()
n: list[list[list[float]]] = [[[0 for ___ in range(npL[__])] for __ in range(len(npL))] for _ in range(EmDim)]
o1: list[float] = [0 for _ in range(EmDim)]
O: list[float] = [0 for _ in range(len(vocab))]
B: list[list[list[float]]] = [[[0 for ___ in range(npL[__])] for __ in range(len(npL))] for _ in range(EmDim)]
W: list[list[list[list[float]]]] = [[[[0 for ____ in range(npL[__])] for ___ in range(npL[__ + 1])] for __ in range(len(npL) - 1)] for _ in range(EmDim)]
Em: list[list[float]] = [[0 for __ in range(EmDim)] for _ in range(len(vocab))]
UEm: list[list[float]] = [[0 for __ in range(EmDim)] for _ in range(len(vocab))]
dB: list[list[list[float]]] = [[[0 for ___ in range(npL[__])] for __ in range(len(npL))] for _ in range(EmDim)]
dW: list[list[list[list[float]]]] = [[[[0 for ____ in range(npL[__])] for ___ in range(npL[__ + 1])] for __ in range(len(npL) - 1)] for _ in range(EmDim)]
dEm: list[list[float]] = [[0 for __ in range(EmDim)] for _ in range(len(vocab))]
dUEm: list[list[float]] = [[0 for __ in range(EmDim)] for _ in range(len(vocab))]
print('created parms')

Tokens: list[int] = []
with open(f'C:/Users/tatar/TTPuKoJIbI/Тексты/fullT.txt', 'r') as I:
    for i in range(261166):
        t = I.readline()
        Tokens += [int(t)]


def download(ext: str) -> None:
    for i in range(len(vocab)):
        with open(DA + f'{ext}/Em/{i}.txt', 'r') as I:
            for o in range(EmDim):
                t = I.readline()
                Em[i][o] = float(t)
        with open(DA + f'{ext}/UEm/{i}.txt', 'r') as I:
            for o in range(EmDim):
                t = I.readline()
                UEm[i][o] = float(t)
    for i in range(EmDim):
        for o in range(len(npL)):
            with open(DA + f'{ext}/B/{i}_{o}.txt', 'r') as I:
                for p in range(npL[o]):
                    t = I.readline()
                    B[i][o][p] = float(t)
    for i in range(EmDim):
        for o in range(len(npL) - 1):
            for p in range(npL[o + 1]):
                with open(DA + f'{ext}/W/{i}_{o}_{p}.txt', 'r') as I:
                    for k in range(npL[o]):
                        t = I.readline()
                        W[i][o][p][k] = float(t)
    print('params loaded')


def upload(ext: str) -> None:
    for i in range(len(vocab)):
        with open(DA + f'{ext}/Em/{i}.txt', 'w') as I:
            for o in range(EmDim):
                I.write(f'{Em[i][o]}\n')
        with open(DA + f'{ext}/UEm/{i}.txt', 'w') as I:
            for o in range(EmDim):
                I.write(f'{UEm[i][o]}\n')
    for i in range(EmDim):
        for o in range(len(npL)):
            with open(DA + f'{ext}/B/{i}_{o}.txt', 'w') as I:
                for p in range(npL[o]):
                    I.write(f'{B[i][o][p]}\n')
    for i in range(EmDim):
        for o in range(len(npL) - 1):
            for p in range(npL[o + 1]):
                with open(DA + f'{ext}/W/{i}_{o}_{p}.txt', 'w') as I:
                    for k in range(npL[o]):
                        I.write(f'{W[i][o][p][k]}\n')
    print('params uploaded')


def fpr(stt: int) -> None:
    global O
    for i in range(ContentSize):
        for o in range(EmDim):
            s = Em[Tokens[stt + i]][o] + B[o][0][i]
            if s != 0:
                n[o][0][i] = abs(s) / s * (abs(s) ** (funcs.mod1 / funcs.mod2))
            else:
                n[o][0][i] = 0

    for i in range(EmDim):
        for o in range(len(npL) - 1):
            n[i][o + 1] = funcs.act(funcs.dropping(funcs.vv_sum(funcs.vm_mpx(n[i][o], W[i][o]), B[i][o + 1]), drop_prt))

    for i in range(EmDim):
        o1[i] = n[i][-1][-1]
    O = funcs.dropping(funcs.vm_mpx(o1, UEm), drop_prt)


def bpr(stt: int) -> None:
    dn: list[list[list[float]]] = [[[0 for ___ in range(npL[__])] for __ in range(len(npL))] for _ in range(EmDim)]
    do1: list[float] = [0 for _ in range(EmDim)]
    dO: list[float] = [0 for _ in range(len(vocab))]

    for i in range(len(vocab)):
        if O[i] != 0:
            dO[i] = 2 * O[i]
    dO[Tokens[stt + ContentSize]] -= 2

    for i in range(EmDim):
        for o in range(len(vocab)):
            dUEm[o][i] += dO[o] * o1[i]
            do1[i] += dO[o] * UEm[o][i]
        dn[i][-1][-1] = do1[i]
        dB[i][-1][-1] = do1[i]

    for i in range(EmDim):
        for o in range(len(npL) - 2, -1, -1):
            dn[i][o] = funcs.vm_div(dn[i][o + 1], W[i][o], n[i][o])
            for p in range(npL[o]):
                if dn[i][o][p] != 0:
                    dB[i][o][p] += dn[i][o][p]
                    for k in range(npL[o + 1]):
                        if dn[i][o + 1][k] != 0:
                            dW[i][o][k][p] += dn[i][o + 1][k] * n[i][o][p]

    for i in range(ContentSize):
        for o in range(EmDim):
            if dn[o][0][i] != 0:
                dEm[Tokens[stt + i]][o] += dn[o][0][i]


def cng(c: float) -> None:
    for i in range(len(vocab)):
        for o in range(EmDim):
            Em[i][o] -= dEm[i][o] * c
            UEm[i][o] -= dUEm[i][o] * c

    for i in range(EmDim):
        for o in range(len(npL)):
            for p in range(npL[o]):
                B[i][o][p] -= dB[i][o][p] * c

    for i in range(EmDim):
        for o in range(len(npL) - 1):
            for p in range(npL[o]):
                for k in range(npL[o + 1]):
                    W[i][o][k][p] -= dW[i][o][k][p] * c


def cost(stt: int) -> float:
    result: float = 0
    for i in range(len(vocab)):
        result += O[i] ** 2
    result += 1 - 2 * O[Tokens[stt + ContentSize]]
    return result


n_trial: int = len(Tokens) - ContentSize - 1
step = 200
download('0')
for l in range(10):
    for p in range(1):
        for o in range(1):
            C: float = 0
            for k in range(p, n_trial, step):
                fpr(k)
                bpr(k)
                C += cost(k)
            print(l, O.index(max(O)), Tokens[k + ContentSize], max(O), O[Tokens[k + ContentSize]], cost(k))
            cng(C * 0.0000000001 / n_trial * step)
            dB: list[list[list[float]]] = [[[0 for ___ in range(npL[__])] for __ in range(len(npL))] for _ in range(EmDim)]
            dW: list[list[list[list[float]]]] = [
                [[[0 for ____ in range(npL[__])] for ___ in range(npL[__ + 1])] for __ in range(len(npL) - 1)] for _ in
                range(EmDim)]
            dEm: list[list[float]] = [[0 for __ in range(EmDim)] for _ in range(len(vocab))]
            dUEm: list[list[float]] = [[0 for __ in range(EmDim)] for _ in range(len(vocab))]

            print(f'{l} {p} {o} {C} {C * step / n_trial}\n')
ans: str = input('allow uploading ')
if ans == '1':
    upload('ed')
