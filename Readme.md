# Reconocimiento Facial

Mediante el uso de un script almacenamiento.py realizaremos la captura de rostros que nos interesa, con otro script realizaremos el entrenamientos y finalmente el reconocimiento facial.

OPENCV tiene 3 metodos incorporados para realizar reconocimiento facial, y porque #Python podemos usar cualquiera de ellos solo cambiando una linea de codigo. Aqui los 3 metodos y como llamarlos:

EigenFaces – cv2.face.EigenFaceRecognizer_create()
FisherFaces – cv2.face.FisherFaceRecognizer_create()
Local Binary Patterns Histograms (LBPH) – cv2.face.LBPHFaceRecognizer_create()
Cada uno resalta componentes principales diferentes, es cuestion de elegir el adecuado de acuerdo a las necesidades de cada proyecto.

En este proyecto usaremos el EigenFaces	
		
1. Como usar la herramienta
Para empezar deberemos instalar OpenCV junto con todas sus dependencias ⚠ Numpy y contrib son importantes ⚠

pip install opencv-contrib-python

2. Almacenamiento (AlmacenamientoRostro.py)

Para realizar el reconocimiento facial necesitaremos de los rostros de las personas que deseemos reconocer. Estos rostros lo obtendremos de un video ya que se muestra variedad de expresiones como: felicidad, tristeza, aburrimiento, sorpresa, entre otros, y posteriormente guardamos las fotos de entrenamiento. la ruta donde se guarda las fotos son:

carpeta_de_proyecto\Data\

El primero de ellos es simple: busca una cara, toma una foto de ella y la guarda en la carpeta correspondiente.

python capture.py nombrePersona

⚠Ten en cuenta que el nombre de la persona es el mismo que pusiste en el nombre de su carpeta.

👌Por default el script toma 300 fotos del rostro, pero recuerda que entre mayor sea el entrenamiento mejores reultados se obtendran.

☝Trata de que solo una parsona aparezca en la escena para no guardar otros rostros con la misma etiqueta o nombre.

3. Entrenamiento (EntrenandoRF.py)

El método que se usará para el reconocimiento de rostros es el eigenfaces. El término "eigen" se refiere a un conjunto de vectores propios. La principal virtud de este método es que se puede representar un conjunto de imágenes utilizando una base formada de imágenes "eigen" cuya dimensión es mucho más pequeña que el conjunto original.

Antes de proceder con el entrenamiento es necesario tener cada una de las imágenes con una etiqueta asociada a la persona a la que pertenecen los rostros. 

4. Reconocimiento (ReconocimientoFacial.py)

Para comenzar a detectar y reconocer caras usaremos el modelo obtenido durante el entrenamiento, abriremos un video y el script se hará cargo de identificar el rostro y poner un recuadro.

5. Video de funcionamiento



























Clona el repositorio a tu máquina:
bash
git clone <URL_de_tu_repositorio>
Navega a la carpeta del repositorio clonado en tu terminal.
Añade tus archivos al área de "staging" (preparación):
bash
git add . # (el punto añade todos los archivos)
Confirma los cambios con un mensaje descriptivo:
bash
git commit -m "Mensaje descriptivo de los cambios"
Sube los cambios a GitHub:
bash
git push origin main # o la rama que estés usando (ej: master)
