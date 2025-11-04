
class App:

    instance = None

    def __init__(self,API_KEY,kafka_bootstrap_servers,serializer):
        self.api_key = API_KEY
        self.kafka_bootstrap_servers=kafka_bootstrap_servers
        self.serializer=serializer
        self.instance = self
    def app_instance(self,API_KEY,kafka_bootstrap_servers,serializer=None):
        if self.instance :
            return self

        app = App(API_KEY,kafka_bootstrap_servers,serializer)
        return app