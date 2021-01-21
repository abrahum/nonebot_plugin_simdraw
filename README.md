<h1 align="center">nonebot-plugin-simdraw</h1>

## 使用方式

- 方式一：

发送`[gamename]抽卡（来一发）`来模拟手游抽卡（目前仅有Fgo与明日方舟卡池文件、欢迎提交其他游戏卡池文件娱乐大家~）

指令后带参数`图`可以抽卡附带你们老婆们和老公们的头像

- 方式二：

使用以下方式调用抽卡函数

```python
nonebot.require("simdraw").draw(times: int, game: str, noimg=True):
    return [Messages]
```

## 配置项

使用本插件需要将在bot.py同级目录下新建/cache/simdraw文件夹，并在文件夹内配置congfig.json与其他游戏卡池信息文件

congfig.json范例：

```json
{
    "fgo": [         //游戏名
        [0.01,5],    //[概率,类别]
        [0.03,4],
        [0.04,-1]
    ],
    "fgomsgs": [     //游戏名+msgs
        "五星从者：", //用于生成抽卡信息
        "四星从者：",
        "五星礼装："
    ],
    "fgocards": "fgo.json" //游戏名+cards:卡池信息文件名
}
```

游戏卡池信息文件范例：

```json
[
    {
        "name": "\u5f17\u6817\u591a",   //角色名
        "url": "https:\/\/fgo.wiki\/images\/3\/3e\/Servant300.jpg", //图片url
        "star": 5  //类别
    }
]
```

本仓库内有fgo与明日方舟的卡池文件与配置文件，欢迎取用~