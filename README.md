# <span style ="color: indigo">The Metaverse: NLP Multi-Classification Modeling</span>

![virtual_reality](https://user-images.githubusercontent.com/105242871/188337225-67fd4808-4264-430c-9f1d-34f09df2a27b.jpg)


**Created By:**

<center>

| Meredith Wang</center> | Brad Gauvin</center> | Mijail Mariano</center> |
| :----:          | :----:        | :----:           |
| [github.com/m3redithw](https://github.com/m3redithw)</center> | [github.com/bradgauvin](https://github.com/bradgauvin)</center> | [github.com/mijailmariano](https://github.com/mijailmariano)</center> |

</center>


September 2022

*Codeup, Kalpana Cohort*

----
### **Table of Contents**

#### [Project Description](https://github.com/MBM-nlp/github_classification_project/blob/d14e62ddfb21831db25bc7472c9d5388c8145b98/README.md?plain=1#L34-L46)
#### Project Goal
#### Process
#### Steps to Reproduce
#### Data Dictionary
#### Exploratory Questions
#### Modeling
#### Recommendations & Next Steps

----
### **Project Description**

<br>

Like many business buzzwords, "The Metaverse" is no different and is a term many businesses are rapidly working to understand and define before it arrives. Traditionally the term has been closely associated to virtual realities much like a video game where individuals can enter and interact with simulated environments and other players. 

Recent studies by McKensey Co. and Wharton School of Business estimate the Metaverse economy to be a roughly $5-13 trillion dollar market by the year 2030. With businesses investing ~$120 billion in the first five months of 2022, and a total of ~$50 billion in 2021 -- The Metaverse is appearing more like a virtual utopia where possibility is only limited by imagination. 

Potentially more important than the idea of entering a virtual reality is the potential access to information that a Metaverse environment can help create. Imagine a doctor being able to enter the Metaverse from anywhere in the world and advising or leading highly specialized medical procedures in communities with unequal access to health care. With the changing landscape of working environments, the Metaverse can offer a future for both employer and employee to work from anywhere and still create the special interactions once only possible in the physical space.

As interesting and alluring as a Metaverse future appears to be, we believe there is still much to understand about this topic and the language people use to describe the Metaverse or better yet, the programming language and code that will create it.

<br>

### **Project Goal**

<br>

This analysis uses GitHub README.md data commonly found in cloudbased repositories to understand the common text patterns in Metaverse related topics and analysis. 

We use computational linguistic-based rules to examine and learn from unique text data found in these repositories. From learned patterns, we build a multiclass machine learning classification model capable of predicting future Metaverse repository coding languages.

In modeling we test and deploy several unique non-linear models and chose to deploy an XGBoost model on the final out-of-sample README text data. The XGBoost model returns an overall predictive accuracy score of ~46%. 

- On average, these results provide us with the potential to accurately predict and study the contents of a "Metaverse" related repo and its primary programming language by ~56% better than a baseline prediction.


*The predicted programming language used in this analysis is the primary language in overall repository percentage in the GitHub repository.* *

----

### **Process: In Brief**

<br>

1. We search and acquire the GitHub README text data of "Metaverse" associated repositories.
2. We perform the following data cleaning processes on the full dataset: filter most non-alphanumeric characters, lemmatize the text, remove stop words and words < 3 letters.
3. We classify & label repositories that contain README text but no primary programming languages as "text".
4. We bucket/group affiliated and low-frequency programming languages to higher-domain languages.
5. We split the larger text dataset into train, validate, and test subset dataset for exploration and modeling.
6. We set exploratory questions and conduct analysis on programmatic text conducting frequency counts, outlier analysis, word clouds, and visual graphs.
7. We identify unique single, paired, and grouped words associated to programming languages.
8. We set a baseline language prediction score and prep the train and validate datasets for modeling.
9. We identify, and train five unique classes of non-linear models.
10. We deploy models on train and validate datasets and measure comparative scores. 
11. We determine the best performing model on out-of-sample data and deploy this model on the test dataset.
12. Finally, we analyze our findings and provide recommendations for future analysis and actionable steps.

----

### **Steps to Reproduce**

<br>

**<span style ="color:darkred">Key Libraries & Modules:</span>**

[![github-shield](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=white)](https://github.com/MBM-nlp/github_classification_project)
[![jupyter-shield](https://img.shields.io/badge/Jupyter_Notebook-grey?logo=jupyter&logoColor=white)](https://jupyter.org/install)
[![python-shield](https://img.shields.io/badge/Python-grey?&logo=python&logoColor=white)](https://www.python.org/)
[![pandas-shield](https://img.shields.io/badge/Pandas-grey?&logo=pandas&logoColor=white)](https://pandas.pydata.org/docs/getting_started/install.html)
[![numpy-shield](https://img.shields.io/badge/Numpy-grey?&logo=numpy)](https://numpy.org/install/)
[![sklearn-shield](https://img.shields.io/badge/_-grey?logo=scikitlearn&logoColor=white&label=scikit-learn)](https://scikit-learn.org/stable/install.html)


[![matplotlib-shield](https://img.shields.io/badge/Matplotlib-3.5.1-lightgrey)](https://matplotlib.org/stable/users/installing/index.html)
[![seaborn-shield](https://img.shields.io/badge/Seaborn-0.11.2-lightgrey)](https://seaborn.pydata.org/installing.html)
[![bs4-shield](https://img.shields.io/badge/BeautifulSoup-4.11.1-lightgrey)](https://pypi.org/project/beautifulsoup4/)
[![wordcloud-shield](https://img.shields.io/badge/WordCloud-1.8.2.2-lightgrey)](https://pypi.org/project/wordcloud/)
[![nltk-shield](https://img.shields.io/badge/NLTK-3.7-lightgrey)](https://www.nltk.org/install.html)
[![xgboost-shield](https://img.shields.io/badge/XGBoost-1.6.1-lightgrey)](https://xgboost.readthedocs.io/en/stable/install.html)


<br>

1.  Note that unique to this analysis are several functions which will require a GitHub profile and API token to connect to GitHub’s API address and extract similar repository data. The script and instructions for creating a GitHub token can be found in the “acquire.py” file. 
2.  However, if wanting to reproduce this exact analysis, you will first need to download/import the necessary environment(s) for recreating the analysis. 
3.  There are several libraries and modules such as Pandas, Matplotlib, Seaborn, NumPy, SKLearn, and “XGBoost” that are used to conduct the analysis. This environment can be referenced under “notebook dependencies” in the final jupyter notebook.
4.  Once the proper environment has been imported, you can read-in the “metaverse.csv” file using Pandas “read_csv” method as shown in the final jupyter notebook and run the report.



----

### **Data Dictionary**

<br>

**Metaverse**

* Refers to a virtual-reality space in which users can interact in a computer-generated environment and potentially other users.

**Bigram**

* Refers to pair and consecutive words found in the text data.

**Language**

* Refers to a programmatic language used to create, manipulate, customize, and/or automate files found in the GitHub repository.

**ReadMe Contents**

* Refers to the text data found in the repository's description file. This file is typically used to provide foundational information on the repository's contents.

**Repo**

* Refers to a unique GitHub web-based folder where project files are stored, edited, and updated over time.

**Trigram**

* Refers to a group of three consecutive words found in the text data.

**Word Cloud**

* Refers to visual representations of the text and where the text's relative size is determined by word frequency found in the text data.  

----

### **Exploratory Questions**

<br>

#### **1. What are the most common words in READMEs?**

Across all Metaverse related repos and programming languages, we learned that key words such as "href", "detail", "summary", "open", and "project" were prominent words used when describing Metaverse repositories. This inferred to us that the "Metaverse" topic may still be developing. 

By identifying words such as "href" and "open" individuals or entities may be leveraging insights from other references or even repositories to better understand the "Metaverse" topic. 

Words like "detail" and "summary" can highlight a "zooming-in" or "zooming-out" approach to defining both the practical and theoretical application of the Metaverse or associated topics. 

#### **2. Does the length of the README vary by programming language?**

We found that the average length of Metaverse repositories differed by programming languages. On average, programming languages such as Rust, TypeScript, C, and regular text tended to contain more words in their README.md files.

On average, programming languages such as HTML, CSS, and Google's "Go" languages contained the least number of texts.

The relatively high use of programs such as "Rust" and "C" indicates the potential need for adaptable programming to create and store ideas.

The frequent use of common text may infer the use of exploring, recording, or summarizing ideas about Metaverse related findings.

#### **3. Do different programming languages use a different number of unique words?**

Yes, our analysis showed that primary programming languages tended to differ in the number of unique words/texts found in their README.md files.

True programming languages such as Java, Rust, and Python - to include text writing languages such as TypeScript and regular text contained the highest number of unique words when describing repositories. 

Since Java is considered a "high-class" programming language, this may be consistent with the high number of unique characters or text found in their respective README.md.

Consistent with previous findings, languages such as C, Rust, Python, TypeScript, and Text represents to us the relatively high-frequency use and thus, unique words found through these languages.

We also found that words such as "project" and "app" consistently appeared across most languages.

#### **4. Are there any words that uniquely identify a programming language?**

Yes, across the 11 programming classification languages studied we found the following three (3) words/text that unique identifies the individual language. 

**C**

* "opensource"
* "inventory"
* "sound"

**CSS**

* "h1"
* "landing"
* "screenshot"

**Go**

* "hyperspace"
* "global"
* "argument"

**HTML**

* "metaversity"
* "immersive"
* "vision"

**Java**

* "chance"
* "accidentally"
* "committing"

**Python**

* "weronikazak"
* "hackathon"
* "linkedin"

**Rust**

* "german"
* "payment"
* "attempt"

**Solidity**

* "metaudio"
* "audio"
* "clean"

**Text**

* "international"
* "snowcrashdao"
* "art"

**TypeScript**

* "playground"
* "explorer"
* "blockbynumber"

**Other**

* "welcome"
* "escape"
* "play"

-----

### **Modeling**

<br>

**<u>Models Tested</u>**

* Decision Tree
* SVM (Support vector machine) classifier
* KNN (k-nearest neighbors) classifier 
* Naive Bayes classifier
* XGBoost

#### **<u>Model Results</u>**

<br>

|Model              |Train    |Validate   |
|----               |----     |----       |
|                   |         |           |
|                   |         |           |
|baseline mean      |     |       |



<u>**``XGBoost Performance Through Test Dataset``**</u>

| XGBoost       | Accuracy     |Relative % Difference  |
|----           |----          |----                   |
| Baseline      |              |                       |
| Train         |              |                       |
| Validate      |              |                       |
| Test (final)  |              |                       |

----

### **Recommendations & Next Steps**

(placeholder)


----

## Planning
Sep 2 Friday
* [x] Acquire * Brad
* [x] Prepare * Mijail

Sep 3-4 Sat-Sun
* [x] Explore * ALL

Sep 5 Monday
* [x] Explore Done

Sep 6 Tuesday noon
* [x] Modeling Done - Meredith

Sep 6 Tuesday night
* [x] Final report - Brad
* [x] MVP done

Sep 7 Wednesday by noon
* [x] Presentation

Sep 7 Wednesday night
* [x] DONE

Sep 8 Thursday 10AM
* [] README DONE - Meredith & Mijail




