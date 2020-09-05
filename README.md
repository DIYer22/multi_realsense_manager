# 鲁棒, 可复用的多 realsense 控制脚本

## 特性
- [x] 对 realsense 良好的鲁棒性
    - 能解决常见错误
    - 支持拔了 USB 再插, 程序接着运作
- [x] 易用的接口
    - 补充: 由于 realsense 配置项本身的复杂性, 很难做到更加简洁
- [x] 支持多进程
- [x] 高可复用
- [x] 灵活, 原汁原味的配置项
- [ ] 系统级重启 USB

## 使用方式

Demo:
```
python multi_realsense_manager/multi_realsense_manager.py
```
使用说明见 "multi_realsense_manager/multi_realsense_manager.py" 代码里的注释
