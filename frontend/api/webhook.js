export default async function handler(req, res) {
  const TELEGRAM_TOKEN = process.env.TELEGRAM_TOKEN; // Токен должен быть в переменной окружения
  const TELEGRAM_URL = `https://api.telegram.org/bot${7701212586:AAE9tAUbvIa8y6VvmbNjL7QV436tGGuUmv0}/sendMessage`;

  if (req.method === 'POST') {
    try {
      const chatId = req.body.message?.chat?.id;
      const text = 'Hello from Vercel!';
      
      // Отправляем сообщение через Telegram API
      const response = await fetch(TELEGRAM_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ chat_id: chatId, text }),
      });

      if (!response.ok) {
        throw new Error(`Telegram API error: ${response.status}`);
      }

      res.status(200).json({ message: 'Webhook received successfully' });
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: error.message });
    }
  } else {
    res.status(405).send('Method Not Allowed');
  }
}
