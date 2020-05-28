### 说明

稍微弄了一下结构，然后把宇神的login和register模块放了进去，其他的没有动。test.py为测试文件，没法直接运行，看看就好了。

### 运行

直接在该md文件所在目录运行下面的指令即可

```
flask run
```

### 环境

我是在python3虚拟环境下搞得，所以导出了一份requirements清单，如果也想在虚拟环境下进行开发，可以执行以下命令

```python
# 创建虚拟环境
python -m venv venv
# 激活进入虚拟环境
venv\scripts\activate
# 安装相应模块
pip install -r requirements.txt
```

当然也可以直接在本机python环境下开发，就直接执行上文的最后一条语句即可。

### 注意

运行flask run的时候，因为和mysql的连接以及ssh的连接，没法使用ctrl+c来退出，只能点击命令行右上角的x按钮退出。