"""
bilibili_api.music

音乐相关 API

音乐主页: https://www.bilibili.com/v/musicplus

音乐信息解释: 部分视频的标签中有里面出现过的音乐的标签, 查询视频标签信息时可以读取到那个音乐标签的音乐 id (`music_id`), 然后即可传入函数查看信息
"""

from .utils.network_httpx import request
from .utils.Credential import Credential
from .utils.utils import get_api
from typing import Optional
from enum import Enum

API_audio = get_api("audio")


class MusicOrder(Enum):
    """
    音乐排序类型

    + NEW: 最新
    + HOT: 最热
    """
    NEW = 1
    HOT = 2


class MusicIndexTags:
    """
    音乐索引信息查找可以用的标签，有语言和类型两种标签，每种标签选一个

    - Lang: 语言标签枚举类
    - Genre: 类型标签枚举类
    """
    class Lang(Enum):
        """
        - ALL: 全部
        - CHINESE: 华语
        - EUROPE_AMERICA: 欧美
        - JAPAN: 日语
        - KOREA: 韩语
        - OTHER: 其他
        """
        ALL = ""
        CHINESE = 3
        EUROPE_AMERICA = 6
        JAPAN = 7
        KOREA = 61
        OTHER = 1

    class Genre(Enum):
        """
        - ALL: 全部
        - POPULAR: 流行
        - ROCK: 摇滚
        - ELECTRONIC: 电子音乐
        - COUNTRYSIDE: 乡村
        - FOLK: 民谣
        - LIVE: 轻音乐
        - CLASSICAL: 古典
        - NEW_CENTURY: 新世纪
        - REGGAE: 雷鬼
        - BLUES: 布鲁斯
        - RHYTHM_BLUES: 节奏与布鲁斯
        - ORIGINAL: 原声
        - WORLD: 世界音乐
        - CHILDREN: 儿童音乐
        - LATIN: 拉丁
        - PUNK: 朋克
        - MEDAL: 金属
        - JAZZ: 爵士乐
        - HIP_HOP: 嘻哈
        - SINGER_SONGWRITER: 唱作人
        - AMUSEMENT: 娱乐/舞台
        - OTHER: 其他
        """
        ALL = ""
        POPULAR = 1
        ROCK = 2
        ELECTRONIC = 3
        COUNTRYSIDE = 4
        FOLK = 5
        LIVE = 6
        CLASSICAL = 7
        NEW_CENTURY = 8
        REGGAE = 9
        BLUES = 10
        RHYTHM_BLUES = 12
        ORIGINAL = 13
        WORLD = 14
        CHILDREN = 15
        LATIN = 16
        PUNK = 17
        MEDAL = 18
        JAZZ = 19
        HIP_HOP = 20
        SINGER_SONGWRITER = 21
        AMUSEMENT = 22
        OTHER = 23


async def get_homepage_recommend(credential: Optional[Credential] = None):
    """
    获取音频首页推荐

    Args:
        credential (Credential | None): 凭据类. Defaults to None.

    Returns:
        dict: 调用 API 返回的结果
    """
    credential = credential if credential else Credential()
    api = API_audio["audio_info"]["homepage_recommend"]
    return await request("GET", api["url"], credential=credential)


async def get_music_index_info(
    keyword: str = "",
    lang: MusicIndexTags.Lang = MusicIndexTags.Lang.ALL,
    genre: MusicIndexTags.Genre = MusicIndexTags.Genre.ALL,
    order: MusicOrder = MusicOrder.NEW,
    page_num: int = 1,
    page_size: int = 10
) -> dict:
    """
    获取首页的音乐视频列表

    Args:
        keyword   (str)                 : 关键词. Defaults to None.
        lang      (MusicIndexTags.Lang) : 语言. Defaults to MusicIndexTags.Lang.ALL
        genre     (MusicIndexTags.Genre): 类型. Defaults to MusicIndexTags.Genre.ALL
        order     (MusicOrder)          : 排序方式. Defaults to OrderAudio.NEW
        page_num  (int)                 : 页码. Defaults to 1.
        page_size (int)                 : 每页的数据大小. Defaults to 10.
    """
    api = API_audio["audio_info"]["audio_list"]
    params = {
        "type": order.value,
        "lang": lang.value,
        "genre": genre.value,
        "keyword": keyword,
        "pn": page_num,
        "ps": page_size
    }
    return await request(
        "GET",
        api["url"],
        params = params
    )