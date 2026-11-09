
import math
FONCTIONS = {
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "sqrt": math.sqrt, "exp": math.exp,
    "log": math.log, "log10": math.log10, "abs": abs,
}
CONSTANTES = {"pi": math.pi, "e": math.e}
    
def convert_f(arg):
    i = 0
    token = []
    while i < len(arg):
        c = arg[i]
        if c.isdigit():
            debut = i
            while i < len(arg) and (arg[i].isdigit() or arg[i] == "."):
                i += 1
            token.append(arg[debut:i])
        elif c.isalpha():
            debut = i
            while i < len(arg) and arg[i].isalpha():
                i += 1
            if arg[debut:i] == "log":
                while i < len(arg) and (arg[i].isdigit() or arg[i] == "."):
                    i += 1
            token.append(arg[debut:i])
        elif c.isspace():
            while i < len(arg) and arg[i].isspace():
                i += 1
        else:
            if c in "+-*/^()√":
                token.append(c)
                i += 1
            else:
                raise ValueError("Caractere Invalide")        
    return token

def convert_to_eq(tokens):
    result = []
    prev = ""                      
    for t in tokens:
        if t == "^":
            t = "**"
        elif t[0].isalpha() and t != "x" and t not in FONCTIONS and t not in CONSTANTES:
            raise ValueError("Nom inconnu : " + t)

        
        if prev != "":
            fin = prev[0].isdigit() or prev == ")" or prev == "x" or prev in CONSTANTES
            debut = t[0].isdigit() or t[0].isalpha() or t == "("
            if fin and debut:
                result.append("*")

        result.append(t)
        prev = t
    return "".join(result)


def create_function(formule):
    chain = convert_to_eq(convert_f(formule))
    code = compile(chain, "<formule>", "eval")
    env = {"__builtins__": {}}
    env.update(FONCTIONS)
    env.update(CONSTANTES)
    def f(x):
        return eval(code, env, {"x": x})
    return f
           

txt = "(x-3)(x+3)" 
x = create_function(txt) 
print(x(3))

