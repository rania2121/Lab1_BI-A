import numpy as np
import matplotlib.pyplot as plt

mois_dict = {
    "janvier":1,
    "fevrier":2,
    "mars":3,
    "avril":4,
    "mai":5,
    "juin":6,
    "juillet":7,
    "aout":8,
    "septembre":9,
    "octobre":10,
    "novembre":11,
    "decembre":12
}

def charger_station(fichier):

    data = np.genfromtxt(
        fichier,
        delimiter=',',
        dtype=str,
        skip_header=1
    )

    mois = np.array([mois_dict[m.lower()] for m in data[:,1]])

    matrice = np.column_stack((
        data[:,0].astype(float),
        mois.astype(float),
        data[:,2:].astype(float)
    ))

    return matrice


stations = {
    "Rabat": charger_station("rabat.csv"),
    "Casa": charger_station("casa.csv"),
    "Marrakech": charger_station("marrakech.csv"),
    "Fes": charger_station("fes.csv")
}


for nom, data in stations.items():

    print("Station :", nom)

    """a"""
    print("Forme :", data.shape)

    """b"""
    print("Nombre observations :", data.shape[0])

    """c"""
    print("Valeurs manquantes :", np.isnan(data).sum())

    """d"""
    print("Années :", np.unique(data[:,0]))

    """e"""
    print("Mois :", np.unique(data[:,1]))


rabat = stations["Rabat"]

"""a"""
data_2024 = rabat[rabat[:,0] == 2024]

"""b"""
janvier_2024 = rabat[
    (rabat[:,0] == 2024) &
    (rabat[:,1] == 1)
]

"""c"""
temp_janvier = janvier_2024[:,3]
print(temp_janvier)

"""d"""
prec_2024 = data_2024[:,5]
print(prec_2024)


annee_data = rabat[rabat[:,0] == 2024]

"""a"""
print("Température moyenne en 2024 :",
      np.nanmean(annee_data[:,3]))

"""b"""
print("Humidité moyenne en 2024 :",
      np.nanmean(annee_data[:,4]))

"""c"""
print("Précipitations totales en 2024 :",
      np.nansum(annee_data[:,5]))

"""d"""
print("Vent moyen en 2024 :",
      np.nanmean(annee_data[:,6]))

"""e"""
print("Pression moyenne en 2024 :",
      np.nanmean(annee_data[:,7]))

"""f"""
print("Score moyen en 2024 :",
      np.nanmean(annee_data[:,9]))


def moyennes_mensuelles(nom_station, annee):

    data = stations[nom_station]

    data = data[data[:,0] == annee]

    resultat = []

    for mois in range(1,13):

        d = data[data[:,1] == mois]

        moyennes = [
            np.nanmean(d[:,3]),
            np.nanmean(d[:,4]),
            np.nanmean(d[:,5]),
            np.nanmean(d[:,6]),
            np.nanmean(d[:,7]),
            np.nanmean(d[:,8])
        ]

        resultat.append(moyennes)

    return np.array(resultat)


M = moyennes_mensuelles("Rabat", 2024)

M_norm = (
    (M - np.nanmin(M, axis=0)) /
    (np.nanmax(M, axis=0) - np.nanmin(M, axis=0))
)

mois = np.arange(1,13)

plt.plot(mois, M_norm[:,0], label="Température")
plt.plot(mois, M_norm[:,1], label="Humidité")
plt.plot(mois, M_norm[:,2], label="Précipitations")
plt.plot(mois, M_norm[:,3], label="Vent")

plt.xlabel("Mois")
plt.ylabel("Valeurs normalisées")

plt.title("Evolution mensuelle-Rabat 2024")

plt.legend()

plt.show()


X = rabat[:, [3,4,5]]

X = X[~np.isnan(X).any(axis=1)]

corr = np.corrcoef(X.T)

print(corr)

plt.scatter(X[:,0], X[:,1])

plt.xlabel("Température")
plt.ylabel("Humidité")

plt.title("Température/Humidité")

plt.show()