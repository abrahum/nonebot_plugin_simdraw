import os
import random
import nonebot
import ujson as json
from nonebot.adapters.cqhttp import MessageSegment

driver: nonebot.Driver = nonebot.get_driver()
cachepath: str
config: dict


def draw(times: int, game: str):
    with open(os.path.join(cachepath, config["%scards" % game]), "r") as f:
        cards = json.load(f)
    cardlist = [[] for _ in range(len(config[game]))]
    for card in cards:
        for i in range(len(cardlist)):
            if card["star"] == config[game][i][1]:
                cardlist[i].append(card)
    rlist = [[] for _ in range(len(config[game]))]
    for _ in range(times):
        i = random.random()
        for j in range(len(rlist)):
            if i < config[game][j][0]:
                rlist[j].append(random.choice(cardlist[j]))
    return rlist


def build_msg(gets: list, msgs: list):
    msg = ""
    for i in range(len(gets)):
        if not gets[i]:
            msg = msg + msgs[i] + "无\n"
        else:
            msg += msgs[i]
            for s in gets[i]:
                msg = msg + s["name"] + " "
            msg += "\n"
    return [msg[:-1]]


def build_imgmsg(gets: list, msgs: list):
    msg = ""
    for i in range(len(gets)):
        if not gets[i]:
            msg = msg + msgs[i] + "无\n"
        else:
            msg += msgs[i]
            for s in gets[i]:
                msg = msg + MessageSegment.image(file=s["url"])
            msg += "\n"
    return [msg[:-1]]


def sim_draw(times: int, game: str, noimg=True):
    if noimg:
        return build_msg(draw(times, game), config["%smsgs" % game])
    else:
        return build_imgmsg(draw(times, game), config["%smsgs" % game])


@driver.on_startup
async def check_data():
    global cachepath, config
    cachepath = os.path.join(os.getcwd(), "cache", "simdraw")
    try:
        with open(os.path.join(cachepath, "config.json"), "r") as f:
            config = json.load(f)
        nonebot.require("nonebot_plugin_simdraw").draw = sim_draw
        nonebot.logger.info("simdraw init success")
    except:
        nonebot.logger.info("config.json not found")
