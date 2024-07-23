import pyautogui
import time
import pytesseract
from PIL import ImageGrab, Image

def locate_button(image_path, threshold=0.8):
    # Загрузка изображения кнопки
    button_image = Image.open(image_path)
    
    # Снимок экрана
    screenshot = ImageGrab.grab()
    
    # Поиск кнопки на снимке экрана
    button_location = pyautogui.locate(button_image, screenshot, confidence=threshold)
    if button_location:
        return button_location
    return None

def click_button(image_path):
    location = locate_button(image_path)
    if location:
        # Получение центра кнопки
        x, y = pyautogui.center(location)
        # Клик по кнопке
        pyautogui.click(x, y)
        return True
    return False

def get_text_from_image(image):
    # Распознавание текста на изображении
    return pytesseract.image_to_string(image)

def capture_and_process():
    # Снимок экрана
    screenshot = ImageGrab.grab()
    
    # Сохранение снимка экрана
    screenshot.save('screenshot.png')
    
    # Получение текста с снимка экрана
    text = get_text_from_image(screenshot)
    print("Текст на экране:", text)

# Основной процесс
def main():
    # Убедитесь, что установлен путь к tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    # Пример использования функций
    if click_button('path/to/play_button_image.png'):
        print("Кнопка 'Play' нажата.")
    else:
        print("Не удалось найти кнопку 'Play'.")

    # Запуск захвата и обработки изображения
    capture_and_process()

# Запуск основного процесса
if __name__ == "__main__":
    main()