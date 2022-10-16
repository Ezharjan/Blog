# Public Blog

<br>

## Brief Instruction
1. `hexo new "file name"`
2. `hexo g`
2. `hexo s`
3. `lua deployer`


<br>
<br>
<br>


## Tutorial

1. `git clone this-repo`
2. `npm i`
3. `hexo new "file name"`
4. `hexo clean` then `hexo s` to view in local serve page
5. Revise blog contents.
6. Unzip and place the `lua-5.3.6_Win32_bin` into your system environment in order to use some automatic tools.
7. Then run `lua deployer` in this folder, or conduct the following commands in console to deploy and push.

<br>

_DO NOT DELETE ANY CONFIGS IN `config.yml`， otherwise you have to unzip `hexo-asset-image.7z` in root folder then move it into the folder of `node_modules` to replace the old ones._

<br>
<br>
<br>
<br>
<br>
<br>
<br>

---

## Reference

1. [Referenced](https://kaiter-plus.gitee.io/2020/03/07/How_To_Freely_Build_Blog/)

<br>

2. [Relate Hexo with Gitee](https://blog.csdn.net/chffy0/article/details/107301792)

<br>


3. Correction of the content above('2.')

<br>

```bash

# Deployment
## Docs: https://hexo.io/docs/one-command-deployment
deploy:
  type: git
  repo: git@gitee.com:softwarelab/softwarelab.git
  branch: master
```


<br>
<br>


1. [Install Hexo-Git-Deployer](https://www.xiongtianci.com/2019/05/15/hexo-d%E5%91%BD%E4%BB%A4%E6%8A%A5%E9%94%99%EF%BC%9AERROR-Deployer-not-found-git/)

<br>

5. [Solved Git Problem](https://blog.csdn.net/fvdfsdafdsafs/article/details/106240185)

<br>

6. Use another repositry to deploy the final `public` webpage as the 'public' folder would be regenerated and all of the files in it will finally be removed after regeneration.

# Finally Successful

1. The more important and convenient methods are shown in blogs of [Tutorial1-Hexo-Gitee-BlogConstruction](https://softwarelab.gitee.io/blogeditor/Tutorial1-Hexo-Gitee-BlogConstruction.html) and [Tutorial2-Hexo-Blog-Image-Problem](https://softwarelab.gitee.io/blogeditor/Tutorial2-Hexo-Blog-Image-Problem.html) in this repository. 
2. About solving the [Image Problem](https://blog.csdn.net/qq_42009500/article/details/118788129). And the usable version of `hexo-asset-image` is also placed in this repository for your convenience, find it as `hexo-asset-image.7z` and replace your version if the problem of image still happens. 


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<p align=right>by Alexander Ezharjan</p>
<p align=right>13th Feb, 2022</p>
