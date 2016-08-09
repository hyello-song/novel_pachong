# novel_pachong
A simple Python3 console program used to download novel from certain websites  
这里是一个用Python3编写的网络小说爬虫，运行于控制台下。  
（GNU GPL V2授权）  
*小说版权归**原作者**所有，本程序仅为交流Python网络操作技术*  
*不得用该程序从事不法活动，由此带来的一切后果本人概不负责*  
define文件夹下包含了几个协议。你也可以编写新协议，格式参见define/Template.py。写好之后在main.py头部的模块导入区添加对你编写的协议的导入，并在字典df中加入索引。  
```Python
from define import snwx, biquge, leduwo, snwx_txt, kanunu, ADD
df = {'snwx':snwx, 'leduwo':leduwo, 'biquge':biquge, 'snwx_txt':snwx_txt, 'kanunu':kanunu, 'ADD':ADD}
```
