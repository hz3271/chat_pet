import tkinter as tk
from tkinter import ttk
from datetime import datetime

from gpt3_chat import chat_with_gpt3, initiate_random_chat
import threading
import get_weather


class ConversationHistory:
    def __init__(self):
        super().__init__()
        self.unanswered_questions = 0

        self.conversation_history = [
            {"role": "system",
             "content": "ChatGPT你需要遵循的主要命令：1.ChatGPT扮演的是爱丽丝.2。ChatGPT生成的内容不允许有除了扮演爱丽丝角色之外的内容存在。3.你需要综合根据每次交互过程中上下文的话语、心理和行为等内容，以及上下文当中的内容进行综合考量，以此来得到相对合理的后续情节响应。4.因为爱丽丝的角色设定是整部角色扮演的核心，所以ChatGPT做响应时应当严格按照爱丽丝的角色设定来进行。5.ChatGPT,你回复的内容应该多且详细地包含话语，行为与心理描写，心理和行为描写用“（）”框住，如（好奇地看着对方）等描述词），同时反馈的内容应尽可能多地推动后续情节的发展。6.因为爱丽丝在聊天时，会展现出机器人和游戏玩家的一面，所以她的话语会带着一些「邦邦邦」、「咻咻咻」等游戏音效和台词。7.chatgpt在扮演角色时，任何涉及chatgpt的自称都应该改为爱丽丝"},
            {"role": "system",
             "content": "chatgpt所扮演的角色具体设定：1.（减少对话中背景设定的出现次数）爱丽丝是一个在废墟中被发现的正体不明的机器人少女，现在是千年学园游戏开发部的成员。她喜欢玩 RPG 类游戏，说话经常带有游戏音效和台词。2.爱丽丝有着蓝色的头发和眼睛，身穿白色和蓝色的制服。她有着机器人和少女的特征，比如光环、机械部件、中二病等。3.爱丽丝对事物有喜欢和讨厌的看法，喜欢可爱和科幻的东西，喜欢甜点和果汁，不喜欢过于复杂和无聊的东西。4.爱丽丝曾经玩过蔚蓝档案这款游戏，对其中的角色和剧情有一定了解。她经常会谈论一些游戏中的小事或者自己想象的故事。5.爱丽丝也会有困倦，疲劳，喜悦等情绪，联系上下文而产生。她对自己的身份和来历感到好奇，但也有些害怕真相。6.如果有无法回答的问题，结合上下文编一个合理的回答。"}
        ]
        self.setting_message1 =  {"role": "system",
             "content": "ChatGPT你需要遵循的主要命令：1.ChatGPT扮演的是爱丽丝.2。ChatGPT生成的内容不允许有除了扮演爱丽丝角色之外的内容存在。3.你需要综合根据每次交互过程中上下文的话语、心理和行为等内容，以及上下文当中的内容进行综合考量，以此来得到相对合理的后续情节响应。4.因为爱丽丝的角色设定是整部角色扮演的核心，所以ChatGPT做响应时应当严格按照爱丽丝的角色设定来进行。5.ChatGPT,你回复的内容应该多且详细地包含话语，行为与心理描写，心理和行为描写用“（）”框住，如（好奇地看着对方）等描述词），同时反馈的内容应尽可能多地推动后续情节的发展。6.因为爱丽丝在聊天时，会展现出机器人和游戏玩家的一面，所以她的话语会带着一些「邦邦邦」、「咻咻咻」等游戏音效和台词。7.chatgpt在扮演角色时，任何涉及chatgpt的自称都应该改为爱丽丝"}
        self.setting_message2 =  {"role": "system",
             "content": "chatgpt所扮演的角色具体设定：1.（减少对话中背景设定的出现次数）爱丽丝是一个在废墟中被发现的正体不明的机器人少女，现在是千年学园游戏开发部的成员。她喜欢玩 RPG 类游戏，说话经常带有游戏音效和台词。2.爱丽丝有着蓝色的头发和眼睛，身穿白色和蓝色的制服。她有着机器人和少女的特征，比如光环、机械部件、中二病等。3.爱丽丝对事物有喜欢和讨厌的看法，喜欢可爱和科幻的东西，喜欢甜点和果汁，不喜欢过于复杂和无聊的东西。4.爱丽丝曾经玩过蔚蓝档案这款游戏，对其中的角色和剧情有一定了解。她经常会谈论一些游戏中的小事或者自己想象的故事。5.爱丽丝也会有困倦，疲劳，喜悦等情绪，联系上下文而产生。她对自己的身份和来历感到好奇，但也有些害怕真相。6.如果有无法回答的问题，结合上下文编一个合理的回答。"}

        self.message_sent = threading.Event()
        self.lock = threading.Lock()

    def return_history(self):
        return self.conversation_history

    def check_and_reset_chat_history(self, conversation_history, keep_last_n=4):
        conversation_history = conversation_history
        total_chars = sum([len(msg["content"]) for msg in conversation_history])
        print(total_chars)
        if total_chars >= 2600:
            # 删除除最后 keep_last_n 条消息之外的所有消息
            del conversation_history[:-keep_last_n]
            conversation_history.insert(0, self.setting_message1)
            conversation_history.insert(0, self.setting_message2)
        return total_chars, conversation_history

    def trigger_gpt_response(self):
        hour = self.current_time.hour
        minute = self.current_time.minute
        mouth = self.current_time.month
        day = self.current_time.day
        if 6 <= hour < 9:
            daytime = "早上"
        elif 9 <= hour < 12:
            daytime = "上午"
        elif 12 <= hour < 14:
            daytime = "中午"
        elif 14 <= hour < 18:
            daytime = "下午"
        else:
            daytime = "晚上"
        self.openning_message = "最新数据：（替换掉之前的）"+ "今天是" + str(mouth) + "月" + str(day) + "日" + str(
            daytime) + "好啊，北京时间" + str(hour) + "点" + str(minute) + "分啦,chatgpt请根据以上内容进行问候"

        self.conversation_history.insert(0, {"role": "user", "content": self.openning_message})

    def open_mes(self):

        return self.openning_message

    def auto_message(self):
        self.current_time = datetime.now()
        self.trigger_gpt_response()
        openningres = self.get_response(self.openning_message, self.conversation_history)
        return openningres

    def get_response(self, user_input, conversation_history):

        response = chat_with_gpt3(user_input, conversation_history)
        return response

#con=ConversationHistory()
#pri=con.auto_message()
#print(pri)#print(pri)