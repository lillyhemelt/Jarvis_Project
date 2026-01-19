import torch
import torch.nn as nn
import torch.nn.functional as F

class JarvisModel(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.token_embedding = nn.Embedding(vocab_size, 384)
        self.position_embedding = nn.Embedding(256, 384)
        self.layers = nn.Sequential(*[nn.TransformerEncoderLayer(d_model=384, nhead=6) for _ in range(6)])
        self.ln_f = nn.LayerNorm(384)
        self.head = nn.Linear(384, vocab_size)

    def forward(self, idx, targets=None):
        B,T = idx.shape
        tok_emb = self.token_embedding(idx)
        pos_emb = self.position_embedding(torch.arange(T, device=idx.device))
        x = tok_emb + pos_emb
        x = self.layers(x)
        logits = self.head(self.ln_f(x))
        return logits
    