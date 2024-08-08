﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define gg = Character('Кадер', color="#c8ffc8")
define al = Character('Альмина', color="#c8ffc8")
define k = Character('Каури', color="#c8ffc8")
define ar = Character('Арабелла', color="#c8ffc8")
define yu = Character('Юстас', color="#c8ffc8")

define kid = False
define self = False
define game2 = False

define gui.text_outlines = [(4, "0124", 0, 0), (3, "0124", 0, 0), (1, "0124", 0, 0), (1, "0124", 0, 0)]

label splashscreen:
    # громкость по умолчанию
    python:
        # при первом запуске
        if not persistent.set_volumes:
            persistent.set_volumes = True
            # музыку потише
            _preferences.volumes['music'] = .5
            _preferences.volumes['sfx'] = .5
            # игра на весь экран
            _preferences.fullscreen = True
    return
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene home

    # show almina at right
    # сон 1
    al "Просыпайся. Эй, соня, просыпайся!"
    al "Проснись и пой!"
    "Я почувствовала как меня ущипнули в плечо."
    # show gg at left
    gg "Ай…"
    al "Что за сонное «ай»? Ты не забыла?"
    gg "Что забыла?"
    al "Просыпайся! Тебе так-то нужно собрать ингредиенты для лавки и для себя."
    al "Думаешь с белоснежными волосами ты долго скроешься?"
    "Сквозь сон приходит осознание сегодняшнего дня."
    "Каждый раз, когда приходит день обновления маскировки я вспоминаю о своей прошлой жизни."
    "Кадер Хишуа, наследница одного из богатейших родов Вэйо. Любящая семья, теплый дом, вкусная еда… Как все это далеко."
    "После того, как родителей убили, я смогла сбежать. Но с моей внешностью долго не скроешься."
    ar "Доброго утра, девочки! Как ваши дела идут?"
    al "Доброго утра! Кадер никак не проснется. Как никак весь учет ведет она, поэтому чего нам не хватает знает только один человек в этой комнате."
    gg "Да, да… сейчас. Доброго утра. С лавкой все хорошо, людям всегда нужны лекарства и косметика."
    ar "Я не всегда интересуюсь исключительно заработком. Тем более принимать других детей, помимо вас троих, было рисковано."
    gg "Но ведь, когда вы пустили нас в дом, были поставлены четкие условия по окупаемости нашего нахождения."
    ar "Да, я не помогаю в ущерб себе, но это не значит, что мне наплевать на птенцов под моим крылом. Так как ты? Скоро твой день рождения, отправитесь в столицу?"
    gg "Думаю чуть позже. Другие дети еще не готовы самостоятельно заниматься лавкой без нас. А день рождения…"
    gg "Думаю, лучший подарок ингредиенты для краски или литий и аммиак."
    ar "Это для твоего нового зелья?"
    gg "Да. Оно должно изменить цвет глаз. Пригодится в столице."
    ar "Поражаюсь твоему таланту. Что ж, мне пора. Хорошего дня."
    gg "До свидания!"
    al "Удачи!"
    al "Но за ингредиентами в любом случае нужно сходить."
    gg "Да-да, знаю. Не нужно напоминать мне лишний раз."
    # show kauri at center
    k "А как по мне не мешало бы, а то забудешь, как саму себя зовут, пока разрабатываешь новые зелья."
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
            


label minigame1:

    $ enemy_deck = [hog_rider2, archers2, princess2, mosquetear2, barbarians2]

    call cardgame1 from _call_cardgame1
    
    jump mini1
    
    return

label mini1:

    scene home
    
    menu:
        "Сыграть еще раз":
            menu:
                "Напомнить правила":
                    gg "Что ж, напомни правила."
                    k "Хорошо. У тебя на руке будет пять карт. На игровом поле 9 ячек."
                    k "Тебе нужно захватить карты противника."
                    k "У каждой карты есть характеристики в месте, где она может соприкасаться с другой картой."
                    k "Чтобы захватить карту, тебе нужно, чтобы твоя карта была по характеристике выше, чем карта противника, там, где они соприкоснутся."
                "Не напоминать правила":
                    gg "Не против еще одной игры?"
                    k "Я только рад!"
            jump minigame1
        "Закончить игру":
            jump scene3_1
            
    return
    
label scene3_1:

    if self:
        # scene3_1
        scene lug
        
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

    scene home
    
    k "Уже стемнело, а их все еще нет."
    gg "Нужно пойти искать их."
    k "Хорошо, я поспрашиваю знакомых."
    gg "Я с тобой."
    k "Лучше останься здесь."
    gg "Вдвоем мы быстрее узнаем где они!"
    k "У нас из знакомых лишь Арабелла и авантюристы. Арабелла скоро вернется, а к авантюристам я могу пойти один."
    k "Дождись Арабеллу. Узнаешь у нее знает ли она что-то."
    "Ожидание тянулось крайне долго."
    # сон 2
    ar "Кадер, почему ты здесь одна?"
    # “Сон мгновенно покинул меня"
    gg "Арабелла, Альмина и дети пропали, вы не слышали что-то о них!?"
    ar "Я слышала от девушек, что они видели, как кто-то продавал девушку, похожую на Альмину, в другие дома."
    gg "Когда!? Кто это был?"
    ar "Я не придала значения этим разговорам. Даже и подумать не могла что кого-то из вас похитят и решат продать!"
    gg "Как теперь найти того человека?..."
    ar "Ты осталась одна?"
    gg "Нет, Каури пошел в тренировочный лагерь, узнать видел ли кто-то ребят."
    ar "Тогда дождемся вестей от него"
    "Снова ожидание?"
    "Что если он ничего не узнает…"
    k "Арабелла, вы здесь! Вы знаете что-то?..."
    ar "Я не придала значение слухам, так что ничего конкретного рассказать не могу. Альмину пытались продать, но кто - я не знаю."
    k "Я знаю…"
    gg "Что?"
    k "Твой горячо любимый родственник, Кадер… Он похищал детей на продажу, теперь и до нас добрался."
    k "Завтра пройдет аукцион. Он собирает у себя в поместье богачей со всей страны. Толстосумы будут играть друг с другом и…"
    k "Покупать людей, предоставленных Юстасом…"
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
    k "Да. Только убедись, что это безопасно для тебя и других невиновных."
    gg "Хорошо. Когда пройдет прием у Юстаса?"
    k "После захода солнца."
    gg "Отлично, утром будет время подготовиться."

# сон 3?

    menu:
        "Использовать аммиак":
            "Пары аммиака достаточно токсичны. Для меня имеющегося лекарства хватит."
            "Ставка более чем оправданная."
            k "Как ты планируешь избавиться от запаха?"
            gg "Ты сейчас чувствуешь запах, поскольку в спирте сильно сконцентрирован аммиак."
            gg "Когда он окажется в воздухе, его запах почувствуется позже, чем газ отравит людей."
            k "А как же «товар»?"
            gg "Они будут находиться в подвале, так что для них газ безопасен."
            k "Хорошо. Это все приготовления?"
            jump scene5_1_0
            
        "Использовать яд":
            $ game2 = True
            gg "Завтра отправлюсь в лес."
            jump scene5_1_2
    
    return
    
label scene5_1_0:
    
    scene home
    
    menu:
        "Да":
            $ game2 = True
            gg "Это все приготовления. Мне осталось дождаться вечера."
            gg "Тебе нужно устроиться в особняк и облить дрова этой жидкостью."
            k "При горении выделится яд?"
            gg "Верно. Как только начнется прием, ты должен будешь уйти."
            jump scene6_1
        "Собрать ядовитые растения":
            $ game2 = True
            gg "Думаю, стоит посмотреть что есть из растений. Может, есть более безопасный вариант."
            jump scene5_1_2

    return

label scene5_1_2:
    
    scene lug
    
    gg "Думаю, я смогу найти достаточно токсичные травы. Их всегда было достаточно."
    
    # определим фон игры, время игры в секундах
    # и зададим параметры игры - спрайты и положение для собираемых предметов
    $ hf_init("lug", 180,
        ("beer", 1013, 705, _("Ландыш. Если употребить в пищу, при должном невезении, может остановиться сердце.")),
        ("elf", 111, 560, _("Лютик. Ядовит как при употреблении в пищу, так и при вдыхании. Может даже вызвать галлюцинации.")),
        ("flowers", 700, 615, _("Шафран. Мало токсичен, нужна слишком большая концетрация. Вкус блюда будет испорчен.")),
        ("skull", 1813, 161, _("Аквилегия. Достаточно ядовитое растение, однако сложно понять токсичность этого сорта.")),
        # НЕОБЯЗАТЕЛЬНЫЕ ПАРАМЕТРЫ:
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
        centered "{size=+24}Ура! Все предметы собраны!"
    else:
        centered "{size=+24}GAME OVER\nНе собрано предметов: [hf_return]."
        
    $ hf_hide()
    with dissolve
    
    jump scene6_1
    
    return
    
label scene6_1:

    scene home
    
    gg "Старая одежда Арабеллы на удивление неплохо на мне сидит. Я и впрямь как дворянка. Хотя, я она и есть…"
    gg "Ну что, пришло время встретиться лицом к лицу со своим злейшим врагом."
    
    scene mansion
    
    gg "Эх, Юстас, не растрачивай ты деньги на особняки и развлечения, может и был бы наследником…"
    gg "Каури уже должен был уйти. Теперь моя очередь вступить в игру."
    yu "Здравствуйте, юная леди. Я раньше вас здесь не видел? Давно вы в прибыли в Еиннс? С какой целью прибыли?"
    yu "Впрочем, не важно, я рад, что сие мероприятие посетила столь прекрасная дама."
    gg "Не думаю, что разделяю вашу радость. В Еиннсе я достаточно давно. Явно дольше, чем следовало бы."
    yu "Почему же? Вас ждут какие-то дела?"
    gg "Дела? Можно и так сказать. Приятно вновь встретиться, я - Кадер Хишуо."
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
    
    $ enemy_deck2 = [lava_hound2, archers2, princess2, mosquetear2, baby_dragon2]

    call cardgame1 from _call_cardgame2
    
    jump mini1
    
    return