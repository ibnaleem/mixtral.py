import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class Mixtral:
    def __init__(self, use_half_precision=False, load_in_4bit=False, use_flash_attention_2=False):
        self.model_id = "mistralai/Mixtral-8x7B-v0.1"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        if use_half_precision:
            self.model = AutoModelForCausalLM.from_pretrained(self.model_id, torch_dtype=torch.float16).to(self.device)
        elif load_in_4bit:
            self.model = AutoModelForCausalLM.from_pretrained(self.model_id, load_in_4bit=True).to(self.device)
        elif use_flash_attention_2:
            self.model = AutoModelForCausalLM.from_pretrained(self.model_id, use_flash_attention_2=True).to(self.device)
        else:
            self.model = AutoModelForCausalLM.from_pretrained(self.model_id).to(self.device)

    def generate_text(self, text, max_new_tokens=20):
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs, max_new_tokens=max_new_tokens)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
