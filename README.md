原理和原因:
1.调用的https://aistudio.baidu.com/aistu ... 385?forkThirdPart=1开源识别模型,这个是已经训练好的本地模型
2.然后使用cv2读取视频每一帧的图片,并且计算时间截
3.因为涉及到很多的运算和人工智能方面的东西,所以不能打包成exe,涉及到的库过分复杂,打包后可能有几个G,过分夸张

和我之前帖子的字幕提取有啥区别呢?
1.之前的需要提供字幕区域,这个不需要
2.之前的必须要有百度开发者的ak和sk才能联网调用(而且还有网络限制,所以容易漏掉)
3.之前的属于调用人家给的网络api,,这个是调用模型,高大上了一些.并且准确程度是有保证的,还可以自己训练
4.之前的识别全屏,几乎不可能,而且速度很慢,为啥呢?因为全屏的图片很大,发送到百度这个过程很久,而且不稳定.
视频字幕提取神器,你不会还在用手记笔记吧?支持所有视频!
https://www.52pojie.cn/thread-1347904-1-1.html
(出处: 吾爱破解论坛)


使用方法:
1.安装python3 64位的
2.安装以下支持库(有基础的不会看不懂吧):
pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
pip install paddlehub --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install shapely -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyclipper -i https://pypi.tuna.tsinghua.edu.cn/simple
3.如果是使用了Anaconda环境的,那就去你的Anaconda环境中文件搜索geos_c.dll 和geos.dll   然后把geos_c.dll拷贝放入Anaconda3\Library\bin目录中
4.设置配置文件  打开 配置.txt 然后按照你的需求和实际情况填写设置(大部分保持默认就行)

视频地址="下载.mp4"
判断帧间隔="60"
识别结果保存目录="test.txt"
是否可视化="是"
精准识别="否"
GPU="否"
注意(请在引号里面修改内容,不要去改变格式):
1.精准识别不建议开启,必须电脑非常好并且GPU填是才能使用,不然速度很慢!
2.如果开始可视化,则会有识别过程显示,并且会在ocr_result中把图片文件保存
3.gpu如果电脑差,开启有时候会比不开慢...
4.判断帧决定多少帧去识别一次,所以大概是帧率的2倍就可以了,如果碰到说话慢的就可以多加点
5.识别结果都是累加的结果,所以请手动清空,或者改文件名
6.视频地址就是你的视频的文件名和目录
5.直接使用命令行调用python main.py
(请调用前用命令将目录切换到文件所在目录例如cd /d D:\视频文字内容提取)


教学演示:https://www.bilibili.com/video/BV1rX4y1P7CZ
