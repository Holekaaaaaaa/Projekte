import funcs
import vocab

DA: str = 'C:/Users/tatar/TTPuKoJIbI/basicai1.2/'
ContentSize: int = 32
EmDim: int = 12
npL: list[int] = [EmDim, EmDim * 2, EmDim]
KQDim: int = 6
L: int = 6
drop_prt: float = 0.1
vocabL = len(vocab.d())

Em: list[list[float]] = [[0 for __ in range(EmDim)] for _ in range(vocabL)]
UEm: list[list[float]] = [[0 for __ in range(EmDim)] for _ in range(vocabL)]
V: list[list[list[list[float]]]] = [[[[0 for ____ in range(EmDim)] for ___ in range(KQDim)] for __ in range(ContentSize)] for _ in range(L)]
K: list[list[list[list[float]]]] = [[[[0 for ____ in range(EmDim)] for ___ in range(KQDim)] for __ in range(ContentSize)] for _ in range(L)]
Q: list[list[list[list[float]]]] = [[[[0 for ____ in range(EmDim)] for ___ in range(KQDim)] for __ in range(ContentSize)] for _ in range(L)]
VOut: list[list[list[list[float]]]] = [[[[0 for ____ in range(KQDim)] for ___ in range(EmDim)] for __ in range(ContentSize)] for _ in range(L)]
B: list[list[list[list[float]]]] = [[[[0 for o in range(npL[i])] for i in range(len(npL))] for __ in range(ContentSize)] for _ in range(L)]
W: list[list[list[list[list[float]]]]] = [[[[[0 for p in range(npL[i])] for o in range(npL[i + 1])] for i in range(len(npL) - 1)] for __ in range(ContentSize)] for _ in range(L)]

Ems: list[list[list[float]]] = [[[0 for ___ in range(EmDim)] for __ in range(ContentSize)] for _ in range(L + 1)]
Ks: list[list[list[float]]] = [[[0 for ___ in range(KQDim)] for __ in range(ContentSize)] for _ in range(L)]
Qs: list[list[list[float]]] = [[[0 for ___ in range(KQDim)] for __ in range(ContentSize)] for _ in range(L)]
Vs: list[list[list[float]]] = [[[0 for ___ in range(EmDim)] for __ in range(ContentSize)] for _ in range(L)]
cVs: list[list[list[list[float]]]] = [[[[0 for ___ in range(EmDim)] for __ in range(ContentSize)] for __ in range(ContentSize)] for _ in range(L)]
CVs: list[list[list[float]]] = [[[0 for ___ in range(EmDim)] for __ in range(ContentSize)] for _ in range(L)]
n: list[list[list[list[float]]]] = [[[[0 for o in range(npL[i])] for i in range(len(npL))] for __ in range(ContentSize)] for _ in range(L)]
P: list[list[list[float]]] = [[[0 for ___ in range(ContentSize)] for __ in range(ContentSize)] for _ in range(L)]
O: list[float] = [0 for _ in range(vocabL)]

dEm: list[list[float]] = [[0 for __ in range(EmDim)] for _ in range(vocabL)]
dUEm: list[list[float]] = [[0 for __ in range(EmDim)] for _ in range(vocabL)]
dV: list[list[list[list[float]]]] = [[[[0 for ____ in range(EmDim)] for ___ in range(KQDim)] for __ in range(ContentSize)] for _ in range(L)]
dK: list[list[list[list[float]]]] = [[[[0 for ____ in range(EmDim)] for ___ in range(KQDim)] for __ in range(ContentSize)] for _ in range(L)]
dQ: list[list[list[list[float]]]] = [[[[0 for ____ in range(EmDim)] for ___ in range(KQDim)] for __ in range(ContentSize)] for _ in range(L)]
dVOut: list[list[list[list[float]]]] = [[[[0 for ____ in range(KQDim)] for ___ in range(EmDim)] for __ in range(ContentSize)] for _ in range(L)]
dB: list[list[list[list[float]]]] = [[[[0 for o in range(npL[i])] for i in range(len(npL))] for __ in range(ContentSize)] for _ in range(L)]
dW: list[list[list[list[list[float]]]]] = [[[[[0 for p in range(npL[i])] for o in range(npL[i + 1])] for i in range(len(npL) - 1)] for __ in range(ContentSize)] for _ in range(L)]

print('created parms')

Tokens: list[int] = []
with open(f'C:/Users/tatar/TTPuKoJIbI/Тексты/fullT.txt', 'r') as I:
    for i in range(261166):
        t = I.readline()
        Tokens += [int(t)]


def download(ext) -> None:
    for i in range(vocabL):
        with open(f'{DA}{ext}/Em/{i}.txt', 'r') as I:
            for o in range(EmDim):
                t = I.readline()
                Em[i][o] = float(t)
        with open(f'{DA}{ext}/UEm/{i}.txt', 'r') as I:
            for o in range(EmDim):
                t = I.readline()
                UEm[i][o] = float(t)

    for k in range(L):
        for i in range(ContentSize):
            for o in range(KQDim):
                with open(f'{DA}{ext}/K/{k}_{i}_{o}.txt', 'r') as I:
                    for p in range(EmDim):
                        t = I.readline()
                        K[k][i][o][p] = float(t)
                with open(f'{DA}{ext}/Q/{k}_{i}_{o}.txt', 'r') as I:
                    for p in range(EmDim):
                        t = I.readline()
                        Q[k][i][o][p] = float(t)
                with open(f'{DA}{ext}/V/{k}_{i}_{o}.txt', 'r') as I:
                    for p in range(EmDim):
                        t = I.readline()
                        V[k][i][o][p] = float(t)
            for o in range(EmDim):
                with open(f'{DA}{ext}/Vout/{k}_{i}_{o}.txt', 'r') as I:
                    for p in range(KQDim):
                        t = I.readline()
                        VOut[k][i][o][p] = float(t)

    for i in range(L):
        for o in range(ContentSize):
            for p in range(len(npL) - 1):
                for k in range(npL[p + 1]):
                    with open(f'{DA}{ext}/W/{i}_{o}_{p}_{k}.txt', 'r') as I:
                        for l in range(npL[p]):
                            t = I.readline()
                            W[i][o][p][k][l] = float(t)

    for i in range(L):
        for o in range(ContentSize):
            for p in range(len(npL)):
                with open(f'{DA}{ext}/B/{i}_{o}_{p}.txt', 'r') as I:
                    for k in range(npL[p]):
                        t = I.readline()
                        B[i][o][p][k] = float(t)
    print('params loaded')


def upload(ext) -> None:
    for i in range(vocabL):
        with open(f'{DA}{ext}/Em/{i}.txt', 'w') as I:
            for o in range(EmDim):
                I.write(f'{Em[i][o]}\n')
        with open(f'{DA}{ext}/UEm/{i}.txt', 'w') as I:
            for o in range(EmDim):
                I.write(f'{UEm[i][o]}\n')

    for i in range(L):
        for o in range(ContentSize):
            for p in range(KQDim):
                with open(f'{DA}{ext}/K/{i}_{o}_{p}.txt', 'w') as I:
                    for k in range(EmDim):
                        I.write(f'{K[i][o][p][k]}\n')
                with open(f'{DA}{ext}/Q/{i}_{o}_{p}.txt', 'w') as I:
                    for k in range(EmDim):
                        I.write(f'{Q[i][o][p][k]}\n')
                with open(f'{DA}{ext}/V/{i}_{o}_{p}.txt', 'w') as I:
                    for k in range(EmDim):
                        I.write(f'{V[i][o][p][k]}\n')
            for p in range(EmDim):
                with open(f'{DA}{ext}/Vout/{i}_{o}_{p}.txt', 'w') as I:
                    for k in range(KQDim):
                        I.write(f'{VOut[i][o][p][k]}\n')

            for p in range(len(npL) - 1):
                for k in range(npL[p + 1]):
                    with open(f'{DA}{ext}/W/{i}_{o}_{p}_{k}.txt', 'w') as I:
                        for l in range(npL[p]):
                            I.write(f'{W[i][o][p][k][l]}\n')

            for p in range(len(npL)):
                with open(f'{DA}{ext}/B/{i}_{o}_{p}.txt', 'w') as I:
                    for k in range(npL[p]):
                        I.write(f'{B[i][o][p][k]}\n')

    with open(f'{DA}{ext}/main.txt', 'w') as I:
        I.write(f'{ContentSize}\n')
        I.write(f'{EmDim}\n')
        I.write(f'{KQDim}\n')
        I.write(f'{L}\n')
        I.write(f'{len(npL)}\n')
        for ly in npL:
            I.write(f'{ly}\n')

    print('params uploaded')


def fpr(stt: int) -> None:
    global O
    for i in range(ContentSize):
        Ems[0][i] = Em[Tokens[stt + i]]

    for i in range(L):
        for o in range(ContentSize):
            Ks[i][o] = funcs.dropping(funcs.vm_mpx(Ems[i][o], K[i][o]), drop_prt)
            Qs[i][o] = funcs.dropping(funcs.vm_mpx(Ems[i][o], Q[i][o]), drop_prt)
            Vs[i][o] = funcs.dropping(funcs.vm_mpx(funcs.vm_mpx(Ems[i][o], V[i][o]), VOut[i][o]), drop_prt)
        for o in range(ContentSize):
            for p in range(ContentSize):
                P[i][o][p] = funcs.vv_mpx(Qs[i][o], Ks[i][p])
                cVs[i][o][p] = funcs.vn_mpx(Vs[i][p], P[i][o][p])
            P[i][o] = funcs.dropping(P[i][o], drop_prt)
        for o in range(ContentSize):
            for p in range(ContentSize):
                CVs[i][o] = funcs.vv_sum(CVs[i][o], cVs[i][o][p])
            Ems[i + 1][o] = funcs.vv_sum(Ems[i][o], CVs[i][o])

        for o in range(ContentSize):
            n[i][o][0] = funcs.act(funcs.vv_sum(Ems[i + 1][o], B[i][o][0]))
        for o in range(ContentSize):
            for p in range(len(npL) - 1):
                n[i][o][p + 1] = funcs.act(funcs.dropping(funcs.vv_sum(funcs.vm_mpx(n[i][o][p], W[i][o][p]), B[i][o][p + 1]), drop_prt))
        for o in range(ContentSize):
            Ems[i + 1][o] = n[i][o][-1]

    O = funcs.dropping(funcs.vm_mpx(Ems[-1][-1], UEm), drop_prt)


def bpr(stt: int) -> None:
    global dUEm

    do: list[float] = [0 for _ in range(vocabL)]
    dems: list[list[list[float]]] = [[[0 for ___ in range(EmDim)] for __ in range(ContentSize)] for _ in range(L + 1)]
    dp: list[list[list[float]]] = [[[0 for ___ in range(ContentSize)] for __ in range(ContentSize)] for _ in range(L)]
    dn: list[list[list[list[float]]]] = [[[[0 for o in range(npL[i])] for i in range(len(npL))] for __ in range(ContentSize)] for _ in range(L)]
    dcVs: list[list[list[list[float]]]] = [[[[0 for ___ in range(EmDim)] for __ in range(ContentSize)] for __ in range(ContentSize)] for _ in range(L)]
    dVs: list[list[list[float]]] = [[[0 for ___ in range(EmDim)] for __ in range(ContentSize)] for _ in range(L)]
    dKs: list[list[list[float]]] = [[[0 for ___ in range(KQDim)] for __ in range(ContentSize)] for _ in range(L)]
    dQs: list[list[list[float]]] = [[[0 for ___ in range(KQDim)] for __ in range(ContentSize)] for _ in range(L)]

    for i in range(vocabL):
        do[i] = 2 * O[i]
    do[Tokens[stt + ContentSize]] -= 2

    dems[-1][-1] = funcs.vm_div(do, UEm, Ems[-1][-1])
    dUEm = funcs.mm_sum(dUEm, funcs.vv_div(do, dems[-1][-1]))

    for i in range(EmDim):
        dn[-1][-1][-1][i] = (dems[-1][-1][i] ** (funcs.mod2 - funcs.mod1)) ** (-1 / funcs.mod2) if dems[-1][-1][i] != 0 else 0
        dB[-1][-1][-1][i] += dn[-1][-1][-1][i]

    for i in range(len(npL) - 2, -1, -1):
        dn[-1][-1][i] = funcs.vm_div(dn[-1][-1][i + 1], W[-1][-1][i], n[-1][-1][i])
        dW[-1][-1][i] = funcs.mm_sum(dW[-1][-1][i], funcs.vv_div(dn[-1][-1][i + 1], n[-1][-1][i]))
        dB[-1][-1][i] = funcs.vv_sum(dB[-1][-1][i], dn[-1][-1][i])

    for i in range(ContentSize):
        dp[-1][-1][i] = funcs.vv_mpx(dn[-1][-1][0], cVs[-1][-1][i])
        dcVs[-1][-1][i] = funcs.vn_mpx(dn[-1][-1][0], P[-1][-1][i])
        dVs[-1][i] = funcs.vn_mpx(dcVs[-1][-1][i], P[-1][-1][i])
        dKs[-1][i] = funcs.vn_mpx(Qs[-1][-1], dp[-1][-1][i])
        dQs[-1][-1] = funcs.vv_sum(dQs[-1][-1], funcs.vn_mpx(Ks[-1][i], dp[-1][-1][i]))

    for i in range(ContentSize):
        dK[-1][i] = funcs.mm_sum(dK[-1][i], funcs.vv_div(dKs[-1][i], Ems[-2][i]))
        dQ[-1][i] = funcs.mm_sum(dQ[-1][i], funcs.vv_div(dQs[-1][i], Ems[-2][i]))
        dVOut[-1][i] = funcs.mm_sum(dVOut[-1][i], funcs.vv_div(dVs[-1][i], funcs.vm_mpx(Ems[-2][i], V[-2][i])))
        dV[-1][i] = funcs.mm_sum(dV[-1][i], funcs.vv_div(funcs.vm_mpx(Ems[-2][i], V[-2][i]), Ems[-2][i]))

    for i in range(ContentSize):
        dems[-2][i] = funcs.vv_sum(funcs.vv_sum(funcs.vm_div_p(funcs.vn_mpx(Qs[-1][-1], dp[-1][-1][i]), K[-1][i]),
                                                funcs.vm_div_p(dQs[-1][i], Q[-1][i])),
                                   funcs.vm_div_p(funcs.vm_div_p(funcs.vn_mpx(dcVs[-1][-1][i], P[-1][-1][i]), VOut[-1][i]), V[-1][i]))

    for i in range(L - 2, -1, -1):
        for o in range(ContentSize):
            dn[i][o][-1] = dems[i + 1][o]

        for o in range(ContentSize):
            for p in range(len(npL) - 2, -1, -1):
                dn[i][o][p] = funcs.vm_div(dn[i][o][p + 1], W[i][o][p], n[i][o][p])
                dW[i][o][p] = funcs.mm_sum(dW[i][o][p], funcs.vv_div(dn[i][o][p + 1], n[i][o][p]))
                dB[i][o][p] = funcs.vv_sum(dB[i][o][p], dn[i][o][p])

        for o in range(ContentSize):
            for p in range(ContentSize):
                dp[i][o][p] = funcs.vv_mpx(dn[i][o][0], cVs[i][o][p])
                dQs[i][o] = funcs.vv_sum(dQs[i][o], funcs.vn_mpx(Ks[i][p], dp[i][o][p]))
                dKs[i][p] = funcs.vv_sum(dKs[i][p], funcs.vn_mpx(Qs[i][o], dp[i][o][p]))
                dVs[i][p] = funcs.vv_sum(dVs[i][p], funcs.vn_mpx(dn[i][o][0], P[i][o][p]))
        for o in range(ContentSize):
            dK[i][o] = funcs.mm_sum(dK[i][o], funcs.vv_div(dKs[i][o], Ems[i][o]))
            dQ[i][o] = funcs.mm_sum(dQ[i][o], funcs.vv_div(dQs[i][o], Ems[i][o]))
            dVOut[i][o] = funcs.mm_sum(dVOut[i][o], funcs.vv_div(dVs[i][o], funcs.vm_mpx(Ems[i][o], V[i][o])))
            dV[i][o] = funcs.mm_sum(dV[i][o], funcs.vv_div(funcs.vm_mpx(Ems[i][o], V[i][o]), Ems[i][o]))

        for o in range(ContentSize):
            dems[i][o] = funcs.vv_sum(funcs.vv_sum(funcs.vm_div_p(dKs[i][o], K[i][o]),
                                                   funcs.vm_div_p(dQs[i][o], Q[i][o])),
                                      funcs.vm_div_p(funcs.vm_div_p(dVs[i][o], VOut[i][o]), V[i][o]))

    for i in range(ContentSize):
        for o in range(EmDim):
            dEm[Tokens[stt + i]][o] += dems[0][i][o]


def cng(c: float) -> None:
    for i in range(vocabL):
        for o in range(EmDim):
            Em[i][o] -= dEm[i][o] * c
            UEm[i][o] -= dUEm[i][o] * c

    for i in range(L):
        for o in range(ContentSize):
            for p in range(KQDim):
                for k in range(EmDim):
                    K[i][o][p][k] -= dK[i][o][p][k] * c
                    Q[i][o][p][k] -= dQ[i][o][p][k] * c
                    V[i][o][p][k] -= dV[i][o][p][k] * c
                    VOut[i][o][k][p] -= dVOut[i][o][k][p] * c
            for p in range(len(npL) - 1):
                for k in range(npL[p + 1]):
                    for l in range(npL[p]):
                        W[i][o][p][k][l] -= dW[i][o][p][k][l] * c
            for p in range(len(npL)):
                for k in range(npL[p]):
                    B[i][o][p][k] -= dB[i][o][p][k] * c


def cost(stt: int) -> float:
    result: float = 0
    for i in range(vocabL):
        result += O[i] ** 2
    result += 1 - 2 * O[Tokens[stt + ContentSize]]
    return result


download('1')
step: int = 150
n_trial: int = len(Tokens) - ContentSize - 1
for l in range(5):
    C = 0
    for k in range(0, n_trial, step):
        fpr(k)
        bpr(k)
        C += cost(k)
    cng(C * 0.00000000001 * step / n_trial)
    print(l, O.index(max(O)), Tokens[k + ContentSize], max(O), O[Tokens[k + ContentSize]], cost(k))
    print(f'{l} 0 0 {C}  {C * step / n_trial}\n')

    dEm: list[list[float]] = [[0 for __ in range(EmDim)] for _ in range(vocabL)]
    dUEm: list[list[float]] = [[0 for __ in range(EmDim)] for _ in range(vocabL)]
    dV: list[list[list[list[float]]]] = [[[[0 for ____ in range(EmDim)] for ___ in range(KQDim)] for __ in range(ContentSize)] for _ in range(L)]
    dK: list[list[list[list[float]]]] = [[[[0 for ____ in range(EmDim)] for ___ in range(KQDim)] for __ in range(ContentSize)] for _ in range(L)]
    dQ: list[list[list[list[float]]]] = [[[[0 for ____ in range(EmDim)] for ___ in range(KQDim)] for __ in range(ContentSize)] for _ in range(L)]
    dVOut: list[list[list[list[float]]]] = [[[[0 for ____ in range(KQDim)] for ___ in range(EmDim)] for __ in range(ContentSize)] for _ in range(L)]
    dB: list[list[list[list[float]]]] = [[[[0 for o in range(npL[i])] for i in range(len(npL))] for __ in range(ContentSize)] for _ in range(L)]
    dW: list[list[list[list[list[float]]]]] = [[[[[0 for p in range(npL[i])] for o in range(npL[i + 1])] for i in range(len(npL) - 1)] for __ in range(ContentSize)] for _ in range(L)]

    Ems: list[list[list[float]]] = [[[0 for ___ in range(EmDim)] for __ in range(ContentSize)] for _ in range(L + 1)]
    Ks: list[list[list[float]]] = [[[0 for ___ in range(KQDim)] for __ in range(ContentSize)] for _ in range(L)]
    Qs: list[list[list[float]]] = [[[0 for ___ in range(KQDim)] for __ in range(ContentSize)] for _ in range(L)]
    Vs: list[list[list[float]]] = [[[0 for ___ in range(EmDim)] for __ in range(ContentSize)] for _ in range(L)]
    cVs: list[list[list[list[float]]]] = [
        [[[0 for ___ in range(EmDim)] for __ in range(ContentSize)] for __ in range(ContentSize)] for _ in range(L)]
    CVs: list[list[list[float]]] = [[[0 for ___ in range(EmDim)] for __ in range(ContentSize)] for _ in range(L)]
    n: list[list[list[list[float]]]] = [
        [[[0 for o in range(npL[i])] for i in range(len(npL))] for __ in range(ContentSize)] for _ in range(L)]
    P: list[list[list[float]]] = [[[0 for ___ in range(ContentSize)] for __ in range(ContentSize)] for _ in range(L)]
    O: list[float] = [0 for _ in range(vocabL)]

C = 0
for k in range(0, n_trial, step):
    fpr(k)
    C += cost(k)
print(O.index(max(O)), Tokens[k + ContentSize], max(O), O[Tokens[k + ContentSize]], cost(k))
print(f'{C}  {C * step / n_trial}\n')
ans: str = input('allow uploading ')
if ans == '1':
    upload('ed2')
