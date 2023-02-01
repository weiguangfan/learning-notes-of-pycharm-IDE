`当你克隆一个现有的Git仓库，
或将一个现有项目置于Git版本控制之下时，
PyCharm会自动检测你的计算机上是否安装了Git。
如果IDE无法找到Git的可执行文件，它会建议你下载它。
PyCharm支持来自Windows Subsystem for Linux 2（WSL2）的Git，该系统在Windows 10 2004版本中可用。
如果Windows上没有安装Git，PyCharm会在WSL中搜索Git并从那里使用它。
另外，对于使用 \wsl$ 路径打开的项目，PyCharm 会自动从 WSL 切换到 Git。
如果你需要手动配置PyCharm以使用WSL中的Git，
请进入IDE设置的 Version Control | Git页面，按Ctrl+Alt+S，
点击Path to Git executable栏的浏览图标，
通过\wsl$路径选择WSL中的Git，例如\\wsl$\debian\usr\bin\git。`



