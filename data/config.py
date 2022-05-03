from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("5309284220:AAHY95J9jgPTxHM3rEcoX32ZE6YKlnUvEqg")  # Bot toekn
ADMINS = env.list("179918218")  # adminlar ro'yxati
IP = env.str("localhost")  # Xosting ip manzili
