# BadRefSR.
Official PyTorch implementation of the paper BadRefSR: Backdoor Attacks Against Reference-based Image Super Resolution.

# Introduction.
We propose a novel attack framework called BadRefSR, which embeds backdoors in the Reference-based image super-resolution(RefSR) model by adding triggers to the reference images and training with a mixed loss function.

# Dataset.
We provide CUFED datasets and the CUFED5 test set with triggers.[Baidu](https://pan.baidu.com/s/1EWXwFtcopcWMsiAoWpgFdw?pwd=qsi3) [Google](https://drive.google.com/file/d/1wQUqgs8getFiyys9jGHbUgwoEhjIxQpU/view?usp=drive_link)

# Model.
We have conducted experiments of BadRefSR on two RefSR models, TTSR [Learning Texture Transformer Network for Image Super-Resolution](https://arxiv.org/abs/2006.04139) and MASA-SR [MASA-SR: Matching Acceleration and Spatial Adaptation for Reference-Based Image Super-Resolution](https://arxiv.org/abs/2106.02299).

# the pretrained weight file.
We provide the pretrained weight file at a poisoning rate of 20% .[Baidu](https://pan.baidu.com/s/1wLkvxT-ht-T4Cw6PX0NE1Q?pwd=p9uy) [Google](https://drive.google.com/file/d/1Srm2wnxwirN9iD7f-MaF0u0pmd0BW8Wy/view?usp=drive_link)

## Acknowledgement
We borrow these codes for our work.[TTSR](https://github.com/researchmm/TTSR) and [MASA-SR](https://github.com/dvlab-research/MASA-SR). We thank the authors for their great work.
