from transformers import pipeline
import json


class TopicModel:
    def __init__(
        self,
        path_label_json="final_topic_labels",
        confidence_threshold=0.1,
    ) -> list:
        self.model_name = "cross-encoder/nli-deberta-v3-small"  # "Recognai/zeroshot_selectra_medium"
        self.model = pipeline(
            "zero-shot-classification", model=self.model_name
        )  # 22.5 M params
        with open(path_label_json, "r") as file:
            self.labels = json.load(file)
        self.confidence_threshold = confidence_threshold

    def predict(self, dialogue) -> list:
        out = []
        try:
            dialogue = ", ".join(dialogue)
            pred = self.model(dialogue, self.labels)
            labels = pred["labels"]
            scores = pred["scores"]
            for label, score in zip(labels, scores):
                if score > self.confidence_threshold:
                    out.append(label)
        except:
            pass
        return out
