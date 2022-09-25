# Funções

caracteres = '' # Todos valores 


# Mostra os números
def mostrar(texto, visor):
    
    global caracteres
    caracteres = caracteres + str(texto)
    formatado = caracteres.replace('.', ',')
    visor.set(formatado)# Passando valor pro visor
        
# Retorna o calculo
def calcular(texto, visor):
    
    global caracteres
    try:
        if texto == '=':
            if texto == '=':
                resultado = eval(caracteres)
            if '.' in str(resultado):
                resultado = f'{resultado:.2f}'
                formatado = resultado.replace('.', ',')
                visor.set(formatado)
            else:
                visor.set(resultado)
            caracteres = str(resultado)
    except SyntaxError:
        limpatela(visor)
    except TypeError:
        limpatela(visor)


# Limpatela
def limpatela(visor):
    
    global caracteres
    caracteres = ''
    visor.set('0')
    