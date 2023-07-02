print("start!")
from run import run_text_to_speech
import winsound


def tts(trans):
    print("************开始生成*************")

    # 文本/模型内部序号/中英文/模型路径/控制路径
    speaker_id = 0  # 选择角色ID

    # generateSound("[ZH]"+input_text+"[ZH]", speaker_id, model_id)

    print("播放合成的声音：")

    run_text_to_speech(trans)
    print("*****************************")
    winsound.PlaySound(r'./test.wav', winsound.SND_FILENAME)

    print("-----------------------------")

tts("主人主人")