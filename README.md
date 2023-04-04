# pkgfile-web
pkgfile在线查询网站

鉴于debian ubuntu等发行版都有官方的在线查包网站而arch没有，故作此网页。

## 示例站点：

https://pkg.aya1.pro


## 自行部署：
要求 python >= 3.8，且系统中有pkgfile命令
```bash
git clone https://github.com/Brx86/pkgfile-web
cd pkgfile-web
pip install fastapi uvicorn
uvicorn app:app --host=0.0.0.0 --port=8000
```