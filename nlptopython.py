# import spacy 

# nlp = spacy.load("en_core_web_sm")

# doc=nlp("Apple is looking for buying uk startup for $1 billion")

# for token in doc:
#     print(token.text)



#SPECIAL CASE TOKENIZATION

# import spacy
# from spacy.symbols import ORTH

# nlp=spacy.load("en_core_web_sm")

# doc=nlp("gimme that")



# special_case=[{ORTH:"gim"},{ORTH:"me"}]

# nlp.tokenizer.add_special_case("gimme",special_case)

# for token in nlp("gimme that"):
#     print(token.text)




#POS (parts of speech) tagging in NLP;

# import spacy
# from spacy import displacy
# nlp=spacy.load("en_core_web_sm")
# doc=nlp("Python is a programming language. Current year is 2025 . Dollar Symbol is $") 

# #print(doc)

# # for token in doc:
# #     print(token)

# for token in doc:
#     print(token,"--->",token.pos_)

# for token in doc:
#     print(token,"--->",token.pos)  #Now this will give the numbers because it gives the numbers

# displacy.serve(doc,style="dep")   # this shows us the visualization part.







#Spacy stopwords removal.

#stopwords ----> these are the words that are often used in the sentence and create confusion to understand context of the document.  ex: a an i me , my , myself, he , him,


# import spacy 
# from spacy.lang.en.stop_words import STOP_WORDS

# #print(STOP_WORDS)
# #print("in" in STOP_WORDS)  #first way to check. 

# nlp=spacy.load("en_core_web_sm")
# # print(nlp.vocab["in"].is_stop)  #second way to check.


# doc=nlp("Python is a programming language. I am learning Natural Language Processing")

# for token in doc:
#     if(nlp.vocab[token.text].is_stop): 
#         print(token.text)


# for token in doc:
#     if not nlp.vocab[token.text].is_stop: 
#         print(token.text)








#Named Entity Recongnition:


# import spacy
# from spacy import displacy

# nlp=spacy.load("en_core_web_sm")

# doc=nlp("Apple is looking at buying U.K startup for $1 billion")

# for token in doc:
#     print(token.text,'-->', token.pos_)

# # displacy.serve(doc,style="ent")

# for entity in doc.ents:
#     print(entity.text)
#     # if entity.label_ == "ORG":
#     #     print(entity.text)





#Lemmatization  -- goal is to reduce different forms of words to common forms.
# ex: am, are, is -> be
# car,cars,car's -> car