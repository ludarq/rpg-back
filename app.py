from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os

# Загружаем переменные окружения
load_dotenv()
PROXY_API_KEY = os.getenv("PROXY_API_KEY")  # Убедитесь, что этот ключ добавлен в Render

# Настройка ProxyAPI
openai.api_key = PROXY_API_KEY
openai.api_base = "https://api.proxyapi.ru/openai/v1"

app = Flask(__name__)

def generate_response(prompt):
    """Генерация ответа от AI с использованием ProxyAPI."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Используемая модель
            prompt=prompt,
            max_tokens=150
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Ошибка при обращении к API: {e}"

@app.route('/start_game', methods=['POST'])
def start_game():
    """Обработка POST-запроса для запуска игры."""
    try:
        data = request.json
        user_prompt = "Вы начинаете приключение в таинственном лесу..."
        ai_response = generate_response(user_prompt)
        return jsonify({"message": ai_response, "game_state": "active"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Получаем порт из переменной окружения или используем 5000
    app.run(host='0.0.0.0', port=port)  # Слушаем на всех интерфейсах
