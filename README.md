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

> **下一步目标：（即为第二代，准备升级到SongReader）**  
> 1、下载书籍时可以选章单独下载，书籍存储方式变为每章分文件，但可以以不同方式导出；  
> 2、加入超时重试功能，逐字解码，从而提高容错性能；  
> 3、研究epub格式，从而支持txt与epub格式导出（还有zip压缩技术也得看看怎么搞）；  
> 4、加入GUI（Qt？GTK？），甚至是阅读功能与书籍管理功能；  
> 5、将提取功能转为依赖正则进行。  

*我得考虑学习java和swift了，不然以后怎么做移动版本。。。*
