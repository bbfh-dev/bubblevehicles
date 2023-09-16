from colorama import Fore


class Log:
    def __init__(self, plugin_name: str):
        self.plugin_name = plugin_name

    def info(self, action: str, subject: str):
        print(
            f"{Fore.LIGHTBLACK_EX}PLUGIN/{Fore.RESET}{self.plugin_name} "
            f"{Fore.LIGHTBLACK_EX}:: "
            f"{action} {Fore.LIGHTYELLOW_EX}{subject}{Fore.RESET}"
        )
