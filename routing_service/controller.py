# controller.py
class Controller:
    def __init__(self, strong_model: str, weak_model: str):
        self.strong_model = strong_model
        self.weak_model = weak_model

    def get_model(self, query: str) -> str:
        if len(query) < 10:
            return self.weak_model
        else:
            return self.strong_model
