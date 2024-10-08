from pathlib import Path
from typing import Dict, Optional, Union

from PIL import Image
import aiofiles
from gsuid_core.help.draw_plugin_help import get_help
from gsuid_core.help.model import PluginHelp
from msgspec import json as msgjson

from ..utils.fonts.starrail_fonts import starrail_font_origin
from ..version import StarRail_version

TEXT_PATH = Path(__file__).parent / "texture2d"
HELP_DATA = Path(__file__).parent / "Help.json"


async def get_help_data() -> Optional[Dict[str, PluginHelp]]:
    if HELP_DATA.exists():
        async with aiofiles.open(HELP_DATA, "rb") as file:
            return msgjson.decode(await file.read(), type=Dict[str, PluginHelp])
    return None


async def get_core_help() -> Union[bytes, str]:
    help_data = await get_help_data()
    if help_data is None:
        return "暂未找到帮助数据..."

    return await get_help(
        "StarRailUID",
        f"版本号:{StarRail_version}",
        help_data,
        Image.open(TEXT_PATH / "bg.jpg"),
        Image.open(TEXT_PATH / "ICON.png"),
        Image.open(TEXT_PATH / "badge.png"),
        Image.open(TEXT_PATH / "banner.png"),
        Image.open(TEXT_PATH / "button.png"),
        starrail_font_origin,
    )
