﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define gg = Character('Кадер', color="#C5D0E6")
define al = Character('Альмина', color="#50C878")
define k = Character('Каури', color="#355E3B")
define ar = Character('Арабелла', color="#8A2BE2")
define yu = Character('Юстас', color="#753313")
define kr = Character('Крупье', color="#D68A59")
define m = Character('Мику', color="#BDDA57")

define kid = False
define self = False
define game2 = False
define amm = False
define poison = False

define persistent.kauri = False
define persistent.almina = False
define persistent.arabella = False
define persistent.yustas = False
define persistent.miku = False
define persistent.cards = False
define persistent.les = False
define persistent.home = False
define persistent.mansion = False
define persistent.cadr = True
define persistent.ref1 = True
define persistent.ref2 = True
define persistent.ref3 = True
define persistent.ref4 = True
define persistent.ref5 = True
define persistent.ref6 = True
define persistent.ref7 = True

init:
    $ blod = ImageDissolve(im.Tile("blod.png"), 3.0, 30, reverse=False)
    $ flash = Fade(.25, 0, .75, color="#fff8dc")
    
define gui.text_outlines = [(4, "0124", 0, 0), (3, "0124", 0, 0), (1, "0124", 0, 0), (1, "0124", 0, 0)]

label splashscreen:
    # громкость по умолчанию
    python:
        # при первом запуске
        if not persistent.set_volumes:
            persistent.set_volumes = True
            # музыку потише
            _preferences.volumes['music'] = 1.0
            _preferences.volumes['sfx'] = .5
            # игра на весь экран
            _preferences.fullscreen = True
    return

define audio.bgmus1 = "audio/bgmus1.wav"
define audio.back_sound = "back_sound.mp3"
define audio.bgmus2 = "audio/bgmus2.wav"
define audio.end1 = "audio/end1.wav"
define audio.end2 = "audio/end2.wav"
define audio.end3 = "audio/end3.wav"

# Игра начинается здесь:
label start:
    play music bgmus1
    scene home
    $ persistent.home = True
    # сон 1
    al "Просыпайся. Эй, соня, просыпайся!"
    al "Проснись и пой!"
    $ persistent.almina = True
    "Я почувствовала как меня ущипнули в плечо."
    # show gg at left
    gg "Ай…"
    show alidle at right
    al "Что за сонное «ай»? Ты не забыла?"
    gg "Что забыла?"
    al "Просыпайся! Тебе так-то нужно собрать ингредиенты для лавки и для себя."
    al "Думаешь с белоснежными волосами ты долго скроешься?"
    "Сквозь сон приходит осознание сегодняшнего дня."
    "Каждый раз, когда приходит день обновления маскировки я вспоминаю о своей прошлой жизни."
    "Кадер Хишуо, наследница одного из богатейших родов Вэйо. Любящая семья, теплый дом, вкусная еда… Как все это далеко."
    "После того, как родителей убили, я смогла сбежать. Но с моей внешностью долго не скроешься."
    show aridle at left
    ar "Доброго утра, девочки! Как ваши дела идут?"
    $ persistent.arabella = True
    hide alidle
    show alsmile at right
    al "Доброго утра! Кадер никак не проснется. Как никак весь учет ведет она, поэтому чего нам не хватает знает только один человек в этой комнате."
    gg "Да, да… сейчас. Доброго утра. С лавкой все хорошо, людям всегда нужны лекарства и косметика."
    ar "Я не всегда интересуюсь исключительно заработком. Тем более принимать других детей, помимо вас троих, было рисковано."
    gg "Но ведь, когда вы пустили нас в дом, были поставлены четкие условия по окупаемости нашего нахождения."
    hide aridle
    show arsmile at left
    ar "Да, я не помогаю в ущерб себе, но это не значит, что мне наплевать на птенцов под моим крылом. Так как ты? Скоро твой день рождения, отправитесь в столицу?"
    gg "Думаю чуть позже. Другие дети еще не готовы самостоятельно заниматься лавкой без нас. А день рождения…"
    gg "Думаю, лучший подарок — ингредиенты для краски или литий и аммиак."
    hide arsmile
    show aridle at left
    ar "Это для твоего нового зелья?"
    gg "Да. Оно должно изменить цвет глаз. Пригодится в столице."
    ar "Поражаюсь твоему таланту. Что ж, мне пора. Хорошего дня."
    hide aridle
    gg "До свидания!"
    al "Удачи!"
    hide alsmile
    show alidle at right
    al "Но за ингредиентами в любом случае нужно сходить."
    gg "Да-да, знаю. Не нужно напоминать мне лишний раз."
    show kidle at center
    k "А как по мне не мешало бы, а то забудешь как саму себя зовут, пока разрабатываешь новые зелья."
    $ persistent.kauri = True
    gg "Ох, это говорит тот, кто вечно пропадает на тренировках."
    k "А сама-то когда в последний раз была на тренировке? Все уже и забыли не только как ты выглядишь, но и как звали тебя!"
    k "Все так и спрашивают меня: «А где та госпожа никто-не-знает-как-зовут?»."
    al "Очень похоже!"
    gg "Ладно, я поняла вас."

    menu:
        "Пойти собирать травы":
            $ self = True
            gg "Пойду травы соберу."
            k "Я с тобой, прикрою если кто-то нападет."
            gg "Хорошо."
            al "Я соберу детей. Может, пусть сегодня отдохнут? Придумаю куда их сводить."
            gg "Хорошая идея."
            al "Тогда пойду разбужу всех."
            jump scene2
        "Отправить детей за травами":
            $ kid = True
            gg "Завтра фестиваль, пусть дети сегодня вместо проведения экскурсий прогуляются. Пусть помимо сбора ингредиентов поиграют."
            al "Тогда я соберу их и прослежу."
            jump scene2
        
        
    return

label scene2:

    scene home
    show kidle at center
    k "Не хочешь пока есть время сыграть?"
    gg "Давай."
    k "Вообще я рад, что однажды ты купила триаду. Легенда, что это игра, с помощью которой победили драконов, странная, но игра и вправду стоящая."
    gg "Решить конфликт с помощью игры достаточно разумное решение."
    gg "Так что победили драконов, победят и тебя!"
    k "Посмотрим!"
    k "Правила еще не забыла?"
    
    menu:
        "Напомнить правила":
            gg "Что ж, напомни правила."
            k "Хорошо. У тебя на руке будет пять карт. На игровом поле 9 ячек."
            k "Тебе нужно захватить карты противника."
            k "У каждой карты есть характеристики в месте, где она может соприкасаться с другой картой."
            k "Чтобы захватить карту, тебе нужно, чтобы твоя карта была по характеристике выше, чем карта противника, там, где они соприкоснутся."

        "Не напоминать правила":
            gg "Ты забыл кто вас научил играть?"
            
    stop music fadeout 5.0
    
    jump minigame1
    
    return
    
label minigame1:

    $ enemy_deck = [hog_rider2, archers2, princess2, mosquetear2, barbarians2]

    call cardgame1 from _call_cardgame1
    
    jump mini1
    
    return

label mini1:
    play music bgmus1
    scene home
    
    menu:
        "Сыграть еще раз":
            menu:
                "Напомнить правила":
                    show kidle at center
                    gg "Что ж, напомни правила."
                    k "Хорошо. У тебя на руке будет пять карт. На игровом поле 9 ячек."
                    k "Тебе нужно захватить карты противника."
                    k "У каждой карты есть характеристики в месте, где она может соприкасаться с другой картой."
                    k "Чтобы захватить карту, тебе нужно, чтобы твоя карта была по характеристике выше, чем карта противника, там, где они соприкоснутся."
                "Не напоминать правила":
                    show kconf at center
                    gg "Не против еще одной игры?"
                    k "Я только рад!"
            jump minigame1
        "Закончить игру":
            $ persistent.cards = True
            show kconf at center
            show alsmile at right
            k "Как-то рано ты вернулась."
            al "Да. Мику забыл своего медвежонка и совершенно не хочет никуда идти без него."
            al "Пойду спущусь за ним."
            hide kconf
            hide alsmile
            show kconf at center
            gg "Да уж. Я рада, что она взяла заботы о детях полностью на себя. Когда мы уедем, ей должно быть проще с ними."
            k "Думаю, она уже заменила им матерей. Моя сестренка лучшая!"
            gg "Как ни странно я с тобой согласна. Она лучшая."
            show alidle at right
            al "Не забывайте что я буду в одиночку следить за детьми и лавкой когда вы уедете."
            al "Не будь я лучшей, доверили бы мне такую честь!?"
            gg "Точно. Вряд ли кто-то другой справился бы."
            al "То-то же!"
            gg "Так что такая умница достойна найти учителя по магии и фармацевтике."
            al "Эй, не начинай... Мы же знаем, что это сейчас слишком дорого для нас."
            al "Если у вас в столице все сложится хорошо, я все равно стану учеником. Просто на год позже. Не страшно."
            k "Ты достойна самого лучшего наставника уже сейчас."
            al "Спасибо, братец."
            show mlyub at left
            m "Кадер! Кадер! Мы нашли котенка! Можно нам его оставить?"
            al "Что думаешь, Кадер?"
            m "Кадер, пожаалуйста!"
            menu:
                "Запретить":
                    hide mlyub
                    show msad at left
                    gg "Это явно плохая идея. Альмина останется одна, еще и за маленьким котенком следить. Мику, ты можешь найти котенку другой дом."
                    al "Да. Может кто-то из трактирщиков возьмет себе котенка для ловли крыс. Думаю, мы сможем его пристроить во время прогулки."
                    m "Хорошо."
                "Разрешить":
                    hide mlyub
                    show msmile at left
                    gg "Если ты сама не против котенка, то почему бы и нет."
                    m "Спасибо! Кадер, ты лучшая!"
                    m "Пойду расскажу всем!"
                    al "Они уже обожают нового члена семьи."
            $ persistent.miku = True
            k "Удачной прогулки."
            al "Спасибо. До вечера!"
            
    jump scene3_1
    return
    
label scene3_1:

    if self:
        # scene3_1
        scene lug
        show kidle at center
        k "Давно мы никуда вместе не выбирались. Перед шестнадцатилетием ты стала затворницей."
        gg "Думаю, ты и сам понимаешь, что мне лучше не высовываться."
        gg "Пока существует магический договор, Юстас знает, что я жива. Значит, меня ищут."
        k "Но ты же как-то скрывалась три года меняя цвет волос."
        gg "В столице этого может не хватить."
        k "Поэтому ты разрабатываешь свое новое зелье?"
        gg "Да, оно должно изменить цвет глаз."
        k "А не боишься что тебя даже жених не узнает в таком случае?"
        gg "Ну, не то чтобы мы с ним часто виделись раньше. Сомневаюсь, что его смутит мой внешний вид. Да и изменения все обратимые."
        k "Ну да."
        gg "Как твои тренировки? Скоро пойдешь на первую охоту?"
        k "Да. Еще около месяца и сформируют отряды. Мы как раз в этот лес пойдем."
        gg "То есть ты решил пойти чтобы лучше узнать местность, а не чтобы защитить хрупкую спутницу?"
        k "Ха-ха, кто еще хрупкая спутница? Лучше бы тоже присоединилась. Сама ведь хотела год-другой перебиться в авантюристах."
        gg "Я еще успею присоединиться к тебе. Может, даже Альмина согласится. Как никак лекарем может быть не каждый."
        gg "Что ж, я закончила. Пойдем домой. Остальные уже должны были вернуться."

        jump scene4_1
    else:
        jump scene3_2
    
    return
    
label scene3_2:

    scene home
    show kidle at center
    k "Не очень похоже, что сегодня кому-то взбредет в голову зайти сюда за лекарствами."
    gg "Поэтому я могу спокойно сосредоточиться на исследованиях."
    k "Поражаюсь сколько всего ты знаешь. Ты вообще человек?"
    gg "Семья занималась военными технологиями, и меня готовили к разработке нового оружия."
    gg "Мне по статусу положено знать столько всего из разных областей. Правда, здесь я только в алхимии практикуюсь."
    k "Могла бы и в магии, ходи ты со мной на тренировки."
    gg "Лучше бы Альмину уговорил раскрыть свой талант целителя."
    k "Да, вам с магией крайне повезло. Все еще поражаюсь, что с помощью какой-то бумажки твой дядя знает, что ты жива."
    gg "Не бумажки, а магического генеалогического древа."
    gg "И с помощью него же он увидел, что всего лишь в шестой линии наследования."
    k "Ну, благодаря нему же он и не получил семейное дело в свои руки."
    gg "Что правда, то правда."
    k "Что будешь делать как вернешься в столицу и заявишь о своих правах?"
    gg "Посмотрим. Я не знаю в каком состоянии производство, да и какие планы у королевской семьи на мое замужество."
    k "На свадьбу хоть пригласишь?"
    gg "Как будто, я позволю вам остаться здесь одним. Ты же помнишь что я все равно присоединюсь к тебе в странствиях?"
    k "А что после?"
    gg "А после будешь служить моим телохранителем. Согласен?"
    k "Вполне, если Альмина будет твоим лекарем."
    gg "Договорились!"
    k "Что-то они задерживаются. Должны были уже вернуться…"

    jump scene4_1
    
    return
    
label scene4_1:

    scene homesum
    show kconf at center
    k "Уже стемнело, а их все еще нет."
    gg "Нужно пойти искать их."
    k "Хорошо, я поспрашиваю знакомых."
    gg "Я с тобой."
    k "Лучше останься здесь."
    gg "Вдвоем мы быстрее узнаем где они!"
    k "У нас из знакомых лишь Арабелла и авантюристы. Арабелла скоро вернется, а к авантюристам я могу пойти один."
    k "Дождись Арабеллу. Узнаешь у нее знает ли она что-то."
    hide kconf
    "Ожидание тянулось крайне долго."
    # сон 2
    show aridle at left
    ar "Кадер, почему ты здесь одна?"
    # “Сон мгновенно покинул меня"
    gg "Арабелла, Альмина и дети пропали, вы не слышали что-то о них!?"
    ar "Я слышала от девушек, что они видели, как кто-то продавал девушку, похожую на Альмину."
    gg "Когда!? Кто это был?"
    hide aridle
    show armedit at left
    ar "Я не придала значения этим разговорам. Даже и подумать не могла что кого-то из вас похитят и решат продать!"
    ar "Еще днем она заглянула к нам и хвасталась, что ее взял в ученики кто-то из клана восточных ведьм!"
    ar "Я и представить не могла, что с ними случилось что-то плохое."
    gg "Как теперь найти того человека?..."
    ar "Ты осталась одна?"
    gg "Нет, Каури пошел в тренировочный лагерь, узнать видел ли кто-то ребят."
    ar "Тогда дождемся вестей от него."
    "Снова ожидание?"
    "Что если он ничего не узнает…"
    show kidle at center
    k "Арабелла, вы здесь! Вы знаете что-то?..."
    ar "Я не придала значение слухам, так что ничего конкретного рассказать не могу. Альмину пытались продать, но кто - я не знаю."
    hide kidle
    show kevil at center
    k "Я знаю…"
    gg "Что?"
    k "Твой горячо любимый родственник, Кадер… Он похищал детей на продажу, теперь и до нас добрался."
    k "Завтра пройдет аукцион. Он собирает у себя в поместье богачей со всей страны. Толстосумы будут играть друг с другом и…"
    k "Покупать людей, предоставленных Юстасом…"
    hide armedit
    show aridle at left
    gg "Пусть подавится своими деньгами, я не позволю ему продать кого-либо еще!"
    ar "Как ты планируешь это сделать? Просто появишься и скажешь что ты главнее и правее?"
    gg "Это тоже вариант. На глазах такого количества людей он меня не убьет. А вот я его - вполне."
    k "Как ты собираешься убить его прилюдно?"
    gg "В мире полно ядовитых растений. Заставлю его съесть или вдохнуть что-то."
    k "План слишком рисковый. Зная кто ты, он точно из твоих рук ничего не примет."
    gg "У меня еще остался аммиак. Его вполне хватит."
    k "Ты сама-то не пострадаешь от этого?"
    gg "Я себя вылечить смогу, в отличии от них."
    k "Разве после того, как ты заявишь что ты Хишуо, он будет с тобой вообще иметь дело?"
    gg "Ты прав. Я могу заставить его сыграть со мной на наследство. А вот яд…"
    gg "Ты сможешь пробраться и отравить что-либо?"
    k "Да. Только убедись, что это безопасно и для тебя, и других пленников."
    gg "Хорошо. Когда пройдет прием у Юстаса?"
    k "После захода солнца."
    gg "Отлично, утром будет время подготовиться."
    hide aridle
    hide kevil
# сон 3?

    menu:
        "Использовать аммиак":
            $ amm = True
            show kidle at center
            "Пары аммиака достаточно токсичны. Для меня имеющегося лекарства хватит."
            "Ставка более чем оправданная."
            k "Как ты планируешь избавиться от запаха?"
            gg "Ты сейчас чувствуешь запах, поскольку в спирте сильно сконцентрирован аммиак."
            gg "Когда он окажется в воздухе, его запах почувствуется позже, чем газ отравит людей."
            k "А как же пленники?"
            gg "Они будут находиться в подвале, так что для них газ безопасен."
            k "Хорошо. Это все приготовления?"
            jump scene5_1_0
            
        "Использовать яд":
        
            gg "Завтра отправлюсь в лес."
            jump scene5_1_2
            
        "Отправиться в столицу":
            show kidle at center
            gg "Если Юстас устраивает такой праздник, то он задействовал в том числе тех людей, кто следил за мной. Я могу отправиться в столицу за помощью."
            k "Слишком рискованно. Кто тебя просто так примет в столице?"
            k "Тебя банально никто не знает, ты просто девочка с улицы."
            gg "Я не собираюсь стучаться к родственникам. Я пойду сразу к королевской семье."
            gg "О самозванках не было никаких новостей. Если придет девочка с улицы и заявит, что она невеста принца, они проверят это."
            k "И как же они за минуту узнают что ты не врешь?"
            gg "Помнишь о магическом генеалогическом древе, которое сделал отец? Вот с помощью него и узнают."
            show kconf at center
            k "Это все еще слишком не надежный план. Скорее всего ты просто не успеешь вернуться."
            gg "Все же я рискну."
            jump end1
    
    return
    
label scene5_1_0:
    
    scene home
    
    menu:
        "Да":
            show kidle at center
            gg "Да, это все. Мне осталось дождаться вечера."
            gg "Тебе нужно устроиться слугой в особняк и облить дрова этой жидкостью."
            k "При горении выделится яд?"
            gg "Верно. Как только начнется прием, ты должен будешь уйти."
            jump scene6_1
        "Собрать ядовитые растения":
            $ amm = False
            $ poison = True
            gg "Думаю, стоит посмотреть что есть из растений. Может, есть более безопасный вариант."
            jump scene5_1_2

    return

label scene5_1_2:
    
    scene lug
    
    gg "Думаю, я смогу найти достаточно токсичные травы. Их всегда было достаточно."
    play music back_sound
    
    if poison:
        $ hf_init("lugsum", 180,
            ("flower1", 1013, 705, _("Ландыш. Если употребить в пищу, при должном невезении, может остановиться сердце.")),
            ("flower2", 311, 660, _("Лютик. Может даже вызвать галлюцинации.")),
            ("flower3", 770, 775, _("Шафран. Мало токсичен, нужна слишком большая концетрация. Вкус блюда будет испорчен.")),
            ("flower4", 1413, 780, _("Аквилегия. Cложно понять токсичность этого сорта.")),
                # включаем смену курсора при наведении
            mouse=True,
            # включаем инвентарь с убиранием из него найденных предметов
            inventory=True,
            # включаем подсказки
            hint=True,
            # включаем подсветку предмета при наведении
            hover=brightness(.05),
            # уменьшаем размеры ячеек инвентаря, чтобы не мешали собирать предметы
            w=200,
            h=200
        )
    else:
        $ hf_init("lug", 180,
            ("flower1", 1013, 705, _("Ландыш. Если употребить в пищу, при должном невезении, может остановиться сердце.")),
            ("flower2", 311, 660, _("Лютик. Может даже вызвать галлюцинации.")),
            ("flower3", 770, 775, _("Шафран. Мало токсичен, нужна слишком большая концетрация. Вкус блюда будет испорчен.")),
            ("flower4", 1413, 780, _("Аквилегия. Cложно понять токсичность этого сорта.")),

            # включаем смену курсора при наведении
            mouse=True,
            # включаем инвентарь с убиранием из него найденных предметов
            inventory=True,
            # включаем подсказки
            hint=True,
            # включаем подсветку предмета при наведении
            hover=brightness(.05),
            # уменьшаем размеры ячеек инвентаря, чтобы не мешали собирать предметы
            w=200,
            h=200
    )

    # покажем вместе с фоном и фигурки на нём
    $ hf_bg()
    with dissolve

    centered "{size=+24}Нужно найти травы.\nНачинаем!"

    # запустим игру
    $ hf_start()

    # жёсткая пауза, чтобы игрок перестал кликать и не пропустил результаты
    $ renpy.pause(1, hard=True)

    # результаты
    if hf_return == 0:
        centered "{size=+24}Ура! Нужные ингредиенты найдены!"
    else:
        centered "{size=+24}Неудача\nНе собрано предметов: [hf_return]."
        
    $ hf_hide()
    with dissolve
    
    scene lugsum
    
    gg "Осталось лишь приготовить порошок. Это не займет много времени."
    gg "Самое сложное - дождаться начала приема в особняке..."
    $ persistent.les = True
    jump scene6_1
    
    return
    
label scene6_1:

    play music bgmus2
    scene homesum
    show arsmile at left
    ar "Каури оставил тебе несколько новых карт. Надеюсь, они помогут тебе."
    gg "Спасибо."
    ar "Кадер, милая, я бы хотела вам помочь. Каури я помогла попасть в особняк. Могу ли я сделать что-то еще?"
    gg "Не думаю."
    ar "Совершенно ничего? Хотя бы заявить стражам об аукционе?"
    gg "Скорее всего у них есть свои люди в страже города."
    gg "Но... В столице, возможно, что-то получится."
    ar "Когда я туда приеду ты скорее всего уже выберешься из особняка."
    gg "Да. Но Юстас может сбежать или произойдет что-либо еще."
    gg "Скажите страже, что он собирается продать наследницу дома Хишуо."
    ar "Хорошо. Если потребуется, я дойду до короля в кратчайшие сроки."
    gg "Не сомневаюсь."
    ar "Я выдвинусь сейчас же. Переодевайся. Удачи."
    hide arsmile
    pause 1.0
    gg "Старая одежда Арабеллы на удивление неплохо на мне сидит. Я и впрямь как дворянка. Хотя, я она и есть…"
    gg "Ну что, пришло время встретиться лицом к лицу со своим злейшим врагом."
    
    scene mansion
    $ persistent.mansion = True
    gg "Эх, Юстас, не растрачивай ты деньги на особняки и развлечения, может и был бы наследником…"
    gg "Каури уже должен был уйти. Теперь моя очередь вступить в игру."
    show yuidle at center
    yu "Здравствуйте, юная леди. Я раньше вас здесь не видел? Давно вы в прибыли в Еиннс? С какой целью прибыли?"
    $ persistent.yustas = True
    yu "Впрочем, не важно, я рад, что сие мероприятие посетила столь прекрасная дама."
    gg "Не думаю, что разделяю вашу радость. В Еиннсе я достаточно давно. Явно дольше, чем следовало бы."
    yu "Почему же? Вас ждут какие-то дела?"
    gg "Дела? Можно и так сказать. Приятно вновь встретиться, я - Кадер Хишуо."
    hide yuidle
    show yuevil at center
    yu "Ты…"
    yu "Я так долго тебя искал, дражайшая племянница."
    gg "Ты можешь обмануть всех собравшихся здесь людей, но не меня."
    gg "Предлагаю не затягивать наш разговор. Любезностями мы оба явно не горим желанием обмениваться."
    yu "Как ты смеешь так разговаривать!? Ты совсем забыла о приличиях!?"
    gg "А ты не забыл о приличиях, убивая мою семью?"
    gg "Предлагаю поступить просто и разумно: решим наш спор в игре."
    yu "Ты что, сказок начиталась?"
    gg "А почему нет. Здесь все играют на деньги. Кто-то проигрывает целое состояние."
    gg "А мы сыграем на семейное дело. Если выиграю я, ты отдашь свою жизнь во искупление греха."
    yu "А если я, твоя жизнь и наследство станут принадлежать мне."
    gg "Согласна."
    yu "По рукам!"
    
    jump minigame2
    
    return
    
label minigame2:

    stop music fadeout 5.0
    
    $ game2 = True
    
    $ enemy_deck = [lava_hound2, archers2, princess2, mosquetear2, baby_dragon2]

    call cardgame2 from _call_cardgame2
    
    return
    
label end1:
    
    stop music fadeout 5.0
    play music end1
    scene home
    gg "Только бы Каури не отправился в резиденцию лично..."
    gg "Арабелла, вы дома? Госпожа Арабелла!"
    show armedit at left
    ar "Кадер?.. Какой прискоробный поворот судьбы..."
    gg "Что? Почему?"
    ar "Каури поднял восстание."
    gg "Что!?"
    gg "Я еще могу успеть его остановить!"
    ar "Кадер, стой..."
    
    scene mansionblodlight
    
    gg "Каури! Каури!"
    show kidle at center
    k "Ты пришла..."
    gg "Что ты сделал? Зачем!? Почему ты не послушал меня?"
    k "Так же как и ты не послушала меня. Я поднял восстание, я же и поплачусь за это."
    gg "Нет, ты не должен!"
    hide kidle
    show kevil at center
    k "Да что ты вообще знаешь о моем долге!? Я не спас сестру, я не спас никого! Они убили каждого с началом нападения!"
    k "Что я должен? Единтсвенное что я должен, так это поплатиться за свои решения!"
    k "В том числе за то, что ты вообще появилась в нашей жизни! Убирайся, лучше бы мы бросили тебя в тот день!"
    gg "Каури, не говори так. Расскажи, что случилось, я могу помочь, я могу сделать хоть что-то!"
    hide kevil
    show kconf at center
    k "Что ты можешь сделать? Вернешь время назад?"
    gg "Нет, но..."
    k "Вот именно."
    k "Убирайся."
    hide kconf
    show kevil at center
    k "Убирайся вон, или я убью тебя!"
    gg "Нет, не убьешь. Я знаю тебя, ты не такой, ты не убийца..."
    scene mansionbloddark
    k "Ха-ха. Не убийца... Я не убийца... Верно. Однако я умру с кровью сестры на руках. Прощай."
    gg "Нет!"
    
    scene home with blod
    pause 2.0
    show arsmile at left
    ar "Ты уверена в своем решении?"
    gg "Да. Я все эти три года грезила о том, как вернусь в родной дом..."
    gg "Да и последнее, что я запомню об этом городе... как мой друг вонзил себе в сердце подаренный мной кинжал."
    ar "Я не об этом. Стоит ли сохранить здесь все как есть? Не терзай себя и не мучай."
    gg "Нет. Раньше меня мучали кошмары о прошлом. Будут мучать и впредь. Однажды кто-то вернется в этот дом и будет видеть сладкие сны."
    gg "Я еще навещу вас. Наверное, где-то через месяц."
    hide arsmile
    show aridle at left
    gg "Не могу смотреть на улицы, пестрящие заголовками о смерти моих друзей. О его смерти..."
    gg "До свидания."
    
    return
    
label end2:

    hide screen deck
    hide screen cards_table
    hide screen points
    hide screen arena
    hide arena

    stop music fadeout 5.0
    
    play music end2
    if amm:
        scene mansionsum
        "Запах аммиака уже начал чувствоваться, да и гостей поубавилось. Значит, все идет по плану."
        "Кашель Юстаса становится чаще."
        show yuidle at center
        yu "Что за улыбка, кх-кх, на твоем лице, дряная девченка?"
        gg "Да так."
        hide yuidle
        show yuevil at center
        yu "Что ты сделала, кх-кх, дрянь!?"
        gg "Совершенно ничего, что сравнилось бы с твоим преступлением."
        yu "Убить эту дрянь!"
        
        jump deadend2
        
    else:
        scene mansionsum
        "В воздухе витает легкий запах трав. Некоторые гости уже вышли на улицу. Юстас тяжело дышит, это хорошо."
        "Все равно глаз с меня он не спустит. Идти некуда. Шах и мат."
        show yuidle at center
        yu "Что ж, сейчас же начнем процедуру передачи наследства. Ты же не против? Хотя кого это волнует!"
        kr "Дамы и господа. Мы начинаем основную часть сегодняшнего мероприятия."
        kr "Сейчас вы увидите лучший товар, что мы отобрали специально для вас!"
        "Нужно срочно их остановить. Детям может сразу же стать плохо..."
        kr "Встречайте, лот номер один: юная красивая девушка, новоиспеченный ученик фармацевта, обладатель целебной магии!"
        "Это же Альмина!.. Нужно срочно что-то придумать."
        menu:
            "Обвинить в домогательствах":
                hide yuidle
                show yuevil at center
                gg "Руки прочь от меня! Кто вам позволил так вести себя в отношении незамужней дамы!?"
                gg "Если вы позволяете себе такое поведение с гостями, что же вы делаете с девушками до выкупа!?"
            "Пригрозить судом":
                hide yuidle
                show yuevil at center
                gg "Что значит не можете сейчас заплатить. Мне ждать конца аукциона!?"
                gg "Я такого отношения не стерплю! Неужто хочешь судиться!?"
        "Все смотрят. Отлично."
        "Давай, Альмина, беги!"
        "Умница."
        transform alpha_dissolve:
            alpha 0.0
            linear 0.5 alpha 1.0
            on hide:
                linear 0.5 alpha 0
        screen countdown:
            timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
            bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve
        $ time = 2
        $ timer_range = 1
        $ timer_jump = 'deadend2'
        show screen countdown
        menu:
            "Бежать":
                hide screen countdown
                "Это мой шанс."
                yu "Схватить ее!"
                gg "Ну и что прикажешь делать с новой пленницей?"
                yu "Убить."
                jump deadend2
            "Прочесть заклинание":
                hide screen countdown
                yu "Что ты творишь, дрянь!?"
                gg "crepitus!"
                scene mansionfire with flash
                gg "Сгорю вместе с тобой!"
                scene home
                pause 2.0
                show kidle at center
                show alidle at right
                k "Доброе утро. Как она?"
                al "Жить будет. Скоро прибудет лекарь из столицы. С его помощью она точно поправится."
                k "Скоро переедешь к наставнице?"
                al "Смотря как сложится ситуация с Кадер. Пока что она не приходит в себя. Думаю, перееду когда она очнется."
                al "Как твои успехи с тренировками?"
                k "Завтра идем на первую охоту. Я не искал никого в отряд на замену Кадер."
                k "Найти кого-то сложно, а она в любой момент может поправиться."
                al "Понимаю. Мне пора идти, справишься с детьми?"
                k "Да. Тебя они слушаются как ручные."
                al "Конечно, я же лучшая!"
                k "Да, лучшая. Удачи на занятиях."
                al "До вечера!"
        
    return
    
label deadend2:

    scene home
    pause 2.0
    show kidle at center
    show alidle at right
    k "Поверить не могу... Кадер так ждала наказания Юстаса и вот... Он идет на плаху, а она мертва..."
    al "Думаю, она хотела бы, чтобы мы жили дальше и без нее."
    k "Знаю, знаю. По сути мы займем ее место в мире, а она ради нас жизнь отдала."
    al "Согласна, это странно. Но мы ничего не можем сделать."
    show arsmile at left
    hide kidle
    show kconf at center
    ar "Альмина, за вами приехали рыцари. Они сопроводят вас во дворец."
    al "Спасибо. Дайте нам еще минуту."
    k "Нет, не нужно."
    ar "Вы еще можете отказаться. Дело Хишуо передадут кому-то другому."
    al "Нет. Если кто-то и должен занять ее место, то это я."
    ar "Хорошо. Удачи."
    
    return
    
label end3:
    hide screen deck
    hide screen cards_table
    hide screen points
    hide screen arena
    hide arena

    stop music fadeout 5.0
    
    play music end3
    
    if amm:
        scene mansionsum
        "Уже отчетливо чувствуется запах аммиака. Дрянь та еще."
        "Держу пари, Юстас, как и я, еле сдерживает слезы."
        show yuevil at center
        yu "Думаешь, кх-кх, я просто так отдам тебе, кх-кх, бизнес?"
        yu "Размечталась, наивная, кх-кх, девченка."
        gg "Поверь, жду я не этого."
        kr "Дамы и господа. Мы начинаем основную часть сегодняшнего мероприятия."
        kr "Сейчас вы увидите лучший товар, что мы отобрали специально для вас!"
        "Черт, нельзя чтобы пленники вышли сейчас."
        show msad at left
        m "Кадер!"
        gg "Мику!? Что ты здесь делаешь!"
        "Нужно срочно вывести его отсюда. Как он вышел из подвала для пленников?..."
        yu "Схватить ее!"
        menu:
            "Бежать":
                
                "Плевать, я успею сбежать."
                yu "Схватить ее немедленно!"
                scene black with blod
                "Черт, как плохо, я уже почти не вижу."
                "Дыши. Только дыши."
            "Прочесть заклинание":
                hide msad
                show mlyub at left
                gg "Мику, спрячься!"
                yu "Что ты творишь, дрянь!?"
                gg "crepitus!"
                scene mansionfire with flash
                gg "Сгори, тварь!"
        scene home
        pause 2.0
        show arsmile at left
        show alidle at right
        ar "Доброе утро, дорогая. Давай помогу."
        al "Нет, не стоит. Я справляюсь."
        ar "Не изводи себя. Ты уже несколько дней постоянно возле кровати детей."
        ar "Какие прогнозы?"
        al "Думаю, Мику уже не спасти. Дома еле хватало лекарств для одного человека..."
        al "Если бы не наставница, у него даже не было бы шанса выжить."
        ar "Ты сделала правильный выбор. Дети - наше будущее, но Кадер твоя подруга и заслужила шанс на жизнь в своей мечте."
        al "Я понимаю, но..."
        ar "Всех не спасти. Пожалуй, тебе, как будущему лекарю, нужно привыкнуть к этой мысли."
        ar "И привыкать делать выбор. Сложный выбор."
        ar "Тем более скоро прибудет лекарь из столицы. Если он не сможет спасти Мику, то ты ничего не могла сделать."
        ar "Отдохни. Я смогу сама дать лекарство и сменить повязки."
        hide alidle
        show alsmile at right
        al "Хорошо. Спасибо."
    else:
        scene mansionsum
        "Знать бы куда Каури подсыпал яд... Со вчера я стала ненавидеть ожидание."
        show yuevil at center
        gg "Ну что, готов расстаться со всем имуществом?"
        yu "Иди к черту! Вина! Принесите мне вина!"
        yu "Сыграем еще раз."
        gg "Хорошо."
        k "Позвольте мне поменять карты господина."
        gg "Да, конечно."
        yu "Не желаешь отведать вина?"
        gg "Предпочитаю не пить. Алкоголь затуманивает разум."
        yu "Кх-кх-кх-кх."
        k "Господин, вы горите!"
        gg "Ну так отведите вашего господина в покои и окажите помощь."
        hide yuevil
        pause 2.0
        k "Уважаемые гости, к сожалению, мы вынуждены перенести аукцион в связи с самочувствием господина Хишуо."
        k "Благодарим за понимание."
        scene home
        pause 2.0
        show kidle at center
        k "Альмина сегодня возвращается?"
        gg "Да. Надеюсь, я успею встретиться с ней до отъезда."
        k "Уверена, что так скоро отправишься в столицу?"
        gg "Да. Узнав, что я жива, королевская семья хочет убедиться что... я это я?"
        k "Ну, ты очень похожа на себя."
        gg "Спасибо!"
        gg "Пойду собирать вещи. Не знаю когда прибудет стража для сопровождения."
        k "Конечно. Думаю, если не пересечетесь с Альминой, встретимся все уже в столице."
        gg "Ты сам пообещал эту встречу. Не забудь!"
        
    return