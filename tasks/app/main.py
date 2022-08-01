import pkgutil

from utils.greetings import say_hello

if __name__ == "__main__":
    config = pkgutil.get_data("app", "config.json").decode("utf-8")
    print(config)
    say_hello()
