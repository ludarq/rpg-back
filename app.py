from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os

# Загружаем переменные окружения
load_dotenv()
PROXY_API_KEY = os.getenv("PROXY_API_KEY")

openai.api_key = PROXY_API_KEY
openai.api_base = "https://api.proxyapi.ru/openai/v1"


app = Flask(__name__)

def generate_response(prompt):
    """Функция для создания ответа на основе ввода пользователя."""
    response = openai.Completion.create(
        engine="text-davinci-003",  # Или модель, которую вы хотите использовать
        prompt=prompt,
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()

@app.route('/start_game', methods=['POST'])
def start_game():
    """Обрабатывает запросы на запуск игры."""
    data = request.json
    user_prompt = "Вы начинаете приключение в таинственном лесу..."
    ai_response = generate_response(user_prompt)
    return jsonify({"message": ai_response, "game_state": "active"})

if __name__ == "__main__":
    app.run(debug=True)
