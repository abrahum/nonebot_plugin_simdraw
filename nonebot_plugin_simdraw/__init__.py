from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event

from .data_source import sim_draw

fgo_draw = on_command("Fgo_Draw", aliases={
                      "FGO抽卡", "FGO来一单", "fgo抽卡", "fgo来一单", "Fgo抽卡", "Fgo来一单"}, rule=to_me())


@fgo_draw.handle()
async def fgo_draw_handler(bot: Bot, event: Event):
    args = str(event.get_message()).strip()
    noimg = True
    if args == "图":
        noimg = False
    msgs = sim_draw(55, noimg=noimg, game="fgo")
    for msg in msgs:
        await fgo_draw.send(msg)

prts_draw = on_command("Prts_Draw", aliases={
                       "明日方舟抽卡", "明日方舟来一单", "方舟抽卡", "方舟来一单"}, rule=to_me())


@prts_draw.handle()
async def prts_draw_handler(bot: Bot, event: Event):
    args = str(event.get_message()).strip()
    noimg = True
    if args == "图":
        noimg = False
    msgs = sim_draw(55, noimg=noimg, game="prts")
    for msg in msgs:
        await prts_draw.send(msg)
