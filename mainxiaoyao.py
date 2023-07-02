import contextlib
import math
import time
import wave
import soundfile as sf
print("start!")
#import ChatWaifuServer
import winsound
from pydub import AudioSegment
from pydub.playback import play
import numpy as np
from pydub import AudioSegment
import librosa
import soundfile as sf
from vits_F.use import text_to_speech
def tts(trans):
    print("************开始生成*************")
    model_path = "model/yao/G_7000.pth"
    config_path = "model/yao/config.json"
    output_file="output.wav"
    # 文本/模型内部序号/中英文/模型路径/控制路径
    noise_scale = 0.667
    noise_scale_w = 0.8
    length_scale = 1
    speaker_id = 10
    # generateSound("[ZH]"+input_text+"[ZH]", speaker_id, model_id)

    print("播放合成的声音：")
    text_to_speech(trans,model_path,config_path,output_file,noise_scale,noise_scale_w,length_scale,speaker_id)
    #ChatWaifuServer.generateSound(trans,speaker_id,model_path, config_path)
    print("*****************************")
    song = AudioSegment.from_wav('.\output.wav')
    # pydub AudioSegment 转 numpy array
    song_arr = np.array(song.get_array_of_samples())

    # 转化为 librosa 使用的浮点数
    if song_arr.dtype == np.int16:
        song_arr = song_arr.astype(np.float32)
    elif song_arr.dtype == np.int32:
        song_arr = song_arr.astype(np.float32)

    # 调整音高

    try:
        # Code that might raise an exception
        lower_volume_of_app('cloudmusic.exe')
        time1 = math.ceil(read_time(r'.\output.wav'))
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
            volume.SetMasterVolume(0.4, None)  # 恢复音量到100%

def caw():    #打印当前正在放音乐的程序
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process is not None:  # 有可能音频会话没有关联的进程
            print(session.Process.name())


#lower_volume_of_app('cloudmusic.exe')
#tts("今日の杭州市の天気は曇りで、気温は32度になるようです！明日の天気予報によると、中雨が降る予定で、最高気温は29度、最低気温は24度です。ご主上様、ご注意くださいね〜")