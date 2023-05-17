from flask import Flask, request, render_template
import PyPDF2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/convert', methods=['POST'])
def convert():
    uploaded_file = request.files['pdf_file']
    
    pdf = PyPDF2.PdfReader(uploaded_file)
    num_pages = len(pdf.pages)
    text = ""
    
    for i in range(num_pages):
        text += pdf.pages[i].extract_text()
    
    with open("static/New_Text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
