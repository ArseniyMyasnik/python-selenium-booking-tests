# python-selenium-booking-tests

Автоматизированные UI-тесты для демонстрационного сайта **Automation In Testing**  
(<https://automationintesting.online/>) на **Python + Selenium WebDriver** c использованием **PyTest** и **Allure Report**.  
Проект построен по паттерну **Page Object Model** и предназначен для демонстрации навыков и скиллов.

---

## Стек технологий

- **Python 3.x** — язык разработки тестов
- **Selenium WebDriver 4.x** — автоматизация браузера
- **PyTest 8.x** — запуск и организация тестов
- **Allure Report 2.x** — отчёты о прохождении тестов
- **webdriver-manager 4.x** — установка драйверов для браузеров
- **Page Object Model (POM)** — архитектура тестов

## Содержание

- [Быстрый старт](#быстрый-старт)
- [Запуск тестов](#запуск-тестов)

---

## Быстрый старт

1. **Клонируйте репозиторий**

  ```bash
  git clone https://github.com/<ваш-аккаунт>/python-selenium-booking-tests.git
  cd python-selenium-booking-tests
  ```

2. **Создайте виртуальное окружение**

  ```bash
  python -m venv venv
  # Linux / macOS
  source venv/bin/activate
  # Windows
  venv\Scripts\activate
  ```

3. **Установите зависимости**

  ```bash
  pip install -r requirements.txt
  ```

## Запуск тестов

  ```bash
  pytest -vv

  # Запуск без GUI (headless режим)
  pytest -vv --headless

  # Формирование отчёта Allure (директория reports/)
  pytest -vv --alluredir=reports
  ```
