# -*- coding: utf-8 -*-
# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = ""

import pylab as plt
import matplotlib.ticker as ticker
import os
import wave

def show_single_wav(speech, name):
    '''
        画出噪声，干净语音，带噪语音，增强语音的波形图
        幅度值范围-0.5~0.5
     '''
    spf = wave.open(speech, 'r')
    sound_info = spf.readframes(-1)
    sound_info1 = plt.fromstring(sound_info, "Int16")

    fig = plt.figure()
    fig1 = fig.add_subplot(111)
    fig1.plot(sound_info1)

    scale_x = 16000
    scale_y1 = 1000
    ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x / scale_x))
    ticks_y1 = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x / scale_y1))
    fig1.xaxis.set_major_formatter(ticks_x)
    fig1.yaxis.set_major_formatter(ticks_y1)
    fig1.tick_params(labelsize=18)

    fig1.set_xlabel('T / s', fontsize=18)
    fig1.set_ylabel('Amp', fontsize=18)
    
    plt.title(name)
    plt.show()
    fig.savefig('pictures/' + name + '-wav.png')
    spf.close()

def show_single_spec(speech, name):
    '''
        :param speech:wav格式的音频
        :return: 频谱图像
    '''
    spf1 = wave.open(speech, 'r')
    sound_info1 = spf1.readframes(-1)
    sound_info1 = plt.fromstring(sound_info1, 'Int16')

    fig = plt.figure()
    fig1 = fig.add_subplot(111)
    f1 = spf1.getframerate()
    # print(len(sound_info1))
    sound_info1 = sound_info1[1817:26054]
    spectrogram1 = plt.specgram(sound_info1, NFFT=256,Fs=f1, cmap='rainbow', scale_by_freq=True, sides='default')

    scale_y = 1000
    ticks_y = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y / scale_y))
    fig1.yaxis.set_major_formatter(ticks_y)
    fig1.tick_params(labelsize=24)

    fig1.set_xlabel('T / s', fontsize=24)
    fig1.set_ylabel('F / kHz', fontsize=24)

    # plt.title(name)
    plt.show()
    fig.savefig(name + '-spec.png')
    spf1.close()


def show_single_floder_spec(wavepath):
    L = []
    pre_name = ""
    file_path = ""
    for root, dirs, files in os.walk(wavepath):
        for file in files:
            if file.endswith(".wav"):
                file_path = os.path.join(root, file)
                pre_name = file[:-4]
                show_single_spec(file_path, pre_name)

def show_single_floder_wav(wavepath):
    L = []
    pre_name = ""
    file_path = ""
    for root, dirs, files in os.walk(wavepath):
        for file in files:
            if file.endswith(".wav"):
                file_path = os.path.join(root, file)
                pre_name = file[:-4]
                show_single_wav(file_path, pre_name)
                

if __name__ == '__main__':
    # print('绘图')

    # 
    # wavpath = "/home/lisen/uestc/code/pandora/waveSamples"
    # show_single_floder_wav(wavpath)

    wavpath2 = "C:\\Education\\kbase\\学术论文\\音频组\\2019自动化学报\\20190918自动化学报返修\\过程文件\\返修版语谱图\\wav2"
    show_single_floder_spec(wavpath2)
    
    # wavpath1 = '/home/lisen/Desktop/noisy_combine/test/0/out_.wav'
    # show_single_spec(wavpath1,'out_')
    # wavpath2 = '/home/lisen/Desktop/noisy_combine/test/0/out_noisy.wav'
    # show_single_spec(wavpath2,'out_noisy')
    # wavpath3 = '/home/lisen/Desktop/noisy_combine/test/0/out_enh.wav'
    # show_single_spec(wavpath3,'out_enh')
    