import nltk
from nltk.tokenize import word_tokenize
import re

def parse_text_nltk(text):
    # Initialize the extracted data dictionary
    extracted_data = {
        "name": None,
        "email": None,
        "phone": None,
        "skills": [],
        "experience": [],
        "education": []
    }

    # Tokenize the text
    tokens = word_tokenize(text)

    # Extract email
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email_matches = re.findall(email_regex, text)
    if email_matches:
        extracted_data["email"] = email_matches[0]


    return extracted_data

    #Extract phone number
    phone_number_regex  = cd




if __name__ == "__main__":
    sample_text = """
    John Doe
    Email - john.doe@example.com
    Phone: +1-234-567-8901
    Skills: Python, Machine Learning, Data Analysis
    Experience: 5 years at ABC Corp
    Education: B.Sc. in Computer Science from XYZ University
    """
    result = parse_text_nltk(sample_text)
    print("Extracted Data:")
    print(result)
