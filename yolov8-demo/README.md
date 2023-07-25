# yolov8训练自己的数据集（win10本地精简版）

## 流程
0.配置环境（下载ultralytics库、pytorch相关依赖、clone项目、配置gpu训练支持）
1.处理数据集：
  1）收集数据，保存在images
  2）标注数据，保存在labels
  3）格式转换，xml2txt.py
  4）拆分数据集，split_dateset.py
  处理后的目录结构：
    datasets
        |_____train   ## 该文件夹下存放训练集
        |        |____images
        |        |____labels 
        |
        |_____val     ## 该文件夹下存放验证集
        |        |____images
        |        |____labels
        |
        |_____test    ## 该文件夹下存放测试集
        |        |____images
        |        |____labels
2.训练模型 python train.py
3.验证模型 训练过程中验证
4.测试模型 python predict.py 


## 数据集按格式准备好后，对工程代码进行修改，注意检查
- data/class.yaml：nc、names
- xml2txt.py：CLASSES
- train.py：训练参数
- predict.py: 用训练得到的最佳模型做预测，修改测试的图片路径