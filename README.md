


[![Sync to Hugging Face hub](https://github.com/Sabry-Ahmed/MACHINE-LEARNING/actions/workflows/main.yml/badge.svg)](https://github.com/Sabry-Ahmed/MACHINE-LEARNING/actions/workflows/main.yml)

# Multimodal Sentiment Analysis System for Large Companies

This project aims to develop a comprehensive sentiment analysis system tailored for large companies, enabling them to extract and understand customer emotions from both text-based (emails) and audio-based (phone calls) interactions. By analyzing these customer interactions, companies can gain valuable insights to enhance their customer experience and satisfaction levels.





# Scheme: Data Input and Deployment Workflow

This scheme illustrates the workflow for inputting data (voices and texts) using a Streamlit application and deploying the code to Hugging Face Spaces using GitHub Actions.

## Step 1: Data Input with Streamlit

1. **User Interaction:**
   - Users interact with a Streamlit web application interface.
   - The application prompts users to input data in the form of voice recordings or text.

2. **Input Options:**
   - Users can either upload audio files (e.g., MP3 or WAV) or enter text directly into the application.

3. **Streamlit Interface:**
   - Streamlit provides an intuitive interface for users to input their data.
   - It offers functionalities such as file upload widgets and text input fields.

## Step 2: Data Processing and Analysis

4. **Data Processing:**
   - The Streamlit application processes the input data, handling both audio files and text inputs.
   - Audio files are converted to text using speech-to-text conversion libraries (e.g., librosa).
   - Text inputs are directly processed for sentiment analysis.

5. **Sentiment Analysis:**
   - Sentiment analysis algorithms analyze the processed text data to determine sentiment (positive, negative, neutral).

## Step 3: Deployment to Hugging Face Spaces

6. **Git Version Control:**
   - The code, including the Streamlit application and sentiment analysis scripts, is version-controlled using Git.
   - Changes and updates are tracked using Git commits.

7. **GitHub Actions:**
   - GitHub Actions are configured to automate the deployment process.
   - Upon pushing changes to the Git repository, GitHub Actions trigger deployment to Hugging Face Spaces.

8. **Hugging Face Spaces:**
   - The code is deployed to Hugging Face Spaces, making the Streamlit application accessible online.
   - Users can interact with the deployed application through the Hugging Face Spaces platform.

![Scheme](./image.png)

## Features
- **Email Sentiment Analysis:** Automatically analyzes the sentiment of customer emails to determine positivity or negativity.
- **Phone Call Sentiment Analysis:** Performs sentiment analysis on recorded phone calls to identify positive or negative feedback.

## Deployment
The project is deployed on the Hugging Face Spaces platform. You can access the application [here](https://huggingface.co/spaces/jokerthejoke/MACHINE-LEARNING).

## How It Works
1. **Data Collection:**
   - Emails and phone call recordings are collected from customer interactions.

2. **Data Processing:**
   - NLP techniques are used to extract text from emails.
   - Speech-to-text conversion tools are employed for phone call recordings.

3. **Sentiment Analysis:**
   - Sentiment analysis algorithms classify the text data into positive or negative sentiments.

## Technologies Used
- Python
- Streamlit
- Hugging Face Spaces
- Docker
- Transformers

## Usage
1. **Local Deployment:**
   - Clone the project repository from [GitHub](https://github.com/Sabry-Ahmed/MACHINE-LEARNING/).
   - Navigate to the project directory.
   - Run `docker-compose up` to deploy the application locally.

2. **Online Access:**
   - Access the application directly via the provided [Hugging Face Spaces link](https://huggingface.co/spaces/jokerthejoke/MACHINE-LEARNING).

## Future Enhancements
- **Database Integration:** Implement a database system to store analyzed data for future reference and analysis.
- **API Development:** Create an API to access the analyzed data and provide graphical representations of sentiment analysis results.
- **Enhanced NLP:** Enhance text processing capabilities to extract and analyze every word of the client's discussion, providing deeper insights into customer feedback.

## Conclusion
Given more time could be made to the Review Simplification Project. Integrating a database system and developing an API would facilitate data storage and access, enabling advanced analytics and visualization. Additionally, further enhancements to NLP capabilities would allow for more comprehensive analysis of customer feedback, leading to more actionable insights for businesses.

---

