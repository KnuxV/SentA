### Small script to manually annotate a sample of publications

1. Manually
Open sample.xlsx with Excel and fill up the "Annotation" column for row where "Annotator" is equal to your first name.
Possible answer are Pos/Neu/Neg

2. Script
I've created a small script to make it easier to read the abstract, highlighting the digital and sustainable keywords in the text.
To use it, you need python installed, and two libraries: pandas and termcolor. 
You can use the following command in your python terminal to install them:
	```pip install -r requirements.txt```
or
```pip install pandas termcolor```

Once this is done, you use the script with:
```python manual_annotation_sentiment.py sample.xlsx your_first_name ```

The annotation is saved after each iteration.
