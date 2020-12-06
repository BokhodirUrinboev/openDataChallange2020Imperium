from django.apps import AppConfig


class ViewerConfig(AppConfig):
    name = 'viewer'

    def ready(self):
        import openDataChallange2020Imperium.viewer.signals

