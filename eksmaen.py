import numpy as np


def fitExponential(t, y):
    n = len(t)  # Antall dager/målinger
    A = np.zeros((n, 2))  # Systemmatrise for inkonsistent system
    b = np.zeros((n, 1))  # Systemets venstre side

    A[:, 0] = [1 for i in range(n)]
    A[:, 1] = t.reshape(1, 14)  # Fullfør
    b = konsentrasjon2.reshape(14, 1)  #Fullfør
    ATA = A.T @ A
    ATb = A.T @ b
    params = np.linalg.solve(ATA, ATb) #Fullfør - Parametere fra løsning av normalligning
    #
    c1 = params[0] #Fullfør - Parameter 1 i eksponentiell modall
    c2 = np.exp(params[1] * t) #Fullfør - Parameter 2 i eksponentiell modell
    return c1, c2


konsentrasjon = np.array([1000.0, 1095.57, 1255.88, 1439.49, 1559.16,
                          1719.35, 1817.89, 1923.63, 2204.12, 2541.18,
                          2699.56, 3056.82, 3409.18, 3743.08])  # Målt algekonsentrasjon

konsentrasjon2 = np.array([np.log(1000.0), np.log(1095.57), np.log(1255.88), np.log(1439.49), np.log(1559.16),
                          np.log(1719.35), np.log(1817.89), np.log(1923.63), np.log(2204.12), np.log(2541.18),
                          np.log(2699.56), np.log(3056.82), np.log(3409.18), np.log(3743.08)])  # Målt algekonsentrasjon

t = np.linspace(0, 13, 14)  # Dager vi målte algekonsentrasjon
print(t)
c1, c2 = fitExponential(t, konsentrasjon2)
print(c1)
print(c2)
#fitExponential(t, konsentrasjon)