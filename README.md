# Log Analyzer Chatbot

This repository contains the code for a Log Analyzer chatbot built using Streamlit. The chatbot is designed to help users analyze logs, search for relevant information, and gain insights from monitoring dashboards through a user-friendly interface. The application consists of three main modules:

## Table of Contents

- [Modules](#modules)
  - [Module 1: Log File Analysis](#module-1-log-file-analysis)
  - [Module 2: Retrieval-Augmented Generation](#module-2-retrieval-augmented-generation)
  - [Module 3: Multimodal Dashboard Analysis](#module-3-multimodal-dashboard-analysis)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Modules

### Module 1: Log File Analysis

This module allows users to upload a log file, and the LogAnalyzer app will find all exceptions in the log file, identify their root causes, and provide remedial actions in a tabular format.

### Module 2: Retrieval-Augmented Generation

In this module, a vector database is created using Wikipedia to implement the Retrieval-Augmented Generation (RAG) technique. Users can search queries, and the app will provide the most accurate results from the vector database.

### Module 3: Multimodal Dashboard Analysis

This module implements a multimodal technique where users can upload an image of a monitoring dashboard. The app will analyze the image, provide insights into important information displayed on the dashboard, and suggest any necessary remedial actions.

## Project Structure

```plaintext
Final-LogAnalysis-LLM/
│
├── .env                        # Environment variables
├── ai_apps/                    # Directory containing AI-related applications
├── data/                       # Directory containing sample data files
├── log_analyzer.py             # Main script for the log analyzer chatbot
├── log_analyzer-v0.py          # Older version of the log analyzer script
├── pexels-anna-nekrashevich-6801648.jpg  # Sample image for multimodal analysis
├── pexels-anna-nekrashevich-6802049.jpg  # Sample image for multimodal analysis
├── Readme.txt                  # Readme file with basic information
└── requirements.txt            # Required dependencies for the project

## Installation
To run this Streamlit app locally, follow these steps:

1. Clone the repository:
        git clone https://github.com/yourusername/log-analyzer-chatbot.git
        cd log-analyzer-chatbot/Final-LogAnalysis-LLM
2. Create a virtual environment and activate it:
        python -m venv venv
        .\venv\Scripts\activate


3. Install the required dependencies:
        pip install -r requirements.txt


## Usage
To start the Streamlit app, run the following command:
        cd .\ai_apps\
        streamlit run .\Home.py

This will launch the app in your default web browser. Navigate through the three pages to use each module:

Log File Analysis: Upload a log file to get a detailed analysis of exceptions, root causes, and remedial actions.
Retrieval-Augmented Generation: Enter search queries to get accurate results from the vector database.
Multimodal Dashboard Analysis: Upload an image of a monitoring dashboard to receive insights and suggested actions.
Contributing
Contributions are welcome! If you have any suggestions or improvements, please submit a pull request or open an issue.