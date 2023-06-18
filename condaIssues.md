# Conda Related Issues

1. View existing Conda environment:
```bash
conda info --envs
conda env list
```

2. Create new environment
```bash
conda create -n ENV_NAME python=3.7 -y
```

3. Activate new environment on Windows:
```bash
activate ENV_NAME
```

4. Remove some installed environment:
```bash
conda remove -n ENV_NAME --all -y
```


5. Clone one conda environment to another:
```bash
conda create -n new_env --clone template_env -y
```


6. Change Python version in current Conda environment:
```bash
conda install python=3.7
```

7. Use `conda activate env_name` command inside a bash file on Linux: 
```bash


conda activate env_name
```

8. 
```bash

```




<br>
<br>

[Download Andoconda](https://www.anaconda.com/)