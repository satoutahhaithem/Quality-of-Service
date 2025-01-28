import matplotlib.pyplot as plt
import numpy as np

# Paramètres pour la partie 2
t1, t2 = 0, 10  # Temps en secondes
b1, b2 = 30, 10  # Nombre de jetons au temps t1 et t2
d = 8  # Débit constant de consommation
r = 5  # Débit de régénération

# Temps et consommation entre t1 et t2
time_2 = np.linspace(t1, t2, 500)
jetons = b1 - d * (time_2 - t1)  # Pente descendante due à la consommation

# Ajout de régénération après t2
time_fill = np.linspace(t2, t2 + (b1 - b2) / r, 200)  # Temps pour remplissage
regen_jetons = b2 + r * (time_fill - t2)  # Régénération linéaire

# Combinaison des périodes
total_time = np.concatenate((time_2, time_fill))
total_jetons = np.concatenate((jetons, regen_jetons))

# Tracé du graphique
plt.figure(figsize=(10, 6))
plt.plot(total_time, total_jetons, label="Évolution des jetons", color="blue")
plt.scatter([t1, t2], [b1, b2], color="red", label="Points de mesure (t1, t2)")
plt.axhline(b1, linestyle="--", color="green", alpha=0.7, label="Nombre initial de jetons b1")
plt.axhline(b2, linestyle="--", color="orange", alpha=0.7, label="Nombre final de jetons b2")
plt.xlabel("Temps (s)")
plt.ylabel("Nombre de jetons")
plt.title("Évolution du nombre de jetons entre t1 et t2 avec consommation (d)")
plt.legend()
plt.grid()
plt.show()
