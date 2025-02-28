import pyautogui
import cv2
import pygetwindow as gw
import time
import numpy as np

# Buscar a janela do mGBA
Emu = gw.getWindowsWithTitle(
    'Pokemon - Fire Red (BR) - VisualBoyAdvance-M 2.1.11')
if not Emu:
    print("Erro: Janela do mGBA não encontrada!")
    exit()
Emu = Emu[0]

# Ativar e focar na janela
Emu.activate()
time.sleep(2)  # Aumente o tempo de espera para garantir o foco

# Carregar a imagem do botão "Start"
template = cv2.imread('start.png', 0)
if template is None:
    print("Erro: Arquivo 'start.png' não foi carregado corretamente!")
    exit()

# Loop para verificar a tela continuamente
max_attempts = 100  # Número máximo de tentativas
attempt = 0

while attempt < max_attempts:
    # Captura a tela corretamente
    screenshot = pyautogui.screenshot(
        region=(Emu.left, Emu.top, Emu.width, Emu.height))
    screenshot = np.array(screenshot)

    # Converte para escala de cinza
    screenshot_cinza = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

    # Comparação com a imagem "start.png"
    result = cv2.matchTemplate(
        screenshot_cinza, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Debug para ver a precisão da detecção
    print(f"🔍 Precisão da detecção: {max_val}")

    limite = 0.6  # Teste valores entre 0.6 e 0.85

    if max_val >= limite:
        print("🎮 Botão 'Start' detectado! Pressionando Return...")
        pyautogui.keyDown('return')  # Pressiona a tecla Return
        time.sleep(0.1)  # Segura a tecla por um breve momento
        pyautogui.keyUp('return')  # Solta a tecla Return
        break
    else:
        print("⌛ Botão 'Start' NÃO detectado. Tentando novamente...")
        pyautogui.press('x')  # Pressiona a tecla X

    attempt += 1
    time.sleep(1)  # Pequeno delay antes da próxima verificação

if attempt >= max_attempts:
    print("❌ Número máximo de tentativas atingido. Encerrando o script.")
