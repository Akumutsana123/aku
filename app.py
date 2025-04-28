from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def beranda():
    return render_template('beranda.html')

@app.route('/tentang')
def tentang_saya():
    return render_template('tentang.html')

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')




if __name__ == '__main__':
    app.run()
