import base64
import io
import os

import webuiapi
from PIL import Image
from webuiapi import b64_img

# create API client with custom host, port


# create API client with custom host, port and https
#api = webuiapi.WebUIApi(host='webui.example.com', port=443, use_https=True)

# create API client with default sampler, steps.
#api = webuiapi.WebUIApi(sampler='Euler a', steps=20)

# optionally set username, password when --api-auth=username:password is set on webui.
# username, password are not protected and can be derived easily if the communication channel is not encrypted.
# you can also pass username, password to the WebUIApi constructor.
#api.set_auth('username', 'password')
i=1
current_model_index = 0  # 初始化模型索引

def change_models(id_):
    global current_model_index  # 声明全局变量
    api = webuiapi.WebUIApi(host='127.0.0.1', port=7860)
    models = api.util_get_model_names()

    # 在模型 23 和 14 之间切换
    if current_model_index == 0:
        api.util_set_model(models[23])
        current_model_index = 1  # 更新当前模型索引
    else:
        api.util_set_model(models[14])
        current_model_index = 0  # 更新当前模型索引

def change_models1():
    api = webuiapi.WebUIApi(host='127.0.0.1', port=7860)
    models = api.util_get_model_names()
    for i, model in enumerate(models, start=0):
        print('{}. {}'.format(i, model))
    api.util_set_model(models[int(input())])

prompt1="((masterpiece)), best quality, extremely detailed CG unity 8k wallpaper,illustration,1girl,angel,angel wings, blue dress, beautiful detailed eyes,absurdly long hair, <lora:kincora2mixA4:0.8>"
negative_prompt="EasyNegative, ng_deepnegative_v1_75t ,verybadimagenegative_v1.3"
sampler_name = 'DPM++ 2M alt Karras'  # 采样器名称
batch_size = 1 # 批处理大小
n_iter = 1  # 迭代次数
steps = 20  # 步骤数
cfg_scale = 7.0  # 配置比例
#width = 1280  # 宽度
#height = 768  # 高度
do_not_save_samples = False # 是否不保存样本
do_not_save_grid = False  # 是否不保存网格
script_name = None  # 脚本名称
send_images = True  # 是否发送图像
save_images = True  # 是否保存图像
alwayson_scripts = {'ControlNet': {'args': []}}  # 始终打开的脚本
denoising_strength=1.5

def text2image(prompt,width,height):
    api = webuiapi.WebUIApi(host='127.0.0.1', port=7860)
    result1 = api.txt2img(
        prompt=prompt,  # 正面提示
        negative_prompt=negative_prompt,  # 负面提示
        sampler_name=sampler_name,  # 采样器名称
        batch_size=batch_size,  # 批处理大小
        n_iter=n_iter,  # 迭代次数
        steps=steps,  # 步骤数
        cfg_scale=cfg_scale,  # 配置比例
        width=width,  # 宽度
        height=height,  # 高度
        do_not_save_samples=do_not_save_samples,  # 是否不保存样本
        do_not_save_grid=do_not_save_grid,  # 是否不保存网格
        script_name=script_name,  # 脚本名称
        send_images=send_images,  # 是否发送图像
        save_images=save_images,  # 是否保存图像
        alwayson_scripts=alwayson_scripts,  # 始终打开的脚本

                        )
    result1.image
    print(result1)
    # 获取第一个图像
    image = result1.images[0]
    image.save(f'output.png')
    image='E:\pythonProject\output.png'



def img2img():
    api = webuiapi.WebUIApi(host='127.0.0.1', port=7860)
    image = Image.open('output.png')
    images = [image]
    result2 = api.img2img(
        images=images,
        prompt=prompt1,  # 正面提示
        negative_prompt=negative_prompt,  # 负面提示
        sampler_name=sampler_name,  # 采样器名称
        batch_size=batch_size,  # 批处理大小
        n_iter=n_iter,  # 迭代次数
        steps=steps,  # 步骤数
        cfg_scale=cfg_scale,  # 配置比例
        width=width,  # 宽度
        height=height,  # 高度
        do_not_save_samples=do_not_save_samples,  # 是否不保存样本
        do_not_save_grid=do_not_save_grid,  # 是否不保存网格
        script_name=script_name,  # 脚本名称
        send_images=send_images,  # 是否发送图像
        save_images=save_images,  # 是否保存图像
        alwayson_scripts=alwayson_scripts,  # 始终打开的脚本
        denoising_strength=denoising_strength

    )
    result2.image
    print(result2)
    # 获取第一个图像
    image = result2.images[0]
    image.save('out1.png')

    os.system('start out1.png')

# 将图像保存到文件
def auto_text2image():
    # 打开文本文件
    i=1
    with open('prompts.txt', 'r') as file:
        # 读取每一行
        for line in file:
            # 去除行尾的换行符
            prompt = line.rstrip('\n')
            i=i+1
            # 使用这一行的内容作为prompt来执行text2img方法
            result = api.txt2img(prompt=prompt)

            # 获取第一个图像
            image = result.images[0]
            image.save(f'output_{i}.png')


#change_models1()
#auto_text2image()

