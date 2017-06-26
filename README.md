# startup
命令行启动程序,可以配置需要启动的可执行文件然后通过命令快速启动.

# 如何使用？
```git
git clone https://github.com/284885166/startup.git
```
#进入工程目录执行以下命令，如果需要全局使用命令则要配置环境变量
```shell
startup list 查询可运行的程序列表
startup add [name] [exeName] [path] 添加一条可运行程序
startup delete [name] 删除一条可运行程序
startup set [name] [exeName] [path] 修改一条可运行程序
startup start [name] 启动程序
```
