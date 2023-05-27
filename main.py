print("start!")
import ChatWaifuServer
import winsound
from pydub import AudioSegment
def tts(trans):
    print("************开始生成*************")
    model_path = "model/H_excluded.pth"
    config_path = "model/config.json"
    # 文本/模型内部序号/中英文/模型路径/控制路径
    speaker_id = 0  # 选择角色ID

    # generateSound("[ZH]"+input_text+"[ZH]", speaker_id, model_id)

    print("播放合成的声音：")

    ChatWaifuServer.generateSound(trans, 0,model_path, config_path)
    print("*****************************")
    winsound.PlaySound(r'.\output.wav', winsound.SND_FILENAME)

    print("-----------------------------")

