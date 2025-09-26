### Описание проекта

### Разворачивание
#### Пуллим проект
```shell
git init
```
```shell
git remote add origin https://github.com/Asenim/cloude-file-storage.git
```
```shell
git pull 
```
Или
```shell
git pull origin master
```
#### Установка зависимостей
##### Через pip
##### Через poetry
#### Получение SECRET_KEY

### Хранение файлов
Если вам важно сохранить файлы не в контейнере, а у себя (даже после удаления контейнера)
Пропишите 
```yaml
services:
  postgres:
    volumes:
      ./pg_data:/var/lib/postgresql/data
    
  minio:
    volumes:
      - ./data:/data
```

### Как поднять dev db
```shell
docker-compose -f docker-compose.dev.yaml up
```
#### Применяем миграции
```shell
python manage.py makemigrations
```
```shell
python manage.py migrate
```

### Запуск приложения
```shell
python manage.py runserver
```
