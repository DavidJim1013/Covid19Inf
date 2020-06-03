# Covid19Inf

数据爬虫于此网站： http://sa.sogou.com/new-weball/page/sgs/epidemic<br>
数据是国内实时的累计确诊，累计治愈，现有疑似，累计死亡，现有确诊，无症状感染者，境外输入以及现有重症的人数<br>

运行此py文件会架设本地的服务器，浏览器访问时，会返回一个Json结构的数据（国内的累计确诊，累计治愈，现有疑似，累计死亡，现有确诊，无症状感染者，境外输入以及现有重症的人数）。

运行前需要安装的包：<br>
1. requests <br>
2. web <br>

如未安装需要去命令行输入：<br>
**$pip install requests** <br>
**$pip install web.py**

要运行此文件：<br>
1. 在Cov19Inf.py的目录里运行命令行<br>
   **$python Cov19Inf.py**
   他会返回一个本地的端口，去浏览器输入此地址即可接收到实时的数据<br>
2. 如果你不能或者不想使用默认端口，你可以使用这样的命令来指定端口号 **$python Cov19Inf.py 1234**<br>
   1234 是自定义的端口
3. 浏览器输入 localhost:8080(默认端口号) 就可看到返回的数据

