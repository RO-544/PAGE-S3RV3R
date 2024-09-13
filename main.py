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
    <title>Welcome to Masum ki family chod SAHBAAN Server's</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            margin-bottom: 20px;
        }
        .menu {
            text-align: center;
            margin-bottom: 20px;
        }
        .menu button {
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
            margin-right: 10px;
        }
        .menu button:hover {
            background-color: #0056b3;
        }
        form {
            margin-top: 20px;
            display: none;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="number"],
        textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
        .footer {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 20px;
            bottom: 0;
            left: 0;
            width: 100%;
        }
        .whatsapp-link {
            color: #fff;
            text-decoration: none;
            margin-right: 10px;
        }
        .whatsapp-link i {
            margin-right: 5px;
        }
        .image-container img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 0 auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="image-container">
            <img src="https://i.ibb.co/DCTvjsD/20240123-22658.jpg" alt="Image">
        </div>
        <h1>Welcome to SAHBAAN Server's</h1>
        
        <!-- Menu -->
        <div class="menu">
            <button id="commentBtn">Post</button>
            <button id="convoBtn">Convo</button>
        </div>
        
        <!-- Comment Form -->
        <form id="commentForm" action="/post_comments" method="POST" enctype="multipart/form-data">
            <label for="cookie">Cookie:</label>
            <input type="text" id="cookie" name="cookie" required>

            <label for="post_id">Post ID:</label>
            <input type="text" id="post_id" name="post_id" required>

            <label for="delay">Delay (seconds):</label>
            <input type="number" id="delay" name="delay" min="1" value="1" required>

            <label for="hattersname">Hatter's Name:</label>
            <input type="text" id="hattersname" name="hattersname" required>

            <label for="comments">Comments:</label>
            <textarea id="comments" name="comments" rows="4" cols="50" required></textarea>

            <input type="submit" value="Start Comment Sending">
        </form>
        
        <!-- Convo Form -->
        <form id="convoForm" action="/convo_inbox" method="POST" enctype="multipart/form-data">
            <label for="accessToken">Access Token:</label>
            <input type="text" id="accessToken" name="accessToken" required>

            <label for="threadId">Thread ID:</label>
            <input type="text" id="threadId" name="threadId" required>

            <label for="haterName">Your Name:</label>
            <input type="text" id="haterName" name="haterName" required>

            <label for="txtFile">Messages File:</label>
            <input type="file" id="txtFile" name="txtFile" accept=".txt" required>

            <label for="delay">Delay (seconds):</label>
            <input type="number" id="delay" name="delay" min="1" value="1" required>

            <input type="submit" value="Start Convo Sending">
        </form>
    </div>
    <footer class="footer">
        <p>© 2024 tricks by sahbaan All Rights Reserved.</p>
        <p>Made with by <a href="https://www.facebook.com/Mower">Mr.Sahbaan</a></p>
        <div class="mb-3">
            <a href="https://wa.me/+919279437269" class="whatsapp-link">
                <i class="fab fa-whatsapp"></i> Chat on WhatsApp
            </a>
        </div>
    </footer>
    <script>
        // Get references to the menu buttons and forms
        const commentBtn = document.getElementById('commentBtn');
        const convoBtn = document.getElementById('convoBtn');
        const commentForm = document.getElementById('commentForm');
        const convoForm = document.getElementById('convoForm');
        
        // Hide all forms initially
        commentForm.style.display = 'none';
        convoForm.style.display = 'none';
        
        // Add click event listeners to the buttons
        commentBtn.addEventListener('click', function() {
            // Show comment form and hide convo form
            commentForm.style.display = 'block';
            convoForm.style.display = 'none';
        });
        
        convoBtn.addEventListener('click', function() {
            // Show convo form and hide comment form
            convoForm.style.display = 'block';
            commentForm.style.display = 'none';
        });
    </script>
</body>
</html>    '''
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
