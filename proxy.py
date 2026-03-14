from flask import Flask, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)  # Разрешаем запросы с любого сайта

# База цен CS.MONEY (эмуляция, так как API требует ключ)
CS_MONEY_PRICES = {
    '★ Karambit | Doppler (Factory New)': 2450.00,
    '★ M9 Bayonet | Gamma Doppler (Factory New)': 2100.00,
    '★ Butterfly Knife | Fade (Factory New)': 1850.00,
    '★ Bayonet | Lore (Minimal Wear)': 1200.00,
    'AK-47 | Fire Serpent (Minimal Wear)': 850.00,
    'M4A4 | Howl (Field-Tested)': 2100.00,
    'AWP | Dragon Lore (Battle-Scarred)': 2800.00,
    'M4A1-S | Hyper Beast (Minimal Wear)': 150.00,
    'Desert Eagle | Hand Cannon (Field-Tested)': 90.00,
    'USP-S | Kill Confirmed (Minimal Wear)': 120.00,
    'Sport Gloves | Vice (Factory New)': 3200.00,
    'Driver Gloves | Crimson Web (Field-Tested)': 950.00
}

@app.route('/api/cs-money', methods=['GET'])
def get_prices():
    try:
        # В реальном проекте здесь должен быть запрос к API CS.MONEY
        # Но так как API требует ключ, мы возвращаем эмулированные цены
        return jsonify({
            'success': True,
            'source': 'CS.MONEY',
            'prices': CS_MONEY_PRICES
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("✅ Прокси-сервер CS.MONEY запущен!")
    print("🌐 URL: http://localhost:5000/api/cs-money")
    print("🚀 Запускай сайт и открывай index.html в браузере")
    app.run(port=5000)
