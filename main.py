import requests
import os

libros = [["P1LPM", "P1MLA", "P1PAA", "P1PCA", "P1PEA", "P1SDA", "P1TPA"],
          ["P2LPM", "P2MLA", "P2PAA", "P2PCA", "P2PEA", "P2SDA"],
          ["P3LPM", "P3MLA", "P3PAA", "P3PCA", "P3PEA", "P3SDA"],
          ["P0SHA", "P0CMA", "P4SDA", "P4LPM", "P4PAA", "P4PCA", "P4PEA"],
          ["P5SDA", "P5LPM", "P5PAA", "P5PCA", "P5PEA", "P5MLA"],
          ["P6SDA", "P6LPM", "P6PAA", "P6PCA", "P6PEA", "P6MLA"]]

nomCarpetas = ["1o", "2o", "3o", "4o", "5o", "6o"]


ruta = os.getcwd()


for i in range(6):

    os.chdir(ruta)
    ruta_destino = os.path.join(ruta, nomCarpetas[i])
    os.mkdir(ruta_destino)
    os.chdir(ruta_destino)

    for y in range(len(libros[i])):

        ruta_libro = os.path.join(os.getcwd(), libros[i][y])
        os.mkdir(ruta_libro)
        os.chdir(ruta_libro)

        count = 0
        seguir = True
        countNom = ""

        while seguir:
            if len(str(count)) == 1:
                countNom = "00" + str(count)
            elif len(str(count)) == 2:
                countNom = "0" + str(count)
            else:
                countNom = str(count)
            url = "https://www.conaliteg.sep.gob.mx/2023/c/" + libros[i][y] + "/" + countNom + ".jpg"
            nombre_archivo = countNom + ".jpg"
            ruta_destino = os.path.join(os.getcwd(), nombre_archivo)
            response = requests.get(url)
            if response.status_code == 200:
                with open(ruta_destino, "wb") as archivo:
                    archivo.write(response.content)
                    count += 1
                    #time.sleep(0.2) #delay por si acaso 
            else:
                os.chdir(os.path.join(ruta, nomCarpetas[i]))
                seguir = False
