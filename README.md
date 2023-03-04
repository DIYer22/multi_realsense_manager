# 简洁, 鲁棒的多 realsense 控制库
## 特性
- **易用**的 Pythonic 接口:
   - 采用面向对象封装, 方便多相机管理
   - 支持 `with` 语法来调用: `with MultiRealsenseManger() as cams:`
   - 数据为 Python 和 numpy 数据格式
- 对 realsense 良好的鲁棒性
    - 能处理常见的错误, 遇到特殊异常会自动 hardware_reset
    - 拔了 USB 程序会阻塞, 重新插入 USB 后, 程序会接着运作
- 易用的配置接口
    - 基于重写类的方法(override method)来实现控制接口
    - 由于 realsense 配置项本身的复杂性, 很难做到更加简洁
- 支持多进程处理多个 realsense
    - 在低端赛扬 CPU 或树莓派上, 时延能降低 50%

## 使用方式

1. Install:
```
pip install multi_realsense_manager
```
2. Demo:
```
python multi_realsense_manager/multi_realsense_manager.py
```
使用说明见 ["multi_realsense_manager/multi_realsense_manager.py"](multi_realsense_manager/multi_realsense_manager.py#L317-371) 代码里的注释

3. 查看 realsense 个数及其 SN/ID:
```
python -c 'print(__import__("multi_realsense_manager").MultiRealsenseManger.get_all_snids())'
```