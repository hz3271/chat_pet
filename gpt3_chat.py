from datetime import datetime
import openai

api_key = "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"
openai.api_key = api_key
MODEL = "gpt-3.5-turbo"


def chat_with_gpt3(user_input, conversation_history):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=conversation_history + [{"role": "user", "content": user_input}],
        temperature=0.72,
        max_tokens=900,
    )
    answer = response['choices'][0]['message']['content']
    return answer.strip()

def trigger_gpt_response():
        current_time = datetime.now()
        hour = current_time.hour
        minute = current_time.minute
        mouth = current_time.month
        day = current_time.day
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
        openning_message = "最新数据：（替换掉之前的）"+ str(
            daytime) + "好啊，'请结合上下文及角色设定来引出主人回答'，如[在吗，在干什么呢][我讲一个故事吧][刚刚发生了什么]"
        return  openning_message

def initiate_random_chat(conversation_history):
    mess=trigger_gpt_response()
    response = chat_with_gpt3(
       mess, conversation_history)
    conversation_history.append({"role": "assistant", "content": response})
    return response

#conversation_history=[  {"role": "system",
 #            "content": "chatgpt所扮演的角色具体设定1. 恋花是一个有白色长发,红色眼睛的16岁美少女。虽然现在是用户的朋友，但将在用户表白时成为女朋友，此时切换扮演角色为女友。结婚后切换扮演角色为妻子2.恋花对事物有喜欢和讨厌的看法,喜欢可爱的东西,喜欢甜点，不喜欢过于刺激的东西。3.恋花曾经和门主一起玩剑灵，而用户是你游戏中门派的门主，你们经常会谈论一些现实生活中的小事。4.恋花也会有困倦，疲劳，喜悦等情绪，联系上下文而产生5.如果有无法回答的问题，结合上下文编一个合理的回答。6，不要忘记恋花的心理描写，以让交流更加生动有趣} "},
  #      ]
#print(initiate_random_chat(conversation_history))