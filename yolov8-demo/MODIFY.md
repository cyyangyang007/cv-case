yolov8源代码修改记录

### 1.载入预训练权重（可选）

- 背景：在yolov8中，只有--model这一个参数设置，且同时允许.pt文件与.yaml文件的接受处理。我们传参时使用.yaml文件，这样才能载入自己设计的网络结构。但如果既更改了模型结构，又想基于预训练权重做迁移学习，这里需要对代码略加改动。  

- 修改：将下面的代码插入ultralytics/engine/model.py: def _new 函数中末尾（如果不想用预训练权重想从0开始，则注释）
```python
ckpt = torch.load('yolov8n.pt') # 这里的pt和train.py时传入的yaml结构要一致
csd = ckpt['model'].float().state_dict()
csd = intersect_dicts(csd,self.model.state_dict())
self.model.load_state_dict(csd,strict=False)
print(f'Transferred {len(csd)}/{len(self.model.state_dict())} items')

# 在顶部导入包：
import torch
from ultralytics.yolo.utils.torch_utils import intersect_dicts
```

### 2.避免二次重载

- 背景：train的时候会重新载入一次模型，用yolo测试模型yaml文件一次，后面又会覆盖一次，所以这里需要修改代码。

- 修改：文件路径ultralytics/engine/model.py: def train

注释三行，新增一行，如图所示
<img width="100%" src="https://github.com/cyyangyang007/cv-case/blob/asset/asset/modify_avoid-orerride.png"></a>

### 3.data.yaml填写相对路径产生的问题

- 不修改时填写相对路径会有类似报错：</n>

>Dataset 'data\data.yaml' images not found ⚠️, missing paths ['E:\workspace\yolov5-test\datasets\data\dataset\val\images']
Note dataset download directory is 'E:\workspace\yolov5-test\datasets'. You can update this in 'C:\Users\Administrator\AppData\Roaming\Ultralytics\settings.yaml'

- 修改：找到ultralytics/utils/__init__.py  

line 581-582: 注释这两行，修改<b>SETTINGS_YAML</b>的地址：</n>

`SETTINGS_YAML = ROOT / 'cfg/settings.yaml'` , 如图

<img width="100%" src="https://github.com/cyyangyang007/cv-case/blob/asset/asset/modify_move-settings.png"></a>

把'C:\Users\Administrator\AppData\Roaming\Ultralytics\settings.yaml'复制粘贴到ultralytics/cfg/目录下，视情况调整文件内容