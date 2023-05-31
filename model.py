import torch
from transformers import RobertaForSequenceClassification, AutoTokenizer
import asyncio

def analyze_sentiment(text):
    model = RobertaForSequenceClassification.from_pretrained("wonrax/phobert-base-vietnamese-sentiment")
    tokenizer = AutoTokenizer.from_pretrained("wonrax/phobert-base-vietnamese-sentiment", use_fast=False)
    input_ids = torch.tensor([tokenizer.encode(text)])
    with torch.no_grad():
        output = model(input_ids)
        return output.logits.softmax(dim=-1).tolist()[0]


title1 = "CEO Techcombank Jens Lottner: Năm 2022 thị trường có nhiều diễn biến bất ngờ, Techcombank đã có lối đi riêng để ứng phó tốt nhất"
title2 = "Lý giải động lực đưa thu nhập ngoài lãi tăng mạnh ở nhiều ngân hàng"

