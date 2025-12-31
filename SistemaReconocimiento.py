import cv2

import numpy as np
import mediapipe as mp
import os
from tkinter import *
from PIL import Image, ImageTk
import imutils
import math

# Rutas
OutFolderPathUser='DataBase/Usuarios'
PathUserCheck='DataBase/Usuarios/'
OutFolderPathFace='DataBase/Rostros'

# 
info=[]

pantalla =Tk()
pantalla.title("FACE RECOGNITION SYSTEM")

pantalla.geometry("1280x728")

pantalla.mainloop