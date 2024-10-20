# Invisibility-Cloak-Proactive-Defense-Against-Visual-Game-Cheating
"Invisibility Cloak" introduces a pioneering proactive defense against FPS game cheating by adding imperceptible perturbations to game visuals, rendering them undetectable to visual aimbots. Tested on popular games like CrossFire and Counter-Strike 2, it effectively blocks cheating behaviors in real-time without compromising visual quality, significantly improving the gaming experience for legitimate players. Explore our project here.

## Open-source Dataset
We open-source our dataset in the paper! Please download from the dataset here:[Game Cheat Dataset](https://drive.google.com/file/d/1MDqzO62xe4-qrpcOfdCEb5oBHq_Q783v/view?pli=1)

## Dataset Structure
```
├── CF 
│   └── <Scenarios> # For CF dataset.
│       └── <Actions Index>
│           └── <Frames> # **.png
├── CS2 
│   └── <Scenarios> # For CS2 dataset.
│       └── <Actions Index>
│           └── <Frames> # **.png
├── dataloader.py # for PyTorch data loader
└── stat.csv # Statistics of the dataset
## Citation

If you find this benchmark helpful for your research, please cite our paper:
```bib
@inproceedings{sun2024invisibility,
  title={Invisibility Cloak: Proactive Defense Against Visual Game Cheating},
  author={Sun, Chenxin and Ye, Kai and Su, Liangcai and Zhang, Jiayi and Qian, Chenxiong},
  booktitle={33rd USENIX Security Symposium (USENIX Security 24)},
  pages={3045--3061},
  year={2024}
}
```
