# Overview

Authors write articles on tech topics on Devopedia. In the Discussion section, they manually identify questions that beginners are most likely to ask to understand the topic. The goal of this project is to have an algorithm to automatically identify such questions.

The algorithm could consider the following sources:
* Google: It's interesting that when you search any topic on Google, it suggests common questions within a snippet titled "People also ask".
* StackOverflow: Useful place to search for most asked questions.
* Quora: The questions here may be somewhat less specific and less technical than on StackOverflow, but quite relevant to Devopedia's work since we aim to introduce the topic to readers at a high level.
* Wikipedia: Content here is not in Q&A format but we could possibly derive questions from the way content is organized into sections and sub-sections.

![Questions suggested by Google Search](assets/dataprep.jpg?raw=true "Questions suggested by Google Search")

The above figure shows what Google suggests when we search for the topic "Data Preparation". The first three questions are extremely relevant. The fourth question has the same intent as the first one and therefore such **duplicates** must be ignored. Another relevant question that Google suggests is "How is data cleaning done?" This is about giving **more details** from an earlier question about the data preparation process. Another question "What are data vizualization tools?" is related to data preparation but **not relevant**. Hence, such a suggestion must be ignored.

[Research tips](https://devopedia.org/site-map/author-guidelines?research-tips) shared on Devopedia's Author Guidelines page might help.

When trying to get information from various sources, prefer to use APIs instead of web scraping.

# Deliverables

Project must be implemented in Python3 with a modular design. Provide basic documentation and examples. No user interface is expected. Selected questions can be simply display on the console.

Code should support the following:
* Obtain content from various sources.
* Identify duplicates or irrelevant questions and ignore them.
* Rephrase the questions so that they are grammatically correct. Sometimes questions suggested by sources are not grammatically correct.
* For each question, give importance score on a scale of 1-10, 10 being very important. Scoring can be done based on how many people have upvoted that question, how many have read the question, the position at which Google suggested it, etc.
* Order questions so that readers are introduced to the basics first and read the details in later questions.
* List a maximum of ten questions. Possibly the ones with highest scores are selected but it's possible to select a couple of low scoring questions if they add diversity to the discussion. For example, one question may address disadvantages/problems/criticisms about the topic. This may not be a popular question but it makes the article more complete by considering all points of view.

# Approach

The present Algorithm is based on attribution of a Users reputation on a source (say, Stackoverflow) and translating it to the reputation score of the Question. We then use some other signals derived from the same source (or a combination of sources) to categorize the questions into Beginner, Intermediate and Expert level questions and rank the questions within each of the categories.
