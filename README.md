# Kiryshka Clickers

## Описание

Clickers Hub — это скрипт на Python для автоматизации кликов в приложении Telegram Desktop, предназначенный для игры в Crypto Clickers. Скрипт автоматически нажимает на кнопку "Play" и ищет определенные цвета на экране для выполнения кликов.

## Установка

Для начала работы с этим скриптом, выполните следующие шаги:

1. **Установите Python**: Убедитесь, что у вас установлен Python версии 3.6 или выше. Скачайте и установите Python с [официального сайта](https://www.python.org/downloads/).

2. **Установите зависимости**: Запустите следующую команду для установки необходимых библиотек Python:
   
   ```bash
   pip install pyautogui pygetwindow keyboard pynput colorama
   ```

## Запуск скрипта

1. **Откройте Telegram Desktop**: Запустите приложение Telegram Desktop и убедитесь, что оно находится в активном окне.

2. **Запустите скрипт**: Сохраните скрипт в файл, например, `crypto_clickers.py`, и запустите его с помощью следующей команды:

   ```bash
   python crypto_clickers.py
   ```

3. **Следуйте инструкциям на экране**: Скрипт предложит ввести название окна и количество игр, которые вы хотите сыграть. Например:

   ```plaintext
   [⚡️] |Kiryshka Clickers| Нажми 1 
   ```
   
   Введите `1`, если ваше окно называется `TelegramDesktop`. Введите количество игр, которые вы хотите сыграть.

4. **Управление скриптом**: Вы можете приостановить и возобновить работу скрипта, нажав клавишу `q`.

## Использование

1. **Запуск игры**: Скрипт автоматически нажимает на кнопку "Play" в приложении Telegram Desktop.

2. **Поиск и клик по бактериям**: Скрипт ищет на экране бактерии, основываясь на их цвете, и кликает по ним.

3. **Пауза и возобновление**: Нажмите `q`, чтобы приостановить или возобновить выполнение скрипта.

## Примечания

- Убедитесь, что окно Telegram Desktop открыто и видимо для скрипта, чтобы он мог правильно определить его координаты.
- Скрипт рассчитан на определенные цветовые диапазоны, которые могут изменяться в зависимости от темной или светлой темы в Telegram.
