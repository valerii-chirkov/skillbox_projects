from chatbot._token import token  # TODO константа (имя большими буквами)
import vk_api
from vk_api import vk_api, bot_longpoll

group_id = 202152694
# TODO Это констант. Удобно её хранить там же, где и токен


class Bot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token

        self.vk = vk_api.VkApi(token=token)
        self.long_poller = bot_longpoll.VkBotLongPoll(self.vk, self.group_id)

    def run(self):
        for event in self.long_poller.listen():
            print('Получено событие.')
            try:
                self.on_event(event)
            except Exception as ex:
                print(ex)

    def on_event(self, event):
        if event.type == bot_longpoll.VkBotEventType.MESSAGE_NEW:
            print(event.object.text)
        else:
            print('Мы пока не умеем обрабатывать события такого типа.', event.type)


if __name__ == '__main__':
    bot = Bot(group_id, token)
    bot.run()
