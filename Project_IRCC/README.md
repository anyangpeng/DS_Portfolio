# Project_IRCC

## Abstract

Over the past few years, Immigration, Refugees and Citizenship Canada (IRCC) has repeatedly announced its ambitious immigration plans, which has attracted great attention from public media and prospective candidates By analyzing the admission data, we try to answer the following questions:

- Question 1: What are the five largest origins of new Canada immigrants?
- Question 2: For the five largest origins of new Canada immigrants, how does the annual total change over time?
- Question 3: What are the most popupar immigration category for people with citizenship of China?
- Question 4: What are the trend for these categories over time?

## Getting and cleaning data

Statistics provided by IRCC are used in this analysis. The raw data is provided in two separate Excel files, and several customized functions are defined to clean up the data. A comparison of the pre- and post-cleaning data is shown below. [Click for details!](https://github.com/anyangpeng/DS_Portfolio/blob/main/Project_IRCC/By_category.ipynb)<br><br>

Pre-cleaning: the multi-level indexing creats many NaN values because of the merged cell.<br>

<p align="center">
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/66216181/109736890-bc501400-7b8a-11eb-9eb9-f9d5ac8f8b2a.png">
</p><br>

Post-cleaning: both index and column names are corrected.<br>

<p align="center">
  <img width="960" alt="image" src="https://user-images.githubusercontent.com/66216181/109737554-ddfdcb00-7b8b-11eb-9892-34fda80039d2.png">
</p><br>

## Analyzing data

Question 1: What are the five largest origins of new Canada immigrants?
To answer this question, the immigration statistics are grouped by the country of citizenship.

<p align="center">
<img width="480" alt="image" src="https://user-images.githubusercontent.com/66216181/109737694-17363b00-7b8c-11eb-8d54-210f2bfda25f.png">
</p><br>
Question 2: For the five largest origins of new Canada immigrants, how does the annual total change over time?<br>
<p align="center">
<img width="960" alt="image" src="https://user-images.githubusercontent.com/66216181/109738446-6d57ae00-7b8d-11eb-8f4a-66351907ff90.png">
</p><br>

From the plot above, a few insights can be drawn:

- Number of new immigrants from Philippines delines overtime.
- A huge influx of immigrants from Syria around the end of 2015, which is due to the refugee resettelment.
- A siginificant drop across all countries in April 2020, which is due to the Covid Lockdown.
- The number of cases bounce back in June 2020 for a short period of time, this may be associated with the reopening of FSW draws.
  <br><br>

Question 3: What are the most popupar immigration category for people with citizenship of China?<br>
<br>

<p align="center">
<img width="360" alt="image" src="https://user-images.githubusercontent.com/66216181/109738700-e5be6f00-7b8d-11eb-9c1d-93d919f2257e.png">
</p><br>

Question 4: What are the trend for these categories over time?<br>

<p align="center">
<img width="400" alt="image" src="https://user-images.githubusercontent.com/66216181/109738819-2ae2a100-7b8e-11eb-8ab3-27387db18784.png">
</p><br>

## Conclusion

From 2015 to 2020, India, Philippines, China, Syria, and Pakistan are the five large origins of new Canada immigrants. Refugee resettelment program significantly facilitates immigration from Syria to Canada at the end of 2015. Most immigrants from China belong to Economic Program and Sponsored Family Program. Covid imposes a huge challenge on all candidates.
