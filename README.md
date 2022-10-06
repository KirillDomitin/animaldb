# AnimalDB

проект созданый для сети приютов для животных в виде веб-оболочки и api для управления базой данных животных.
___

## Использование
***
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
***
1. Установка и активация виртуального окружения.
    * установка
   ```
   python3 -m venv myvenv
    ```

    * активируй виртуальное окружение
    *
        * Linux
   ```
   source myenv/bin/activate
   ```
    *
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
***
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
