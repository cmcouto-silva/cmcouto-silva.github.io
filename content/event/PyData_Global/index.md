---
title: "Introduction to Machine Learning Pipelines: How to Prevent Data Leakage and Build Efficient Workflows"

event: PyData Global
event_url: ""

location: "Global - Remote" 
# address:
#   street: 450 Serra Mall
#   city: Stanford
#   region: CA
#   postcode: '94305'
#   country: United States

abstract: "<p style='text-align: justify;'>This webinar will introduce machine learning pipelines and discuss their importance in building efficient and robust workflows. It will explain how pipelines help to prevent data leakage and ensure model stability by allowing for proper separation of training, validation, and test data. Through a blend of theory and practice, it will provide and explain code chunks in Python using well-known open-source packages like scikit-learn (pipeline and column transformers) and feature-engine to ensure a complete understanding of the .fit(), .transform(), and .predict() methods. By the end of this webinar, the audience will have a solid understanding of the theory behind machine learning pipelines and practical examples of using them effectively in their projects.</p>"

summary: "A 2‑hour workshop on machine learning pipelines at PyData Global, focusing on data leakage prevention and efficient model building with scikit-learn and other tools."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2023-12-08'
# date_end: '2023-12-08T15:00:00Z'
all_day: true

authors: [admin]
tags: [statistics, machine learning, data science]

# Is this a featured talk? (true/false)
featured: false

# image:
#   caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
#   focal_point: Right

links:
  - icon: github
    icon_pack: fab
    name: Code
    url: https://github.com/cmcouto-silva/Talks/tree/main/PyDataGlobal
  - icon: file-pdf
    icon_pack: fa
    name: Slides
    url: https://github.com/cmcouto-silva/Talks/blob/main/PyDataGlobal/slides/PyDataGlobal2023_slides.pdf
  - icon: python
    icon_pack: fab
    name: Workshop details
    url: https://global2023.pydata.org/cfp/talk/review/QMNF983WSYZTRPTULAQDWDBM8B9SBRVH
  - icon: file
    icon_pack: fa
    name: Certification
    url: talks/PyDataGlobal.pdf
  
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''

# # Projects (optional).
# #   Associate this post with one or more of your projects.
# #   Simply enter your project's folder or file name without extension.
# #   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
# #   Otherwise, set `projects = []`.
# projects:
#   - example
---

**Objective:**

By the end of this session, participants will have a comprehensive understanding of machine learning pipelines, equipped with the knowledge to prevent data leakage and build efficient, robust ML models using a range of tools and libraries relevant to today's data science landscape (focus on scikit-learn).
{style="text-align: justify;"}

**Introduction:**

This workshop will commence with an overview of the machine learning (ML) project lifecycle, emphasizing the critical role of model validation. Key attention will be given to defining and understanding data leakage – its causes, consequences, and prevention strategies.
{style="text-align: justify;"}

**Hands-on learning:**

Participants will engage in practical exercises demonstrating the nuances of data preprocessing and model training. These activities are designed to illustrate the occurrence of data leakage, how to identify it, and effective strategies to prevent it.
{style="text-align: justify;"}

The workshop will compare and contrast methods to avert data leakage, both with and without the use of pipelines. Participants will gain insights into the additional steps required when not using pipelines and understand the benefits of implementing the scikit-learn pipeline in their workflows.
{style="text-align: justify;"}

We will explore how essential libraries like Scikit-learn, Feature-engine, and Imbalanced-learn, integrate into this process. The workshop will provide practical examples using these tools, from basic to relatively complex pipeline implementations.
{style="text-align: justify;"}

Towards the conclusion, the workshop will delve into how advanced autoML libraries like PyCaret employ pipelines. Additionally, we will quickly explore the application of pipeline conventions in other libraries, such as Spark ML, to highlight the widespread use and importance of this approach in various ML ecosystems.
{style="text-align: justify;"}
