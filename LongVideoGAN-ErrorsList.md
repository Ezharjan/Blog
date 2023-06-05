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

### Causes & Errors:

1. Cause: Running the following command after installing all the required environments:

```bash
python generate.py --outdir=outputs/horseback --seed=49 --lres=https://nvlabs-fi-cdn.nvidia.com/long-video-gan/pretrained/horseback_lres.pkl --sres=https://nvlabs-fi-cdn.nvidia.com/long-video-gan/pretrained/horseback_sres.pkl
```

Error output:

```
Setting up PyTorch plugin "bias_act_plugin"... Failed!
ImportError: DLL load failed while importing bias_act_plugin: The specified module could not be found.
```

Mysteriously Solved: After 1 day without doing anything.


2. Cause: Try to train my own model based on the dataset made by the video from my previously developed application called Traffic Editor:

```bash
python -m torch.distributed.run --nnodes=1 --nproc_per_node=8 train_lres.py --outdir=runs/lres --dataset=datasets --batch=64 --grad-accum=20 --gamma=1.0 --metric=fvd2048_128f > error_train.log 2>&1
```
Error output:
```
NOTE: Redirects are currently not supported in Windows or MacOs.
WARNING:__main__:
*****************************************
Setting OMP_NUM_THREADS environment variable for each process to be 1 in default, to avoid your system being overloaded, please further tune the variable for optimal performance in your application as needed. 
*****************************************
[W ..\torch\csrc\distributed\c10d\socket.cpp:601] [c10d] The client socket has failed to connect to [DESKTOP-63Q8UGP]:29500 (system error: 10049 - The requested address is not valid in its context.).
[W ..\torch\csrc\distributed\c10d\socket.cpp:601] [c10d] The client socket has failed to connect to [DESKTOP-63Q8UGP]:29500 (system error: 10049 - The requested address is not valid in its context.).
Traceback (most recent call last):
  File "D:\Projects\long-video-gan\train_lres.py", line 356, in <module>
Traceback (most recent call last):
  File "D:\Projects\long-video-gan\train_lres.py", line 356, in <module>
    main()
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1128, in __call__
    main()
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1128, in __call__
    return self.main(*args, **kwargs)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1053, in main
    return self.main(*args, **kwargs)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1053, in main
    rv = self.invoke(ctx)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1395, in invoke
    rv = self.invoke(ctx)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1395, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 754, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 754, in invoke
    return __callback(*args, **kwargs)
  File "D:\Projects\long-video-gan\train_lres.py", line 323, in main
    distributed.init(temp_dir)
  File "D:\Projects\long-video-gan\torch_utils\distributed.py", line 56, in init
    return __callback(*args, **kwargs)
  File "D:\Projects\long-video-gan\train_lres.py", line 323, in main
    torch.cuda.set_device(get_local_rank())
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\cuda\__init__.py", line 350, in set_device
    distributed.init(temp_dir)
  File "D:\Projects\long-video-gan\torch_utils\distributed.py", line 56, in init
    torch.cuda.set_device(get_local_rank())
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\cuda\__init__.py", line 350, in set_device
    torch._C._cuda_setDevice(device)
RuntimeError: CUDA error: invalid device ordinal
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

    torch._C._cuda_setDevice(device)
RuntimeError: CUDA error: invalid device ordinal
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

Traceback (most recent call last):
  File "D:\Projects\long-video-gan\train_lres.py", line 356, in <module>
    main()
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1128, in __call__
    return self.main(*args, **kwargs)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1053, in main
    rv = self.invoke(ctx)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1395, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 754, in invoke
    return __callback(*args, **kwargs)
  File "D:\Projects\long-video-gan\train_lres.py", line 323, in main
    distributed.init(temp_dir)
  File "D:\Projects\long-video-gan\torch_utils\distributed.py", line 56, in init
    torch.cuda.set_device(get_local_rank())
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\cuda\__init__.py", line 350, in set_device
    torch._C._cuda_setDevice(device)
RuntimeError: CUDA error: invalid device ordinal
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

Traceback (most recent call last):
  File "D:\Projects\long-video-gan\train_lres.py", line 356, in <module>
    main()
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1128, in __call__
    return self.main(*args, **kwargs)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1053, in main
    rv = self.invoke(ctx)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1395, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 754, in invoke
    return __callback(*args, **kwargs)
  File "D:\Projects\long-video-gan\train_lres.py", line 323, in main
    distributed.init(temp_dir)
  File "D:\Projects\long-video-gan\torch_utils\distributed.py", line 56, in init
    torch.cuda.set_device(get_local_rank())
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\cuda\__init__.py", line 350, in set_device
    torch._C._cuda_setDevice(device)
RuntimeError: CUDA error: invalid device ordinal
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

Traceback (most recent call last):
  File "D:\Projects\long-video-gan\train_lres.py", line 356, in <module>
    main()
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1128, in __call__
    return self.main(*args, **kwargs)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1053, in main
    rv = self.invoke(ctx)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1395, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 754, in invoke
    return __callback(*args, **kwargs)
  File "D:\Projects\long-video-gan\train_lres.py", line 323, in main
    distributed.init(temp_dir)
  File "D:\Projects\long-video-gan\torch_utils\distributed.py", line 56, in init
    torch.cuda.set_device(get_local_rank())
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\cuda\__init__.py", line 350, in set_device
    torch._C._cuda_setDevice(device)
RuntimeError: CUDA error: invalid device ordinal
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

Traceback (most recent call last):
  File "D:\Projects\long-video-gan\train_lres.py", line 356, in <module>
    main()
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1128, in __call__
    return self.main(*args, **kwargs)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1053, in main
    rv = self.invoke(ctx)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1395, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 754, in invoke
    return __callback(*args, **kwargs)
  File "D:\Projects\long-video-gan\train_lres.py", line 323, in main
    distributed.init(temp_dir)
  File "D:\Projects\long-video-gan\torch_utils\distributed.py", line 56, in init
    torch.cuda.set_device(get_local_rank())
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\cuda\__init__.py", line 350, in set_device
    torch._C._cuda_setDevice(device)
RuntimeError: CUDA error: invalid device ordinal
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

Traceback (most recent call last):
  File "D:\Projects\long-video-gan\train_lres.py", line 356, in <module>
    main()
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1128, in __call__
    return self.main(*args, **kwargs)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1053, in main
    rv = self.invoke(ctx)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 1395, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\click\core.py", line 754, in invoke
    return __callback(*args, **kwargs)
  File "D:\Projects\long-video-gan\train_lres.py", line 323, in main
    distributed.init(temp_dir)
  File "D:\Projects\long-video-gan\torch_utils\distributed.py", line 56, in init
    torch.cuda.set_device(get_local_rank())
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\cuda\__init__.py", line 350, in set_device
    torch._C._cuda_setDevice(device)
RuntimeError: CUDA error: invalid device ordinal
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

WARNING:torch.distributed.elastic.multiprocessing.api:Sending process 13452 closing signal CTRL_C_EVENT
WARNING:torch.distributed.elastic.agent.server.api:Received 2 death signal, shutting down workers
WARNING:torch.distributed.elastic.multiprocessing.api:Sending process 13452 closing signal SIGINT
WARNING:torch.distributed.elastic.multiprocessing.api:Sending process 13452 closing signal SIGTERM
Traceback (most recent call last):
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\agent\server\api.py", line 723, in run
    result = self._invoke_run(role)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\agent\server\api.py", line 865, in _invoke_run
    run_result = self._monitor_workers(self._worker_group)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\metrics\api.py", line 129, in wrapper
    result = f(*args, **kwargs)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\agent\server\local_elastic_agent.py", line 306, in _monitor_workers
    result = self._pcontext.wait(0)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\multiprocessing\api.py", line 288, in wait
    return self._poll()
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\multiprocessing\api.py", line 664, in _poll
    self.close()  # terminate all running procs
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\multiprocessing\api.py", line 331, in close
    self._close(death_sig=death_sig, timeout=timeout)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\multiprocessing\api.py", line 708, in _close
    handler.proc.wait(time_to_wait)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\subprocess.py", line 1209, in wait
    return self._wait(timeout=timeout)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\subprocess.py", line 1506, in _wait
    result = _winapi.WaitForSingleObject(self._handle,
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\multiprocessing\api.py", line 62, in _terminate_process_handler
    raise SignalException(f"Process {os.getpid()} got signal: {sigval}", sigval=sigval)
torch.distributed.elastic.multiprocessing.api.SignalException: Process 23100 got signal: 2

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\run.py", line 798, in <module>
    main()
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\multiprocessing\errors\__init__.py", line 346, in wrapper
    return f(*args, **kwargs)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\run.py", line 794, in main
    run(args)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\run.py", line 785, in run
    elastic_launch(
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\launcher\api.py", line 134, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\launcher\api.py", line 241, in launch_agent
    result = agent.run()
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\metrics\api.py", line 129, in wrapper
    result = f(*args, **kwargs)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\agent\server\api.py", line 730, in run
    self._shutdown(e.sigval)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\agent\server\local_elastic_agent.py", line 289, in _shutdown
    self._pcontext.close(death_sig)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\multiprocessing\api.py", line 331, in close
    self._close(death_sig=death_sig, timeout=timeout)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\multiprocessing\api.py", line 701, in _close
    handler.close(death_sig=death_sig)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\site-packages\torch\distributed\elastic\multiprocessing\api.py", line 587, in close
    self.proc.send_signal(death_sig)
  File "C:\ProgramData\Anaconda3\envs\lvg\lib\subprocess.py", line 1581, in send_signal
    raise ValueError("Unsupported signal: {}".format(sig))
ValueError: Unsupported signal: 2

```


*Unsolved yet.*



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