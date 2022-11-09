from flask import Flask, render_template, request, redirect

from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    query = "SELECT * FROM users"
    results = connectToMySQL('esquema_usuarios_ch').query_db(query) #ejecuta el query que tenemos en la variable query
    return results



#para insertar valores en la base de datos (first_name, last_name, email,.. los mismos valores q tiene el esquema y bd en 
#mysql) son las llaves q tenemos en el diccionario q estamos enviando... revisar el return en google/insertar y en mysql
#ejecutar el select * from para ver si se agregó
@app.route('/insertar')
def insertar():
    data = {
        "first_name": "Juana",
        "last_name":"De Arco",
        "email": "juana@codingdojo.com"
    }
    #INTERPOLACION: %(LLAVE)s..... RESULT ejecuta el query
    query = "INSERT INTO users(first_name, last_name, email) VALUES ( %(first_name)s, %(last_name)s, %(email)s )" 
    result = connectToMySQL('esquema_usuarios_ch').query_db(query, data)
    return data['first_name']+" registrada"





if __name__=="__main__":
    app.run(debug=True)