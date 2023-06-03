# Errors While Reimplementing [Long-Video-GAN](https://github.com/NVlabs/long-video-gan)

## Windows Platform

Using Windows 11 platform, the platform information is shown as below:

```
Currently activated conda environment: lvg.
Current pytorch version is: 2.0.1+cu118.
Current CUDA is available!
Sat Jun  3 08:37:28 2023
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.98                 Driver Version: 535.98       CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                     TCC/WDDM  | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 3090      WDDM  | 00000000:01:00.0  On |                  N/A |
| 36%   37C    P8              24W / 350W |    870MiB / 24576MiB |      2%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+

+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A      4828    C+G   C:\Windows\explorer.exe                   N/A      |
|    0   N/A  N/A      5428    C+G   ...m Files\Mozilla Firefox\firefox.exe    N/A      |
|    0   N/A  N/A      5984    C+G   ...siveControlPanel\SystemSettings.exe    N/A      |
|    0   N/A  N/A      6368    C+G   ...ekyb3d8bbwe\PhoneExperienceHost.exe    N/A      |
|    0   N/A  N/A      7140    C+G   ...2txyewy\StartMenuExperienceHost.exe    N/A      |
|    0   N/A  N/A      8880    C+G   ...nt.CBS_cw5n1h2txyewy\SearchHost.exe    N/A      |
|    0   N/A  N/A     10100    C+G   ...on\113.0.1774.57\msedgewebview2.exe    N/A      |
|    0   N/A  N/A     10456    C+G   ...t.LockApp_cw5n1h2txyewy\LockApp.exe    N/A      |
|    0   N/A  N/A     11268    C+G   ...CBS_cw5n1h2txyewy\TextInputHost.exe    N/A      |
|    0   N/A  N/A     12672    C+G   ...0.0_x64__p7pnf6hceqser\snipaste.exe    N/A      |
|    0   N/A  N/A     12824    C+G   ...61.0_x64__8wekyb3d8bbwe\GameBar.exe    N/A      |
|    0   N/A  N/A     13480    C+G   ...m Files\Mozilla Firefox\firefox.exe    N/A      |
|    0   N/A  N/A     13768    C+G   ...GeForce Experience\NVIDIA Share.exe    N/A      |
|    0   N/A  N/A     13964    C+G   C:\Windows\explorer.exe                   N/A      |
|    0   N/A  N/A     15888    C+G   ...Programs\Microsoft VS Code\Code.exe    N/A      |
|    0   N/A  N/A     17328    C+G   ...__8wekyb3d8bbwe\WindowsTerminal.exe    N/A      |
|    0   N/A  N/A     18000    C+G   ...__8wekyb3d8bbwe\WindowsTerminal.exe    N/A      |
+---------------------------------------------------------------------------------------+

nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Thu_Feb_10_19:03:51_Pacific_Standard_Time_2022
Cuda compilation tools, release 11.6, V11.6.112
Build cuda_11.6.r11.6/compiler.30978841_0
```

### Errors:

1. Running the following command after installing all the required environments:

```bash
python generate.py --outdir=outputs/horseback --seed=49 --lres=https://nvlabs-fi-cdn.nvidia.com/long-video-gan/pretrained/horseback_lres.pkl --sres=https://nvlabs-fi-cdn.nvidia.com/long-video-gan/pretrained/horseback_sres.pkl
```

Error output:

```
Setting up PyTorch plugin "bias_act_plugin"... Failed!
ImportError: DLL load failed while importing bias_act_plugin: The specified module could not be found.
```

Mysteriously Solved: After 1 day without doing anything.


## Linux Platform


### Errors:

1. Running the following command for installing the environments:

```bash
conda env create -f environment.yml -n lvg
```

Error output:

```
Cuda not compatible.
```