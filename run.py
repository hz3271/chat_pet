import torch
import winsound

import vits.commons
import vits.utils
from vits.data_utils import TextAudioLoader, TextAudioCollate, TextAudioSpeakerLoader, TextAudioSpeakerCollate
from models import SynthesizerTrn
from vits.text.symbols import symbols
from vits.text import text_to_sequence

import soundfile as sf

length_scale = 1


def get_text(text, hps):
    text_norm = text_to_sequence(text, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = vits.commons.intersperse(text_norm, 0)
    text_norm = torch.LongTensor(text_norm)
    return text_norm


def run_text_to_speech(text, config_path='./configs/biaobei_base.json', model_path='./model/Paimen/G_1434000.pth',
                       output_path='./', filename='test', length_scale=1.0, device='cpu'):
    device = torch.device(device)
    hps = vits.utils.get_hparams_from_file(config_path)

    net_g = SynthesizerTrn(
        len(symbols),
        hps.data.filter_length // 2 + 1,
        hps.train.segment_size // hps.data.hop_length,
        **hps.model).to(device)

    _ = net_g.eval()

    _ = vits.utils.load_checkpoint(model_path, net_g, None)

    audio_path = f'{output_path}/{filename}.wav'
    stn_tst = get_text(text, hps)
    with torch.no_grad():
        x_tst = stn_tst.to(device).unsqueeze(0)
        x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).to(device)
        audio = net_g.infer(x_tst, x_tst_lengths, noise_scale=.667, noise_scale_w=0.8, length_scale=length_scale)[0][
            0, 0].data.cpu().float().numpy()

    sf.write(audio_path, audio, samplerate=hps.data.sampling_rate)

# run_text_to_speech('旅行者怎么办啊，正业好像被丘丘人打成了猪。')
# winsound.PlaySound(r'../model/test.wav', winsound.SND_FILENAME)
