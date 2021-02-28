# Project_Color
## Abstract
For scientific publishing, color has become increasingly important. A good color scheme will often make a publication appear more professional. *Project_color* contains several subprojects intended to facilitate the selection of color schemes.


A list of sub-projects

- [Color Identification](#Color-Identification)
- [Color Recommendation](#Color-Recommendation)
- [Traditional Chinese Colors](#Traditional-Chinese-Colors)


## Color Identification
### Objectives
As the first step of Project_color, a database of popular palette is needed. One trivial way would be scraping this data from online sources. Alternatively, palette can be extracted from paintings by prestigeous artists. Data is obtained from Kaggle.
### Method
877 paintings by Van Gogh were used as the training data to creat a popular color shceme database based on the palette extracted from eaching painting. Many people have done similar things or other datasets using KMeans algorithm. In this demo, 10 clusters were allowed for each painting, and only the 5 most common clusters were used to get the palette. [Click for details!](https://github.com/anyangpeng/DS_Portfolio/blob/main/Project_color/Color_Identification/Get_color_code.ipynb)
### Results
An example of the original input image and the palette extracted from it is shown blow. The script works properly, however, the results is far from perfect. A more accurate method will be discussed in the future.
<p align="center">
  <img width="360" alt="image" src="https://user-images.githubusercontent.com/66216181/109397948-35d3d200-78ff-11eb-91f9-7bf159efd266.png">
  <img width="771" alt="image" src="https://user-images.githubusercontent.com/66216181/109398264-77fe1300-7901-11eb-826e-31bd0cdce33c.png">

</p>
After testing the performance of the script, all 877 paintings were fed into the script to generate a dataset which stores the palette for each painting.

## Color Recommendation
### Objectives
After constructing the database of polular palette, the next step is to generate a recommended color scheme for a given color. 
### Method
The most intivie approach is to find the given color in the database and return the matching colors from the same palette. Alternatively, an embedding modle can be trained to predict co-occurence. The first approach is used to demonstrate user cases  with single input color. The Similarity between colors is quantified by the Euclidean distance in LAB color space. [Click for details!](https://github.com/anyangpeng/DS_Portfolio/blob/main/Project_color/Color_Recommendation/Color_recommendation.ipynb)
### Results
<p align="center">
  <img width="180" alt="image" src="https://user-images.githubusercontent.com/66216181/109398944-69b1f600-7905-11eb-85f6-4ece54d08f2e.png">
  
  <img width="120" alt="image" src="https://user-images.githubusercontent.com/66216181/109399005-bdbcda80-7905-11eb-8323-5010604a4f6c.png">

</p>

Given a color *(the key)* similar to the second color in the palette from the aforementioned example, the script successfully locate the most similar color in the entire VanGogh dataset *(the value)*. The recommended colors are the remaining colors in the same palette.


## Traditional Chinese Colors
Unfinished projects.
