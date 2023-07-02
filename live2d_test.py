import asyncio
import tkinter as tk
import json
import websockets
import threading
import time


class Simple:
    def __init__(self):
        #self.master = master
        self.websocket = None
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        #self.i = 0
        self.start_connect
        #master.title("简单示例")

        #self.text_box = tk.Text(master)
        #self.text_box.pack()

        #self.connect_button = tk.Button(master, text="连接", command=self.start_connect)
        #self.connect_button.pack()

        #self.test_button = tk.Button(master, text="测试气泡", command=self.send_message)
        #self.test_button.pack()

    async def connect(self):
        uri = "ws://127.0.0.1:10086/api"
        async with websockets.connect(uri) as websocket:
            self.websocket = websocket
            msg = {"msg": 10000, "msgId": 1}
            await self.websocket.send(json.dumps(msg))
            print("***连接中***")
            while True:
                time.sleep(1)
                response = await self.websocket.recv()
                print(response)
                if isinstance(response, str):
                    response = json.loads(response)
                msg_value = response.get('msg', None)
                if msg_value == 10000:
                    print("***连接成功***")
                else:
                    print(response)

    def start_connect(self):
        def target():
            self.loop.run_until_complete(self.connect())
        threading.Thread(target=target).start()

    def send_message(self,text):

        msg1 = {
            "msg": 11000,
            "msgId": 1,
            "data": {
                "id": 0,
                "text": str(text),
                "textFrameColor": 0x000000,
                "textColor": 0xFFFFFF,
                "duration": 1000
            }
        }

        def target():
            asyncio.run_coroutine_threadsafe(self.websocket.send(json.dumps(msg1)), self.loop)
        threading.Thread(target=target).start()


#root = tk.Tk()
#my_gui = Simple(root)
#root.mainloop()
