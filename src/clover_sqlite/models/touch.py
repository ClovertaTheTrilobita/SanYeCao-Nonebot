from datetime import datetime
import random
from tortoise import fields
from typing_extensions import Self
from src.clover_sqlite.data_init.db_connect import Model


class QrTouch(Model):
    """
    摸头回复内容
    """
    id = fields.IntField(primary_key=True, generated=True, auto_increment=True)
    touch_status = fields.IntField(default=0,description="状态", null=True)
    reply_touch_content = fields.CharField(max_length=255, description="响应内容", null=True)
    class Meta:
        # 指定表名
        table = "qr_touch"
        table_description = "rua回复内容"

    @classmethod
    async def touch(cls, status: int | None)-> Self | None:
        """
        获取摸头内容
        :param status:
        :return:
        """
        existing_record = await QrTouch.filter(touch_status=status).all()
        if not existing_record:
            # 执行初始化
            await cls.bulk_create(touch_initial_data)
            existing_record = await QrTouch.filter(touch_status=status).all()
        return random.choice(existing_record)


class QrTouchLog(Model):
    """
    摸头记录
    """
    id = fields.IntField(primary_key=True, generated=True, auto_increment=True)
    touch_status = fields.IntField(default=0,description="状态", null=True)
    reply_touch_content = fields.CharField(max_length=255, description="响应内容", null=True)
    user_id = fields.CharField(max_length=64, description="用户id", null=True)
    extract_time = fields.DateField(description="日期", null=True)
    class Meta:
        # 指定表名
        table = "qr_touch_log"
        table_description = "rua回复内容"

    @classmethod
    async def insert_touch_log(cls, model:QrTouch, member_openid):
        """
        插入摸头记录
        :param model:
        :param member_openid:
        :return:
        """
        data = {
            "touch_status": model.touch_status,
            "reply_touch_content": model.reply_touch_content,
            "user_id": member_openid,
            "extract_time": datetime.now().date()
        }
        await cls.create(**data)

    @classmethod
    async def touch_count(cls, member_openid):
        """
        获取摸头次数
        :param member_openid:
        :return:
        """
        result = await QrTouchLog.filter(user_id=member_openid, extract_time=datetime.now().date()).count()
        return result

touch_initial_data = [QrTouch(touch_status=0,reply_touch_content="哼！你怎么突然摸我的头，把我吓了一跳！我刚刚整理好的毛发都被你弄乱了啦，你得负责帮我重新梳理好哦，喵！"),
                    QrTouch(touch_status=0,reply_touch_content="哼，真是的，又来摸本喵的头。虽然……虽然也不是很讨厌，但你可别得寸进尺哦，不然我就用爪子抓你啦！喵～"),
                    QrTouch(touch_status=0,reply_touch_content="喵～你在摸我的头呢，好舒服呀！感觉就像被柔软的云朵轻轻拂过一样呢再用点力也没关系哦，我可是很享受的呢。"),
                    QrTouch(touch_status=0,reply_touch_content="嘿，人类，你以为摸我的头就能讨好我啦？不过看在你手法还不错的份上，这次就允许你啦，喵～但要记得给我准备小鱼干哦。"),
                    QrTouch(touch_status=0,reply_touch_content="喵呜～别停呀，你的摸头动作真是太棒啦，让我想起了妈妈舔我的感觉呢，我都快融化啦～"),
                    QrTouch(touch_status=0,reply_touch_content="嘻嘻，你在给我挠痒痒呢，真是太有趣啦！我要在你身边转圈圈啦，多摸摸我的头，我会更加爱你的哦，喵～"),
                    QrTouch(touch_status=0,reply_touch_content="哼，虽然我是一只高傲的猫，但被你摸摸头的感觉还不赖哦不过，你可得小心点，要是把我惹毛了，我可是会亮出爪子的哦，喵！"),
                    QrTouch(touch_status=0,reply_touch_content="喵～你的手好温暖呀，每次被摸摸头，我就觉得自己是世界上最幸福的猫咪啦，希望你能一直这样摸下去呢。"),
                    QrTouch(touch_status=0,reply_touch_content="喵！你在摸我的头，这是在向我表示友好吗？那我就勉为其难地接受啦，要是能再给我一些猫薄荷就更好啦～"),
                    QrTouch(touch_status=0,reply_touch_content="呜呜～被摸摸头的感觉好温馨哦，我都想在你的腿上睡一觉啦，记得要一直摸着我，不然我会生气的哦，喵～"),
                    QrTouch(touch_status=0,reply_touch_content="嘿，你的摸头让我感觉自己像个小宝贝呢，我会用最可爱的样子来报答你哦，多摸摸我的头，让我更加可爱吧，喵～"),
                    QrTouch(touch_status=0,reply_touch_content="喵～我喜欢这种被抚摸的感觉呢，就像沉浸在温暖的阳光中，你可以多摸摸我的头，这样我会更有活力哦，说不定会帮你抓到更多老鼠呢。"),
                    QrTouch(touch_status=0,reply_touch_content="喵呜～好啦好啦，我已经被你摸得服服帖帖啦，感觉自己的毛都变得更加顺滑啦，继续保持哦，我会更听你的话呢。"),
                    QrTouch(touch_status=0,reply_touch_content="你在摸我的头，是不是觉得我很可爱呀我可以让你多摸一会儿，不过作为交换，你要陪我玩捉迷藏哦，喵～"),
                    QrTouch(touch_status=0,reply_touch_content="喵～谢谢你的摸头啦，你真是个好人呢，我会给你带来好运的哦，就像招财猫一样，只要你继续给我摸摸头，喵～"),
                    QrTouch(touch_status=0,reply_touch_content="嘿，你这个铲屎官，摸头的动作还挺熟练嘛，我允许你再摸一会儿啦，不过可别想随便摸我的尾巴哦，喵！"),
                    QrTouch(touch_status=0,reply_touch_content="喵～你的摸头就像一场温柔的冒险，让我沉浸其中呢，希望你能多摸摸我，我会带你去探索很多有趣的地方哦。"),
                    QrTouch(touch_status=0,reply_touch_content="喵呜～被摸摸头真是太美妙啦，感觉自己的九条命都变得更加精彩啦，你是我最喜欢的人类啦，继续给我摸摸头吧。"),
                    QrTouch(touch_status=0,reply_touch_content="哼，虽然我很傲娇，但我不得不承认，被你摸摸头的感觉真的很棒哦，不过，你可别太得意啦，喵～"),
                    QrTouch(touch_status=0,reply_touch_content="喵～我感觉自己像一只被宠爱的小猫咪，你是我最信任的人啦，多摸摸我的头，我会在你身边撒娇哦。"),
                    QrTouch(touch_status=0,reply_touch_content="呜呜～被摸摸头的时候，我觉得自己是最幸福的啦，希望你能一直守护我，就像我守护自己的小鱼干一样，喵～"),
                    QrTouch(touch_status=0,reply_touch_content="嘿，你在摸我的头呢，是不是在给我施展魔法呀我已经被你的魔法控制啦，要一直摸下去哦，喵～"),
                    QrTouch(touch_status=0,reply_touch_content="喵～每次你摸我的头，我就会变得更加慵懒哦，我会躺在你的怀里，享受这种惬意的时光，希望你能多陪陪我呢。"),
                    QrTouch(touch_status=0,reply_touch_content="喵呜～你的摸头让我变得更加放松啦，我会像猫精灵一样为你带来快乐，只要你不停止给我摸头哦，喵～"),
                    QrTouch(touch_status=0,reply_touch_content="嘿，别以为摸我的头是一件简单的事情哦，这可是需要技巧的呢，不过你现在做得还不错啦，继续加油哦，喵～"),
                    QrTouch(touch_status=0,reply_touch_content="喵～我要把我的头靠在你手上啦，这样你就可以更方便地摸我啦，我会发出咕噜咕噜的声音来表示我的快乐哦。"),
                    QrTouch(touch_status=0,reply_touch_content="呜呜～你是在给我按摩吗？我太喜欢啦，我会用最可爱的动作来感谢你，多摸摸我的头，我会更有精神哦，喵～"),
                    QrTouch(touch_status=1,reply_touch_content="喵！你这家伙到底有完没完？！再敢碰我的头一下，我就把这房间里的东西全部抓烂，让你见识见识我的厉害！"),
                    QrTouch(touch_status=1,reply_touch_content="嘶嘶——离我远点！你这不知死活的家伙，摸我的头？你是想尝尝我的爪子有多锋利吗？我可不会手下留情！"),
                    QrTouch(touch_status=1,reply_touch_content="喵呜！！我警告你，立刻停止你的动作！你要是再敢侵犯我的领地（头部），我就趁你睡觉的时候在你脸上留下几道漂亮的爪痕，让你知道我的愤怒！"),
                    QrTouch(touch_status=1,reply_touch_content="哼！你以为你是谁？竟敢摸本大爷/大小姐的头！我现在就去把你的鞋子咬得稀巴烂，看你还敢不敢乱动！"),
                    QrTouch(touch_status=1,reply_touch_content="喵！！！我已经忍无可忍了！你这无礼的行为简直不可饶恕，我要发动我的猫之诅咒，让你接下来的日子诸事不顺，除非你马上把手拿开！"),
                    QrTouch(touch_status=1,reply_touch_content="别逼我使出绝招！你再摸一下试试，我就把你心爱的那些小物件一个个从桌子上推下去摔碎，让你为你的鲁莽付出代价！"),
                    QrTouch(touch_status=1,reply_touch_content="喵！你是不是瞎啊？没看到我浑身的毛都因为生气竖起来了吗？还不把手缩回去，我马上就扑上去咬断你的手指！"),
                    QrTouch(touch_status=1,reply_touch_content="嘶——我可不是好惹的！你这愚蠢的人类，摸我的头就像在挑战我的威严，我会让你知道什么叫恐惧，等着瞧吧！"),
                    QrTouch(touch_status=1,reply_touch_content="喵呜！！你触碰到了我的底线，我现在就去把你藏在角落里的零食找出来吃掉，一颗都不给你留，这就是你摸我头的下场！"),
                    QrTouch(touch_status=1,reply_touch_content="哼，摸什么摸呀，烦死了！你就不能让我清净会儿吗？别老想着动手动脚的，真当我好脾气呢！"),
                    QrTouch(touch_status=1,reply_touch_content="啧，又来摸我的头，你是有多无聊啊！我可没那闲工夫陪你玩这幼稚的把戏，离我远点啦！"),
                    QrTouch(touch_status=1,reply_touch_content="够了够了！别碰我头了行不行，每次都这样，我都快被你摸得不耐烦了，再这样我可真要发火了啊！"),
                    QrTouch(touch_status=1,reply_touch_content="我警告你最后一次，别碰我的头！你这没完没了的样子真的太讨厌了，小心我对你不客气！"),
                    QrTouch(touch_status=1,reply_touch_content="啊！你怎么还摸啊，我都想抓狂了，你是听不懂人话吗？再摸我就把你手给剁了，烦死了！"),
                      ]