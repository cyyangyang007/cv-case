# yolov5训练自己的数据集-python版（win10本地速通教程）
>本仓库仅抽取了训练所需的基础文件，旨在快速开启第一步
>项目在python3.6环境下实测通过，各依赖对应版本见requirements.txt
>官方github：git clone https://github.com/ultralytics/yolov5

## 流程
0. 配置环境  
    - Clone本项目
    - 配置GPU训练环境
        + 检查显卡驱动（版本太旧下载[更新](https://www.nvidia.cn/Download/index.aspx?lang=cn)）：`nvidia-smi`  
        + 安装对应版本CUDA[下载exe](https://developer.nvidia.com/cuda-toolkit-archive)  
        + 配置CUDNN，需要注册登录[下载](https://developer.nvidia.cn/rdp/cudnn-archive)  
            * 解压后复制到C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1里  
            * 环境变量下方的path中添加bin、include、lib、libnvvp四个子目录
        + （非必要）新建python本地虚拟环境  
            * `cd <工程目录>`  
            * `python -m venv <环境名称>`  
            * 激活虚拟环境：`.\<环境名称>\Scripts\activate` (退出用 `deactivate`)  
    - 批量安装依赖  
        + pytorch-gpu建议离线安装，防止安装过程中断[whl文件下载](https://download.pytorch.org/whl/torch_stable.html)  
            * 本地使用的是torch-2.0.0+cu118和torchvision-0.15.0+cu118  
        + 其余依赖对应版本见requirements.txt
            * `cd <requirements.txt所在目录>`  
            * `pip install -r requirements.txt`  
        + 检查已安装的库 `pip freeze`

1. 处理数据集：`cd data`  
    - 修改data.yaml：path、nc、names
    - 收集数据，保存在images/
        + 统一文件后缀如jpg，png
    - 标注数据，保存在labels/
    - 处理数据（注意修改参数）
        + 确认数据集的classes：`python find_classes.py`  
        + VOC转YOLO格式(新增txt目录)：`python xml2txt.py`  
        + 拆分数据集（train、val、test）：`python split_dateset.py`  
            * 示例仅放了7张图，拆分时可能产生空集
        + 修改模型输出类别的个数，打开cfg/yolov5.yaml，修改nc

2. 使用模型：use.py  
train、val、test、export语句都在其中，更多用例参考对应的py文件
