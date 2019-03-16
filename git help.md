git log
---------------
````
## 按q结束，上下键查看
git log

## 单行显示每天日志
git log --onelie

## 显示length条日志
git log -[length]

## 跳过skip条日志显示
git log --skip=[skip]

## 显示每次提交的更多信息
git log --pretty=raw

## 显示提交的改动记录，等价于git show [commit_id]
git log -p

## --graph参数会绘制提交的线索
git log --graph

## 显示每次的文件改动
git log --name-status

## 筛选出yourname用户提交的日志
git log --author yourname

## 从提交的关键字筛选日志
git log --grep keywords

## 根据文件名筛选日志
git log -p fileName.xxx

## 将日志输出到文件
git log --name-status --oneline > logfile.txt

```


