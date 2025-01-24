# Урок 1: Введение в Django

## 📋 Что такое Django?

<span style="color: #3498db;">**Django**</span> — это высокоуровневый веб-фреймворк на языке Python, который позволяет быстро и эффективно разрабатывать веб-приложения. Он следует принципу <span style="color: #2ecc71;">"Don't Repeat Yourself" (DRY)</span> и <span style="color: #f39c12;">"Convention over Configuration"</span>, что делает его очень удобным для использования. Django предоставляет множество встроенных инструментов и библиотек, которые упрощают разработку, такие как ORM (Object-Relational Mapping) для работы с базами данных, система маршрутизации (URL routing), шаблонизатор для генерации HTML и встроенная админка для управления данными.

---

## 🎯 Для чего используется Django?

Django используется для создания веб-сайтов и веб-приложений. Он предоставляет множество встроенных инструментов и библиотек, которые упрощают разработку, такие как:

- <span style="color: #9b59b6;">**ORM (Object-Relational Mapping):**</span> Позволяет работать с базами данных через Python-код, абстрагируясь от SQL-запросов.
- <span style="color: #3498db;">**Система маршрутизации (URL routing):**</span> Упрощает управление URL-адресами и их сопоставление с представлениями.
- <span style="color: #2ecc71;">**Шаблонизатор:**</span> Позволяет генерировать HTML-страницы с использованием Python-кода.
- <span style="color: #f39c12;">**Встроенная админка:**</span> Предоставляет готовый интерфейс для управления данными в базе данных.

---

## 🏗️ Архитектура MTV

Django следует архитектуре <span style="color: #2ecc71;">**MTV (Model-Template-View)**</span>, которая аналогична архитектуре <span style="color: #3498db;">MVC (Model-View-Controller)</span>. Давайте разберем каждый компонент:

- <span style="color: #9b59b6;">**Model (Модель):**</span> Описывает данные и их структуру. В Django модели определяются в виде Python-классов.
- <span style="color: #3498db;">**Template (Шаблон):**</span> Отвечает за представление данных. Шаблоны в Django — это HTML-файлы с вставками Django-кода.
- <span style="color: #2ecc71;">**View (Представление):**</span> Обрабатывает запросы и возвращает ответы. Представления в Django — это Python-функции или классы.

#### Пример модели

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
```

**Объяснение:**
- <span style="color: #f39c12;">`Article`</span> — это модель, которая представляет статью.
- <span style="color: #3498db;">`title`</span> — поле для заголовка статьи, максимальная длина 200 символов.
- <span style="color: #2ecc71;">`content`</span> — поле для текста статьи.
- <span style="color: #9b59b6;">`published_date`</span> — поле для даты публикации статьи, автоматически устанавливается при создании записи.

---

## 🛠️ Создание проекта

### 1️⃣ Что такое Django проект?

Django проект — это контейнер для всех приложений и настроек, которые составляют ваше веб-приложение. Проект включает в себя конфигурационные файлы, такие как `settings.py`, `urls.py` и `wsgi.py`, а также директорию для хранения статических файлов и шаблонов.

---

### 2️⃣ Создание репозитория

1. **Создайте репозиторий на GitHub:**
   - Перейдите на GitHub и создайте новый репозиторий с именем <span style="color: #3498db;">`itg`</span>.

2. **Склонируйте репозиторий на локальную машину:**
   ```sh
   git clone https://github.com/yourusername/itg.git
   cd itg
   ```

---

### 3️⃣ Установка зависимостей

1. Создайте виртуальное окружение:
   ```sh
   python -m venv venv
   ```

2. Активируйте виртуальное окружение:
   - <span style="color: #2ecc71;">Linux/MacOS:</span>
     ```sh
     source venv/bin/activate
     ```
   - <span style="color: #f39c12;">Windows:</span>
     ```sh
     .\venv\Scripts\activate.bat
     ```

3. Установите Django:
   ```sh
   pip install django
   ```

4. Сохраните зависимости в файл `requirements.txt`:
   ```sh
   pip freeze > requirements.txt
   ```

---

### 4️⃣ Запуск проекта

1. **Запустите сервер разработки:**
   ```sh
   python manage.py runserver
   ```

2. **Остановите сервер:**
   - Используйте комбинацию клавиш <span style="color: #f39c12;">`Ctrl+C`</span>.

3. **Сделайте коммит:**
   ```sh
   git add .
   git commit -m "Запуск проекта Django"
   ```

---

## ✅ Заключение

Первый урок завершён. Мы создали проект, настроили виртуальное окружение, создали приложение и представление. В следующем уроке мы углубимся в работу с URL и шаблонами.

