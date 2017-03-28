import numpy

def dot(Macierz, wektor):
    out=[]
    for i in range(0, len(Macierz)):
        l= 0.0
        for j in range(0, len(wektor)):
            l= l+ Macierz[i][j]*wektor[j]
        out.append(l)
    return out

n = int(raw_input("Liczba zmiennych: "))
funkcja = []
for i in range (0, n):
   funkcja.append(int(raw_input("wspolczynniki przy x" + str(i + 1) + ': ')))

m=int(raw_input("Liczba ograniczen"))
A = []
b = []
for i in range(0, m):
    h =[]
    for j in range(0, n):
        h.append(int(raw_input('Wpolczynnik przy x' + str(j + 1) + ': ')))
    b.append(int(raw_input('Podaj wyraz wolny:')))
    for j in range(0, m):
        if i == j:
            h.append(1)
        else:
            h.append(0)
    A.append(h)
    funkcja.append(0)
 


funkcja = [funkcja]
k = m + n

def wybierz_kolumny(wyb, nast):
    if nast == k:
        if len(wyb) == m:
            O = []
            for i in range(0, m):
                wiersz = []
                for j in wyb:
                    wiersz.append(A[i][j])
                O.append(wiersz)

            if numpy.linalg.matrix_rank(O) == m:
                kandydat_0 = dot(numpy.linalg.inv(O), b)
                i = 0
                kandydat_1 = []
                for j in range(0, k):
                    if i < m and j == wyb[i]:
                        kandydat_1.append(kandydat_0[i])
                        i = i + 1
                    else:
						kandydat_1.append(0.0)
                max_wartosc = dot(funkcja, kandydat_1)[0]
                return max_wartosc
		return float('-inf')

    else:
        wynik = wybierz_kolumny(wyb, nast +1)
        if len(wyb) < m:
            wyb.append(nast)
            wynik = max(wybierz_kolumny(wyb, nast +1), wynik)
            wyb.pop()
        return wynik

wyb = []
max_wartosc = wybierz_kolumny(wyb, 0)

print 'Wartosc maksymalna:', max_wartosc
