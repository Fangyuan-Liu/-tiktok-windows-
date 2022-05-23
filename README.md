# 爬虫爬取tiktok单条视频的评论（windows版）
事情是这样的：zy老师在b站上看到了一个从tiktok搬运的天使热线视频（tiktok：[I urge you to call 707-998-8410 🥺 (tiktok.com)](https://www.tiktok.com/@iamtheodoratheexplora/video/7076259537858121002)），灵感一现，决定大创搞这个了。为了获取该视频对观看者的影响，我们根据老师意见，决定找40人访谈+分析视频底下的评论（咳，不过最后大改了）。于是我连夜琢磨如何爬取tiktok评论（爬虫速成（bushi

Github上搜到一个俄罗斯小哥（如果是妹子，请允许我道歉dbq）的项目：https://github.com/romanovsavelij/TikTokCommentsFetcher，但由于系统不同（我用的是windows，因为我没用过Linux，勿喷......感觉自己老是因为这些东西被嘲讽😥）+Tik Tok网站验证机制更新的缘故，并不能直接用他们的代码，so......我笨拙地改了一波（听我说，谢谢有道翻译和百度

requirements是直接用的原项目的，因为我真的不懂这些......sos

**最后，这只是一个非专业人员的业余爱好，以项目驱动为导向的，非常粗糙非常费劲地爬成功了后，因为idea改了，所以其实这个代码是被废弃了的，目前没啥优化的想法（牛仔很忙的（手动狗头（或者你愿意教我的话，我也非常乐意~**

小白不是很懂Github的规矩，所以如果这个项目有任何问题，欢迎友善提醒，本人无任何恶意侵权的想法，非常感谢！邮箱：liufangyuan0211@qq.com

## 文档

### 使用这个代码前你需要:
1) 下载chromedriver
2) 科学上网
2) 拥有一个Google账号
2) 拥有一个Tik Tok账号
2) 安装好了Python并配置了环境，你需要time和seleium库

### 注意事项（踩过的坑:
1. 科学上网不能用HK的，Tik Tok在香港已经停止运行......
2. 注册Google账号时，保证浏览器使用语言和科学上网的归属地一致，不然可能会导致无法用中国电话号码验证
3. 不要频繁只用一个Tik Tok账号登录，会因为登录频繁而失败的。爬取全部评论前的试验都可以不登录Tik Tok的账号，游客是可以看到评论的！
4. 好好学XPath......（吐血（🤡竟是我自己
5. 使用该代码时，可能会有失败概率，因为Tik Tok它有时候不按常理出牌hhh多试几次就好了（祝你顺利）
5. 我刚刚看了一下，嗯，tiktok是不是不能加载所有评论了？？？？？？？？？？

### 使用方法

请看instruction.pdf

### 输入

1. 需要爬取的Tik Tok视频链接
2. 手动输入验证码（Google的验证码真的挺难的hhh
3. 手动登录Tik Tok账号（这步应该有办法优化，但是再说吧
4. 手动copy标签（？不知道学名叫啥，因为每次加载的这个值都不同，看instructions.pdf吧）

### 输出

当前目录下的一个名为“raw_corpus.txt”的文本文档（考虑到csv无法兼容Tik Tok里的一些emoji，应该是编码方式的问题，这里改成输出文本文档了）

### 技术

Python, selenium库