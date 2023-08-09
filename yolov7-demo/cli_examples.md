More detail see https://github.com/WongKinYiu/yolov7/blob/main/README.md

## Transfer learning
Single GPU finetuning for custom dataset
``` shell
# finetune p5 models
python train.py --workers 4 --device 0 --batch-size 16 --data data/data.yaml --img 640 640 --cfg cfg/training/yolov7-tiny.yaml --weights 'weights/yolov7_training.pt' --name yolov7-custom --hyp data/hyp.scratch.tiny.yaml

# finetune p6 models
python train_aux.py --workers 4 --device 0 --batch-size 16 --data data/data.yaml --img 1280 1280 --cfg cfg/training/yolov7-tiny.yaml --weights 'weights/yolov7-tiny.pt' --name yolov7-custom --hyp data/hyp.scratch.tiny.yaml
```

## Evaluation
旨在获得验证数据集上的最佳 mAP
``` shell
python test.py --data data/data.yaml --img 640 --batch 32 --conf 0.001 --iou 0.65 --device 0 --weights runs/train/exp5/weights/best.pt --name yolov7_val
```

# Inference
旨在真实世界中获得最佳的推理结果  
On video:
``` shell
python detect.py --weights runs/train/exp5/weights/best.pt --conf 0.25 --img-size 640 --source yourvideo.mp4
```
On image:
``` shell
python detect.py --weights runs/train/exp5/weights/best.pt --conf 0.25 --img-size 640 --source data/test/images/
```

## Export
**Pytorch to ONNX with NMS (and inference)**
```shell
# pip install onnx

python export.py --weights yolov7-tiny.pt --grid --end2end --simplify \
        --topk-all 100 --iou-thres 0.65 --conf-thres 0.35 --img-size 640 640 --max-wh 640
```