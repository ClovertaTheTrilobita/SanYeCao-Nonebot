import os
import random
from datetime import datetime
from tortoise import fields
from typing_extensions import Self
from src.clover_sqlite.data_init.db_connect import Model
from src.configs.path_config import tarots_img_path


class MajorArcanaLog:
    pass


class MajorArcana(Model):
    """
    大阿尔克纳牌
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, unique=True, description="牌名")
    upright_meaning = fields.TextField(description="正位含义")
    reversed_meaning = fields.TextField(description="逆位含义")
    image = fields.CharField(max_length=255, description="图片文件名")

    class Meta:
        # 指定表名
        table = "major_arcana"
        table_description = "大阿尔克纳牌"

    @classmethod
    async def tarotChoice(cls, user_id: str | None) -> MajorArcanaLog | None:
        """
        大阿尔克纳牌抽取
        :param user_id:
        :return:
        """
        record = await MajorArcanaLog.getTarotLog(user_id)
        if record:
            return record
        # 0正1逆
        ints = random.randint(0, 1)
        arcana = await cls.all()
        if not arcana:
            await cls.bulk_create(Major_arcana_initial_data)
            arcana = await cls.all()
        tarots = random.choice(arcana)
        # 正位
        if ints == 0:
            return await MajorArcanaLog.insertTarotLog(tarots, user_id, tarots_img_path+tarots.image,"正位")
        # 逆位
        if ints == 1:
            return await MajorArcanaLog.insertTarotLog(tarots, user_id, tarots_img_path+tarots.image,"逆位")


class MajorArcanaLog(Model):
    """
    大阿尔克纳牌
    """
    id = fields.IntField(pk=True)
    user_id = fields.CharField(max_length=255, description="用户id")
    ints = fields.CharField(max_length=64,description="正逆")
    name = fields.CharField(max_length=64, description="牌名")
    meaning = fields.TextField(description="正位/逆位含义")
    image = fields.CharField(max_length=255, description="图片文件名")
    create_time = fields.DateField(auto_now_add=True)

    class Meta:
        # 指定表名
        table = "major_arcana_log"
        table_description = "大阿尔克纳牌抽取日志"

    @classmethod
    async def insertTarotLog(cls, model: MajorArcana | None, user_id: str | None, image: str | None, ints:str | None) -> Self | None:
        """
        插入大阿尔克纳牌抽取日志
        :param model:
        :param user_id:
        :param image:
        :param ints:
        :return:
        """

        if ints == "正位":
            meaning = model.upright_meaning
        else:
            meaning = model.reversed_meaning
        data = {
            'user_id': user_id,
            'ints': ints,
            'name': model.name,
            'meaning': meaning,
            'image': image,
            'create_time':datetime.now().date()
        }

        return await cls.create(**data)

    @classmethod
    async def getTarotLog(cls, user_id: str | None ) -> Self | None:
        """
        查询大阿尔克纳牌抽取日志
        :param user_id:
        :return:
        """
        return await cls.filter(user_id=user_id,create_time = datetime.now().date()).first()


Major_arcana_initial_data = [
    MajorArcana(
        name="愚者 (The Fool) ",
        upright_meaning="从零开始; 好赌运; 不墨守成规; 追求新奇的梦想; 冒险; 放浪形骸; 艺术家的气质; 异于常人; 直攻要害、盲点; 爱情狩猎者; 爱情历经沧桑; 不拘形式的自由恋爱",
        reversed_meaning=" 不安定; 孤注一掷会失败; 缺乏责任感; 损失; 脚跟站不稳; 堕落; 没发展; 没计划; 走错路; 行为乖张; 轻浮的恋情; 感情忽冷忽热; 不安定的爱情之旅",
        image="The Fool.jpg"),
    MajorArcana(
        name="魔术师 (The Magician)",
        upright_meaning="好的开始; 具独创性; 有发展的; 新计划成功; 想像力丰富或有好点子; 有恋情发生; 拥有默契良好的伴侣; 有新恋人出现; 值得效仿的对象出现",
        reversed_meaning=" 失败; 优柔寡断; 才能平庸; 有被欺诈的危险; 技术不足; 过于消极; 没有判断力; 缺乏创造力; 爱情没有进展 ",
        image="The Magician.jpg"),
    MajorArcana(
        name="女祭司 (The High Priestess)",
        upright_meaning="知性、优秀的判断力; 具洞察力及先见之明; 强大的战斗意志; 冷静的统率力; 学问、研究等精神方面幸运; 独立自主的女性; 柏拉图式的爱情; 有心灵上交往至深的友人; 冷淡的恋情 ",
        reversed_meaning=" 无知、缺乏理解力; 研究不足; 不理性的态度; 自我封闭; 神经质; 洁癖; 与女性朋友柒争执; 对人冷淡; 晚婚或独身主义; 没有结果的单相思; 气色不好; 不孕",
        image="The High Priestess.jpg"),
    MajorArcana(
        name="皇后 (The Empress)",
        upright_meaning="充满创造力与母性光辉; 生活富足、美满; 事业上有出色的规划与执行能力，易取得成果; 感情中温柔体贴，是理想的伴侣; 孕育新生命或有新的创意项目诞生",
        reversed_meaning=" 创造力受阻; 生活陷入混乱，经济上可能出现问题; 感情中可能变得情绪化、占有欲强; 缺乏实际行动，计划难以实现; 健康方面可能有妇科问题",
        image="The Empress.jpg"),
    MajorArcana(
        name="皇帝 (The Emperor)",
        upright_meaning="以坚强的意志力及手腕获致成功; 富裕和力量; 有责任感; 良好的处理能力; 具领导能力; 男性的思考; 坚持到底; 虽有点专制却值得信赖; 条件诱人的提亲; 与年长者恋爱 ",
        reversed_meaning=" 不成熟; 意志薄弱; 虚有其表; 看不清现实; 欠缺实务能力; 因傲慢而招人反感; 工作过度; 固执; 没有经济基础; 没有好对象; 苦恋结束; 勉强的感情",
        image="The Emperor.jpg"),
    MajorArcana(
        name="教皇 (The Hierophant) ",
        upright_meaning="受人信赖; 有贵人相助; 贡献; 受上司重视; 能胜任工作; 拥有一颗温柔的心; 受惠于有益的建言; 接触宗教的事物大吉; 与年长的异性有缘; 良缘; 深情宽大的爱; 有结良缘的机会 ",
        reversed_meaning=" 没信用; 没有贵人相助; 孤立无援; 不受欢迎的好意; 依赖心是最大的敌人; 太罗嗦而讨人厌; 碍于私情而无法成功; 心胸狭窄; 得不到亲人的谅解的恋情; 彼此过于关心; 缘分浅薄的恋情 ",
        image="The Hierophant.jpg"),
    MajorArcana(
        name="恋人 (The Lovers) ",
        upright_meaning="幸运的结合; 有希望的将来; 有共同做事的伙伴; 与人合作或社团活动; 敏感决定前进之路的好时机; 有意气相投的朋友; 爱情机会将到来; 罗曼蒂克的恋情; 爱的预感",
        reversed_meaning=" 分离; 消解; 不合作的态度; 眼花缭乱; 没有满意的成果; 无法持续; 退休; 妨碍; 血气方刚; 多情的人; 分手; 冷漠的爱; 背信; 逃避爱情; 短暂的恋情",
        image="The Lovers.jpg"),
    MajorArcana(
        name="战车 (The Chariot)",
        upright_meaning="前进必胜; 先下手为强; 独立; 起程; 在颠簸中仍有好成绩; 活泼; 有野心; 以速度取胜; 有开拓精神; 握有指挥权; 战胜敌手; 富行动力的恋情; 恋爱的胜利者 ",
        reversed_meaning=" 失败; 丧失战斗意志; 状态不佳; 挫折; 性子过急为失败之因; 不感兴趣; 效率不佳; 资金运转困难; 无奋斗精神; 有强劲敌手进入; 被拒绝; 因怯懦而使恋情不顺 ",
        image="The Chariot.jpg"),
    MajorArcana(
        name="力量 (Strength) ",
        upright_meaning="不屈不挠的精神; 将不可能化为可能的意志力; 全力以赴; 突破难关; 坚强的信念和努力; 挑战已知危险的勇气; 神秘的力量; 旺盛的斗志; 轰轰烈烈的恋情; 克服困难的真实爱情",
        reversed_meaning=" 疑心病; 犹豫不决; 实力不足; 无忍耐力; 危险的赌注; 勉强为之而适得其反; 丧失自信; 喜欢故弄玄虚; 体力不足; 自大自负; 误用力气 ",
        image="Strength.jpg"),
    MajorArcana(
        name="隐士 (The Hermit) ",
        upright_meaning="智能与卓越见解; 不断地追求更高层次的东西; 思虑周密; 冷静沉着; 不多言; 接触知性事物吉; 正中核心的建言; 活动慢慢进行较有成果; 出局; 追求柏拉图式的爱情; 暗中的爱情",
        reversed_meaning=" 一视同仁; 不够通融; 不专心易生错误; 过分警戒，无法顺利进行; 秘密泄漏; 过于固执不听别人的意见; 孤独; 动机不单纯; 因怨言及偏见招人嫌; 轻浮的爱情; 怀疑爱情",
        image="The Hermit.jpg"),
    MajorArcana(
        name="命运之轮 (The Wheel of Fortune) ",
        upright_meaning="机会到来; 随机应变能力佳; 好运; 转换期; 意想不到的幸运; 升迁有望; 变化丰富; 好时机; 宿命的相逢; 一见钟情; 幸运的婚姻; 富贵的身份 ",
        reversed_meaning=" 低潮期; 时机未到; 评估易出错; 时机不好; 没有头绪; 处于劣势; 生活艰苦; 情况恶化; 计划停滞需要再等待; 失恋; 短暂的恋情; 易错失良机; 不敌诱惑; 爱情无法持久 ",
        image="The Wheel of Fortune.jpg"),
    MajorArcana(
        name="正义 (Justice)",
        upright_meaning="公正; 严正的意见; 良好的均衡关系; 严守中立立场; 凡事合理化; 身兼两种工作; 协调者; 与裁判、法律相关者; 表里一致的公正人物; 以诚实之心光明正大地交往; 彼此能获得协调 ",
        reversed_meaning=" 不公正; 不平衡; 不利的条件; 偏颇; 先入为主的观念; 偏见与独断; 纷争、诉讼; 问心有愧; 无法两全; 天平两边无法平衡; 性格不一致; 无视于社会道德观的恋情; 偏爱",
        image="Justice.jpg"),
    MajorArcana(
        name="倒吊人 (The Hanged Man)",
        upright_meaning="接受考验; 无法动弹; 被牺牲; 有失必有得; 从痛苦的体验中获得教训; 过度期; 不贪图眼前利益; 浴火重生; 多方学习; 奉献的爱; 明知辛苦但全力以赴",
        reversed_meaning=" 无谓的牺牲; 折断骨头; 有噩运、居于劣势; 任性妄为; 不努力; 变得没有耐性; 利己主义者; 受到惩罚; 无偿的爱; 缺乏共同奋斗的伙伴",
        image="The Hanged Man.jpg"),
    MajorArcana(
        name="死神 (Death)",
        upright_meaning="失败; 毁灭之日将近; 损害继续延续; 失业; 进展停滞; 交易停止; 为时已晚; 停滞状态; 生病或意外的暗示; 味如嚼蜡的生活; 不幸的恋情; 恋情终止; 彼此间有很深的鸿沟; 别离 ",
        reversed_meaning=" 起死回生的机会; 脱离低迷期; 改变印象; 回心转意再出发; 挽回名誉; 奇迹似地康复; 突然改变方针; 已经死心的事有了转机; 斩断情丝，重新出发",
        image="Death.jpg"),
    MajorArcana(
        name="节欲 (Temperance) ",
        upright_meaning="单纯化; 顺畅; 交往平顺; 两者相融顺畅; 调整; 彼此交换有利条件; 平凡中也有重要的契机; 平顺的心境; 纯爱; 从好感转为爱意; 深爱 ",
        reversed_meaning=" 消耗; 每节制的损耗，对身心产生不好的影响; 疲劳; 不定性的工作; 缺乏调整能力; 下降; 浪费; 不要与人 合作; 不融洽; 爱情的配合度不佳 ",
        image="Temperance.jpg"),
    MajorArcana(
        name="恶魔 (The Devil)",
        upright_meaning="被束缚; 堕落; 恶魔的私语; 卑躬屈膝; 欲望的俘虏; 荒废的生活; 举债度日; 病魔入侵; 夜游过多; 不可告人的事; 恶意; 不可抗拒的诱惑; 私密恋情; 沉溺于感官刺激之下",
        reversed_meaning=" 逃离拘束; 长期的苦恼获得解放; 斩断前缘; 越过难关; 暂时停止; 拒绝诱惑; 舍弃私欲; 治愈长期病痛; 别离 时刻; 如深陷泥沼爱恨交加的恋情",
        image="The Devil.jpg"),
    MajorArcana(
        name="塔 (The Tower) ",
        upright_meaning="致命的打击; 纷争; 纠纷不断; 与周遭事物对立，情况恶化; 意想不到的事情; 急病; 受牵连; 急剧的大变动; 信念奔溃; 逆境; 破产; 没有预警，突然分离; 破灭的爱; 玩火自焚",
        reversed_meaning=" 紧迫的状态; 险恶的气氛; 内讧; 即将破灭; 急需解决的问题; 承受震撼; 背水一战; 注意刑事问题; 因骄傲自大将付出惨痛的代价; 状况不佳; 困境; 爱情危机; 分离的预感 ",
        image="The Tower.jpg"),
    MajorArcana(
        name="星辰 (The Star) ",
        upright_meaning="愿望达成; 前途光明; 充满希望的未来; 美好的生活; 曙光出现; 大胆的幻想; 水准提高; 新的创造力; 想像力; 理想的对象; 美好的恋情; 爱苗滋生 ",
        reversed_meaning=" 挫折、失败; 理想过高; 缺乏想像力; 异想天开; 事与愿违; 失望; 从事不喜欢的工作; 好高骛远; 情况悲观; 不可期待的对象; 没 有爱的生活; 秘密恋情; 仓皇失措",
        image="The Star.jpg"),
    MajorArcana(
        name="月亮 (The Moon) ",
        upright_meaning="不安与动摇; 心中不平静; 谎言; 暧昧不明; 鬼迷心窍; 暗藏动乱; 欺骗; 终止; 不安的爱; 三角关系",
        reversed_meaning=" 从危险的骗局中逃脱; 状况稍为好转; 误会冰释; 破除迷惘; 时间能解决一切; 眼光要长远; 静观等待; 早期发现早期治疗有效; 事前察知危险; 对虚情假意的恋情已不在乎 ",
        image="The Moon.jpg"),
    MajorArcana(
        name="太阳 (The Sun)",
        upright_meaning="丰富的生命力; 巨大的成就感; 人际关系非常好; 爱情美满; 内心充满了热情和力量; 一定能够实现的约定; 飞黄腾达; 无忧无虑",
        reversed_meaning=" 情绪低落; 事情失败; 朋友的离去和人际关系的恶化; 无法安定内心; 忧郁孤单寂寞; 爱情不顺 利; 取消的计划; 工作上困难重重 ",
        image="The Sun.jpg"),
    MajorArcana(
        name="审判 (Judgement)",
        upright_meaning="复活的喜悦; 开运; 公开; 改革期; 危机解除; 决断; 荣升; 崭露头角; 好消息; 爱的使者; 恢复健康; 坦白; 复苏的爱; 再会; 爱的奇迹 ",
        reversed_meaning="一败不起; 幻灭; 离复苏还有很长的时间; 不利的决定; 不被采用; 还未开始就结束了; 坏消息; 延期; 无法决定; 虽重新开始，却又恢复原状; 分离、消除; 恋恋不舍",
        image="Judgement.jpg"),
    MajorArcana(
        name="世界 (The World)",
        upright_meaning="完成; 成功; 拥有毕生的志业; 达成目标; 永续不断; 最盛期; 完美无缺; 接触异国，将获得幸运; 到达标准; 精神亢奋; 快乐的结束; 模范情侣 ",
        reversed_meaning=" 未完成; 无法达到计划中的成就; 因准备不足而失败; 中途无法在进行; 不完全燃烧; 一时不顺利; 饱和状态; 烦恼延续; 精神松弛; 个人惯用的表现方式; 因不成熟而 使情感受挫; 合谋; 态度不够圆融",
        image="The World.jpg")]
