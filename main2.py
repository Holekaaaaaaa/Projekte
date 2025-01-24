import dict
import funcs

DA: str = 'C:/Users/tatar/TTPuKoJIbI/basicai22/'
ContentSize: int = 20
EmDim: int = 20
KSize: list[int] = [7, 7, 5]
npL: list[int] = [16, 16, 64]
drop_prt: float = 0.075

vocab = dict.d()
Em: list[list[float]] = [[0 for __ in range(EmDim)] for _ in range(len(vocab))]
UEm: list[list[float]] = [[0 for __ in range(npL[-1])] for _ in range(len(vocab))]
K: list[list[list[float]]] = [[[0 for ___ in range(KSize[_])] for __ in range(KSize[_])] for _ in range(len(KSize))]
Kn: list[list[list[float]]] = [[[0 for ___ in range(EmDim - sum(KSize[:_]) + _)] for __ in range(EmDim - sum(KSize[:_]) + _)] for _ in range(len(KSize) + 1)]
B: list[list[float]] = [[0 for __ in range(npL[_])] for _ in range(len(npL))]
W: list[list[list[float]]] = [[[0 for ___ in range(npL[_])] for __ in range(npL[_ + 1])] for _ in range(len(npL) - 1)]
n: list[list[float]] = [[0 for __ in range(npL[_])] for _ in range(len(npL))]
O: list[float] = [0 for _ in range(len(vocab))]
dKn: list[list[list[float]]] = [[[0 for ___ in range(EmDim - sum(KSize[:_]) + _)] for __ in range(EmDim - sum(KSize[:_]) + _)] for _ in range(len(KSize) + 1)]
dn: list[list[float]] = [[0 for __ in range(npL[_])] for _ in range(len(npL))]
dO: list[float] = [0 for _ in range(len(vocab))]
dK: list[list[list[float]]] = [[[0 for ___ in range(KSize[_])] for __ in range(KSize[_])] for _ in range(len(KSize))]
dEm: list[list[float]] = [[0 for __ in range(EmDim)] for _ in range(len(vocab))]
dUEm: list[list[float]] = [[0 for __ in range(npL[-1])] for _ in range(len(vocab))]
dn0: list[list[float]] = [[0 for __ in range(npL[_])] for _ in range(len(npL))]
dW: list[list[list[float]]] = [[[0 for ___ in range(npL[_])] for __ in range(npL[_ + 1])] for _ in range(len(npL) - 1)]

print('created parms')
Tokens: list[int] = []
with open('C:/Users/tatar/TTPuKoJIbI/Тексты/fullT.txt', 'r') as I:
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
            for o in range(npL[-1]):
                t = I.readline()
                UEm[i][o] = float(t)
    for i in range(len(KSize)):
        with open(DA + f'{ext}/K/{i}.txt', 'r') as I:
            for o in range(KSize[i]):
                for p in range(KSize[i]):
                    t = I.readline()
                    K[i][o][p] = float(t)
    for i in range(len(npL)):
        with open(DA + f'{ext}/B/{i}.txt', 'r') as I:
            for o in range(npL[i]):
                t = I.readline()
                B[i][o] = float(t)
    for i in range(len(npL) - 1):
        for o in range(npL[i + 1]):
            with open(DA + f'{ext}/W/{i}_{o}.txt', 'r') as I:
                for p in range(npL[i]):
                    t = I.readline()
                    W[i][o][p] = float(t)
    print('params loaded')


def upload(ext: str) -> None:
    for i in range(len(vocab)):
        with open(DA + f'{ext}/Em/{i}.txt', 'w') as I:
            for o in range(EmDim):
                I.write(f'{Em[i][o]}\n')
        with open(DA + f'{ext}/UEm/{i}.txt', 'w') as I:
            for o in range(npL[-1]):
                I.write(f'{UEm[i][o]}\n')
    for i in range(len(KSize)):
        with open(DA + f'{ext}/K/{i}.txt', 'w') as I:
            for o in range(KSize[i]):
                for p in range(KSize[i]):
                    I.write(f'{K[i][o][p]}\n')
    for i in range(len(npL)):
        with open(DA + f'{ext}/B/{i}.txt', 'w') as I:
            for o in range(npL[i]):
                I.write(f'{B[i][o]}\n')
    for i in range(len(npL) - 1):
        for o in range(npL[i + 1]):
            with open(DA + f'{ext}/W/{i}_{o}.txt', 'w') as I:
                for p in range(npL[i]):
                    I.write(f'{W[i][o][p]}\n')
    print('params uploaded')


# forwarding
def fpr(token: int) -> None:
    global O
    for i in range(ContentSize):
        Kn[0][i] = Em[Tokens[token + i]]
    for i in range(len(KSize)):
        Kn[i + 1] = funcs.act_m(funcs.dropping_m(funcs.conv(Kn[i], K[i]), drop_prt))

    for i in range(npL[0]):
        n[0][i] = Kn[-1][i // (EmDim - sum(KSize) + len(KSize))][i % (EmDim - sum(KSize) + len(KSize))] + B[0][i]
    n[0] = funcs.act_v(n[0])
    for i in range(len(npL) - 1):
        n[i + 1] = funcs.act_v(funcs.dropping(funcs.vv_sum(funcs.vm_mpx(n[i], W[i]), B[i + 1]), drop_prt))
    O = funcs.act_v(funcs.dropping(funcs.vm_mpx(n[-1], UEm), drop_prt))


# back propagating
def bpr(token: int, token_s: int) -> None:
    for i in range(len(vocab)):
        dO[i] = 2 * O[i] * funcs.dexp(funcs.mod1, funcs.mod2, O[i])
    dO[Tokens[token]] -= 2
    dn0[-1] = funcs.vm_div(dO, UEm, n[-1])
    for i in range(len(vocab)):
        for o in range(npL[-1]):
            dUEm[i][o] += dO[i] * dn0[-1][o]

    for i in range(len(npL) - 2, -1, -1):
        dn0[i] = funcs.vm_div(dn0[i + 1], W[i], n[i])
        dn[i] = funcs.vv_sum(dn[i], dn0[i])
        for o in range(npL[i]):
            if n[i][o] != 0:
                for p in range(npL[i + 1]):
                    if dn0[i + 1][p] != 0:
                        dW[i][p][o] += dn0[i + 1][p] * n[i][o]

    for i in range(npL[0]):
        dKn[-1][i // (EmDim - sum(KSize) + len(KSize))][i % (EmDim - sum(KSize) + len(KSize))] = \
            dn0[0][i] * funcs.dexp(funcs.mod1, funcs.mod2, dn0[0][i])

    for i in range(len(KSize) - 2, -1, -1):
        dKn[i] = funcs.mk_div(dKn[i + 1], K[i], Kn[i])
        dK[i] = funcs.mm_sum(dK[i], funcs.mm_div(Kn[i], dKn[i + 1]))

    for i in range(token_s, token_s + ContentSize):
        for o in range(EmDim):
            dEm[Tokens[i]][o] += dKn[0][i - token_s][o]


# applying changes
def cng(c: float) -> None:
    for i in range(len(vocab)):
        for o in range(EmDim):
            Em[i][o] -= dEm[i][o] * c
        for o in range(npL[-1]):
            UEm[i][o] -= dUEm[i][o] * c

    for i in range(len(npL) - 1):
        for o in range(npL[i]):
            for p in range(npL[i + 1]):
                W[i][p][o] -= dW[i][p][o] * c

    for i in range(len(npL)):
        for o in range(npL[i]):
            B[i][o] -= dn[i][o] * c

    for i in range(len(KSize)):
        for o in range(KSize[i]):
            for p in range(KSize[i]):
                K[i][o][p] -= dK[i][o][p] * c


def cost(token: int) -> float:
    result: float = 0
    for i in range(len(vocab)):
        result += O[i] ** 2
    result += 1 - 2 * O[Tokens[token]]
    return result


n_trial: int = len(Tokens) - ContentSize - 1
step: int = 50
download('ed2')
for l in range(5):
    C = 0
    for k in range(0, n_trial, step):
        fpr(k)
        C += cost(Tokens[k + ContentSize])
        bpr(k + ContentSize, k)
    print(O.index(max(O)), Tokens[k + ContentSize], max(O), O[Tokens[k + ContentSize]], cost(Tokens[k + ContentSize]))
    cng(C * 0.00000000000001 / (n_trial / step))
    dKn: list[list[list[float]]] = [[[0 for ___ in range(EmDim - sum(KSize[:_]) + _)] for __ in range(EmDim - sum(KSize[:_]) + _)] for _ in range(len(KSize) + 1)]
    dn: list[list[float]] = [[0 for __ in range(npL[_])] for _ in range(len(npL))]
    dO: list[float] = [0 for _ in range(len(vocab))]
    dK: list[list[list[float]]] = [[[0 for ___ in range(KSize[_])] for __ in range(KSize[_])] for _ in range(len(KSize))]
    dEm: list[list[float]] = [[0 for __ in range(EmDim)] for _ in range(len(vocab))]
    dUEm: list[list[float]] = [[0 for __ in range(npL[-1])] for _ in range(len(vocab))]
    dn0: list[list[float]] = [[0 for __ in range(npL[_])] for _ in range(len(npL))]
    dW: list[list[list[float]]] = [[[0 for ___ in range(npL[_])] for __ in range(npL[_ + 1])] for _ in range(len(npL) - 1)]
    print(f'{l} 0 0 {C} {C * step / n_trial}\n')

ans: str = input('allow uploading ')
if ans == '1':
    upload('ed2')
