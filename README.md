# Stepik-POM

Выполнено в vs studio code

Драйвер браузера указать в переменную path ОС, например:

```c:/chromediver```

Используя терминал:
venv
Создать venv python -m venv <Имя окружения, например venv>
.\<Имя окружения, например venv>\Scripts\activate ```Переключиться на venv и активировать скрипт```

Обновляем pip после подключения к venv
```pip install --update pip```

Установка зависимостей:
```pip install -r requirements.txt```

используя команду ```pytest -v --language (по выбору)``` в терминале стартануть все тесты. Либо pytest <Имя_теста.py>

Так же командой стартануть тесты, которые помечены тегом "need_review":

```pytest -v --tb=line --language=en -m need_review```

Тесты заведомо failed помечены @pytest.mark.xfail отобразятся в прогоне.

УДАЧИ ВАМ В РЕВЬЮ И ПЕРЕРАСТИТЕ В SOFTWARE PYTHON DEVELOPER!
