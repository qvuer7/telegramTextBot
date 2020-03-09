
def text1_rendering(text):

    style1_Text1 = "🏆"

    for i in text:
        style1_Text1 = style1_Text1 + i

    style1_Text1 = style1_Text1 + "🏆"
    return style1_Text1

def text2_rendering(text):
    style1_Text2 = ""

    for i in text:
        style1_Text2 = style1_Text2 + i
    return style1_Text2

def text3_rendering(text):
    style1_Text3 = ""

    for i in text:
        style1_Text3 = style1_Text3 + i
    return style1_Text3


style = f"🏆ТВОЙ ТЕКСТ 1🏆 \n\n🏒🎾🏀⚽️ \n\nТВОЙ ТЕКСТ 2 \n\n🔵ТВОЙ ТЕКСТ 4 \n\n🔵ТВОЙ ТЕКСТ5 \n\n🔵ТВОЙ ТЕКСТ6 \n\n🎩Match prediction:\nТВОЙ ТЕКСТ 7 \nPhoto"


def set_message(text1 = 'ТВОЙ ТЕКСТ 1',text2 = "ТВОЙ ТЕКСТ 2 ", text3 = "ТВОЙ ТЕКСТ 3", text4 = "ТВОЙ ТЕКСТ 4", text5 = "ТВОЙ ТЕКСТ 5",text6 = "ТЕКСТ6", text7 = 'ТЕКСТ7', emoji = 1 ):
    emojis = {1 : "🏒",
              2 : "🎾",
              3 : "🏀",
              4 : "⚽"}
    style1 = f"🏆{text1}🏆 \n\n{emojis[emoji]} {text2}️ \n\n🔵{text3} \n\n🔵{text4} \n\n🔵{text5} \n\n{text6} \n\n🎩Match prediction:\n{text7} \nPhoto"
    return style1




