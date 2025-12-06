from flask import Flask, flash, redirect, render_template, request, session, url_for, jsonify
import os
from summarize import Summarizer

app = Flask(__name__)
app.secret_key = os.urandom(24)
summarizer = Summarizer()

@app.route('/')
def index():
    # Check for query parameters first
    original_text = request.args.get('original_text', '')
    summary = request.args.get('summary', '')
    show_result = request.args.get('show_result', False)
    
    # If not in query parameters, try to get from session
    if not original_text and 'original_text' in session:
        original_text = session.get('original_text', '')
        summary = session.get('summary', '')
        show_result = session.get('show_result', False)
    
    return render_template('index.html', 
                          original_text=original_text, 
                          summary=summary, 
                          show_result=show_result)

@app.route('/summarize', methods=['POST'])
def summarize():
    # Process the text...
    text = request.form.get('text')

    summary_text = summarizer.pipeline(text)

    session['original_text'] = text
    session['summary'] = summary_text
    session['show_result'] = True
    
    return render_template('index.html', original_text=text, summary=summary_text, show_result=True)

if __name__ == '__main__':
    # This will run the app on all available network interfaces,
    app.run(host='0.0.0.0', debug=True)