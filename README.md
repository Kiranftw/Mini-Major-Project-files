CV Analysis Dashboard
Overview
The CV Analysis Dashboard is a Python-based application designed to help job seekers analyze their resumes in comparison to a job description. It uses artificial intelligence (through the Gemini Generative AI API) to:

Evaluate the relevance of a resume to a job description.
Identify missing skills and keywords.
Provide course recommendations for upskilling.
Generate a professional cover letter based on the resume and job description.
This desktop application features a graphical user interface (GUI) built with Tkinter, along with visualizations (using Matplotlib) to present the relevance score in an intuitive gauge chart.

Features
Resume Parsing: Extracts text from resumes in various formats (PDF, DOCX, TXT, DOC) and compares it with a provided job description.
Relevance Scoring: Calculates a relevance score (as a percentage) to show how well the resume matches the job requirements.
Missing Skills & Keywords: Identifies any missing skills or keywords in the resume.
Course Recommendations: Provides suggestions for online courses or certifications to fill any skill gaps.
Cover Letter Generation: Generates a professional cover letter tailored to the job description and resume content.
Visual Dashboard: Displays results and visualizations (gauge chart) in a user-friendly GUI.
Installation
Prerequisites
Ensure you have the following installed on your system:

Python 3.7 or higher
Pip (Python package installer)
Required Python Packages
Install the necessary packages using pip. Open your terminal or command prompt and run:

bash
Copy
Edit
pip install matplotlib ipython pypandoc python-dotenv numpy pandas pdfplumber docx2txt google-generativeai
API Key Configuration
This project uses the Gemini Generative AI API. You need to:

Obtain your API key from the Gemini platform.
Create a file named .env in the project directory.
Add the following line to your .env file (replace YOUR_API_KEY_HERE with your actual API key):
ini
Copy
Edit
GEMINI_API_KEY=YOUR_API_KEY_HERE
Alternatively, you can hardcode the API key in the code (not recommended for production use).

Usage
Run the Application:

Open your terminal or command prompt in the project directory and run:

bash
Copy
Edit
python your_script_name.py
(Replace your_script_name.py with the name of your main Python file.)

Using the Dashboard:

Job Description: Enter the job description text in the provided text area.
Upload Resume: Click the "Browse" button to select your resume file (supported formats: PDF, DOCX, TXT, DOC).
Submit: Click the "Submit" button to run the analysis.
Results: View your relevance score, missing skills/keywords, course recommendations, and a resume summary.
Cover Letter: If your relevance score meets the threshold, click "Cover Letter?" to generate a professional cover letter. You can also save the cover letter to a file.
How It Works
Text Extraction: The application extracts text from the resume file using different libraries depending on the file type.
Resume Analysis: The extracted resume text and job description are sent to the Gemini Generative AI API with a prompt that instructs the model to compare the resume to the job description and output the relevance score, missing skills, keywords, and recommendations in JSON format.
Visualization: The relevance score is displayed as a gauge chart, providing a visual indicator of the resume's match quality.
Course & Cover Letter Generation: Based on the analysis, the application can suggest relevant courses for missing skills and generate a custom cover letter if the resume meets the required relevance threshold.
Troubleshooting
Constructor Issues:
Ensure that the constructor methods are named __init__ (with two underscores) and not _init_.

API Key Problems:
Verify your API key is correct and is stored properly in the .env file. Check that the environment variables are loaded correctly.

File Format Errors:
Make sure that you are uploading one of the supported file formats (PDF, DOCX, TXT, DOC). If the resume text extraction fails, an error message will be displayed.

License
This project is provided for educational and demonstration purposes. You may modify or use this code as needed for personal or academic projects. (Include a proper license if you plan to distribute the project.)

Acknowledgements
Thanks to the developers of Tkinter, Matplotlib, and the various libraries used in this project.
Special thanks to the Gemini Generative AI team for their API which powers the resume analysis.
