import os, time, random
from playsound import playsound as ps

user = os.getlogin()
print(user)
exists = os.path.exists(f'/Users/{user}/Documentsrickroll.mp3')
print(exists)
while True:
    if not exists:
        os.system(f'cp rickroll.mp3 /Users/{user}/Documents')
        time.sleep(random.randrange(1, 120))
        ps(f'/Users/{user}/Documents/rickroll.mp3')
    else:
        time.sleep(random.randrange(1, 120))
        ps(f'/Users/{user}/Documents/rickroll.mp3')