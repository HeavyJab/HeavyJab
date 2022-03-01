import requests, json, random

f = open("./README.md", "w")
res = requests.get(f'https://meme-api.herokuapp.com/gimme')
result = json.loads(res.text)
f.write(f'''<p align="center">
    <img src="{result['url']}" >
</p>
<h3 align="center">{result['title]}</h3>
<h3 align="center">Have a nice day!</h3>
''')
f.close()
