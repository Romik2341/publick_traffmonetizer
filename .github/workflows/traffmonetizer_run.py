from github import Github

# Встановлення змінних оточення для автентифікації API GitHub
GITHUB_TOKEN = "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"  # Потрібно замінити на свій особистий токен GitHub

# Створення підключення до GitHub за допомогою токена
g = Github(GITHUB_TOKEN)

# Налаштування деталей воркфлоу
owner = "Romik2341"  # Потрібно замінити на ваше користувацьке ім'я GitHub
repo_name = "publick_traffmonetizer"  # Потрібно замінити на назву вашого репозиторію
workflow_name = "main"  # Потрібно замінити на назву вашого воркфлоу
workflow_file = ".github/workflows/main.yml"  # Потрібно замінити на шлях до файлу вашого воркфлоу

# Отримання репозиторію
repo = g.get_user(owner).get_repo(repo_name)

# Завантаження вмісту файлу воркфлоу
with open(workflow_file, 'r') as file:
    content = file.read()

# Цикл для створення тисячі воркфлоу
for i in range(18):
    # Створення нового воркфлоу за шаблоном
    new_workflow = repo.create_workflow(workflow_name, content)

    # Запуск нового воркфлоу
    new_workflow.create_dispatch()

print("Active work [18] workflows!")
