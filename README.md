# API для проекта YaTube
## _Превосходный современный программный интерфейс практически для всех видов и типов приложений_
Данный проект представляет из себя программный интерфейс для обмена данными использущий один из самых распространённых форматов передачи данных — JSON который реализован на базе Django REST framework.

[![N|Solid](https://pictures.s3.yandex.net/resources/Untitled_1_1624618790.png)]()

В проекте реализованы такие возможности как:
* Получение, Создание, Обновление(в том числе Частичное), Удаление публикаций
* Получение, Добавление, Обновление(в том числе Частичное), Удаление комментариев
* Получение Списка сообществ и информации о каждом сообществе
* Подписки на авторов постов

Для авторизации пользователей применяется JWT-токен

Проект получил высокие оценки ревьюера.
Вот как отзывается о нем [Максим Митягин]:
> Отличная работа! Ты как обычно меня радуешь своими решениями!) Есть немного важных замечаний и рекомендаций! Доделай, плз, и возвращай на проверку! Ты молодец!)


Кроме того как говорит моя [девушка]:
> Я считаю что этот проект очень сексуален и ты сексуален когда делаешь его


### Технологии 

| Plugin | Release version |
| ------ | ------ |
| Python **3.7** | [Release Date: June 27, 2018] |
| Django **2.2.16** | [Release notes] |
| djangorestframework **3.12.4** | [3.12.4 Date: 26th March 2021] |
| djangorestframework-simplejwt **4.7.2** | [Project description] |
| Pillow **8.3.1** | [8.3.1 CONTENTS] |
| PyJWT **2.1.0** | [Docs] |
| djoser **2.1.0** | [Project description] |
| requests **2.26.0** | [Released: Jun 29, 2022] |

### Для запуска проекта необходимо:

Клонировать репозиторий и перейти в него в командной строке:

```sh
git clone git@github.com:kotbarbarossa/api_final_yatube.git
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```sh
python3 -m venv env
source venv/bin/activate
```

Обновить pip:

```sh
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```sh
pip install -r requirements.txt
```

Выполнить миграции:

```sh
python3 manage.py migrate
```

Запустить проект:
```sh
python3 manage.py runserver
```

### Тестирование прямо в браузере!
У django есть удобный встроенный интерфейс который доступен из коробки по адресу:
```sh
http://127.0.0.1:8000/api/v1/
```
С помощью него можно отправить различные типы запросов к API и получить соответствующие ответы!

> Если этот Readme был полезен не забудь поддержить подпиской на мой (не свзанный с програмированием) [youtube] канал!
Ведь это дает +50 кармы от фракции Бородатых Котов Вегетарианцев!


[![N|Solid](https://yt3.ggpht.com/T4mi6URGIZyh2G4RxRoVp6iBb9ldzwa_cpUJQ7d70UHruSO0q0Hopm8DET9ZoSvhnnbWWHHNiQ=s176-c-k-c0x00ffffff-no-rj)](https://www.youtube.com/channel/UC0NWbtRrU1YvsCP_0Slq-9A/featured)

### Автор 
**Эльдар Барбаросса**
[INSTAGRAM]


[//]: # (links)

   [Максим Митягин]: <https://github.com/mityagin>
   [девушка]: <vk.com/julia_super_fox>
   [Release Date: June 27, 2018]: https://www.python.org/downloads/release/python-370/
   [Release notes]: https://docs.djangoproject.com/en/4.0/releases/2.2.16/
   [3.12.4 Date: 26th March 2021]: https://www.django-rest-framework.org/community/release-notes/#312x-series
   [Project description]: https://pypi.org/project/djangorestframework-simplejwt/4.7.2/
   [8.3.1 CONTENTS]: https://pillow.readthedocs.io/en/stable/releasenotes/8.3.1.html
   [Docs]: https://pyjwt.readthedocs.io/en/2.1.0/
   [Project description]: https://pypi.org/project/djoser/
   [Released: Jun 29, 2022]: https://pypi.org/project/requests/
   [youtube]: https://www.youtube.com/channel/UC0NWbtRrU1YvsCP_0Slq-9A/
   [INSTAGRAM]: https://instagram.com/kot.barbarossa?igshid=YmMyMTA2M2Y=

