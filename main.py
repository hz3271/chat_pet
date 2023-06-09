import contextlib
import math
import time
import wave
import soundfile as sf
print("start!")
import ChatWaifuServer
import winsound
from pydub import AudioSegment
def tts(trans):
    print("************开始生成*************")
    model_path = "model/yuzi/H_excluded.pth"
    config_path = "model/yuzi/config.json"
    # 文本/模型内部序号/中英文/模型路径/控制路径
    speaker_id = 0  # 选择角色ID

    # generateSound("[ZH]"+input_text+"[ZH]", speaker_id, model_id)

    print("播放合成的声音：")

    ChatWaifuServer.generateSound(trans, 0,model_path, config_path)
    print("*****************************")
    try:
        # Code that might raise an exception
        lower_volume_of_app('cloudmusic.exe')
        time1 = math.ceil(read_time('.\output.wav'))
        winsound.PlaySound(r'.\output.wav', winsound.SND_FILENAME)
        time.sleep(time1)
        restore_volume_of_app('cloudmusic.exe')
    except Exception:  # Catch any type of exception
        print("-------未运行网易云------")
        print(Exception)
        winsound.PlaySound(r'.\output.wav', winsound.SND_FILENAME)


def read_time(fname):
    data, samplerate = sf.read(fname)
    duration = len(data) / samplerate
    print(duration)
    return duration

from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

def lower_volume_of_app(app_name):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == app_name:
            print(f'Current volume of {app_name}:', volume.GetMasterVolume())
            volume.SetMasterVolume(0.03, None)  # 将音量调低到%

def restore_volume_of_app(app_name):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == app_name:
            volume.SetMasterVolume(0.6, None)  # 恢复音量到100%

def caw():    #打印当前正在放音乐的程序
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process is not None:  # 有可能音频会话没有关联的进程
            print(session.Process.name())


#lower_volume_of_app('cloudmusic.exe')
#tts("「私たちが話している今、時刻は0時15分です。もうとても遅いのですが、私はまだあなたと話ができてとても嬉しいです。面白い話を共有したり、お互いの生活や趣味について知り合うことができるからです。あなたは今日何をしましたか？」")