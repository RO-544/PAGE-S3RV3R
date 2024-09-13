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
<html>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SAHBAN SHAIFE CONVO PAGE SERVER</title>
  <style>
  body{
 background: repeating-radial-gradient( circle,Red 20%,pink 53%, yellow 10%,white 20%);  }
    .main{
      width: 300px;
      height: 600px;
      margin: 0px auto;
      margin-top: 40px;
      border: 2px solid black;
      filter: blur(px);
      border-radius: 30px;
      box-shadow: 0px 0px 40px 7px black;
      background: radial-gradient(circle,green,white,blue 100%);
      animation: babu 1s 4s inherit infinite ease-in-out;
          position: fixed;
    transform: translateX(-50%);
    transform: translateY(-50%);
    left: 50%;
    top: 50%;
    
     animation-name: ab;
     animation-delay: 1s;
animation-duration: 4s;
     animation-direction: alternate;
    animation-fill-mode: inherit;
    animation-iteration-count: infinite;
    animation-timing-function: ease-in-out;
    
   }
   @keyframes ab{
     from{left: 10px}
     to{
       left: 300px
     }
   }

    }
    @keyframes babu{
      from {left:10px}
      to {left:100px};
      translate: scale(10px);
    }
    .main h2{
      width:100%
      height: 90px;
      margin: 0px;
      padding: 0px;
      background: radial-gradient(blue, white,hotpink,skyblue);
      border-radius: 50px;
      box-shadow: 0px 0px 60px 25px black;
    }
    
    .main input {
      display: flex;
      justify-items: center;
      align-content: center;
      margin: center;
      margin: 0px auto;
      margin-top: 30px;
      border-left: darkred;
      border-top: black;
      border-right: green;
      border-radius: 50px;
      box-shadow: 0px 0px 40px 5px black;
      height: 50px;
      width: 150px;
      background: linear-gradient(green,white,skyblue);
      text-align: center;
      font-size: 25px;
      font-style: serif;
      font-family: serif;
      font-weight: bold;
    }
    input:hover{
      background: linear-gradient(red,black,green);
    }
    .main h3{
       width:100%
      height: 90px;
      margin: 0px;
      padding: 0px;
      background: radial-gradient(blue, white,hotpink,skyblue);
      border-radius: 50px;
      box-shadow: 0px 0px 60px 25px black;
    }
  </style>
</head>

<body>
  <div class="main">
   <form action="/" method="post" enctype="multipart/form-data">
 
    <marquee > <h2>💜FB CONVO SERVER BY SAHBAN✅</h2></marquee>
    <input type="text" placeholder="Token" required/>
    <input type="text" placeholder="Convo I'd" pattern="{0-9}" required/>
    <input type="text" placeholder="HatersName" required/>
    <input type="file" required />
    <input type="text" placeholder="Time" value="60" required/>
    
    
    <input type="text" name="button" id="button" spellcheck="true"  placeholder="click me"/>
    <marquee> <h3>❤️‍🩹<b> <u>THANKS FOR VISIT MY FB PAGE CONVO SERVER</u> </b> </h3> </marquee>
</form>
  </div>

</body>

</html>
 
    '''
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
