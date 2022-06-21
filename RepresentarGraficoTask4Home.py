import matplotlib.pyplot as plt
import numpy as np

# np.random.seed(19680801)

plt.rcdefaults()
fig, ax = plt.subplots()

# Datos de ejemplo
people = ('User1', 'User2', 'User3', 'User4', 'User5')
y_pos = np.arange(len(people))

# TESTING number random por cada objeto del array
print(3 + 10 * np.random.rand(len(people)))

# Inserta un numero random por cada usuario
performance = 3 + 10 * np.random.rand(len(people))

error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # invierte los datos que se muestran para que empieze en el 1
ax.set_xlabel('Inicios de sesión')
ax.set_title('Usuarios logueados hoy')
plt.show()
