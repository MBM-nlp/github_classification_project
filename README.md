
# <span style ="color: indigo">The Metaverse: NLP Multi-Classification Modeling</span>

![virtual_reality](https://user-images.githubusercontent.com/105242871/188337225-67fd4808-4264-430c-9f1d-34f09df2a27b.jpg)


**Created By:**

| Meredith Wang | Brad Gauvin | Mijail Mariano |
| ----          | ----        | ----           |
| [github.com/m3redithw](https://github.com/m3redithw) | [github.com/bradgauvin](https://github.com/bradgauvin) | [github.com/mijailmariano](https://github.com/mijailmariano) |


September 2022

*Codeup, Kalpana Cohort*


----

### **Project Goal**

In this analysis we study "Metaverse" related text data and use natural language processing techniques to predict programmatic languages* of future GitHub Metaverse repositories.

(placeholder) Why the metaverse?

#### **Project Description**

This analysis uses README.md data found on GitHub repositories to understand the common text patterns in metaverse related topics and analysis. We use computational linguistic-based rules to examine and learn from unique text data found in these repositories. From learned patterns, we build a multiclass machine learning classification model capable of predicting future metaverse repository coding languages.

*The predicted programming language used in this analysis is the primary language in overall repository percentage in the GitHub repository.* *

----

### **Data Dictionary**

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

### **Steps to Reproduce**

1.  Note that unique to this analysis are several functions which will require a GitHub profile and API token to connect to GitHub’s API address and extract similar repository data. The script and instructions for creating a GitHub token can be found in the “acquire.py” file. 
2.  However, if wanting to reproduce this exact analysis, you will first need to download/import the necessary environment(s) for recreating the analysis. 
3.  There are several libraries and modules such as Pandas, Matplotlib, Seaborn, NumPy, SKLearn, and “XGBoost” that are used to conduct this analysis. This environment can be referenced under “notebook dependencies” in the final jupyter notebook.
4.  Once the proper environment has been importer, you can then read-in the “metaverse.csv” file using Pandas “read_csv” method as shown in the final jupyter notebook and run the report.

----

### **Exploratory Questions**

#### **1. What are the most common words in READMEs?**

Across all metaverse related repos and programming languages, we learned that key words such as "href", "detail", "summary", "open", and "project" were prominent words used when describing metaverse repositories. This inferred to us that the "metaverse" topic may still be developing. 

By identifying words such as "href" and "open" the metaverse topic may be leveraging insights from other references or even repositories to better understand the "metaverse" topic. 

Words like "detail" and "summary" can highlight a "zooming-in" or "zooming-out" approach to defining both the practical and theoretical application of the metaverse or associated topics. 

#### **2. Does the length of the README vary by programming language?**

We found that the average length of Metaverse repositories differed by programming languages. On average, programming languages such as Rust, TypeScript, C, and regular text tended to contain more words in their README.md files.

On average, programming languages such as HTML, CSS, and Google's "Go" languages contained the least number of texts. 

The relatively high use of programs such as "Rust" and "C" indicates the potential need for adaptable programming to create and store ideas.

The frequent use of common text may infer the use of exploring, recording, or summarizing ideas about metaverse related findings. 

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



# Process
## Planning
Sep 2 Friday
* [x] Acquire * Brad
* [x] Prepare * Mijail

Sep 3-4 Sat-Sun
* [x] Explore * ALL

Sep 5 Monday
* [x] Explore Done

Sep 6 Tuesday noon
* [ ] Modeling Done - Meredith

Sep 6 Tuesday night
* [ ] Final report - Brad
* [ ] MVP done

Sep 7 Wednesday by noon
* [ ] Presentation

Sep 7 Wednesday night
* [ ] DONE

Sep 8 Thursday 10AM
* [ ] README DONE - Meredith & Mijail

## Data Acquisition
[acquire](acquire.py)

## Data Preparation
[prepare](prepare.py)

## Data Exploration

## Modeling
* Decision Tree
* SVM (Support vector machine) classifier
* KNN (k-nearest neighbors) classifier 
* Naive Bayes classifier
* XGBoost
