from PyPDF2 import PdfReader
from google import genai


client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=""" You are a PDF summarizer. Read the attached PDF and produce a clear, structured summary.

Give me:
1. A high-level overview of the entire document.
2. Key points and important details.
3. Any important data, insights, or conclusions.
4. A short final takeaway in plain language.

Keep the summary concise, accurate, and easy to understand. Ignore formatting artifacts or irrelevant page content.
    """,
    files=["example.pdf"]  # Replace with your PDF file path
)



def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file.
    
    Returns:
        str: Extracted text from the PDF.
    """
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text



def save_text_to_file(text, output_path):
    """
    Save text to a file.
    
    Args:
        text (str): Text to be saved.
        output_path (str): Path to save the text file.
    """
    with open(output_path, 'w') as file:
        file.write(text)
        
    try:
        print(f"Text successfully saved to {output_path}")
    except Exception as e:
        print(f"An error occurred while saving the text: {e}")
        

def summarize_text(text):
    """
    Placeholder for text summarization logic.
    
    Args:
        text (str): Text to be summarized.
    
    Returns:
        str: Summarized text.
    """
    
    
    return response.text  

def main():
    pdf_path = 'example.pdf'  # Replace with your PDF file path
    output_path = 'output.txt'  # Replace with your desired output file path
    
    try:
        text = extract_text_from_pdf(pdf_path)
        save_text_to_file(text, output_path)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()