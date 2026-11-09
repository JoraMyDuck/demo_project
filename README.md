# demo_project

Учебный репозиторий к практической работе №1 «Жизненный цикл ПО. Работа с системой контроля версий Git».

## Содержимое

| Файл | Назначение |
|---|---|
| `hello.py` | функция `greet(name)` — возвращает приветствие, при пустом имени выбрасывает `ValueError` |
| `test_hello.py` | модульные тесты для `greet` (`unittest`) |

## Запуск

```bash
python hello.py          # Привет, Мир!
python -m unittest -v    # запуск тестов
```

## История разработки

1. `Initial commit: add README` — инициализация репозитория (ветка `master`).
2. `Add greet function` — функция `greet` в ветке `feature/greeting`, затем слияние в `master` (fast-forward).
3. `Add git unit tests` — модульные тесты.
4. `Add README and .gitignore` — описание проекта.
