- git配置ssh连接github
```
# 有效的邮箱地址 生成ssh key
ssh-keygen -t rsa -C "xxx@yy.com"

# 查看ssh key
cd ~/.ssh 或 cd .ssh -> ls

# github配置ssh key
github->Settings->SSH Keys->Add SSH key->copy id_rsa.pub内容

# 用户配置
git config --global user.name "wd7023"
git config --global user.email "xxx@yy.com"

# 测试github是否联通
ssh -T git@github.com

# 查看系统config信息
git config --system --list

# 查看当前用户（global）配置
git config --global --list

# 查看当前仓库配置信息
git config --local --list
```


- git log
````
# 按q结束，上下键查看
git log

# 单行显示每天日志
git log --oneline

# 显示length条日志
git log -[length]

# 跳过skip条日志显示
git log --skip=[skip]

# 显示每次提交的更多信息
git log --pretty=raw

# 显示提交的改动记录，等价于git show [commit_id]
git log -p

# --graph参数会绘制提交的线索
git log --graph

# 显示每次的文件改动
git log --name-status

# 筛选出yourname用户提交的日志
git log --author yourname

# 从提交的关键字筛选日志
git log --grep keywords

# 根据文件名筛选日志
git log -p fileName.xxx

# 将日志输出到文件
git log --name-status --oneline > logfile.txt

```


