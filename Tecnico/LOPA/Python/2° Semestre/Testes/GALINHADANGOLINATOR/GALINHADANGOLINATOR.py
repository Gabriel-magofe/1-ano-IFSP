
import time as T
import pyautogui as a

a.FAILSAFE = True
# a.PAUSE = 0.6

largura, altura = a.size()
print(f"Resolução da tela: {largura}x{altura}")

a.press("win")
T.sleep(0.3)
a.write("edge")
a.press("enter")
T.sleep(1)
a.write("https://cptstatic.s3.amazonaws.com/imagens/enviadas/materias/materia5571/habitos-e-caracteristicas-da-galinha-da-angola-cpt.jpg")
a.press("enter")
T.sleep(0.3)
a.press("f11")


# a.hotkey("win", "r")
# a.write("cmd")
# a.moveTo(162, 988, duration=2.0)
# a.click()
# # T.sleep(0.5)
# a.moveTo(352, 266, duration=2.0)
# a.click()
# a.write("dir /s")
# a.press("enter")
# T.sleep(5)
# print(a.position())
