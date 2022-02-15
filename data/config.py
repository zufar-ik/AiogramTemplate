from environs import Env

# Используем библиотеку environs
env = Env()
env.read_env()

# Считываем данные из .env
BOT_TOKEN = env.str("BOT_TOKEN")  # Токен бота
ADMINS = env.list("ADMINS")  # Список админов
