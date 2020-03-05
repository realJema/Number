import flask
from flask import request, jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


def converts(nombre=0): #Cette fonction convertie des nombres de chiffre en lettre
    if nombre==1: return 'un'
    elif nombre==2: return 'deux'
    elif nombre==3: return 'trois'
    elif nombre==4: return 'quatre'
    elif nombre==5: return 'cinq'
    elif nombre==6: return 'six'
    elif nombre==7: return 'sept'
    elif nombre==8: return 'huit'
    elif nombre==9: return 'neuf'
    elif nombre==10: return 'dix'
    elif nombre==11: return 'onze'
    elif nombre==12: return 'douze'
    elif nombre==13: return 'treize'
    elif nombre==14: return 'quatorze'
    elif nombre==15: return 'quinze'
    elif nombre==16: return 'seize'
    elif 16<nombre<=19: return dix(nombre)
    elif nombre>19:
        if nombre==20: return 'vingt'
        elif nombre==30: return 'trente'
        elif nombre==40: return 'quarante'
        elif nombre==50: return 'cinquante'
        elif nombre==60: return 'soixante'
        elif nombre==80: return 'quatre-vingt'
        elif nombre==10**2: return 'cent'
        elif nombre==10**3: return 'mille'
        elif nombre==10**5: return 'cent mille'
        elif nombre==10**6: return 'un million'
        elif nombre==10**9: return 'un milliard'
        elif 20<nombre<100: return dizaine(nombre)
        elif 100<nombre<1000: return centaine(nombre)
        elif 1000<nombre<1000000: return mille(nombre)
        elif 1000000<nombre<1000000000: return million(nombre)
        else: exit('Out of range')
    else: return 'Invalid'


def dix(nombre):
    nombre = nombre-10
    return 'dix-' + converts(nombre)


def dizaine(nombre) :
    if 20 < nombre < 30 or 30 < nombre < 40 or 40 < nombre < 50 or 50 < nombre < 60 or 60 < nombre < 70 or 80 < nombre < 90 :
        pref=int(str(nombre)[0])
        suf= int(str(nombre)[1])
        pref=pref*10
        return converts(pref) + ' ' +converts(suf)
    elif 70 <= nombre < 80 or 90 <= nombre < 100 :
        pref=int(str(nombre)[0])
        suf= int(str(nombre)[1])
        pref=(pref-1)*10
        suf=suf+10
        return converts(pref) + ' ' +converts(suf)


def centaine(nombre):
    pref=int(str(nombre)[0])
    suf= int(str(nombre)[1:])
    if pref == 1 : 
        return converts(pref*100) + ' ' + converts(suf)  
    elif 2<=pref<=9 :
        if suf != 0 :
            return converts(pref) + ' cent ' + converts(suf)
        else :
            return converts(pref) + ' cent'


def mille(nombre):
    if  1000 < nombre < 10000 :
        pref=int(str(nombre)[0])
        suf= int(str(nombre)[1:])
        if pref == 1 : return converts(pref*1000) + ' ' + converts(suf)  
        elif 2 <= pref <= 9 :
            if suf != 0 :
                return converts(pref) + ' mille ' + converts(suf)
            else :
                return converts(pref) + ' milles'
    elif 10000 <= nombre < 100000 :
        pref=int(str(nombre)[0: 2])
        suf= int(str(nombre)[2:])
        if suf != 0 :
            return converts(pref) + ' mille ' + converts(suf)
        elif suf == 0 :
            return converts(pref) + ' milles'
    elif 100000 <= nombre < 1000000 :
        pref=int(str(nombre)[0: 3])
        suf= int(str(nombre)[3:])
        if suf != 0 :
            return converts(pref) + ' mille ' + converts(suf)
        elif suf == 0 :
            return converts(pref) + ' milles'

def million(nombre):
    if  1000000 < nombre < 10000000 :
        pref=int(str(nombre)[0])
        suf= int(str(nombre)[1:])
        if 1 <= pref <= 9 :
            if suf != 0 :
                return converts(pref) + ' million ' + converts(suf)
            else :
                return converts(pref) + ' millions'
    elif 10000000 <= nombre < 100000000 :
        pref=int(str(nombre)[0: 2])
        suf= int(str(nombre)[2:])
        if suf != 0 :
            return converts(pref) + ' million ' + converts(suf)
        elif suf == 0 :
            return converts(pref) + ' millions'
    elif 100000000 <= nombre < 1000000000 :
        pref=int(str(nombre)[0: 3])
        suf= int(str(nombre)[3:])
        if suf != 0 :
            return converts(pref) + ' million ' + converts(suf)
        elif suf == 0 :
            return converts(pref) + ' millions'

def milliard(nombre):
    if  1000000000 < nombre < 10000000000 :
        pref=int(str(nombre)[0])
        suf= int(str(nombre)[1:])
        if 1 <= pref <= 9 :
            if suf != 0 :
                return converts(pref) + ' milliard ' + converts(suf)
            else :
                return converts(pref) + ' milliards'
    elif 10000000000 <= nombre < 100000000000 :
        pref=int(str(nombre)[0: 2])
        suf= int(str(nombre)[2:])
        if suf != 0 :
            return converts(pref) + ' milliard ' + converts(suf)
        elif suf == 0 :
            return converts(pref) + ' milliards'
    elif 100000000000 <= nombre < 1000000000000 :
        pref=int(str(nombre)[0: 3])
        suf= int(str(nombre)[3:])
        if suf != 0 :
            return converts(pref) + ' milliard ' + converts(suf)
        elif suf == 0 :
            return converts(pref) + ' milliards'


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Convertisseur de Nombres</h1>
<p>Programme pour convertir les chiffres en lettres.</p>'''


@app.route('/api/convert', methods=['GET'])
def api_all():
    if 'value' in request.args:
        value = int(request.args['value'])
    else:
        return "Error: No value field provided. Please specify a value."
        
    return converts(value), 200

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()