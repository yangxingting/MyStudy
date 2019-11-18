#### 将文件链接在一起

```shell
ln -s  test.txt demo/exaple.txt.lnk  # 将test 和 exaple 两个文件链接在一起
cat  exaple.txt.lnk  # 打开exaple.txt

```



#### 用户组合权限

```shell
who #查看当前登录用户
w  #详细查看当前登录用户信息

#添加用户组
sudo groupadd test_group

#查看用户组 group id
cd p
cat etc/group

#在用户组总新建user
 # 添加新用户到用户id为1001的用户组 -m: home目录下创建该用户默认目录 创建者：parallels
sudo useradd -G 1001 -m -c "parallels" 

#查看用户组信息
id (用户组名称) 

#用户名密码管理
sudo passwd （用户名） # 重置用户的密码
cat  /etc/passwd  # 查看密码文件 
sudo cat etc/shadow #查看密码信息

# 列出所有用户最后登录信息
last 

#文件权限
[root@www /]# ls -l
total 64
dr-xr-xr-x   2 root root 4096 Dec 14  2012 bin
dr-xr-xr-x   4 root root 4096 Apr 19  2012 boot

#在Linux中第一个字符代表这个文件是目录、文件或链接文件等等。
#当为[ d ]则是目录
#当为[ - ]则是文件；
#若是[ l ]则表示为链接文档(link file)；
#若是[ b ]则表示为装置文件里面的可供储存的接口设备(可随机存取装置)；
#若是[ c ]则表示为装置文件里面的串行端口设备，例如键盘、鼠标(一次性读取装置)

```

![363003_1227493859FdXT](https://www.runoob.com/wp-content/uploads/2014/06/363003_1227493859FdXT.png)

```shell
# 第0位确定文件类型
# 第1-3位确定属主（该文件的所有者）拥有该文件的权限
# 第4-6位确定属组（所有者的同组用户）拥有该文件的权限
# 4-6位确定属组（所有者的同组用户）拥有该文件的权限

# ------权限更改---------
chmod -R o-r test/*    #将test 文件夹下面的所有文件， o：其他用户权限，-r:减去可读权限

(1)user
(2)group
(3)others

u, g, o 来代表三种身份的权限

a 则代表 all，即全部的身份。读写的权限可以写成 r, w, x，也就是可以使用下表的方式来看：

```

![image-20190821162743199](/Users/aiding/Library/Application Support/typora-user-images/image-20190821162743199.png)

```shell
如果我们需要将文件权限设置为 -rwxr-xr-- ，可以使用 chmod u=rwx,g=rx,o=r 文件名 来设定:

```



#### 系统日志 

```shell
cd / #回到根目录
cd var/log  #查看系统日志目录
```



#### 系统信息

```shell
ps -eH #查看电脑目前所有进程   e：所有  H：层级关系
top  # 查看电脑时时的进程
kill 9508  # 结束PID 为9508 的进程
```



#### pipe 管道 

```shell
#将从文件中检索到的内容 less 查看
grep '^.[AaBb]' name.txt | less   
# less,more,head,tail...都是可以接受standard input的命令，所以他们是管道命令
#ls,cp,mv并不会接受standard input的命令，所以他们就不是管道命令了。

```



#### grep 检索

```shell
grep -i '^abc'  name.txt  # 检索以abc为开头的内容   -i:忽略大小写 
grep -i 'abc$'  name.txt  # 检索以abc为结尾的内容   -i:忽略大小写
grep '^[AaBbCcDd]'  name.txt  #检索以 A或a或B或b或...开头的内容
grep '^.[AaBb]'  name.txt   #检索 第一位不限制，第二位置是A或者a或B或者b 的内容

```



#### wc导出 

```shell
wc -clw name.txt  # 列出文件有 几行几列  -c:只显示Bytes数  -l:显示行数  -w:只显示字数
```



#### eco 和 >> 的结合

```shell
echo "this content add name2.txt" >> name2.txt   # 将内容追加到 文件中
```

####  

#### sort排序

```shell
sort file.txt 
```



#### cut剪切文件内容

```shell
cut -d"/" -f3 name2.txt >> namelist.txt  #-d 设置/为切割符， -f 表示第几列,这里取第三列
```



#### 符号倒入值  >

```shell
cat name1.txt > namelist.txt   #  覆盖原来的位置
cat name1.txt >> namelist.txt   # 在原来基础上追加内容
```



#### 读取file头部/尾部

```shell
head -n 20 file.txt  #读取文档头部  默认10行   （ -n  20 ：指定20行 ）
tail file.txt      # 读取文档尾部
tail -f /var/log/secure   #监控用户登录
```



#### 打包

```shell
#  打包、解压
tar -cf  tartest.tar test   # 打包（ -cf ： create file ）
tar -tf  tartest.tar       #在不解压的情况下 预览文件list 
tar -tvf  tartest.tar       #在不解压的情况下 更加详细预览文件list 

tar -xf  tartest.tar   # 解压打包文件  
```

```shell
 # gz 打包、解压
 tar -czf   gziptest.gz test   # 打包gzip
 tar -xzf    gziptest.gz       # gizp  解包
```

```shell
# bzip2 打包 解压
tar -cjf bzip2.bz2 test    # 打包压缩
tar -cjf bzip2.bz2 test     #解压
```

```shell
# zip打包
zip -r ziptest.zp test    #打包压缩
unzip  ziptest.zp        #解压
```

```shell
# 查看文件
less readtest.txt  # 按页查看  ： /(搜索内容)
head readtest.txt  #读取头部 默认10行  
head -n 20 readtest.txt # 读取头部20行

tail readtest.txt  #读取文件尾巴内容  默认10行
tail -n 20 readtest.txt  #读取文件尾巴内容 最末尾20行

#tail监控用户登录
tail -f /var/log/secure

```

#### 切换管理员权限

```shell
su -   
```



#### linux文件管理命令

```shell
mkdir  /  mkdir filea fileb file  # 创建单个文件夹 或 多个文件夹
mkdir -p  目录1/目录2/目录3   #创建多个递进关系文件夹
ls  -R   	 #列出目录结构

cp  目录A/文件  目录B     #拷贝
mv  目录A/文件  目录B			#移动
mv  目录A/文件A  目录B/文件B（重命名）  #重命名

rm    -i     文件      # 提示性删除文件
rmdir  -i    空目录    # 提示性删除空目录
rm     -R    目录       # 删除整个文件夹（递归删除，先删除文件夹下的所有文件，最后删除文件夹）

```



#### linux文件管理目录

```shell
cd ~   # 回到默认目录
cd /   # 回到系统根目录

# 目录结构
1    boot  etc   lib    media  opt   root  sbin  sys  usr
bin  dev   home  lib64  mnt    proc  run   srv   tmp  var

bin :  封装平时run的程序
boot:  开机、内核、相关硬件 等程序
lib:   资源库、问文件
sbin:  超级管理员run的程序
tmp:   临时的文件
home :  用户的主目录


```



#### linux自带的说明书

```shell
man ls    			 # 查看命令说明
info cd   		 	 # 查看命令的描述信息
apropos find 		 # 查找大概有什么作用的命令 ， 查找有 发现作用的相关命令

info  # 有小星号可以跳入查看  （加入超链接的说明书）

#查看其他文档
/usr/share/doc/

```



#### 在系统查找文件

```shell
locate ls    # 查询系统中的datebase 特点速度快
find  /文件路径/  -name 'test.txt'  #搜寻files ystem  
whereis  ls  
```



####单引号和双引号的区别

```shell
`echo "hello,world by $LOGNAME"`      # 双引号内可以引用变量

`echo 'hello,world by $LOGNAME' `      # 单引号不能引用变量，以纯文本输出
```



####模糊查询

```
ls *.`txt`
ls tes?.txt
ls [Tt]est[0-9]*
```



####环境 变量
```shell
env      #查看环境
export   #出口变量
```



####打开上一步变量存储
```shell
cd -
```



####linux 历史记录
```shell
history         #查看历史操作记录
!(步骤序列号)     #调用历史操作记录

ehco  $HISTFILESIZE     # 总共可以保存多少条history
```



####uname 操作
```shell
uname    #查看系统名称
uname  -a    #查看系统所有信息
uname  -v    #查看系统版本号
uname  -m    #查看系统硬件信息
uname  -r -m -v  #组合查看
```



####查看系统正在运行的程序
```shell
top    #时时更新  q：退出
```




####关机命令
```shell
shutdown|halt| poweroff
```



####用户切换
```shell
su (username)
```



####用户查看,查看当前用户
```shell
whoami
```



####显示环境变量路劲
```shell
echo $PATH
```



#### 列表显示
```shell
ls              #列表显示目录
li-a(all)       #列表显示目录所有信息
ls-l            #列表显示 详细
ls-R            #目录层级列表显示
ls-s            #排序显示list
ls-t            #按照修改时间排序
```



####删除httpd
```shell
sudo yum aotoremove httpd
```



####展开httpd安装信息
```shell
yum list installed httpd
```



####安装httpd
```shell
sudo yum into httpd
```



####查看httpd 信息
```shell
yum info httpd
```



#### 查询httpd
```shell
search httpd
```



#### 查找本机httpd 目录信息
```shell
which httpd
```

