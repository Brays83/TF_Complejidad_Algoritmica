from flask import Flask, render_template, request, redirect, url_for

app= Flask(__name__)

@app.route("/",methods =['GET','POST'])
def home():
    if request.method == 'POST':

        year =request.form['year']
        if(int(year) >= 2100 and int(year)< 1900):
            error="El año es incorrecto"
            return render_template('home.html',error = error)
        
        raiting =request.form['raiting']
        category =request.form['category']

        subcategory =request.form['subcategory']
        if(category=='Selecciona la Categoria'):
            error="La categoria es obligatoria"
            return render_template('home.html',error = error)
        
        streming =request.form['streming']
 
        
        print(request.form)

        return redirect(url_for('matchs'))
    return render_template('home.html',)


@app.route("/matchs")
def matchs():

    return render_template('matchs.html')

#iniciar en cosola

#flask --app main --debug run