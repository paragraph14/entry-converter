from flask import Flask, render_template, request
from jekyll_entry_converter import make_entry

app = Flask(__name__)

@app.route('/')
def text_input():
    return render_template('text_input.html')
    
@app.route('/text_post', methods=['POST', 'GET'])
def get_text():
    if request.method == 'POST':
        text = request.form['text']
    else:
        return 'methode error'
    post = make_entry.make_blog_post(text)
    filename = 'test file name'
    return render_template('post_view.html', post=post, filename=filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
