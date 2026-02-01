from datetime import datetime
from os import getcwd

from src.clover_splatoon.stages import RegularScheduleItem, BankaraScheduleItem, CoopScheduleItem
from src.configs.path_config import temp_path
from nonebot_plugin_htmlrender import template_to_pic
from playwright.async_api import async_playwright
from src.clover_splatoon.splatoon_data import stage3

async def save_img(data: bytes):

    """
     保存日报图片
     :param data:
     :return:
     """
    file_path = temp_path + f"{datetime.now().date()}splatoon.png"
    with open(file_path, "wb") as file:
        file.write(data)

async def generate_splatoon_report_image(regular: RegularScheduleItem, bankara: BankaraScheduleItem, coop: CoopScheduleItem):
    now = datetime.now()

    week = {  # noqa: RUF012
        0: "周一",
        1: "周二",
        2: "周三",
        3: "周四",
        4: "周五",
        5: "周六",
        6: "周日",
    }

    regular_list = [
        [
            stage3[str(regular.regularMatchSetting.vsStages[0].vsStageId)]["cname"],
            regular.regularMatchSetting.vsStages[0].image.url

        ],
        [
            stage3[str(regular.regularMatchSetting.vsStages[1].vsStageId)]["cname"],
            regular.regularMatchSetting.vsStages[1].image.url
        ]
    ]


    bankara_list_challenge = [
        [
            stage3[str(bankara.bankaraMatchSettings[0].vsStages[0].vsStageId)]["cname"],
            bankara.bankaraMatchSettings[0].vsStages[0].image.url
        ],
        [
            stage3[str(bankara.bankaraMatchSettings[0].vsStages[1].vsStageId)]["cname"],
            bankara.bankaraMatchSettings[0].vsStages[1].image.url
        ]
    ]

    bankara_list_open = [
        [
            stage3[str(bankara.bankaraMatchSettings[1].vsStages[0].vsStageId)]["cname"],
            bankara.bankaraMatchSettings[1].vsStages[0].image.url
        ],
        [
            stage3[str(bankara.bankaraMatchSettings[1].vsStages[1].vsStageId)]["cname"],
            bankara.bankaraMatchSettings[1].vsStages[1].image.url
        ]
    ]

    coop_list = [
        [
            stage3[coop.setting.coopStage.name]["name"],
            coop.setting.coopStage.thumbnailImage.url
        ],
        [
            wp.image.url for wp in coop.setting.weapons
        ]
    ]

    data = {
        "data_regular": regular_list,
        "data_bankara_challenge": bankara_list_challenge,
        "data_bankara_open": bankara_list_open,
        "data_coop": coop_list,
        "week": week[now.weekday()],
        "date": now.date(),
        "time": datetime.now().strftime("%H:%M"),
        "full_show": True,
    }
    async with async_playwright() as p:
        browser = await p.chromium.launch()

    image_bytes = await template_to_pic(
        template_path=getcwd() + "/src/clover_splatoon/resources",
        template_name="main.html",
        templates={"data": data},
        pages={
            "viewport": {"width": 578, "height": 1885},
            "base_url": f"file://{getcwd()}",
        },
        wait=2,
    )
    await save_img(image_bytes)
    await browser.close()
    return image_bytes