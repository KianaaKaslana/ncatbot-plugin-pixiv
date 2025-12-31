import asyncio
import os
from typing import TYPE_CHECKING
from pixivpy3 import AppPixivAPI
from ncatbot.core.helper.forward_constructor import ForwardConstructor
from ncatbot.utils import ncatbot_config
if TYPE_CHECKING:
    from plugin import pixiv
from ncatbot.core.event import GroupMessageEvent
from ncatbot.plugin_system import (
    NcatBotPlugin,
    command_registry,
    group_admin_filter,
    group_filter,
)
from ncatbot.utils import get_log
LOG=get_log()
async def get_good_pic(plugin:"pixiv",user_id:str,api:AppPixivAPI,event:GroupMessageEvent):
    fcr=ForwardConstructor(user_id=ncatbot_config.bt_uin)
    fcr.attach_text("这是你想要的好图")
    result=api.illust_recommended()
    path = "./plugins/pixiv/pixiv_download"
    try:
        os.makedirs(path)
    except FileExistsError as e:
        LOG.warning(e)
    for pic in result.illusts[:3]:
        success = False
        url = None
        LOG.info(f"处理插画{pic.title},id:{pic.id}")
        if pic.meta_single_page and 'original_image_url' in pic.meta_single_page:
            url = pic.meta_single_page.original_image_url
            if url != None:
                image_name=f"{user_id}_{pic.id}.jpg"
                image_path=path+"/"+image_name
                success = api.download(url=url,
                                       path=path,
                                       name=image_name,)
                fcr.attach_text(f"作品名:{pic.title}\npid:{pic.id}\n作者:{pic.user['name']}")
                fcr.attach_image(image_path)
        if not url and pic.meta_pages:
            try:
                url = pic.meta_pages[0].image_urls.original
                image_name=f"{user_id}_{pic.id}_0.jpg"
                image_path=path+"/"+image_name
                success = api.download(url=url,
                                       path=path,
                                       name=image_name)
                fcr.attach_text(f"作品名:{pic.title}\npid:{pic.id}\n作者:{pic.user['name']}")
                fcr.attach_image(image_path)
            except Exception as e:
                fcr.attach_text("处理多图时出错")
                LOG.info(f"处理多图时出错：{e}")
        elif not url:
            LOG.info("无原图")
            url = pic.image_urls.large
            image_name=f"{user_id}_{pic.id}.jpg"
            image_path=path+"/"+image_name
            success = api.download(url=url,
                                path=path,
                                name=image_name)
            fcr.attach_text(f"作品名:{pic.title}\npid:{pic.id}\n作者:{pic.user['name']}")
            fcr.attach_image(image_path)
        if success:
            LOG.info("success")
        else:
            LOG.info("fail")
    forward = fcr.to_forward()
    await plugin.api.post_group_forward_msg(event.group_id, forward)