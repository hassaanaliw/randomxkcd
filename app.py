import os
from flask import Flask, render_template
import requests
import random
from lxml import html

app = Flask(__name__)
app.config.update(
    DEBUG=True,
)


@app.route('/')
def index():

    return render_template('index.html',data=parse())


def parse():
    comics_list = []

    #open ten random xkcd comics between 1 & 1446

    for i in range(0,10):
        source = requests.get("http://xkcd.com/%d" % random.randint(1,1446)).text
        tree = html.fromstring(source.encode('utf-8'))

        img = tree.xpath('//div[@id="comic"]/img/@src')
        alt = tree.xpath('//div[@id="comic"]/img/@alt')

        try: 
            img[0]
        except:
            img.append('http://i0.kym-cdn.com/photos/images/newsfeed/000/178/254/c86.jpg')
            alt.append("Error: Image Not Found.")   


        comics_list.append({
            'img':img[0],
            'alt':alt[0]
            })

    return comics_list


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
