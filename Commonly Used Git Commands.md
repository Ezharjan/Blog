1. 不删除工作空间改动代码，撤销 commit，不撤销 git add .
```bash
git reset --soft HEAD~1
```

2. 将所有工作撤回到git add之前
```bash
git reset .
```


3. 执行下述命令来储藏以迁移master分支下的修改到dev分支：
```bash
git stash
```

4. 先切换到dev分支下：
```bash
git checkout dev
```

5. 然后，取出之前储藏的修改：
```bash
git stash pop
```


6. 查看储藏记录列表
```bash
git stash list
```

7. 可以通过下述命令来标记此次储藏，以便后期查看
```bash
git stash save [stashMessage]
```


8. 前文提到的可以通过git stash pop用于取出最近一次储藏的修改到工作区，而通过查看储藏列表的index的可以取出指定储藏中的修改到工作区
```bash
# 取出指定index的储藏的修改到工作区中
git stash apply stash@{index} 
# 将指定index的储藏从储藏记录列表中删除
git stash drop stash@{index}
```