import tkinter.filedialog
import pygame

root = tkinter.Tk()
root.withdraw()

input('Este programa irá rodar um arquivo mp3. Para continuar, aperte enter e selecione o arquivo.')

pygame.mixer.init()
pygame.init()

file_path = tkinter.filedialog.askopenfilename()
pygame.mixer_music.load(file_path)
pygame.mixer.music.play()
input()
pygame.event.wait()