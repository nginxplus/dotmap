组建版本：
Python 2.7.11
Django (1.10.1)
echarts 3

根据Nginx的access.log日志。来进行访问量统计，结果反馈到地图的原点上。

整体架构非常简单，后端采集程序collection.py定期写入数据到data.db。

后端接口：http://127.0.0.1:8000/api/<YYYYmmdd>

前端通过Ajaxs异步读取接口数据进行渲染。

效果图：
![promisechains](https://raw.githubusercontent.com/Leon2018/dotmap/master/%E6%95%88%E6%9E%9C%E5%9B%BE.png)
