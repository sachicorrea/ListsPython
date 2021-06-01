""" Modulo Listas
    Funciones para practicas con listas
    Santiago Correa Restrepo
    Mayo 30-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

# Function to get a cummulative sum from a list of items
def suma_acumulativa(lista_numeros):
  #cummulative terms of a list
  sm = 0
  cum_list = []

  for i in lista_numeros:
    sm += i
    cum_list.append(sm)
  return cum_list

# Function to transate English words to Pig Latin
def traductor_pig_latin(lista_palabras):

  # vowel alphabet
  vowel = 'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'

  # Algorithm to extract the words that start with a vowel or consonant from a list
  transformedList = []

  for w in lista_palabras:   
    startsVowel = w.startswith(vowel)

    # Change variable startsVowel for True if English words start with a vowel; otherwise False
    if startsVowel == False:
      transformedList.append(w)
      newList = transformedList.copy()

      translatedWords = [x + 'yay' for i, x in enumerate(newList)]
    else:
      newList = transformedList.copy()
      translatedWords = [x[1:] + x[0] + 'ay' for i, x in enumerate(newList)]
  print(translatedWords)

# Function to identify fruits that start with A vowel
def identificador_frutas(lista_frutas):
  # vowel alphabet
  vowel = 'A', 'a'

  print([f for f in lista_frutas if f.startswith(vowel)])

def son_palindromos(frase_uno, frase_dos):
  #TODO Comentar código
  #TODO Implementar la función
  return "No implementada aún"
