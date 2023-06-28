import random

def handle_response(message) -> str:
    p_message = message.content

    if p_message == "my username":
        return str(message.author)
    
    if p_message.startswith("!add ") and p_message.endswith((".jpg", ".png", ".gif", ".jpeg")) and str(message.author) == "shiniowo":
        f = open("cats.txt", "a")
        f.write("\n" + p_message[5:])
        f.close()
        return "image added"

    elif p_message.startswith("!add ") and p_message.endswith(".jpg", ".png", ".gif", ".jpeg") and not str(message.author) == "shiniowo":
        return "you dont have permission to do that"
    
    if p_message == ":D":
        return "https://cdn.discordapp.com/attachments/404757168462495745/1123085772128526406/image.png"

    p_message = p_message.lower()

    if p_message == "hello":
        return "hey there"
    
    if p_message == "roll":
        return str(random.randint(1,6))
    
    if p_message == "!help":
        return "`this is a help message that you can modify.`"

    if p_message == "element of surprise":
        return "https://yt3.ggpht.com/GGKGmj9xVwNn5SIcuB9AOhgu8MaPI2HQQRBLXbrUHgj_0DN6n6MJj0sJpVP5gRFiVPPktWk3mb_1xw=s640-nd-v1"

    
    if p_message == "fuck you":
        return "stay mad"
    
    if p_message == "!cat":
        f = open("cats.txt", "r")
        data = f.read()
        images = data.split('\n')
        f.close()

        lines = len(images)
        return images[random.randint(0,random.randint(0,lines-1))]


