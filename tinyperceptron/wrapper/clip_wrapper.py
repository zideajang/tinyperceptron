from typing import List

import torch
import clip
from PIL import Image


# "ViT-B/32"

class CLIPModelWrapper:
    def __init__(self,config) -> None:
        self.config =  config
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load(config['name'], device=self.device)

    def encode_image(self,image_path:str):
        image = self.preprocess(Image.open(image_path)).unsqueeze(0).to(self.device)
        image_features = self.model.encode_image(image)
        return image_features
    def encode_text(self,text_list:List[str]):
        text = clip.tokenize(text_list).to(self.device)
        text_features = self.model.encode_text(text)

    def pred(self,image_path,text):
        with torch.no_grad():
            image = self.preprocess(Image.open(image_path)).unsqueeze(0).to(self.device)
            text = clip.tokenize(text).to(self.device)

            logits_per_image, logits_per_text = self.model(image, text)
            probs = logits_per_image.softmax(dim=-1).cpu().numpy()

        print("Label probs:", probs)  # prints: [[0.9927937  0.00421068 0.00299572]]
        print(probs[0][0] > probs[0][1])

if __name__ == "__main__":
    clip_model_wrapper = CLIPModelWrapper(config={"name":"ViT-B/32"})
    clip_model_wrapper.pred("../../data/cat.png",["cat","dog","tiger"])