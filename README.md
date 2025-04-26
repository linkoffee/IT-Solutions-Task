# IT-Solutions-Task
`Веб-сервис для управления движением денежных средств (ДДС)`

### Инструкция по установке:
1. Склонируйте репозиторий
```console
git clone https://github.com/linkoffee/IT-Solutions-Task.git
cd IT-Solutions-Task
```
2. Создайте виртуальное окружение
```console
py -3.11 -m venv venv
source venv/bin/activate      # Для Linux/MacOS
source venv\Scripts\activate  # Для Windows 
```
3. Установите зависимости
```console
pip install -r requirements.txt
```
4. Примените БД миграции:
```console
python manage.py migrate
```
5. Создайте суперпользователя (администратора):
```console
python manage.py createsuperuser
```
(Введите имя пользователя, email и пароль при запросе)

6. Запустите сервер локально:
```console
python manage.py runserver
```
После этого веб-приложение будет доступно по адресам: http://localhost:8000/ или http://127.0.0.1:8000/ \
Админ панель веб-приложения будет доступна по адресам: http://localhost:8000/admin/ или http://127.0.0.1:8000/admin/

### Превью:

![](https://habrastorage.org/webt/ia/rb/pz/iarbpzegxfsgmcs8h2aqrpbywxc.png)
![](https://habrastorage.org/webt/ec/bh/tk/ecbhtkbfwx5plf9fqwibjtfscue.png)

---

Автор: [Михаил Копочинский](https://github.com/linkoffee)
