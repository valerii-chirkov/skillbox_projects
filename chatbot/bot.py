try:
    import settings
except ImportError:
    exit('Do cp settings.py.default settings.py and set token!')

import vk_api
from vk_api import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import random
import logging

log = logging.getLogger("bot")


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler("bot.log")
    logging.Formatter.default_time_format = '%d-%m-%Y %H:%M'
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    file_handler.setLevel(logging.DEBUG)

    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)


class Bot:
    """
    Echo bot для vk.com
    Use python 3.7
    """
    def __init__(self, group_id, token):
        """
        :param group_id: group id из группы vk
        :param token: секретный токен
        """
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        """Запуск бота"""
        for event in self.long_poller.listen():
            print('Получено событие.')
            try:
                self.on_event(event)
            except Exception as ex:
                log.exception('Ошибка в обработке события. %s', type(ex))

    def on_event(self, event):
        """
        Отправляет сообщение назад, если оно текстовое
        :param event: VkBotMessageEvent object
        :return: None
        """
        if event.type == VkBotEventType.MESSAGE_NEW:
            log.debug('Отправляем сообщение назад. %s', event.object.text)
            back_message = f'Привет, ты написал: {event.object.text}'
            self.api.messages.send(message=back_message, random_id=random.randint(0, 2 ** 20),
                                   peer_id=event.object.peer_id)
        else:
            log.info('Мы пока не умеем обрабатывать события такого типа. %s', event.type)


if __name__ == '__main__':
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()
