from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CONVO SERVER BY SAHBAN SHAIFE</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            color: white;
            transition: background-color 1s ease;
        }
        .container {
            text-align: center;
            padding: 50px;
            background-color: pink;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }
        input, button {
            display: block;
            margin: 10px auto;
            padding: 10px;
        }
        .file-input {
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>TERE BHAI ABHI ZINDA HAI 😕 NO TENTION SBKI GAND DAD DO</h1>
        <form action="/submit" method="post" enctype="multipart/form-data">
            <label for="convo_id">👉🌿Convo_id Dal Babu 😘</label>
            <input type="text" id="convo_id" name="convo_id">

            <label for="tokens_file">👉😙Apna Tokens File dalo Mele jaanu💘</label>
            <input type="file" id="tokens_file" name="tokens_file" class="file-input">

            <label for="np_file">👉💜apna Np File dalo Babu 😘❤️</label>
            <input type="file" id="np_file" name="np_file" class="file-input">

            <label for="hater_name">👉🦈yha tere Hater ka name dal gand fad de us bsdk ka</label>
            <input type="text" id="hater_name" name="hater_name">

            <label for="speed">👉❤️‍🩹yha time dal de babu 🥲</label>
            <input type="text" id="speed" name="speed" value="60">

            <button type="submit">👉💚YHA Apna Details Submit kr aur kiss le💋😙✅</button>
            <p> Gand Fad do Apne Dushmano ki ABHI Zinda Hain tere Sahban Shaife Bhai sbki gand fad dega</p>
            <p> Aur kuchh Chahiye TOH MUJE Masg bta dena Sb kuchh tere liye Hajir hai ❤️‍🩹💜💚💙💛🧡💖💗💘💝</p>
            <p> Bhai Wo dekh TERE DUSHMAN ki gand Jal kar koyla koyla ho gya 🥲😳😂😂😂😂😂😂😂😂</p>
        </form>
    </div>

    <script>
        const colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange'];
        let currentIndex = 0;

        function changeBackgroundColor() {
            document.body.style.backgroundColor = colors[currentIndex];
            currentIndex = (currentIndex + 1) % colors.length;
        }

        setInterval(changeBackgroundColor, 1000);
    </script>
</body>
</html>

    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
