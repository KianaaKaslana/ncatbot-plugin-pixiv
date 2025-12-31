import asyncio
import os
from datetime import datetime
from typing import Dict, List, Set, Tuple
from pixivpy3 import AppPixivAPI
from ncatbot.core.event import GroupMessageEvent
from ncatbot.plugin_system import (
    NcatBotPlugin,
    command_registry,
    group_admin_filter,
    group_filter,
)
from . import command
from ncatbot.utils import get_log
LOG=get_log()

class pixiv(NcatBotPlugin):
    name = "recommend_pixiv"
    version = "1.0.0"
    auther = "shy_robot"
    description = "发送推荐图"
    napi=AppPixivAPI(
            proxies={
                # 方案A: 使用SOCKS5代理（推荐，Clash默认端口7891）
                #'http': 'socks5://127.0.0.1:7891',
                #'https': 'socks5://127.0.0.1:7891',
                # 方案B: 或使用HTTP代理（Clash默认端口7890）
                'http': 'http://127.0.0.1:7890',
                'https': 'http://127.0.0.1:7890',
            }
    )
    # 从环境变量或配置文件获取刷新令牌，避免硬编码
    refresh_token = os.getenv("PIXIV_REFRESH_TOKEN", "")
    user_id = 123456
    refresh_task=None
    async def on_load(self):
        LOG.info(f"pixivp Loaded ")
        try:
            self.napi.auth(refresh_token=self.refresh_token)
            LOG.info(f"pixiv api 认证成功 ")
        except Exception as e:
            LOG.error(f"pixiv api 认证失败 {e}")
        self.refresh_task = asyncio.create_task(self.periodic_refresh_auth())
    async def periodic_refresh_auth(self):
        while True:
            await asyncio.sleep(60*60)
            try:
                self.napi.auth(refresh_token=self.refresh_token)
                LOG.info(f"P站api刷新成功")
            except Exception as e:
                LOG.info(f"P站api刷新失败")
    @command_registry.command('好图推荐',description="从p站上发送3张推荐的图")
    @group_filter
    async def pixiv_search(self, event:GroupMessageEvent):
        LOG.info(f"收到来自{event.user_id}的好图请求")
        await command.get_good_pic(self,user_id=event.user_id,api=self.napi,event=event)
