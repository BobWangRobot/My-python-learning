from sys import exit
import random

i = [1, 2, 3]

def street():
    print("这天，你走在街上\n迎面遇到一个老乞丐拦住你")
    next = input("请选择：\n1.不理他，继续走\n2.停下看看\n>>>")
    if "1" in next or "不"in next:
        kind()
    elif"2"in next or "停"in next:
        print("老乞丐拿出一本破旧的小册子\n对你说：“少年，我看你根骨奇佳，是天生的练武奇才！”")
        print("“这本《如来神掌》就10块钱卖给你吧。”")
        print("若是有朝一日打通了任督二脉，必然前途无量啊！")
        choose = input("请选择：1.买\n2.不买\n>>>")
        if "1" in choose or "买" in choose:
            kongfu()
        elif "2" in choose or "不"in choose:
            captain()
        else:
            print("老乞丐叫到：“不买就不买，说什么废话！”")
            end("你走回了家，又是平常的一天")
    else:
        print("无法识别，请重新输入！")
        street()

def kongfu():
    print("你将《如来神掌》带回了家，日日苦练不止。")
    print("练了一段时日，你发现自己毫无进步，依然被隔壁胖虎追着打。")
    persistence = input("还要继续下去吗？\n1.继续练。2.放弃。\n>>>")
    if"1"in persistence or "继续练"in persistence:
        boss()
    elif"2"in persistence or"放弃"in persistence:
        end("你放弃了成为了武学大师的梦想，就这样过着平凡的日子，并将《如来神掌》传给了子女。")
        exit(0)
    else:
        print("无法识别，请重新输入！")
        kongfu()

def boss():
    print("虽然没什么进步，但你依然没有放弃成为武学大师的梦想")
    print("因为你坚信，自己就是天生的练武奇才，只是还未打通任督二脉。")
    input("按下Enter继续")
    a = "--------"
    print(a*8,"18年后",a*8)
    print("这天清晨，像往常一样，你正在后院练武。")
    print("外面传来一阵打斗声")
    print("你出门查看，看见一对中年夫妇正与一个秃头黑衣人生死相搏")
    print("那对中年夫妇，赫然是你的偶像：杨过，小龙女！")
    print("生死关头，你该如决断？")
    determination = input("冲上去帮忙！ 或者 逃跑\n>>>")
    if "冲" in determination:
        print("你冲进战团，被秃头黑衣人一掌打飞")
        input("按下Enter继续")
        fortune = random.randint(0,10)
        if fortune >= 3:
            print("你倒在地上，口吐鲜血。")
            print("但是，这一掌也间接打通了你的任督二脉。")
            print("你多年积累的真气一朝爆发，迅速修复了你的伤势。")
            print("你感到自己充满了力量，对着秃头黑衣人遥遥使出一记如来神掌。")
            print("“砰！”的一声巨响，黑衣人被轰飞。")
            input("按下Enter继续")
            print("你实现了自己的梦想\n终成一代大师\n从此\n江湖留下了你的传说")
            exit(0)
        else:
            end("你伤势过重，不幸身亡。\n死后，被杨过夫妇厚葬。")

def captain():
    print("你劈手打掉老乞丐的破书，大叫：\n“我可是要成为海贼王的男人！！！！！！”")
    print("~~~~~~~~``````~~~~~~~~"*5)
    input("按下Enter继续")
    print("数年后，你成为了一名海盗")
    print("这天，你所在的船遭遇海军的突袭\n船长和大副全部身亡\n指挥船员的任务交给你了！！！")
    enemy = random.randint(250,500)
    team = random.randint(250,500)
    print("你有两个选择：1.投降\n2.血战到底")
    chance = input("你将如何选择：\n>>>")
    if "1"in chance or "投降" in chance:
        end("你被海军抓获，处以绞刑。")
    elif "2"in chance or "血战到底" in chance:
        print("~~~~~~~~~~~~"*4,"进入战场","~~~~~~~~~~~~"*4)
        print("敌方共%d人，我方共%d人" % (enemy, team))
        for b in i:
            print("---------------"*3,"第%d回合"% b ,"---------------"*3)
            print("你带领船员们发起了进攻")
            input("进攻（按下Enter发起攻击）")
            injury = random.randint(50, 100)
            self = random.randint(50, 100)
            enemy = enemy - injury
            team = team - self
            print("船员在你的带领下奋勇杀敌\n敌人死伤%d人，还剩%d人" %(injury,enemy) )
            print("我方死伤%d人,还剩%d人"%(self,team))
        print("~~~~~~~~~~~~" * 4, "战斗结束", "~~~~~~~~~~~~" * 4)
        if enemy < team:
            print("敌人溃退了！")
            input("按下Enter键乘胜追击")
            print("你击退了海军，获得了胜利！")
            print("从此，你纵横七海，所向无敌，终成一代海贼王。")
            exit(0)
        else:
            print("我方溃败了！")
            end("很不幸，你在战斗中身亡")

def kind():
    print("老乞丐突然扯住你的衣角，求你给他一口吃的。")
    mind = input("1.给他买些食物\n2.不管他，匆匆走开")
    if "1" in mind:
        treasure()
    elif "2" in mind:
        end("你回到家中，结束了平淡的一天")
    else:
        print("无法识别，请重新输入！")
        kind()

def treasure():
    print("老乞丐狼吞虎咽般吃光了你给的食物，然后离开了。")
    print("几天后，你去山中游玩，不慎迷路。")
    print("走着走着，突然发现一个山洞，洞口装着一个大铁门")
    print("你试着寻找开门方法")
    door()

def door():
    open_door = input("1.念动咒语。\n2.用力推门\n3.离开\n请选择：")
    if "1" in open_door or "念动"in open_door:
        for r in i:
            say = input("请念咒语：")
            if say == "芝麻开门":
                break
        if say == "芝麻开门":
            print("门开了")
            road()
        else:
            print("机关开启，毒箭放出")
            end("你中毒而死")
    elif "2"in open_door or "用力" in open_door:
        print("机关开启，毒箭放出")
        end("你中毒而死")
    elif "3"in open_door or "离开"in open_door:
        end("你回到了家")
    else:
        end("你不慎掉下了悬崖，粉身碎骨")

def road():
    print("面前有两条路，你选哪条？")
    choose = input("左？右？\n请选择：")
    if "左" in choose:
        print("机关开启，毒箭放出")
        end("你中毒而死")
    elif "右"in choose:
        print("你眼前出现了一个堆满金币的藏宝室")
        room()
    else:
        print("机关开启，毒箭放出")
        end("你中毒而死")
def room():
    how_muich = input("你准备拿走多少？")
    if how_muich.isdigit():
        how_muich = int(how_muich)
    else:
        print("请输入数量")
        greedy()

    if how_muich > 150:
        print("你正忙着搬金币，强盗们回来了")
        print("他们抓住并杀死了你")
        end("人为财死，鸟为食亡")
    else:
        print("你拿走了金币，从此过上了富足的生活")
        exit(0)

def end(why):
    print(why)
    print("Game Over.")

street()
#总结：if语句，要用or判断时，需要用完整的语句。