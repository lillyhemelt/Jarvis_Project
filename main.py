import torch
from Jarvis_core import perception, expression, actions, cognition
from model import JarvisModel
from tokenizer import SimpleTokenizer

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def initialize_jarvis():
    with open('training_data.txt', 'r', encoding='utf-8') as f:
       text = f.read()
    tokenizer = SimpleTokenizer(text)
    model = JarvisModel(tokenizer.vocab_size).to(device)
    model.load_state_dict(torch.load('jarvis_model.pth'))
    model.eval()
    return model, tokenizer

def run_jarvis():
    print("---SYSTEM STARTUP---")
    model, tokenizer = initialize_jarvis()
    expression.speak("systems initialized. I am online ma'am")
    while True:
        command = perception.listen()
        if command:
            print(f"User command: {command}")
            response = cognition.process(command, model, tokenizer)
            expression.speak(response)
            if "go to sleep" in command or "shutdown" in command:
                expression.speak("shutting down. Goodbye ma'am.")
                break

if __name__ == "__main__":
    run_jarvis()