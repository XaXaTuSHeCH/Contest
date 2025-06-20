# Инструкция по запуску проекта

## Требования
- Python 3.9 или выше  
- pip  

## Проверьте установку командой:  
```
python --version
pip --version
```

# Склонируйте этот репозиторий и перейдите в папку с ним:
```
git clone <URL_ВАШЕГО_РЕПОЗИТОРИЯ>
cd <ИМЯ_ПАПКИ_РЕПОЗИТОРИЯ>
```
# Создайте и активируйте виртуальное окружение:
## Windows:
```
python -m venv venv
venv\Scripts\activate
```
## Linux/macOS:
```
python3 -m venv venv
source venv/bin/activate
```
# Установите зависимости:
```
pip install --upgrade pip
pip install -r requirements.txt
```
# Запуск:
## Обучение:
### перейдите в файл Train.py в data='./path/to/data.yaml' (14 строка) вставьте путь до data.yaml вашего датасета, вместо ./path/to/data.yaml
### Запустите скрипт:
```
python Train.py
```
## Валидация (на размеченных данных):
### перейдите в файл Valid.py в data='./path/to/data.yaml' (14 строка) вставьте путь до data.yaml вашего датасета, вместо ./path/to/data.yaml
### Запустите скрипт:
```
python Valid.py
```
## Тестирование (на изображениях без разметки):
### перейдите в файл Train.py в source='./path/to/images' (14 строка) вставьте путь до data.yaml вашего датасета, вместо ./path/to/images
### Запустите скрипт:
```
python Test.py
```