import numpy as np
import matplotlib.pyplot as plt

temperatures = np.array([
    12, 14, 15, 13, 16, 18, 20,
    21, 19, 17, 16, 18, 22, 24,
    25, 27, 29, 30, 28, 26, 24,
    23, 21, np.nan, 20, 19, 18, 17
])

print("Type :", type(temperatures))
print("Dimension :", temperatures.ndim)
print("Forme :", temperatures.shape)
print("Taille :", temperatures.size)
print("Type des éléments :", temperatures.dtype)


"""a"""
print("Première température :", temperatures[0])
print("Dernière température :", temperatures[-1])
"""b"""
print(temperatures[0:7])
"""c"""
print(temperatures[0:14])
"""d"""
print(temperatures[temperatures>25])
"""e"""
indices=np.where((temperatures>=18)&(temperatures<=28))
print(indices)
print(temperatures[(temperatures>=18)&(temperatures<=28)])


print("Moyenne:", np.nanmean(temperatures))
print("Minimum:",np.nanmin(temperatures))
print("Maximum:",np.nanmax(temperatures))
print("Médiane:",np.nanmedian(temperatures))
print("Écart-type:",np.nanstd(temperatures))

"""a"""
t_min=np.nanmin(temperatures)
t_max=np.nanmax(temperatures)
temp_minmax=(temperatures-t_min)/(t_max-t_min)
print("Températures normalisées (min-max):",temp_minmax)
"""b"""
moyenne=np.nanmean(temperatures)
ecarttype=np.nanstd(temperatures)
temp_zscore=(temperatures-moyenne)/ecarttype
print(temp_zscore)

T=temperatures.reshape(4,7)
print(T)


"""a"""
print("La première semaine :",T[0])
"""b"""
print("Le troisième jour :",T[:, 2])
"""c"""
print("Température moyenne par semaine :",np.nanmean(T,axis=1))
"""d"""
print("Température moyenne par jour :",np.nanmean(T,axis=0))
"""e"""
print("Température maximale par semaine :",np.nanmax(T, axis=1))
humidite = np.array([
    75, 72, 70, 73, 68, 65, 60,
    58, 62, 66, 70, 67, 61, 59,
    55, 52, 48, 45, 50, 53, 57,
    60, 63, 66, np.nan, 70, 72, 74
])

precipitations = np.array([
    2.5, 0.0, 1.2, 3.1, 0.0, 0.0, 0.5,
    0.0, 1.8, 2.0, 0.0, 0.0, 0.3, 0.0,
    0.0, 0.0, 0.0, 0.0, 1.1, 2.4, 0.0,
    0.0, 0.7, np.nan, 3.0, 1.5, 0.0, 0.0
])

"""a"""
data=np.column_stack((temperatures,humidite,precipitations))
print(data)
"""b"""
data_clean=data[~np.isnan(data).any(axis=1)]
print(data_clean)
"""c"""
corr=np.corrcoef(data_clean.T)
print(corr)
"""d"""
plt.scatter(data_clean[:,0],data_clean[:,1])
plt.xlabel("Température")
plt.ylabel("Humidité")
plt.title("Nuage de points : Température vs Humidité")
plt.show()