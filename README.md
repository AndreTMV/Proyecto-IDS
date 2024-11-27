# **Guía de pasos para la práctica con Git**

Sigue estos pasos para trabajar de manera colaborativa con Git y gestionar las ramas correctamente.

---

## **1. Clonar el repositorio**

Descarga el repositorio en tu máquina local con el comando:

git clone <URL-del-repo>

---

## **2. Crear y cambiar de rama**

Crea una nueva rama y cámbiate a ella en un solo paso:

git checkout -b <nombre-de-la-rama>

---

## **3. Verificar las ramas disponibles**

Lista todas las ramas disponibles y verifica en cuál estás trabajando:

git branch

La rama activa estará marcada con un asterisco `*`.

---

## **4. Subir la rama al repositorio remoto**

Envía tu rama recién creada al repositorio remoto para compartirla:

git push -u origin <nombre-de-la-rama>

---

## **5. Añadir archivos, hacer un commit y subir cambios**

Realiza cambios en tu rama y sigue estos pasos para guardarlos y enviarlos al repositorio remoto:

1. Añade los archivos al área de preparación:
   git add .

2. Haz un commit con un mensaje descriptivo:
   git commit -m "mensaje del commit"

3. Envía los cambios a tu rama remota:
   git push -u origin <nombre-de-la-rama>

---

## **6. Fusionar las ramas con `main`**

Cuando los cambios estén listos, fusiona tu rama con la rama principal (`main`):

1. Cambia a la rama `main`:
   git checkout main

2. Fusiona la rama en `main`:
   git merge <nombre-de-la-rama>

---

### **Notas importantes**

- Recuerda resolver cualquier conflicto que pueda surgir durante el merge.
- Después de hacer el merge, considera eliminar las ramas que ya no necesites con:
  git branch -d <nombre-de-la-rama>
