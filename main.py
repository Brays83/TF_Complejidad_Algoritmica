from flask import Flask, render_template, request, redirect, url_for
import sys
sys.path.append('./data')
app= Flask(__name__)
import data

@app.route("/",methods =['GET','POST'])
def home():
    PeliculasRecomendadas = []
    if request.method == 'POST':

        year =request.form['year']
        if(int(year) >= 2100 and int(year)< 1900):
            error="El año es incorrecto"
            return render_template('home.html',error = error)
        
        raiting =request.form['raiting']
        category =request.form['category']
        subcategory =request.form['subcategory']
        edad = request.form['year_old']
        if(category=='Selecciona la Categoria'):
            error="La categoria es obligatoria"
            return render_template('home.html',error = error)
        
        streming =request.form['streming']
 
        h=data.ReadData(int(year),int(category),int(subcategory),int(raiting),int(edad),streming)
        h.dfs(streming)
        print(h.MoviesRecomendadas)
        print(request.form)
        PeliculasRecomendadas = h.MoviesRecomendadas
        #PeliculasRecomendadas = ["hola","adios","culo"]

        #return redirect(url_for('matchs',PeliculasRecomendadas))
        return render_template('matchs.html',Movies=PeliculasRecomendadas)
    return render_template('home.html')


@app.route("/matchs")
def matchs():
    
    
    return render_template('matchs.html',)

#iniciar en cosola

#flask --app main --debug run