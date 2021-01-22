import paddlehub as hub
import cv2,copy,os
import time


class Ocr():
    def __init__(self,mobile):
        if mobile=='否':
            # 加载移动端预训练模型
            self.ocr = hub.Module(name="chinese_ocr_db_crnn_mobile")
        else:
            # 服务端可以加载大模型，效果更好
            self.ocr = hub.Module(name="chinese_ocr_db_crnn_server")
    def get_text(self,image,visualization,gpu):
        if gpu ==True:
            os.environ["CUDA_VISIBLE_DEVICES"] = "1"
        text=''
        results = self.ocr.recognize_text(
            images=[image],  # 图片数据，ndarray.shape 为 [H, W, C]，BGR格式；
            use_gpu=gpu,  # 是否使用 GPU；若使用GPU，请先设置CUDA_VISIBLE_DEVICES环境变量
            output_dir='ocr_result',  # 图片的保存路径，默认设为 ocr_result；
            visualization=visualization,  # 是否将识别结果保存为图片文件；
            box_thresh=0.5,  # 检测文本框置信度的阈值；
            text_thresh=0.5)  # 识别中文文本置信度的阈值；

        data=results[0]['data']
        save_path = results[0]['save_path']
        for infomation in data:
            text=text+' '+infomation['text']
        return text,save_path
if __name__ == '__main__':
    time_start=time.time()
    with open('配置.txt', 'r',encoding='utf-8')as f:
        setting = f.read()
        setting = setting.split('\n')
    voidPath=setting[0].split('"')[1]
    timeS = int(setting[1].split('"')[1])
    testPath = setting[2].split('"')[1]
    show=setting[3].split('"')[1]
    mobile=setting[4].split('"')[1]
    gpu=setting[5].split('"')[1]
    print("视频地址:", voidPath)
    print('判断帧间隔:', timeS)
    print('识别结果保存目录:', testPath)
    print('是否可视化:', show)
    print('精准识别:', mobile)
    print('GPU:', gpu)
    if gpu=='是':
        gpu=True
    else:
        gpu=False
    c = 0
    cap = cv2.VideoCapture(voidPath)
    last_text = ''
    now_text = ''
    text = ''
    orc=Ocr(mobile)
    #返回帧率
    fps=int(cap.get(cv2.CAP_PROP_FPS))
    try:
        while (cap.isOpened()):
            t1=time.time()
            now_text = ''
            c = c + 1
            ret, frame = cap.read()
            if c % timeS == 0:  # c除尽timeS时取帧保存，图片，即隔timeS保存一次图片
                #运算时间
                m, s = divmod(c//fps, 60)
                h, m = divmod(m, 60)
                if show=='是':
                    now_text, save_path = orc.get_text(frame, True,gpu)
                    try:
                        image = cv2.imread(save_path)
                        x, y = image.shape[0:2]
                        image=cv2.resize(image, (int(y ), int(x )))
                        cv2.imshow('Video Subtitle Extraction', image)
                        k = cv2.waitKey(60)
                        # q键退出
                        if (k & 0xff == ord('q')):
                            break
                        #os.remove(save_path)
                    except:
                        pass

                else:
                    now_text, save_path = orc.get_text(frame,False )
                if now_text!=last_text:#判断是否重复
                    text=now_text +f'[{h}:{m}:{s}]'+ '\n'
                    last_text=copy.copy(now_text)
                    print(text,f'用时:{time.time()-t1}')
                    with open(testPath, 'a+')as f:
                        f.write(text)
    except Exception as err:
        print(err)
    cap.release()
    cv2.destroyAllWindows()
    time_stop = time.time()
    input(f'全部完成用时:{time_stop-time_start}')




