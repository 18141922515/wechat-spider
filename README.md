
## 所需环境

1. mysql：用来存储抓取到的数据以及任务表
2. redis：任务缓存，减少操作mysql的次数

## 安装配置

> 以下安装说明安需查看，仅作为参考。因每个人环境不同，可能安装会有些差异，可参考网上的资料

### 1. 安装mysql

### 2. 安装redis

### 3. 安装证书

 1. 可用浏览器访问 mitm.it 然后下载，或者百度如何安装mitmproxy证书
 2. 双击运行
 3. 安装到本地计算机
 4. 需要密钥时跳过
 5. 选择“将所有的证书都放入下列存储”，接着选择“受信任的根证书颁发机构”
 6. 最后，弹出警告窗口，直接点击“是”


### 4. 配置代理


打开chrome 设置->高级
![A580D0082CCEE0621F98FAF003C5530E](media/A580D0082CCEE0621F98FAF003C5530E.png)
![95AE10B3227FDE0637AB227A5A8267E3](media/95AE10B3227FDE0637AB227A5A8267E3.png)



## 使用说明

### 1. 安装如上说明安装好证书及配置好代理
### 2. 正确配置config.yaml

主要是配置mysql及redis的链接信息，确保能正确链接上

### 3. 创建数据库 wechat

![-w418](media/15610827417503.jpg)


### 4. 启动wechat-spider

此步骤如果config里的auto_create_tables值为true时，会自动创建mysql数据表。建议首次启动时设置为true，创建完表后设置为false
    
### 5. 下发公众号任务

录入数据到wechat_account_task, 如：
![-w503](media/15584579051963.jpg)
只填写__biz就好, 如：MzIxNzg1ODQ0MQ==

### 6. 点击任意一公众号，查看历史消息

![-w637](media/15584585019970.jpg)

当出现如上红框中的提示信息时，说明大功告成了，过一会可以去数据库里验证数据了


