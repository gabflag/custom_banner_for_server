import pyfiglet


def display_banner(message):
    custom_fig = pyfiglet.Figlet(font='big')
    banner = custom_fig.renderText(message)
    print(banner)


server_name = "Your Banner"
display_banner(f"{server_name}")
