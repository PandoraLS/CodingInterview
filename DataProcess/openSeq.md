# OpenSeq2Seq 搭建

## docker 安装

省略...

## nvidia-docker 安装

[github](https://github.com/NVIDIA/nvidia-docker)

```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```

## 注册 NGC(NVIDIA GPU Container) 账号

需要用到一个`docker`镜像,必须注册

+ 安装[NGC CLI](https://ngc.nvidia.com/setup/installers/cli)
+ 获取密钥配置本地账号信息[api-key](https://ngc.nvidia.com/setup/api-key)

显示登录成功就好了

## 本地代码clone

```bash
git clone https://github.com/NVIDIA/OpenSeq2Seq.git
```

## 镜像下载与容器运行

### 下载

```bash
docker pull nvcr.io/nvidia/tensorflow:19.05-py3
```

### 创建容器

```bash
docker run --name open --gpus all -v /path/to/data:/path/to/mount/ --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 -it -d nvcr.io/nvidia/tensorflow:19.05-py3
```

+ `--name` 指定容器名字
+ `-v` 表示挂载主机目录到容器中,存放代码
+ `-it` 表示交互
+ `-d` 表示永久运行
+ `--gups` gpu使用

把代码目录与数据集目录挂载到相应路径下。不出意外的话，使用如下如下命令查看：

```bash
docker container ps -a
```
将会看到自己的容器。然后进入容器：

```bash
docker exec -it open bash
```

open是你的容器名字，输入 `nvidia-smi`,检查是否有如下输出
```
Sat Feb 29 13:48:40 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 430.64       Driver Version: 430.64       CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce RTX 2060    Off  | 00000000:01:00.0  On |                  N/A |
| 34%   33C    P8    12W / 170W |    454MiB /  5931MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
+-----------------------------------------------------------------------------+
```

## run

先下载一点点`librispeech`数据集测试，再修改数据集路径，网络参数，vocab路径等基本配置。
1. 修改下载脚本 `openseq2seq/scripts/import_librivox.py`,，使用小数据集测试。
2. 配置文件 `example_configs/speech2text/jasper-Mini-for-Jetson.py`,修改数据集路径与 batchsize 等。`"vocab_file": "open_seq2seq/test_utils/toy_speech_data/vocab.txt",`

run：
```
python run.py --config_file=example_configs/speech2text/jasper-Mini-for-Jetson.py --mode=train_eval --enable_logs
```

还需要再安装几个package
docker 常见命令
docker container start open_lisen
docker container stop open
docker exec -it open_lisen bash
docker container ps -a
docker rm open_lisen

