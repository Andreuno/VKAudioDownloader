import vk_api, json, random
from urllib.request import urlretrieve
from modules.logging.log import *
from modules.vkapi.auth import *
from vk_api import audio

# | | | | | | | | | | | | | | | | | | | | | | DEFS

def get_vkapi(login, pas, token = None):
    '''
    Авторизируется по токену или логину и паролю
    '''

    user_agent = random.choice(open('settings/user_agents.txt').read().splitlines())

    if token != '':
        log('main Авторизируемся по токену')
        vka = vkauth(login, pas, token = token, captcha_handler = None, user_agent=user_agent)
        vkapi = vka.auth()

    else:
        log('main Авторизируемся')
        vka = vkauth(login, pas, captcha_handler = None, user_agent=user_agent)
        vkapi = vka.auth()

        if type(vkapi).__name__ != 'bool':
            pass

        else:
            logpr('Ошибка авторизации.')

    return vkapi


def del_chars(line):
    ''' Удаляет символы, недопустимые в названии файла.
    line - имя файла или строка из которой нужно удалить недопустимые символы символы.'''

    for char in line:
        if char in "\\/?:*\"\'\<\>|":
            line = line.replace(char,'')

    return line


# | | | | | | | | | | | | | | | | | | | | | | | | | | | | |  SETTINGS

login = 'ЛОГИН'
password = 'ПАРОЛЬ'
token = '' # токен, если хотите авторизавываться по нему
owner_id = 85571327 # ID владельца альбома
album_id = 3 # ID Альбома

# | | | | | | | | | | | | | | | | | | | | | | BODY

vkapi = get_vkapi(login, password, token)

if vkapi:
    print('Успешная авторизация')
    music = audio.VkAudio(vkapi)
    result = music.get(owner_id, album_id)

    ''' result = [...]
    {'id': 456239771, 'owner_id': 85571327, 'url': 'https://sgi1.43222.vkuseraudio.net/p3/f926da00a15f46.mp3?extra=ixmky7XjX-tWT4WIoky5Dtsw-5YotcGWyvZjQDdpMSctdBls9qhw4Hgv9npmMzsf2EC2C3KOR_7ioHAXHie8fgxbu4flMkBEclQqY5mVhIvhiDoILeKBNc7T5p-0y5tmXoW9Ss4p5G3tRx7OJHTs57g', 'artist': 'MARUV', 'title': 'Siren Song', 'duration': 171}
    '''

    for au in result:
        try:
            args = [del_chars(au['title']), del_chars(au['artist'])]

            urlretrieve(au['url'], 'music/-{} - {}.mp3'.format(*args))

            print('Загружено аудио -', au['title'])

        except Exception as E:
            print('Ошибка', E)


else:
    print('Ошибка авторизации.')
