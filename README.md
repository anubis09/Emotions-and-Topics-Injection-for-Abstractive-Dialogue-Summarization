# Emotions and Topics Injection for Abstractive Dialogue Summarization
## Abstract
In this study, we present novel extensions aimed at improving abstractive chat summarization, building upon the SICK framework, which highlighted the benefits of incorporating commonsense knowledge among dialogue participants. The first enhancement involves extracting _emotions_ from the dialogue and integrating them into the model, while the second extension focuses on injecting predicted custom _topics_ into the summarization process. Our framework demonstrates promising results, laying the groundwork for future investigations. The findings indicate that injecting commonsense knowledge enriched by extracted topics has a substantial impact compared to emotion injection. However, both extensions contribute to enhancing the model, resulting in more informative and consistent summaries.

**[Paper Link](https://drive.google.com/file/d/1uXpdkUM9fsKetN4qUub6lFwNeHDxzhth/view?usp=sharing)**

## Folder legend
- In the notebooks/ folder you can find the file used for fine-tuning bert into Emotion BERT, and the file used for choosing the topic labels.
- In the data/ folder you can find Dataset_json.ipynb. This file is used to inject the emotion or the topic knowledge into the samsum commonsense json.
The weights for running EmotionBERT can be downloaded at:
```
https://drive.google.com/drive/folders/1WQS1s_172jpHog5GeCc83PIwnsAZ-Qgp?usp=sharing
```

## Setting
To utilize our dialogue summarization framework follow these steps.

The following command will clone the project:
```
git clone https://github.com/SeungoneKim/SICK_Summarization.git
```


### Dataset Download
Our experiments were conducted on SAMSum dataset.

Also, you could download the preprocessed commonsense data from the url below:
```
https://drive.google.com/drive/folders/1z1MXBGJ3pt0lC5dneMfFrQgxXTD8Iqrr?usp=share_link
```

and put it under the directory of SICK_summarization/data/COMET_Data.
```
mkdir data/COMET_data
```

After downloading the commonsense data, please download the modified datasets json from the url below :
```
https://drive.google.com/drive/folders/1AvGSWYY0XOoKqahUnDsTW0bZl1ssduE5?usp=sharing
```
and put them under the directory "SICK_Summarization/src/data/COMET_Data/paracomet/dialogue/samsum/"

### Weights
After downloading the datasets information, please download the weights of the models.
Link for the weights of the model without extensions
```
https://drive.google.com/drive/folders/1KgNyBeJ8yCjyZZizWmHbewDXWDjIE8dU?usp=sharing
```
Link for the weights of the model with emotion injection
```
https://drive.google.com/drive/folders/1H_agjR6D1tpNa9mWf1aQGKrHaiuEuvAo?usp=sharing
```
Link for the weights of the model with topic injection
```
https://drive.google.com/drive/folders/1-lfkO6kxZv5IemyWKT_tmxf4REelsQXk?usp=sharing
```
### Training & Evaluation
In the main.ipynb you can train and inference the model on samsum dataset.
Please be aware to insert the path to the different weight and dataset path.

