# AnimalDB

проект созданый для сети приютов для животных в виде веб-оболочки и api для управления базой данных животных.
___

## Использование

* ***Администратор онже superuser.***
  Предпологается, что имеется несколько приютов и в каждом приюте свой набор животных. Изначально приюты создаются
  администратором.

* ***Зарегистрированые пользователи.***
  Далее, каждый зарегистрированный пользователь является работником конкретного приюта и имеет право
  просматривать только животных из своего приюта. Зарегистрированые пользователи могут заводить животных в базу данных,
  просматривать конкретного животного ,редактировать и "мягко" удалять.

* ***Обычные пользователи (анонимные).***
  Могут просматривать список всех животных во всех приютах, а так же детальную информацию конкретного животного.

## Установка

1. Установка и активация виртуального окружения.
    * установка
   ```
   python3 -m venv myvenv
    ```

    * активируй виртуальное окружение
        * Linux
         ```
          source myenv/bin/activate
         ```
        * Windows
         ```
          myenv\Scripts\activate
         ```
2. Клонируем репозиторий
    ```
   https://github.com/KirillDomitin/animaldb.git
   ```
3. установи зависимости
    ```
   pip3 install -r requirements.txt
   ```
4. Создаем миграции и выполняем их

    ```
    python3 manage.py makemigrations
    ```

    ```
    python3 manage.py migrate
    ```

5. Запускаем локальный сервер
    ```
    python3 manage.py runserver
    ``` 

## Настройка

Все основные настройки файле `animaldb/settings.py`
Первым делом следует создать суперпользователя командой

 ```
 python3 manage.py createsuperuser
 ```

По умочанию подключена PostgreSQL изменить можно тут:

```python 
### animaldb/settings.py
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'animaldb',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

Так же при разворачивании проекта на сервере рекомендуется удалить строку:

```python
### animaldb/settings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',  # Отключить на боевом сервере
    ]
}
```
 
# API
___
## Получение списка всех животных из всех приютов

**GET метод**
```
/api/v1/animallist/  
```

Пример:

```
http://localhost:8000/api/v1/animallist/
```

___
## Получение информации по конкретному животному

**GET метод**
```
/api/v1/animallist/{id}/
```
Параметры:

**{id}** - уникаляный идентификатор животного

Пример:
```
http://localhost:8000/api/v1/animallist/3
```
Поля ответа:

* nickname(str) - кличка,
* age(SmallInteger) - возраст,
* weight(Decimal) - вес,
* height(PositiveSmallInteger) - рост,
* identifying_mark(Text) - особые приметы
* shelter(int) - идентификатор приюта
___

## Добавление животного в базу

**POST метод**

```
/api/v1/animallist/
```
Параметры:

**data (body)** - {
  "nickname": "string",
  "age": 0,
  "weight": 0,
  "height": 0,
  "identifying_mark": "string",
  "shelter": 0
}

Пример:

```json
{
  "nickname": "Tom",
  "age": 2,
  "weight": 3.0,
  "height": 36,
  "identifying_mark": "Особые приметы ",
  "shelter": 1
}
```
Поля ответа:

* nickname(str) - кличка,
* age(SmallInteger) - возраст,
* weight(Decimal) - вес,
* height(PositiveSmallInteger) - рост,
* identifying_mark(Text) - особые приметы
* shelter(int) - идентификатор приюта
___

## Удаление животного
Метод DELETE не удаляет животного из базы данных, а только помечает его и не отображает в веб интерфейсе


метод **DELETE**

```djangourlpath
/api/v1/animallist/{id}/
```
Параметры:

**{id}** - уникальный идентификатор животного

Пример заприоса:
```
http://localhost:8000/api/v1/animallist/3
```
Пример ответа:
```json
{
  "nickname": "Tom the cat",
  "age": 3,
  "weight": 3.0,
  "height": 35,
  "identifying_mark": "",
  "shelter": 1
}
```

___
## Внесение изменений в детальную информацию о животном

метод **PUT** / **PATCH**

```djangourlpath
/api/v1/animallist/{id}/
```
Параметры:

**{id}** - уникальный идентификатор животного

**data (body)** - {
  "nickname": "string",
  "age": 0,
  "weight": 0,
  "height": 0,
  "identifying_mark": "string",
  "shelter": 0
}

Пример body:
```json
{
  "nickname": "Tom the cat",
  "age": 3,
  "weight": 3.0,
  "height": 35,
  "identifying_mark": "",
  "shelter": 1
}
```

___
Все api методы так же доступны в 'swagger' документации по адресу:
<http://localhost:8000/api/v1/>