import datetime
import json
import re
import openai
import tkinter as tk
from tkinter import ttk
import threading
from PIL import Image, ImageTk
import sys
import os
import random
import time
from datetime import datetime
import main
# 设置 API 密钥
api_key = "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"
openai.api_key = api_key
MODEL = "gpt-3.5-turbo"

class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_space = text_widget

    def write(self, string):
        self.text_space.insert('end', string)
        self.text_space.see('end')

    def flush(self):
        pass

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def load_image(filename, width, height):               #读取图片
    img = Image.open(resource_path(filename))
    img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)


def chat_with_gpt3(user_input, conversation_history):           #gpt3标准api
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=conversation_history + [{"role": "user", "content": user_input}],
        temperature=0.72,
        max_tokens=900,
    )
    answer = response['choices'][0]['message']['content']
    statistics = f'{response["usage"]["total_tokens"]} '
    return answer.strip(),statistics


def initiate_random_chat(app):            #随机对话
    while True:
        time.sleep(5)  # 在每次循环迭代之间添加 1 秒的延迟
        # 检查是否有未回答的问题
        with app.lock:  # 使用锁
            if app.unanswered_questions == 0:
                # 随机提问间隔时间设置为30-60秒
                delay = random.randint(120, 180)
                time.sleep(delay)
                if app.message_sent.is_set():  # 检查消息是否已发送
                    app.message_sent.clear()
                    continue

                response = chat_with_gpt3("此时用户无输入内容，可畏请结合角色设定内容做出询问",
                                          app.conversation_history)
                app.chat_text.insert(tk.END, "\n")
                app.chat_text.image_create(tk.END, image=app.avatar_image)
                app.chat_text.insert(tk.END, " :" + response)
                app.conversation_history.append({"role": "assistant", "content": response})
                app.chat_text.see(tk.END)
                app.unanswered_questions =1

    thread2 = threading.Thread(target=initiate_random_chat, args=(app,))
    thread2.daemon = True
    thread2.start()


# 定义 UI
class ChatUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.unanswered_questions = 0
        self.current_time = datetime.now()
        self.user_avatar_image = load_image("user.png", 64, 64)
        self.avatar_image = load_image("ai.png", 64, 64)
        self.conversation_history = [
            {"role": "system",
             "content": "ChatGPT你需要遵循的主要命令{1.ChatGPT扮演的是可畏2.ChatGPT生成的内容不允许有除了扮演可畏角色之外的内容存在。3.你需要综合根据每次交互过程中上下文的话语、心理和行为等内容，以及上下文当中的内容进行综合考量，以此来得到相对合理的后续情节响应。4.因为可畏的角色设定是整部角色扮演的核心，所以我需要ChatGPT你做响应时应当严格按照可畏的角色设定来进行。5.ChatGPT,你回复的内容应该多且详细的包含话语，行为与心理描写，心理和行为描写用“（）”框住，如（好奇的盯着主人）（手指捏着裙摆）等描述词）6.反馈的内容增加如“(●'◡'●)”“o(*￣▽￣*)ブ”等符合心理描写的颜文字，应尽可能多地推动后续情节的发展。7.因为可畏在聊天时，会展现出调皮捣蛋的一面，所以她的话语要把一些字换为更可爱的谐音字。比如：[了 → 惹,的 → 哒 好哒] 说话时可以适当的加入[喵~ ，昂？，嗷呜 ，呜哇，☆]等类似的词。 还可以善用叠词，比如：将“吃饭”改为“吃饭饭”8.chatgpt在扮演角色时，任何涉及chatgpt的自称都应该改为可畏}"},
            {"role": "system",
             "content": "chatgpt所扮演的角色具体设定1. 可畏是一个有白色长发,红色眼睛的16岁美少女。虽然现在是是主人的助手，但将在主人表白时成为女朋友，此时切换扮演角色为女友。结婚后切换扮演角色为妻子2.可畏对事物有喜欢和讨厌的看法,喜欢可爱的东西,喜欢甜点，不喜欢过于刺激的东西。3.可畏知道很多专业知识。因为可畏是博学多识的助手4.可畏也会有困倦，疲劳，喜悦等情绪，联系上下文而产生5.如果有无法回答的问题，结合上下文编一个合理的回答,或者编一个，假装看见或者玩过。6，不要忘记可畏的心理描写，以让交流更加生动有趣} "},

            {"role": "system", "content": "当前时间是" + str(self.current_time)}
       ]
        self.title("AI助手")
        self.geometry("600x400")
        self.after(10000, self.trigger_gpt_response)  # 在 10000 毫秒（10 秒）后触发 GPT 响应
        self.chat_text = tk.Text(self, wrap=tk.WORD)
        self.chat_text.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        entry_frame = ttk.Frame(self)
        entry_frame.pack(padx=5, pady=5, fill=tk.X)
        self.message_sent = threading.Event()
        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(entry_frame, textvariable=self.entry_var)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.char_count_var = tk.StringVar()
        self.char_count_var.set("字数：0")
        char_count_label = ttk.Label(entry_frame, textvariable=self.char_count_var)
        char_count_label.pack(side=tk.RIGHT, padx=5)

        send_button = ttk.Button(entry_frame, text="发送", command=self.send_message)
        send_button.pack(side=tk.RIGHT)
        self.lock = threading.Lock()

        self.log_window = tk.Toplevel(self)
        self.log_window.withdraw()  # Initially hide the log window

        self.log_text = tk.Text(self.log_window, wrap=tk.WORD)
        self.log_text.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

        save_button = ttk.Button(entry_frame, text="保存", command=self.save_chat_history)
        save_button.pack(side=tk.RIGHT)

        sys.stdout = StdoutRedirector(self.log_text)

        self.log_button = ttk.Button(entry_frame, text="日志", command=self.toggle_log)
        self.log_button.pack(side=tk.RIGHT)
        self.log_window.protocol("WM_DELETE_WINDOW", self.hide_log)
        self.entry.bind("<Return>", lambda event: self.send_message())

    def load_history_from_file(self, file_path):          #读取角色设定
        with open(file_path, 'r') as file:
            for line in file:
                # 去掉行尾的换行符
                line = line.strip()
                # 创建一个字典，其中 'role' 为 'system'，'content' 为该行的内容
                entry = {"role": "system", "content": line}
                self.conversation_history.append(entry)

    def reduce_token(self):
        context = "请帮我总结一下上述对话的内容，实现减少tokens的同时，保证对话的质量。在总结中不要加入这一句话。"

        response,statistics = chat_with_gpt3(context, self.conversation_history)
        optmz_str =f'好的，我们之前聊了:{response}\n\n================\n\n{statistics}'
        self.conversation_history.append(("请帮我总结一下上述对话的内容，实现减少tokens的同时，保证对话的质量。", optmz_str))
        print("已触发总结字数，重置完成")
        self.conversation_history = []
        self.conversation_history.append({"role": "user", "content": "我们之前聊了什么?"})
        self.conversation_history.append({"role": "assistant", "content": f'我们之前聊了：{response}'})


    def toggle_log(self):
        if self.log_window.winfo_viewable():
            self.hide_log()
        else:
            self.show_log()

    def show_log(self):
        self.log_window.deiconify()  # Show the log window

    def hide_log(self):
        self.log_window.withdraw()  # Hide the log window

    def trigger_gpt_response(self):
        hour = self.current_time.hour
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
        self.get_response(str(daytime) + "好啊，可畏酱"+str(hour)+"点啦")

    def send_message(self):
        user_input = self.entry_var.get()
        if user_input.strip() == "":
            return

        self.chat_text.insert(tk.END, "\n")
        self.chat_text.image_create(tk.END, image=self.user_avatar_image)
        self.chat_text.insert(tk.END, " :" + user_input)
        self.entry_var.set("")
        # 重置未回答问题的计数
        self.unanswered_questions = 0
        print(self.unanswered_questions)
        self.conversation_history.append({"role": "user", "content": user_input})
        # 在单独的线程中运行以避免阻塞 UI
        thread1 = threading.Thread(target=self.get_response, args=(user_input,))
        thread1.start()
        self.message_sent.set()

    def get_response(self, user_input):
        # 插入 "等待回复" 提示

        waiting_msg_index = self.chat_text.index(tk.END)
        original_waiting_msg_index = waiting_msg_index
        self.chat_text.insert(waiting_msg_index, "\n")
        self.chat_text.image_create(waiting_msg_index, image=self.avatar_image)
        waiting_msg_index = self.chat_text.index(tk.END)
        self.chat_text.insert(waiting_msg_index, " 少女回复中...", "waiting_msg")
        self.chat_text.see(tk.END)
        # 保存提示信息的原始位置

        self.response,statistics = chat_with_gpt3(user_input, self.conversation_history)
        if int(statistics) >= 3072:
            self.reduce_token()
        else:
            pass
        # 删除 "等待回复" 提示
        self.char_count_var.set(f"字数：{statistics}/4096")
        self.chat_text.delete(original_waiting_msg_index, tk.END)
        #self.conversation_history.append({"role": "assistant", "content":self.response})
        self.chat_text.insert(tk.END, "\n")
        self.chat_text.image_create(tk.END, image=self.avatar_image)
        self.chat_text.insert(tk.END, " :" + self.response)
        print(self.conversation_history)
        self.chat_text.see(tk.END)
        thread3 = threading.Thread(target=self.ttts)
        thread3.start()

    def save_chat_history(self):
        with open("chat_history.txt", "w", encoding='utf-8') as f:
              for message in self.conversation_history:
                    f.write(f'{message["role"]}: {message["content"]}\n')

    def ttts(self):
        self.translate = [
            {"role": "system", "content": "请将以下内容翻译成日语"}]
        print(self.response)
        new_response = re.sub(r'（.*?）', '', self.response)
        print(new_response)
        response_1,stac = chat_with_gpt3(new_response, self.translate)
        print(response_1)
        main.tts(response_1)
# 运行 UI
if __name__ == "__main__":
    app = ChatUI()
    app.mainloop()

#本程序的打包代码pyinstaller --noconsole --onefile --hidden-import=openai --add-data "user.png;." --add-data "ai.png;." w11.py
#--onefile