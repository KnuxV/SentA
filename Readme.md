# Sentiment Analysis on the Intersection database (publications dealing with both digital and sustainable development)

## Main tool used 
We used this model [Deberta-v3-base-absa-v1.1](https://huggingface.co/yangheng/deberta-v3-base-absa-v1.1?text=%5BCLS%5D+when+tables+opened+up%2C+the+manager+sat+another+party+before+us.+%5BSEP%5D+manager+%5BSEP%5D)

## Sample

- ```sample_fully_annotated.xlsx``` contains the final result with annotations from all sentiment models

## Results
- Box plots for each digital category and one that combines everything
![box_all.jpg](img%2Fbox_all.jpg)
- Two heatmaps: the second one plots sentiment for intersection with more than 100 keywords
![sent_heatmap_gr100_pubs.jpeg](img%2Fsent_heatmap_gr100_pubs.jpeg)
- 

## Notebooks
- [check_dt_keywords](/home/kevin-desktop/PycharmProjects/SentA/notebook/check_dt_keywords.ipynb)  
  (Optional) Used for checking why the annotation of digital keywords differed from WOS annotation. A fix is offered
- [dt_keywords](/home/kevin-desktop/PycharmProjects/SentA/notebook/dt_keywords.ipynb)  
Compute mean and standard deviation for each SDG ==> Results available for [keywords](/home/kevin-desktop/PycharmProjects/SentA/results/mean_std_for_keywords.xlsx)
and [categories](/home/kevin-desktop/PycharmProjects/SentA/results/mean_std_for_cat.xlsx)
- [Sample SA](/home/kevin-desktop/PycharmProjects/SentA/notebook/sentiment_analysis_sample.ipynb)  
 Compute F1-score, Accuracy on a sample
- [working_on_sample](/home/kevin-desktop/PycharmProjects/SentA/notebook/working_on_sample.ipynb)  
Useless, 


## Results
- [description.docx](/home/kevin-desktop/PycharmProjects/SentA/results/description.docx)  
contains a small description of the evaluation method
- [inter.pkl](/home/kevin-desktop/PycharmProjects/SentA/results/inter.pkl)  
Pickle file 53494*4 columns WOS-ID[AB, TXT, DE, TI] TXT = AB+DE+TI
- [inter_digi_keywords_exploded.pkl](/home/kevin-desktop/PycharmProjects/SentA/results/inter_digi_keywords_exploded.pkl)  
Pickle file 90705*4 columns WOS-ID[AB, TXT, DE, TI] // 1 line per keyword // same thing but the TXT column = 1 keyword 
- [res_sent_merged.pkl](results%2Fres_sent_merged.pkl)  
Same as the exploded but with 31 columns of added information
- [score.xlsx](results%2Fscore.xlsx)  F1score-Acc- Recall - Precision for each sentiment model
- [table_sentiments.csv](results%2Ftable_sentiments.csv) Base for heatmap of sentiment for each intersection SDG-DT
- 