### Table of Content
1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>
The code in this repository requires no additional libraries beyond the Anaconda distribution of Python. It should run without issues using Python version 3.*.

## Project Motivation<a name="motivation"></a>
This project was completed as part of the Udacity Data Scientist Nanodegree, focusing on the analysis of real-world survey data from the Stack Overflow Developer Surveys (2021–2024). The goal was to answer critical questions about trends and challenges in the tech industry, including:

How have programming languages, databases, and tools evolved over the past four years?

What is the current adoption and future potential of AI tools in development environments?

Can we develop a recommendation model to predict programming language preferences based on developer attributes?

This analysis serves as a practical demonstration of data science methodologies, from exploratory analysis to machine learning, providing insights into the evolving preferences of developers worldwide.

## File Descriptions <a name="files"></a>
This repository includes the following files:

tech_trends_ai_use.ipynb:
Explores trends in programming languages, databases, and AI tool usage.
Visualizes insights into developer preferences and adoption patterns.

model.ipynb:
Implements a Random Forest Classifier to predict programming language preferences.

functions.py:
Utility functions to streamline analysis: 

The raw survey data (survey_results_public_(2021-2024).csv) is not included in this repository but can be downloaded from the [Stack Overflow website](https://survey.stackoverflow.co/).

## Results<a name="results"></a>
The main findings of this analysis include:

Trends in Technology:
JavaScript and Python remain dominant, with rising interest in TypeScript and Rust.
PostgreSQL continues to grow in popularity among databases, while emerging platforms like Supabase gain traction.

AI Tool Adoption:
Developers are increasingly using tools like ChatGPT and GitHub Copilot for tasks like writing code and debugging.
Positive sentiment toward AI tools indicates high potential for future integration, despite challenges like trust and ethics.

Programming Language Recommendations:
A Random Forest Classifier achieved an accuracy of 27.38%, performing well for dominant languages but struggling with less frequent ones.
The complete findings and detailed analysis are available in the Jupyter Notebooks.

The results can be found at the post available [here](https://medium.com/@gracorabello/insights-from-stack-overflow-surveys-2021-2024-7a3dff8d7e2c).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>
Licensing: Credit to Stack Overflow for the survey data. The data's licensing and additional details can be found [here](https://survey.stackoverflow.co/).

Authors: Developed by [Graco Rabello](https://www.linkedin.com/in/gracorabello/).

Acknowledgements: Special thanks to Udacity for the guidance provided in the Data Scientist Nanodegree program.

Feel free to use the code in this repository for your own projects or learning purposes!
