import torch
from model import JarvisModel
from tokenizer import SimpleTokenizer

with open('training_data.txt', 'r', encoding='utf-8') as f:
    text = f.read()

tokenizer = SimpleTokenizer(text)
data = torch.tensor(tokenizer.encode(text), dtype=torch.long)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = JarvisModel(vocab_size=tokenizer.vocab_size).to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)

def train():
    model.train()
    for inter in range(5000):
        ix = torch.randint(high=len(data)-257, size=(32,))
        x = torch.stack([data[i:i+256] for i in ix]).to(device)
        y = torch.stack([data[i+1:i+256+1] for i in ix]).to(device)

        logits = model(x)
        loss = torch.nn.functional.cross_entropy(logits.view(-1, logits.size(-1)), y.view(-1))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if inter % 500 == 0:
            print(f"Step {iter}: Loss {loss.item()}")

        torch.save(model.state_dict(), 'jarvis_model.pth')

if __name__ == "__main__":
    train()