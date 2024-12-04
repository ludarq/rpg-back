from flask import Flask, request, jsonify
import requests

# Укажите ваш API-ключ Proxy API
PROXY_API_KEY = "sk-RZjfDDIvjxyIG3W4jU6YDAs3ITMBfL6d"
PROXY_API_URL = "https://api.proxyapi.ru/openai/v1/chat/completions"

app = Flask(__name__)

def generate_response(prompt):
    headers = {
        "Authorization": f"Bearer {PROXY_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 150
    }

    # Выполняем POST-запрос к Proxy API
    response = requests.post(PROXY_API_URL, headers=headers, json=data)
    
    # Проверяем статус ответа и возвращаем текст
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("text", "").strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

@app.route('/start_game', methods=['POST'])
def start_game():
    # Получаем данные из POST-запроса
    data = request.json
    user_prompt = "Вы начинаете приключение в таинственном лесу..."
    
    # Генерируем ответ через Proxy API
    ai_response = generate_response(user_prompt)
    
    return jsonify({"message": ai_response, "game_state": "active"})

if __name__ == "__main__":
    app.run(debug=True)
