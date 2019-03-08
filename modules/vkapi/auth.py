import vk_api
from __main__ import log, logpr


class vkauth:
    def __init__(self, login = None, password = None, token = None, captcha_handler = None, proxies = None, user_agent = None):
        self.login = login
        self.password = password
        self.token = token
        self.proxies = proxies
        self.user_agent = user_agent
        self.captcha_handler = captcha_handler
        log('vkauth\nlogin = {}\npassword = {}\ntoken = {}\nproxy = {}\nuser_agent = {}\ncaptcha_handler = {}'.format(login, password, token, proxies, user_agent, captcha_handler))

    def auth(self):
        if self.token:
            try:
                self.vkapi = vk_api.VkApi(token = self.token,
                                            proxies = self.proxies,
                                            user_agent = self.user_agent,
                                            captcha_handler = self.captcha_handler,
                                            app_id = 2685278,
                                            scope = 1073737727)

                self.vkapi._auth_token(reauth = True)
                self.vkapi.method('account.setOffline')

            except Exception as E:
                log('Ошибка авторизации: {}\nАккаунт: {}:{}'.format(E, self.login, self.password))
                return False

        elif self.login and self.password:
            try:
                self.vkapi = vk_api.VkApi(login = self.login,
                                            password = self.password,
                                            proxies = self.proxies,
                                            user_agent = self.user_agent,
                                            captcha_handler = self.captcha_handler,
                                            app_id = 2685278,
                                            scope = 1073737727)

                self.vkapi.auth(reauth = True)

            except Exception as E:
                log('Ошибка авторизации: {}\nАккаунт: {}:{}'.format(E, self.login, self.password))
                return False

        return self.vkapi
