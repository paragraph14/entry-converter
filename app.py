from flask import Flask, render_template, request
import make_blog_post

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
    post = make_blog_post.make_blog_post(text)
    return render_template('post_view.html', post=post)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
