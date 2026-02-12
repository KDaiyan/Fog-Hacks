## FogHacks -- [YOLOv10 Fork Specialized for Fog-based Object Detection](https://github.com/THU-MIG/yoloe)


This specialized YOLOv10 model is tailored towards fast, real-time object detection for foggy environments. While the base YOLOv10 model  already provides proficient detection capabilities, this version is refined to improve accuracy and reliability specifically in foggy settings. The model is trained on a high-performance computing unit (HPC) and then used on a Raspberry Pi for inference. The system on the Pi will continuously poll for camera images and return outputs such as object bounds, risk percentages, and confidence scores.


## Installation
`conda` virtual environment is recommended but not necessary.\
`python 3.9` minimum is required.  

This set up is intended for local machine and the HPC. It will work on Raspberry Pi as well, however, the intention is to import the specialized model from Hugging Face  on the Pi instead.

```
conda create -n foghacks python=3.9
conda activate foghacks
python install.py
```

## Acknowledgement

The code base is built with [ultralytics](https://github.com/ultralytics/ultralytics) and [RT-DETR](https://github.com/lyuwenyu/RT-DETR).

Thanks for the great implementations! 

## Citation

If our code or models help your work, please cite our paper:
```BibTeX
@article{wang2024yolov10,
  title={YOLOv10: Real-Time End-to-End Object Detection},
  author={Wang, Ao and Chen, Hui and Liu, Lihao and Chen, Kai and Lin, Zijia and Han, Jungong and Ding, Guiguang},
  journal={arXiv preprint arXiv:2405.14458},
  year={2024}
}
```