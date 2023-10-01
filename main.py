import requests
import base64
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

username = config['GitHub']['username']
repository = config['GitHub']['repository']
days = config['GitHub']['days']

repo_url = f'https://api.github.com/repos/{username}/{repository}/contents'
readme_path = 'README.md'

access_token = config['GitHub']['access_token']

new_content = f"""<h1>Hi there, I'm Felix</h1>

<p align="center"> 18y. Student in Germany 🇩🇪 at Gymnasium Ebingen. A passionate person for everything round about coding, tech and science. Before I start studying computer science at a university in Germany, I'm going to improve and refine my skills as much as possible. You've got a challenge for me? Text me! Anyway. Have fun on my GitHub account. 😄</p>


<br>
<br>

# 📊 GitHub Stats:

![Metrics](/github-metrics.svg)


# 💻 Tech Stack:
<p align="center">
<img src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
<img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white" alt="sqlite">
<img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white" alt="MariaDB">
<img src="https://img.shields.io/badge/php-%23777BB4.svg?style=for-the-badge&logo=php&logoColor=white" alt="PHP">
<img src="https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white" alt="C">
<img src="https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++">
<img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white" alt="Css">
<img src="https://img.shields.io/badge/dart-%230175C2.svg?style=for-the-badge&logo=dart&logoColor=white" alt="Dart">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
<img src="https://img.shields.io/badge/kotlin-%230095D5.svg?style=for-the-badge&logo=kotlin&logoColor=white" alt="Kotlin">
<img src="https://img.shields.io/badge/firebase-%23039BE5.svg?style=for-the-badge&logo=firebase" alt="Firebase">
<img src="https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&amp;logo=Arduino&amp;logoColor=white" alt="Ardunio">
<img src="https://img.shields.io/badge/minecraft-62B47A?style=for-the-badge&amp;logo=minecraft&amp;logoColor=white" alt="Minecraft">
<img src="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&amp;logo=mongodb&amp;logoColor=white" alt="MongoDB"> 
<img src="https://img.shields.io/badge/apache-%23D42029.svg?style=for-the-badge&logo=apache&logoColor=white" alt="Apache">
<img src="https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&amp;logo=Raspberry-Pi" alt="Raspberry Pi"> 
<img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" alt="Html">
<img src="https://img.shields.io/badge/swift-F54A2A?style=for-the-badge&logo=swift&logoColor=white" alt="Swift">
<img src="https://img.shields.io/badge/Git-fc6d26?style=for-the-badge&logo=git&logoColor=white" alt="Git">
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white" alt="Java">
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux">
<img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E" alt="Javascript">
<img src="https://img.shields.io/badge/android-%2320232a.svg?style=for-the-badge&logo=android&logoColor=%a4c639" alt="Android">
<img src="https://img.shields.io/badge/Unity-%2320232a.svg?style=for-the-badge&logo=unity&logoColor=white" alt="Unity">
<img src="https://img.shields.io/badge/IOS-%2320232a.svg?style=for-the-badge&logo=apple&logoColor=white" alt="IOS">
<img src="https://img.shields.io/badge/unreal-%2320232a.svg?style=for-the-badge&logo=unreal-engine&logoColor=white" alt="Unreal">
<img src="https://img.shields.io/badge/GitHub-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" alt="Github">
<img src="https://img.shields.io/badge/jetbrains_ides-000000?style=for-the-badge&amp;logo=jetbrains&amp;logoColor=white" alt="JetBrains"> 
<img src="https://img.shields.io/badge/apple-000000?style=for-the-badge&amp;logo=apple&amp;logoColor=white" alt="apple">
</p>


# 

<br><br>

<p align="center">
<a href="mailto:fehennerich@outlook.de" >
<img align="center" alt="Felix Hennerich | Gmail" width="26px" src="https://github.com/SatYu26/SatYu26/blob/master/Assets/Gmail.svg" />
</a> &nbsp;&nbsp;

<a href="https://discord.gg/Qb6BzpAt8V" target="_blank">
<img align="center" alt="N1tr0xFelix | Discord" width="24px" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/discord.svg" />
</a> &nbsp;&nbsp;

<a href="https://twitter.com/HennerichFelix" target="_blank">
<img align="center" alt="HennerichFelix | Twitter" width="24px" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" />
</a> &nbsp;&nbsp;

<a href="https://www.instagram.com/felixderkeinennamenkennt/" target="_blank">
<img align="center" alt="Felixderkeinennamenkennt | Instagram" width="24px" src="https://github.com/SatYu26/SatYu26/blob/master/Assets/Instagram.svg" />
</a> &nbsp;&nbsp;

<a href="https://github.com/FelixHennerich" target="_blank">
<img align="center" alt="FelixHennerich | GitHub" width="26px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Github-desktop-logo-symbol.svg/1024px-Github-desktop-logo-symbol.svg.png" />
</a> &nbsp;&nbsp;

<a href="https://www.youtube.com/channel/UCKNT0NCikpds9nWKhIQcS3w" target="_blank">
<img align="center" alt="1BlueNitrox | YouTube" width="26px" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" />
</a> &nbsp;&nbsp;
<p> 
<div align="center">
:heart_eyes: Thanks for watching our profile! Have a nice day! :wink: <br/>
Current coding streak: {days} days <br/>
&copy; 2023 Hash-HQ

</div>
"""

headers = {
    'Authorization': f'token {access_token}',
    'Accept': 'application/vnd.github.v3+json'
}

response = requests.get(f'{repo_url}/{readme_path}', headers=headers)
data = response.json()

new_content_bytes = new_content.encode('utf-8')
new_content_base64 = base64.b64encode(new_content_bytes).decode('utf-8')
data['content'] = new_content_base64

commit_message = 'Aktualisierung der README-Datei über die API'

commit_data = {
    "message": commit_message,
    "content": data['content'],
    "sha": data['sha']
}

commit_response = requests.put(f'{repo_url}/{readme_path}', json=commit_data, headers=headers)

config['GitHub']['days'] = str(int(config['GitHub']['days']) + 1)

with open('config.ini', 'w') as configfile:
    config.write(configfile)

if commit_response.status_code == 200:
    print('README-Datei erfolgreich aktualisiert.')
else:
    print(f'Fehler beim Aktualisieren der README-Datei: {commit_response.status_code}')