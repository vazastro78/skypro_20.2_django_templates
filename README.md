# 20.2 Шаблонизация в Django - Домашняя работа

Ключевые слова:
- 20.2 Шаблонизация в Django
- skypro_python41.0
- Урок 20.2
- шаблоны
- templates
- django
- шаблонный фильтр
- шаблонный тег

### Критерии выполнения заданий
- [x] задание 1
- [x] задание 2
- [x] задание 3
- [x] задание 4

### Задание 1
Задание 1

- Создайте новый контроллер и шаблон, которые будут отвечать за отображение отдельной страницы с товаром, на которой необходимо вывести всю информацию о самом товаре.

Примечание: Для создания шаблонов лучше использовать UI kit Bootstrap, при возникновении проблем можно брать за основу данный шаблон.

>commit: d108303816e9fcb9f88910856a106c83387eaf14
> 
>Шаблоны20.2 Задание1 Добавлены контроллер и шаблон главной страницы на основе bootstrap

### Задание 2
В созданный ранее шаблон для главной страницы выведите список товаров в цикле. Для единообразия выводимых карточек отображаемое описание необходимо обрезать после первых выведенных 100 символов.

>commit: f3ea10568bf595161f355242818117561a0e420e
> 
>Шаблоны20.2 Задание2 список товаров на главной странице в цикле

### Задание 3
Из-за расширения количества шаблонов появляется слишком много повторяющегося кода, поэтому выделите общий (базовый) шаблон, а также подшаблон с главным меню.

В подшаблон вынесите общие для всех кодовые части (HTML-код). Не забудьте разместить блок с контентом, куда будут вставляться шаблоны, которые используют подшаблон:
{% block content %}
{% endblock %}
И подключите их к другим шаблонам с помощью
{% extends 'путь к базовому шаблону' %}
Код расширенного шаблона разместите внутри блока с контентом.

Примечание: При необходимости можно выделить больше общих шаблонов.

>commit: 658a9c28dc0ab51eddc90e1b22716223ad769531
> 
>Шаблоны20.2 Задание3 Разделить базовый шаблон и подшаблоны

### Задание 4

Для выводимого изображения на странице реализуйте шаблонный фильтр или шаблонный тег, который преобразует переданный путь в полный путь для доступа к медиафайлу.

  - создан тег get_media_prefix
  - создан фильтр mediapath

>commit: d0ae18ebdea8bc472e7c9f7aba98d32dd681f93b
> 
>Шаблоны20.2 Задание4 Создан шаблонный фильтр mediapath или шаблонный тег get_media_prefix 

#### github
create repository on github and synchronize with offline repository

git remote add origin git@github.com:vazastro78/skypro_20.2_django_templates.git 
git branch -M main
git push -u origin main
