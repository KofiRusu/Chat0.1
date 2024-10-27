from transformers_config import AutoTokenizer, AutoModelForCausalLM
from pytorch import torch

class LlamaModel:
    def __init__(self, model_name: str):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map='gpu' if self.device.type == 'cuda' else 'cpu'
        ).to(self.device)
        
        if self.device.type == 'cuda':
            print(f"Model loaded on GPU: {torch.cuda.get_device_name(0)}")
        else:
            print("GPU not available. Model loaded on CPU.")

    def generate_response(self, input_text: str, max_new_tokens: int = 150) -> str:
        try:
            inputs = self.tokenizer(input_text, return_tensors='pt').to(self.device)
            outputs = self.model.generate(**inputs, max_new_tokens=max_new_tokens)
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return response
        except Exception as e:
            return f"Error generating response: {str(e)}"

# Initialize the model with the appropriate model name
llama_model = LlamaModel('path_to_llama3.2')
