def convertEmoji(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😒"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(convertEmoji("Hi Hari :) , I'm sad :("))
