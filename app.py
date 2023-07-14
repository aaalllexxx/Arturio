from aengine_flask.app import App
import os

base_dir = os.path.dirname(os.path.realpath(__file__))


class MyApp(App):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(MyApp, cls).__new__(cls)
        return cls.__instance


app = MyApp()
app.load_config(base_dir + "/config.json")
flask_app = app.app
