def kp_rand(size,seed): # zmodyfikowana funkcja zwracająca listę wag i listę wartości
    lista_wag = []
    lista_wartosci = []
    print("data:",size,size)
    for a in range(size):
        for b in range(2):
            seed = (seed*69069+1)&0xFFFFFFFF
            d = (seed%99+1)
            print('{:2d}'.format(d),end=" " )
            if b%2==0:
                lista_wartosci.append(d)
            if b%2==1:
                lista_wag.append(d)
            
        print()
    print()
    return lista_wag, lista_wartosci

def knapsack(pojemnosc, liczba_elementow, lista_wag, lista_wartosci):
    macierz = [[0 for x in range(pojemnosc + 1)] for x in range(liczba_elementow + 1)]  # inicjalizacja wypełnionej zerami macierzy do przechowywania wyników

    for i in range(liczba_elementow + 1):   # iteracja po elementach plecaka i pojemności; +1 ze względu na indeksowanie 
        for j in range(pojemnosc + 1):
            if lista_wag[i - 1] <= j:   # sprawdzenie, czy waga elementu nie przekracza pojemnosci plecaka
                # jesli warunek jest spelniony to wybierany jest element o większej wartosci
                macierz[i][j] = max(lista_wartosci[i - 1] + macierz[i - 1][j - lista_wag[i - 1]], macierz[i - 1][j])    
            else:
                # jeśli nie jest spełniony to wartosc zostaje przypisana do poprzedniego wiersza macierzy
                macierz[i][j] = macierz[i - 1][j]
    # zwracany jest ostatni element macierzy zawierający informacje o największej możliwej wartosci przedmiotów w plecaku            
    return macierz[liczba_elementow][pojemnosc]

size = 100
seed = 100
wartosci, wagi = kp_rand(size, seed)

result = knapsack(size, size, wagi, wartosci)

print("Maksymalna wartość przedmiotów w plecaku:", result)
