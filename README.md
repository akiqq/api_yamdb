### Описание проекта
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории:«Книги», «Фильмы», «Музыка». Список категорий может быть расширен (например, можно добавить категорию «Картины» или «Ювелирные изделия»). Произведению может быть присвоен жанр из списка предустановленных (например, «Легенда», «Поп» или «Триллер»). Администратор может добавлять произведения, категории и жанры. 
Пользователи оставляют к произведениям отзывы и ставят произведению оценку в диапазоне от 1 до 10; из пользовательских оценок формируется рейтинг. Пользователь может оставить только один отзыв на одно произведение. Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

### Используемый стек:
Python 3.10, Django 3.2, DRF 3.12, JWT, DJOSER, SQLite
### Как запустить проект:
Скачать и установить python 3.10 с сайта https://www.python.org/.

Зарегистрируйтесь на GitHub, при регистрации укажите имя пользователя, адрес электронной почты и придумайте пароль. После того как вы нажмёте кнопку «Создать аккаунт», система попросит вас подтвердить электронную почту. Загляните в почтовый ящик, там будет письмо с кодом подтверждения.

Скачайте и установите GitBash.
Запустите Git Bash (если у вас Windows) или Терминал (на Linux/MacOS). Выполните команду <code>ssh-keygen</code>
Консоль попросит ввести путь к файлу, в который будут сохранены сгенерированные ключи, и одновременно предложит сохранить их в файл по умолчанию:
<code>
Enter file in which to save the key (/home/имя_пользователя/.ssh/id_rsa):
</code>
Сохраните ключи в папку по умолчанию: для этого нажмите Enter на Windows или Return на macOS.
При создании ключей система попросит придумать пароль для доступа к ключам. Когда вы будете задавать пароль, в терминале ничего не отобразится, даже звёздочки.
Рисунок в окне терминала будет свидетельствовать, что ключи успешно созданы:
![](https://pictures.s3.yandex.net/resources/S0_8_1667171287.png)

Теперь необходимо сохранить открытый ключ в вашем аккаунте на GitHub. 
Выведите ключ в терминал командой:
<code> cat .ssh/id_rsa.pub </code>

Cкопируйте ключ от символов ssh-rsa , включительно, и до конца:

![](https://pictures.s3.yandex.net/resources/S0_9_1667171307.png)

Зайдите в свой аккаунт на GitHub, перейдите в раздел настроек.

Выберите пункт SSH and GPG keys; для создания нового ключа нажмите на кнопку New SSH key в правом верхнему углу.

Откроется страница с двумя полями ввода:
Title (заголовок ключа). Когда будете задавать заголовок, учитывайте, что в дальнейшем вы, возможно, добавите и другие ключи. Например, с другого своего компьютера, чтобы получить с него доступ к репозиториям на GitHub. Поэтому выбирайте для каждого ключа уникальные заголовки, например ключ с домашнего компьютера можно назвать HomePC, а с рабочего — WorkPC.
Key (ключ). Сюда необходимо вставить скопированный из терминала ключ.

Нажмите кнопку Add SSH key — ключ добавится к вашему аккаунту. Если вы захотите получить SSH-доступ к своему аккаунту на GitHub с нескольких компьютеров, для каждого из них должен быть создан и добавлен свой SSH-ключ.

Место, где хранится и обновляется код проекта, чаще всего в виде файлов, называют репозито́рием.

### Клонировать репозиторий и перейти в него в командной строке:
Напечатайте в терминале команду git clone, после неё поставьте пробел, вставьте скопированный адрес и выполните команду:

<code>git clone git@github.com:akiqq/api_yamdb.git</code>

### Cоздать и активировать виртуальное окружение:

python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
### Установить зависимости из файла requirements.txt:

pip install -r requirements.txt
### Выполнить миграции:

python3 manage.py migrate
### Запустить проект:

python3 manage.py runserver

### Примеры запросов:

<br>POST http://127.0.0.1:8000/api/v1/auth/signup/
<pre><code>
{
  "email": "user@example.com",
  "username": "string"
}
</code></pre>

Пример ответа.
<pre><code>
{
  "username": "string",
  "confirmation_code": "string"
}
</code></pre>

<br>POST http://127.0.0.1:8000/api/v1/auth/token/
Получаем токен.
<pre><code>
{
  "username": "string",
  "confirmation_code": "string"
}
</code></pre>

Пример ответа.
<pre><code>
{
  "token": "string"
}
</code></pre>

GET http://127.0.0.1:8000/api/v1/categories/<br>
<pre><code>
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "name": "string",
      "slug": "string"
    }
  ]
}
</code></pre>

POST http://127.0.0.1:8000/api/v1/categories/ 
<pre><code>
{
"username": "string",
"password": "string"
}
</code></pre>

PATCH http://127.0.0.1:8000/api/v1/titles/{titles_id}/
<pre><code>
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
</code></pre>

Пример ответа: 
<pre><code>
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
</code></pre>

DELETE http://127.0.0.1:8000/api/v1/titles/{titles_id}/

GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
<pre><code>
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "text": "string",
      "author": "string",
      "score": 1,
      "pub_date": "2019-08-24T14:15:22Z"
    }
  ]
}
</code></pre>

POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/

<pre><code>
{
  "text": "string",
  "score": 1
}
</code></pre>

Пример ответа.
<pre><code>
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
</code></pre>

GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
<pre><code>
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
</code></pre>

POST http://127.0.0.1:8000/api/v1/users/
<pre><code>
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
</code></pre>

Пример ответа.
<pre><code>
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
</code></pre>
Авторы: <br>[Александр](https://github.com/akiqq) - Тимлид 
<br>[Дмитрий](https://github.com/Bacepok) - Разработчик 
<br>[Владимир](https://github.com/v-mcsimoff) - Разработчик
