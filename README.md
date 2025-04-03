# LMQFormer: A Laplace-Prior-Guided Mask Query Transformer for Lightweight Snow Removal <br> (Accepted by IEEE TCSVT)

<img src=".\img\result.png" alt="result" style="zoom:50%;" />


Qualitative results on synthetic datasets. From top to bottom rows: Snow100K, SRRS, CSD, SnowKitti2012, and SnowCityScapes. Please zoom in for better visual quality.

# Abstract:

Snow removal aims to locate snow areas and recover clean images without repairing traces. Unlike the regularity and semitransparency of rain, snow with various patterns and degradations seriously occludes the background. As a result, state-of-the-art snow removal methods usually retain a large parameter size. In this work, a lightweight yet highly efficient snow removal network called Laplace Mask Query Transformer (LMQFormer) is proposed by Lin, Junhong; Jiang, Nanfeng; Zhang, Zhentao; Chen, Weiling; and Zhao, Tiesong.

In snowy environments, surveillance through drones, helicopters, and stationary cameras faces a critical challenge—snow accumulation on camera lenses and snowy images, which severely obstructs visibility. To address this issue, the LMQFormer model is leveraged for real-time snow removal, ensuring clearer images for improved surveillance and monitoring.

To deploy this solution effectively on edge devices such as drones, the model is converted to ONNX format and optimized for efficient inference. Qualcomm AI Hub is used for compiling and profiling the model, ensuring it runs seamlessly on resource-constrained IoT devices.


Experimental results on popular datasets demonstrate the efficiency of the model, achieving state-of-the-art snow removal quality with significantly reduced parameters and the lowest running time.
[[Paper Download]]([LMQFormer: A Laplace-Prior-Guided Mask Query Transformer for Lightweight Snow Removal | IEEE Journals & Magazine | IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/10092769))

# Network Architecture

<img src=".\img\network.png" alt="network" style="zoom:50%;" />


# Setup and environment

#### To generate the recovered result you need:

1. Python 3.7
2. CPU or NVIDIA GPU + CUDA CuDNN
3. Pytorch 1.8.0
4. python-opencv

#### Testing

The model is trained on five snow removal datasets, including Snow100K, SRRS, CSD, SnowKitti2012 and SnowCityScapes.

Please replace weights_dir data_dir and result_dir in test.py, and put your testset in data_dir.

#### Pre-trained model
It can be downloaded from：

Link:  https://drive.google.com/drive/folders/1WiFnUh6WRIiFr7sb-h3lAcoqzi6ZyTvz?usp=sharing 

# Qualcomm Ai hub
The model has been compiled and profiled in Qualcomm AI Hub to optimize its performance on specific chipsets such as QC8550. 
This ensures efficient execution by leveraging hardware acceleration and optimizing resource utilization. 
A link to Qualcomm AI Hub is also provided: https://aihub.qualcomm.com/

# Citations

Bibtex:
```
@ARTICLE{10092769,
  author={Lin, Junhong and Jiang, Nanfeng and Zhang, Zhentao and Chen, Weiling and Zhao, Tiesong},
  journal={IEEE Transactions on Circuits and Systems for Video Technology}, 
  title={LMQFormer: A Laplace-Prior-Guided Mask Query Transformer for Lightweight Snow Removal}, 
  year={2023},
  volume={33},
  number={11},
  pages={6225-6235},
  doi={10.1109/TCSVT.2023.3264824}}

```
