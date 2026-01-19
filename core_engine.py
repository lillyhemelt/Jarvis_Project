import torch
from . import perception, expression, actions, cognition
from model import JarvisModel
from tokenizer import SimpleTokenizer

class JarvisEngine:
    def __init__(self):
        with open('training_data.txt', 'r', encoding='utf-8') as f:
            self.tokenizer = SimpleTokenizer(f.read())
            self.model = JarvisModel(self.tokenizer.vocab_size)
            self.model.load_state_dict(torch.load('jarvis_brain.pth'))
        self.model.eval()

    def run(self):
        expression.speak("Hello, I am Jarvis. How can I assist you today?")
        while True:
            user_text = perception.listen()
            if user_text:
                response = cognition.process(user_text, self.model, self.tokenizer)
                expression.speak(response)