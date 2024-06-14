import requests
import pprint
from requests.utils import quote
import streamlit as st

url = "http://127.0.0.1:8000"  # localhost url most be changes after deployment


st.title("LM Translate")

#Option 2: A POST requests that sends all texts at once


print("\nPost request that sends all sentences at once")

c1, c2 = st.columns(2)

lang= {
    'anglais' :'en',
    'francais':'fr',
    'lingala' :'ln',
    'haoussa' :'ha',
    'yorouba' :'yo',
    'zoulou'  :'zul'

}

src_lang        = st.selectbox("Langue source",list(lang.keys()) )
texts           = st.text_area("Saisissez le texte à traduire",'' )
target_lang     = st.selectbox("Langue cible", list(lang.keys()))


if st.button("Traduire"):
    
    r = requests.get(url+"/translate?target_lang="+lang[target_lang]+"&source_lang="+lang[src_lang]+"&text="+quote(texts))
    #print(f'La reponse est sous la forme suivante:{r.json()}')
    translated_text = r.json()
    if translated_text != '':
        st.text_area("Texte traduit", translated_text[0]) 
        
        # afficher le text traduit
        #c1.write(f'traduction reussi apres {translate_time:.2f} %  secondes')
    else: 
        c1.write(f'traduction de {src_lang} % vers {target_lang}% impossible, desole! ')



