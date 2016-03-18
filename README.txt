------------------------------------------------------------------------------------------------
Первая задача.
1) Установите Web-сервер nginx

2) В директории /home/box (домашняя директория) создайте следующую структуру директорий

/home/box/web
          |---public
          |   |---img
          |   |---css
          |   |---js
          |---uploads
          |---etc

3) Настройте nginx так что бы:

    Все URL, начинающиеся с /uploads/  (например /uploads/1.jpeg) отдавались из директории /home/box/web/uploads
    Все URL с расширением (например /img/1.jpeg) отдавались из директории /home/box/web/public
    Все URL без расширения (например /question/123)  возвращали HTTP 404

4) Фрагмент конфига nginx который обслуживает ваш проект должен находиться в файле /home/box/web/etc/nginx.conf и должен быть включен в основной конфиг с помощью символической ссылки.

5) Запустите nginx, так что бы он принимал запросы на порту 80 и обслуживал бы любые домены.

6) Не забудьте закомитить и сохранить на github полученную структуру директорий и конфиги.
------------------------------------------------------------------------------------------------
Вторая задача
				Запуск WSGI приложений

1) Разверните репозиторий со своим проектом в директориию /home/box/web

2) Создайте WSGI приложение в файле /home/box/web/hello.py

WSGI приложение должно возвращать документ с MIME-типом text/plain, содержащий все GET параметры, по одному на каждую строку.

Например при запросе  /?a=1&a=2&b=3 приложение должно вернуть такой текст

a=1
a=2
b=3

3) Настройте Gunicorn таким образом, что бы он запускал приложение  /home/box/web/hello.py , и принимал соединения на IP адресе 0.0.0.0 на порту 8080 .  (Использования IP = 0.0.0.0 необходимо для тестирования). Конфиг разместить в файле /home/box/etc/hello.py и подключите его с помощью символической ссылки /etc/gunicorn.d/hello.py

4) Настройте nginx так что бы location /hello/ проксировался на cервер Guincorn

Таким образом, WSGI приложение должно быть доступно по URL

    http://127.0.0.1/hello/
    http://127.0.0.1:8080/

------------------------------------------------------------------------------------------------
Создание Django приложения

1) Разверните репозиторий со своим проектом в директориию /home/box/web

2) В директории /home/box/web  с помощью утилиты django-admin.py создайте новый Django-проект с названием ask

3) Внутри директории проекта создайте приложени с название qa  (questions and answers)

C учетом директорий созданных на предыдущих задания, должна получится следующая структура директорий.

.
├── ask
│   ├── ask
│   ├── manage.py
│   └── qa
├── etc
├── public
└── uploads

4) В файле ask/qa/views.py создайте тестовый контроллер со следующим содержимым:

from django.http import HttpResponse 
def test(request, *args, **kwargs):
    return HttpResponse('OK')

5) Добавьте в urls.py  маршрут для следующих URL

/
/login/
/signup/
/question/<123>/    # вместо <123> - произвольный ID
/ask/
/popular/
/new/

6) Настройте Gunicorn таким образом, что бы он запускал ваше Django-приложение по адресу 0.0.0.0:8000 . (старый hello-world скрипт останется работать на порту 8080).  Nginx должен проксировать запросы как в предыдущем задании.

В результате ваше Django приложение должно отдавать по URL вида http://127.0.0.1/question/<123>/  страницы с кодом 200.  Содержимое страницы не имеет значение - главное, что был хотя бы 1 символ. По другим URL ваше приложение должно возвращать код HTTP 404.
-------------------------------------------------------------------------------------------------------------
Создание моделей в Django приложении

1) Разверните репозиторий со своим проектом в директорию /home/box

2) Создайте базу данных в MySQL для своего проекта. В установленном MySQL заведен пользователь с именем root и без пароля. Таким образом для создания создания пользователя и базы данных вы можете выполнять команды таким образом

mysql -uroot -e "create database ..."

Подробнее про создание пользователей и баз данных в MySQL можно прочитать тут:

    http://dev.mysql.com/doc/refman/5.5/en/create-database.html
    http://dev.mysql.com/doc/refman/5.5/en/create-user.html
    http://dev.mysql.com/doc/refman/5.5/en/grant.html

Т.к. база понадобится нам в последующих заданиях - сохраните все введенные команды в отдельном файле, что бы потом вы могли легко их повторить.

3) В вашем приложении qa  в файле models.py определите следующие модели обладающие следующими полями (названия моделей и полей важны!)

Question - вопрос
title - заголовок вопроса
text - полный текст вопроса
added_at - дата добавления вопроса
rating - рейтинг вопроса (число)
author - автор вопроса
likes - список пользователей, поставивших "лайк"

Answer - ответ
text - текст ответа
added_at - дата добавления ответа
question - вопрос, к которому относится ответ
author - автор ответа

В качестве модели пользователя - используйте django.contrib.auth.models.User  из стандартной системы авторизации Django.

4) С помощью команды manage.py syncdb  создайте необходимые таблицы для ваших моделей
----------------------------------------------------------------------------------------
Отображение данных

1) Разверните репозиторий со своим проектом в директориию /home/box

2) Создайте view для обработки следующих страниц

URL = /?page=2

Главная страница. Список "новых" вопросов. Т.е. последний заданный вопрос - первый в списке. На этой странице должна работать пагинация. Номер страницы указывается в GET параметре page.  На страницу выводится по 10 вопросов. В списке вопросов должны выводится заголовки (title) вопросов и ссылки на страницы отдельных вопросов.

URL = /popular/?page=3

Cписок "популярных" вопросов. Сортировка по убыванию поля rating. На этой странице должна работать пагинация. Номер страницы указывается в GET параметре page.  На страницу выводится по 10 вопросов. В списке вопросов должны выводится заголовки (title) вопросов и ссылки на страницы отдельных вопросов.

URL = /question/5/

Страница одного вопроса. На этой странице должны выводится заголовок (title), текст (text) вопроса и все ответы на данный вопрос, без пагинации.  В случае неправильного id вопроса view должна возвращать 404.

3) Создайте простейшие шаблоны для отображения данных этих страниц.
----------------------------------------------------------------------------------------------------
Обработка форм

1) Разверните репозиторий со своим проектом в директориию /home/box

2) В файле qa/forms.py  создайте следующие формы для добавления вопроса и ответа.

AskForm - форма добавления вопроса
title - поле заголовка
text - поле текста вопроса

AnswerForm - форма добавления ответа
text - поле текста ответа
question - поле для связи с вопросом

Имена классов форм и полей важны! Конструкторы форм должны получать стандартные для Django-форм аргументы, т.е. должна быть возможность создать объект формы как AskForm() или AnswerForm(). На данном этапе формы могут не учитывать авторизацию пользователей, т.е. создавать вопросы и ответы с произвольным либо пустым автором. В формах реализуйте необходимые методы для валидации и сохранения данных (clean и save)

3) Создайте view и шаблоны для отображения и сохранения форм

URL = /ask/

При GET запросе - отображается форма AskForm, при POST запросе форма должна создавать новый вопрос и перенаправлять на страницу вопроса - /question/123/

URL = /question/123/

При GET запросе должна отображаться страница ответа и на ней AnswerForm

URL = /answer/

При POST запросе форма AnswerForm добавляет новый ответ и перенаправляет на страницу вопроса /question/123/

Для поддержки CSRF защиты - выведите в шаблонах форм {% csrf_token %}.

import os                                                                       
import unittest                                                                 
import sys                                                                      
sys.path.append('/home/box/web/ask')                                            
os.environ['DJANGO_SETTINGS_MODULE'] = 'ask.settings'                           
                                                                                
from django import forms

class TestImport(unittest.TestCase):                                            
    def test_import(self):                                                      
        import qa.forms

class TestAskForm(unittest.TestCase):                                           
    def test_from(self):                                                        
        from qa.forms import AskForm                                            
        assert issubclass(AskForm, (forms.Form, forms.ModelForm)), "AskForm does
 not inherits from Form or ModelForm"                                           
        f = AskForm()                                                           
        title = f.fields.get('title')                                           
        assert title is not None, "AskForm does not have title field"           
        assert isinstance(title, forms.CharField), "title field is not an instan
ce of forms.CharField"                                                          
        text = f.fields.get('text')                                             
        assert text is not None, "AskForm does not have text field"             
        assert isinstance(text, forms.CharField), "text field is not an instance
 of forms.CharField"

 class TestAnswerForm(unittest.TestCase):                                        
    def test_from(self):                                                        
        from qa.forms import AnswerForm                                         
        assert issubclass(AnswerForm, (forms.Form, forms.ModelForm)), "AnswerFor
m does not inherits from Form or ModelForm"                                     
        f = AnswerForm()                                                        
        text = f.fields.get('text')                                             
        assert text is not None, "AnswerForm does not have text field"          
        assert isinstance(text, forms.CharField), "text field is not an instance
 of forms.CharField"                                                            
        question = f.fields.get('question')                                     
        assert question is not None, "AnswerForm does not have question field"  
        assert isinstance(question, (forms.IntegerField, forms.ChoiceField)), "a
uthor field is not an instalce of IntegerField or ChoiceField"                  
                                                                                
suite = unittest.TestLoader().loadTestsFromTestCase(globals().get(sys.argv[1])) 
unittest.TextTestRunner(verbosity=0).run(suite)