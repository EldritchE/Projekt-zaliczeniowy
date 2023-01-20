def color_text(color, text):
    colors = {'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m', 'magenta': '\033[35m',
              'cyan': '\033[36m', 'white': '\033[37m', 'black': '\033[30m'}

    if color not in colors:
        return text
    else:
        return colors[color] + text + '\033[0m'
