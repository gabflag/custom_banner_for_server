import pyfiglet


def display_banner(message):
    custom_fig = pyfiglet.Figlet(font='big')
    banner = custom_fig.renderText(message)
    banner_without_quotes = banner.replace("'", ' ')
    print(banner_without_quotes)


server_name = "Your Server"
print("echo '")
display_banner(f"{server_name}")
print("'")
