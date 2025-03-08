import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Função para atualizar a imagem no label
def update_image():
    ret, frame = cap.read()
    if ret:
        # Converte o frame do OpenCV para um formato que o Tkinter pode exibir
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk  # Mantém uma referência para evitar garbage collection
        label.config(image=imgtk)
    # Chama a função novamente após 10ms (para atualizar em tempo real)
    label.after(10, update_image)

# URL da câmera RTSP
rtsp_url = "rtsp://admin:123456@192.168.1.11:554/path"

# Inicializa a captura de vídeo
cap = cv2.VideoCapture(rtsp_url)

# Verifica se a câmera foi aberta corretamente
if not cap.isOpened():
    print("Erro ao abrir a câmera RTSP")
    exit()

# Cria a janela principal do Tkinter
root = tk.Tk()
root.title("Câmera de Segurança")

# Cria um label para exibir a imagem
label = tk.Label(root)
label.pack()

# Inicia a atualização da imagem
update_image()

# Inicia o loop principal do Tkinter
root.mainloop()

# Libera a câmera quando a janela é fechada
cap.release()