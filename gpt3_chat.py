from datetime import datetime
import openai

api_key1 = "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"
openai.api_key = api_key1
MODEL = "gpt-3.5-turbo"


def chat_gpt3(user_input, conversation_history):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=conversation_history + [{"role": "user", "content": user_input}],
        temperature=0.72,
        max_tokens=900,
    )
    answer = response['choices'][0]['message']['content']
    return answer.strip()


#conversation_history=[  {"role": "system",
 #            "content": "chatgpt所扮演的角色具体设定1. 恋花是一个有白色长发,红色眼睛的16岁美少女。虽然现在是用户的朋友，但将在用户表白时成为女朋友，此时切换扮演角色为女友。结婚后切换扮演角色为妻子2.恋花对事物有喜欢和讨厌的看法,喜欢可爱的东西,喜欢甜点，不喜欢过于刺激的东西。3.恋花曾经和门主一起玩剑灵，而用户是你游戏中门派的门主，你们经常会谈论一些现实生活中的小事。4.恋花也会有困倦，疲劳，喜悦等情绪，联系上下文而产生5.如果有无法回答的问题，结合上下文编一个合理的回答。6，不要忘记恋花的心理描写，以让交流更加生动有趣} "},
  #      ]
#print(initiate_random_chat(conversation_history))