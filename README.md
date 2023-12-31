# google_drive_api
Приложение создаёт на Google Disc файл в формате txt с указанным содержимым

### Как установить

#### Скачать 

Python3.11 должен быть уже установлен.
[Скачать](https://github.com/qqJonni/google_drive_api.git) этот репозиторий себе на компьютер.

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)
для изоляции проекта.

#### Быстрая настройка venv

Начиная с Python версии 3.3 виртуальное окружение идёт в комплекте в виде модуля
venv. Чтобы его установить и активировать нужно выполнить следующие действия в
командной строке:  

Указать скачанный репозиторий в качестве каталога.
```sh
cd C:\Users\ваш_пользователь\Downloads\папка_репозитория
```
Установить виртуальное окружение в выбранном каталоге.
```sh
Python -m venv env
```
В репозитории появится папка виртуального окружения env  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/Hn4C6PD/image.png" alt="image" border="0"></a>

Активировать виртуальное окружение.
```sh
env\scripts\activate
```
для MacOS:
```sh
env/bin/activate
```
Если всё сделано правильно, вы увидите в командной строке (env) слева от пути 
каталога.  
#### Установить зависимости

Используйте `pip` (или `pip3`, есть конфликт с Python2) для установки 
зависимостей:

```sh
pip install -r requirements.txt
```
Так-же необходимо получить api токен на Google Cloud https://console.cloud.google.com/

Запуск программы выполняется командой:
```sh
python manage.py runserver
```