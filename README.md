# Социальная сеть YaTube
### Описание 
_API для проекта YaTube._
### Технологии 
Python **3.7**
Django **2.2.16**
djangorestframework **3.12.4**
djangorestframework-simplejwt **4.7.2**
Pillow **8.3.1**
PyJWT **2.1.0**
djoser **2.1.0**
requests **2.26.0**

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:kotbarbarossa/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/bin/activate
```

Обновить pip:

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Автор 
**Эльдар Барбаросса**