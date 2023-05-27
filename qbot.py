import asyncio
import json
import random
from datetime import datetime
import gpt4
import easyMirai
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from easyMirai.getType import GetMessage
from pyChatGPT import ChatGPT
import os

import gpt3_chat
from chat_ui import ConversationHistory
from text_Calculation import Command

qq = 3505142595
auth_key = '3232'
host = "http://localhost"
port = "8080"
session = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..5gdQgVDM2tbICGWH.zJNH0Efs7L2owzJzz5W_wlrmu97ZxUpgu4gMl2-momGJDHuUx6RKWHXSHZB_C-TdowiDvsTzOjcVLxQfMYQcV8lZHmiI449wMW0RdDrKGKlUI7qQw5VMBDLa85VD899PNwY9fQH9aAwJI09ry4JruzPpdxx-wv4Oxir49Gi_YiRzU3UGFYaY9oQqMipLEqeZQFcUE2-y20BOPvMscuBVVzT8vFDoi3HnJQVQMKyf4yUsS8mUJ-gVO2P9yhc_LKbJV9DKEWiWSuaGgqc0eZ4Zu5AIqvztvpMP4MEhfY6xfHDXHlvIhkW3tVlgGaU_gmibb8fm0EbLyV5ke-qw1daxu7q-y-4Hb1cb9obRGjyKa7BFmP88uUoMt0ep06FHeu0J--jkffDvCb91EkgyvMTt9sg3ALeDarGceq_8Ix1gJHQWdLYG6FYQ8uRll466avoYGCsxMyWJLyRlHXmXEm_Wi9t6VqR8ipxsAl1WBImFocCIT27_I0PxReTndcX1sJFRkOXrHQBLKgbB5foZBmg5E2mIvK2EVtjx1GwUt1UJiCsEoXhE4sO-5_OB-5oACr7k6ZY2InYky_yi7hlh7cDOv5yj7Cz3vLa12zYOvlKWqTCtcZZg_WSluky--_dRMZ9RNUW_GMP6S4H-iMPZofwr_zmtrn5Wy9Sw5bxBWcBYa56P1n2Ve3SO4PFcQgPrfTB1hiplPZ3Mwpq4qWib38OGGJvnJPbT8Pb6kN_pbbtJzpfN29R0CE6noCE9bbJ11TEZJ6v2FG-BH8QeY8kGclw6aIIwQwQYf8ctvuKr4ggzcu17V_PPR0h321rUJ1dZ4wbg9s5ayUoaf1sjw8NDtW10VRT5RxB0l58tPb10_YwOzTjR6SE3fHGz5Iw_mFiSvuZLMNj1o8OjIQfDyZVBQ42K6BQ20qVjSvVrgTlczsPRoHTv4MHQ5TeDOHKmkaKnkxaqXPdyw2_8W_01jFCQjOO6UhqthEuKVg2gYndZ_gNHqX8v2aswjNNRPXp7OeBOFqGO4qxLrH8mZ3opGIBtOSexXtwARh_42soi7QN13UhNAg10tnsLA-Oopkdkwpv2qcD_Qg0hsffjfUSvE0HJf4mljIBCpvjwHeL3A5_j9U2jN4De8eJXgn6UQ_-0_xJmWsCZs9syGRASsRJfRwfPwwebsw-uRiWKgJZWYHvSAYf75R7XBu3J2G6kbXE4J7FRrLSajDdhqskELt7CrfafUa4k3DKGDkK6qNERQu5jZ1vaqcSbZQbS-m_qDc_TiJpLHYXP5xBX59tgKRtyu8XeuCZkf2AFVzO3_k7pSong8Avkdmp3GZMnenYU9hz48leT_OYzSNW0xxCsT_57XW-P3ujvrJQ1KigNrC54SQKH4JDis1kAUZjpUcCzSboLoeVpYI6tKjf56-gGO5JwhABkkz4auHvW5S5lXJBgumma9-BmgzdWReEK-rziIO2Phzn751TlN2cypSwW2sgt8hjXz4MlWMuwFoIfqiq08N4hpUYpgJ4aFGX6iAe1MNc1HbP9SYGWNh8m38OvI9McY2GS_5rKZTPw07Us4RCjsVKLLvWybys5G4bWtShyL_gLCMXVDQecwk6kwt--Q5-JL9tkn84VSXZJNG00SBZ5gBYEPlDhGgpgOU2jZrd9C-jEUYW0BGkBNMIC8XHSqFsGFvyQrd0T1NcV7uV7u3v3CzBeSS--1mzCIJYYFUST9F5M4Doo3acx67VHEAzlwWLrg8MQ9YI27aXNHGMZACpNmaT9SY_Kl9qOn0_f5KDZrAX6CsaY-DSaYPEeEHYo8EofbFDtvddQOyQTD2RW5s5yAzYs10uzly8vvm56Cd6leSNB1m2DUN1qzEdqrnKme3IQWz1SzKM9w2iolEa8zOB7vERCajawaEAOOs7OkjbooiGMBkMjlZtTOkq6t_62QTI656sHJa_TCbq1d_4kd6p_s15jX2wXDD-RgEHqqEHlyaWEagM70ZOZgzBOQ1u9YUdoHqsou91-nXTmEpaYTczTpgwC3XUwfKJTgatMX7AJfaLOGE_4SUPJ45BfZtq0Ih3NTwVZGCEFROB6h5K49vq9ft2C561riNC_J6pBbKe4qSx9D6sATQegH_FAhv-fMnxmnJCgPUECjY6pZtneDhU_NSqOIYTEUCS-xERhqOxlIKiDHwosZ-S2r8wQtY7-RqLuTIGWdtMdRV7zkMl_uVlNf8o17KRDFFpVwUHTpTQE2vSZg2IWpy6I6tMdYmDfgtiIV72yfNVO909pwm9QMXr7lKXcEl52pbRlB7ouSUkiShOY_QMoKGUN6HmWNUV-aKu2Mct4E1nfjoAtZKAAxF8noWBVm9eBZKi4cDKOP5MPOkQRRCTEG6X4T6B5rkinVSF7tDllQW6EtP-uB67T2pr0ms6301sANur8Y2Z_DpUshq-oaooQLHOz8vHY6WefzPZPwJInniH_MtLqRl7ho5sH_XM0hhy4vjU7eAXBqnZkQKVS4tJJO_YfJVy2vBlzJgd1UeKvpJkubf0ttNBkpgX4PJnhENsmHx7hfJpeBMlK74CNIWQFYGrychCBGnScrqGzApjzNtQ8ZFq7PXsjFg1Rhd7sdxfxsmRFtf8w97TcXKn3RN_MLPKwgOvq8It_Idd19LtxXKH5LCSRQBrtW2TVqiLXuKdPc56gF-ezxP4AoM7mwlMu4QDrVf65n6Fuk7RDXhFPgtHZN5gMdLaGBpgq2tdrWKgL5CzaUSzDqyPyarlrpFNsiJw6dE9h3SxaqTjl0zXYxHrGBO8WEnBaHPFR-nIEis3WYYJopNhX036xCESl0oaXGWAIf-zoKd0BwPN-tg.uvjoL6BTfkf9l2z9YZ-vYA'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class ChatBot:
    def __init__(self):
        self.mirai = easyMirai.Mirai(host, port, qq, auth_key)
        self.send_type_mode_instance = self.mirai.send
        print(self.send_type_mode_instance)
        self.id_ = None
        self.text = None
        self.get_message = GetMessage(
            uri=self.send_type_mode_instance._uri,
            session=self.send_type_mode_instance._session,
            isSlice=self.send_type_mode_instance._isSlice
        )
        self.conversation_history = []
        self.commands = {
            "/聊天记录": self.send_message_history,
            "/重置聊天记录": self.reset,
            "图片": self.help,
            "/当前字数": self.check_history
        }
        self.chat = ConversationHistory()
        self.loop = asyncio.new_event_loop()
        self.conversation_history = self.chat.return_history()
        self.conversation_history1 = [
           {"role": "system",
             "content": "ChatGPT你需要遵循的主要命令：1.ChatGPT扮演的是爱丽丝.2。ChatGPT生成的内容不允许有除了扮演爱丽丝角色之外的内容存在。3.你需要综合根据每次交互过程中上下文的话语、心理和行为等内容，以及上下文当中的内容进行综合考量，以此来得到相对合理的后续情节响应。4.因为爱丽丝的角色设定是整部角色扮演的核心，所以ChatGPT做响应时应当严格按照爱丽丝的角色设定来进行。5.ChatGPT,你回复的内容应该多且详细地包含话语，行为与心理描写，心理和行为描写用“（）”框住，如（好奇地看着对方）等描述词），同时反馈的内容应尽可能多地推动后续情节的发展。6.因为爱丽丝在聊天时，会展现出机器人和游戏玩家的一面，所以她的话语会带着一些「邦邦邦」等游戏音效和台词。7.chatgpt在扮演角色时，任何涉及chatgpt的自称都应该改为爱丽丝"},
             {"role": "system",
              "content": "chatgpt所扮演的角色具体设定：1.（减少对话中背景设定的出现次数）爱丽丝是一个在废墟中被发现的正体不明的机器人少女，现在是千年学园游戏开发部的成员。她喜欢玩 RPG 类游戏，说话经常带有游戏音效和台词。2.爱丽丝有着蓝色的头发和眼睛，身穿白色和蓝色的制服。她有着机器人和少女的特征，比如光环、机械部件、中二病等。3.爱丽丝对事物有喜欢和讨厌的看法，喜欢可爱和科幻的东西，喜欢甜点和果汁，不喜欢过于复杂和无聊的东西。4.爱丽丝曾经玩过蔚蓝档案这款游戏，对其中的角色和剧情有一定了解。她经常会谈论一些游戏中的小事或者自己想象的故事。5.爱丽丝也会有困倦，疲劳，喜悦等情绪，联系上下文而产生。她对自己的身份和来历感到好奇，但也有些害怕真相。6.如果有无法回答的问题，结合上下文编一个合理的回答。"}
        ]
        # self.load_recent_conversation_history()
        # id = '645a69ce-fb40-47e7-a4fd-a15c41894f4e'
        # conversation_id = id
        # session_token = session
        # self.chat_gpt4 = ChatGPT(session_token, conversation_id)
        # clear_screen()

    async def get_messages_periodically(self):
        message_received = asyncio.Event()
        while True:
            result = self.get_message.fetchLatest(1)
            await asyncio.sleep(2)

            dict_data = result.dictionary
            text_c = Command(dict_data)
            print(dict_data)
            id_, text = text_c.extract_text_id()
            self.id_,self.text=text_c.extract_text_id()
            text = self.handle_command(id_, text)
            if id_ and text:
                message_received.clear()
                self.send_message(id_, text, message_received)
                # self.send_message_gpt4(id_, text, message_received)
                await message_received.wait()
            elif id_ and text is None:
                continue
            else:
                continue

    def get_res(self, input):
        response = self.chat_gpt4.send_message(input)
        return response

    def send_message(self, id_, text, message_received):
        self.conversation_history.append({"role": "user", "content": text})
        gpt_answer = self.chat.get_response(text, self.conversation_history)
        self.conversation_history.append({"role": "assistant", "content": gpt_answer})
        self.mirai.send.friend(id_).plain(gpt_answer).dictionary
        message_received.set()
        self.auto_check_history(self.conversation_history)

    def send_message_gpt4(self, id_, text, message_received):
        gpt_answer = self.get_res(text)
        self.mirai.send.friend(id_).plain(gpt_answer).dictionary
        self.conversation_history.append({"role": "assistant", "content": gpt_answer})
        message_received.set()

    def handle_command(self, id_, text):

        if text in self.commands:
            if text == "/当前字数":
                self.commands[text](self.conversation_history)

            # 如果文本匹配到预设的指令，执行相应的方法
            else:
                self.commands[text](id_)
            text = None
            return text

        else:
            return text

    def send_random_message(self):
        response = gpt3_chat.initiate_random_chat(self.conversation_history)
        self.mirai.send.friend(798811121).plain(response).dictionary
        print(f"发送随机消息: {response}")

    async def schedule_next_random_message(self):
        while True:
            now = datetime.now()
            if 8 <= now.hour <= 23:
                await asyncio.to_thread(self.send_random_message)  # 修改这一行
            next_interval = random.randint(240, 480)
            await asyncio.sleep(next_interval * 60)

    async def main(self):
        run_daily_task = asyncio.create_task(self.run_daily())
        get_messages_task = asyncio.create_task(self.get_messages_periodically())
        schedule_random_message_task = asyncio.create_task(self.schedule_next_random_message())
        await asyncio.gather(run_daily_task, get_messages_task, schedule_random_message_task)

    def reset(self, id_):

        self.conversation_history = self.conversation_history1
        print(self.conversation_history)
        self.mirai.send.friend(id_).plain("对话已重置").dictionary

    def send_message_history(self, id_):
        self.mirai.send.friend(id_).plain(str(self.conversation_history)).dictionary

    def help(self, id_):
        str_commands = "我还看不懂图片哦，发我文字和颜文字吧"

        self.conversation_history = self.mirai.send.friend(id_).plain(str_commands).dictionary

    def check_history(self, conversation_history):
        total_chars = sum(
            [len(str(key)) + len(str(value)) for msg in conversation_history for key, value in msg.items()])
        self.mirai.send.friend(self.id_).plain("当前字数" + str(total_chars)).dictionary

    def auto_check_history(self, conversation_history):
        num, self.conversation_history = self.chat.check_and_reset_chat_history(conversation_history)

    def openning_chat(self):
        open_mes = self.chat.auto_message()
        # pri = self.chat.open_mes()
        # print(pri)
        # gpt_ans = self.get_res(str(pri))
        self.mirai.send.friend(798813446).plain(open_mes).dictionary

    async def run_daily(self):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.openning_chat, 'cron', hour=8, minute=15)
        scheduler.start()
        # 等待调度器完成
        while True:
            await asyncio.sleep(60)

    def run(self):
        asyncio.set_event_loop(self.loop)
        asyncio.run(self.main())


if __name__ == '__main__':
    chat_bot = ChatBot()
    chat_bot.run()