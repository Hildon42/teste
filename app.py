from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__)


# conexão com o banco dedados
conn = sqlite3.connect('gestao_audiovisual.db')
cursor = conn.cursor()


# criação de tabelas se não existire,
cursor.execute('''
    CREATE TABLE IF NOT EXISTS audiovisual (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        nomeaudivisual TEXT,
        nome_tipoproduc TEXT,
        nome_gen TEXT,
        data_assis TEXT
    )
''')


conn.commit() # salvar
conn.close()  # Fechar



@app.route('/')
def index():
    conn = sqlite3.connect('gestao_audiovisual.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM audiovisual')
    audiovis = cursor.fetchall()
    conn.close
    return render_template('index.html', audiovisual=audiovis)


@app.route('/novo_audiovisual', methods=['GET', 'POST']) 
def novo_audiovisual():
    if request.method == 'POST':
        usuario = request.form['usuario']
        nomeassis = request.form['nomeaudivisual']
        nometipo = request.form['nome_tipoproduc']
        genero = request.form['nome_gen']
        data = request.form['data_assis']


        conn = sqlite3.connect('gestao_audiovisual.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO audiovisual (usuario, nomeaudivisual, nome_tipoproduc, nome_gen, data_assis)
            VALUES (?, ?, ?, ?, ?)
        ''', (usuario, nomeassis, nometipo, genero, data))

        conn.commit()
        conn.close()

        return redirect(url_for('index'))
    return render_template('novo_audiovisual.html')


@app.route('/limpar_audio')
def limpar_audio():
    conn = sqlite3.connect('gestao_audiovisual.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM audiovisual')
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)





