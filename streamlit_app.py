import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px
#import os

#from fonctions import calcul_conso_gpl,rendement, calcul_energy_hfo, price_hfo, price_gpl, euro_to_dollar, dollar_to_CFA, dollar_to_ZAR, dollar_to_din_tun, dollar_to_mur, space_in_numbers, courbe
#from gen_pdf import gen_pdf
#from bokeh.plotting import figure
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb

#import altair as alt
#from vega_datasets import data


def calcul_energy_hfo(conso):
    return conso*11774

def calcul_conso_gpl(energy):
    return energy/13800

def price_hfo(conso):
    return conso*408.9

def price_gpl(conso) : 
    return conso*602

def euro_to_dollar(eur):
    return eur * 1.09

def dollar_to_CFA(dollar):
    return dollar * 600.72

def dollar_to_ZAR(dollar): 
    return dollar * 18.34

def dollar_to_mur(dollar):
    return dollar * 45.5

def dollar_to_din_tun(dollar):
    return dollar * 3.09

def space_in_numbers(x):
    n= ""
    
    for i in range(1,len(x) + 1):
        if i%3 == 0 and i != len(x):
            n = " " + x[-i] + n
        else :
            n = x[-i] + n
    
    return n


def courbe(base,n,p):
    l=np.zeros((p,n))
    for j in range (p):
        for i in range(n):
            #c = np.random.randint(0,2)
            #if c == 0 : 
                #l[j][i] = base - base*np.random.rand()
                #base = l[j][i]
               # print(i,j)
           
           # else : 
                l[j][i] = base + 0.01*base*np.random.rand()
                base = l[j][i]
                #print(i,j)
        
    return l

def rendement(a):
    l=[]
    for i in range(a+1):
        if i < 8:
            l+= [1 - i*0.018]
        else :
            l += [0.8 + 0.2*(1/(1+ i**0.5))]
        
    return l

#Tab icon and name
st.set_page_config(page_title='Comparaison HFO vs GPL',page_icon='Logo_TotalEnergies.png', initial_sidebar_state="expanded", layout = "wide")

#Application title
st.header('Application de comparaison des coûts de fonctionnement entre le HFO et le GPL')




#Sidebar
with st.sidebar : 
    st.header('Menu')
    st.divider()
    
    #Instantiation of variables
    if 'en' not in st.session_state : 
        st.session_state['en'] = False

    if 'fr' not in st.session_state : 
        st.session_state['fr'] = True
        
    if 'ram' not in st.session_state : 
         st.session_state['ram'] = False
          
    if 'filter' not in st.session_state : 
         st.session_state.filter = False
         
    if 'nb_ram' not in st.session_state :
        st.session_state['nb_ram'] = 0
    
    if 'ram_cost' not in st.session_state :
        st.session_state['ram_cost'] = 0
    
    if 'nb_fil' not in st.session_state :
        st.session_state['nb_fil'] = 0
        
    if 'money' not in st.session_state : 
        st.session_state['money'] = ' $'
        
    if 'conso' not in st.session_state :
        st.session_state['conso'] = 0
    
    if 'price_hfo' not in st.session_state :
        st.session_state['price_hfo'] = 0
        
    if 'nb_employee' not in st.session_state :
        st.session_state['nb_employee'] = 0
        
    if 'salary' not in st.session_state :
        st.session_state['salary'] = 0
        
    if 'pci_hfo' not in st.session_state :
        st.session_state['pci_hfo'] = 0
        
    if 'pui' not in st.session_state :
        st.session_state['pui'] = 0
        
    if 'nb_h_per_day' not in st.session_state :
        st.session_state['nb_h_per_day'] = 0
        
    if 'nb_day_per_week' not in st.session_state :
        st.session_state['nb_day_per_week'] = 0
        
    if 'price_kWh' not in st.session_state :
        st.session_state['price_kWh'] = 0
        
    if 'country' not in st.session_state :
        st.session_state['country'] = 'Autres'
        
    if 'meth' not in st.session_state :
        st.session_state['meth'] = 'Personnel interne'
        
    if 'choose' not in st.session_state :
        st.session_state['choose'] = "Page d'accueil"
        
    if 'presta' not in st.session_state :
        st.session_state['presta'] = 0
    
    if 'presta_unknow' not in st.session_state :
        st.session_state['presta_unknow'] = False
        
    if 'other_unknow' not in st.session_state :
        st.session_state['other_unknow'] = False
        
    if 'meth_other' not in st.session_state :
        st.session_state['meth_other'] = ''
    
    if 'price_other_meth' not in st.session_state :
        st.session_state['price_other_meth'] = 0
        
    if 'pieces' not in st.session_state :
        st.session_state['pieces'] = False
    
    if 'change_pcs' not in st.session_state :
        st.session_state['change_pcs'] = ''
    
    if 'but_pcs' not in st.session_state :
        st.session_state['but_pcs'] = ''
        
    if 'c' not in st.session_state :
        st.session_state['c'] = []
        
    if 'cl' not in st.session_state :
        st.session_state['cl'] = []
    
    if 'sum_pcs' not in st.session_state :
        st.session_state['sum_pcs'] = 0
    
    if 'eau' not in st.session_state :
        st.session_state['eau'] = 0
        
    if 'eau_l' not in st.session_state :
        st.session_state['eau_l'] = 0
    
    if 'eau_nb' not in st.session_state :
        st.session_state['eau_nb'] = 0
        
    if 'nett' not in st.session_state :
        st.session_state['nett'] = False
        
    if 'nett_meth' not in st.session_state :
        st.session_state['nett_meth'] = 'Opérateurs interne'
        
    if 'same_empl' not in st.session_state :
        st.session_state['same_empl'] = False
        
    if 'n' not in st.session_state :
        st.session_state['n'] = []
    
    if 'ne' not in st.session_state :
        st.session_state['ne'] = []
        
    if 'but_nett' not in st.session_state :
        st.session_state['but_nett'] = ''
    
    if 'nett_eq' not in st.session_state :
        st.session_state['nett_eq'] = ''
        
    if 'sum_nett' not in st.session_state :
        st.session_state['sum_nett'] = 0
        
    if 'nb_empl2' not in st.session_state :
        st.session_state['nb_empl2'] = 0
    
    if 'nett_presta' not in st.session_state :
        st.session_state['nett_presta'] = 0
    
    if 'nett_cost' not in st.session_state :
        st.session_state['nett_cost'] = 0
    
    if 'additif' not in st.session_state :
        st.session_state['additif'] = False
        
    if 'cost_add' not in st.session_state :
        st.session_state['cost_add'] = 0
        
    if 'name_add' not in st.session_state :
        st.session_state['name_add'] = ''
        
    if 'cons_add' not in st.session_state :
        st.session_state['cons_add'] = 0
    
    if 'add' not in st.session_state :
        st.session_state['add'] = []
        
    if 'but_add' not in st.session_state :
        st.session_state['but_add'] = ''
        
    if 'sum_add' not in st.session_state :
        st.session_state['sum_add'] = 0
        
    if 'chaud' not in st.session_state :
        st.session_state['chaud'] = False
        
    if 'nb_chaud' not in st.session_state :
        st.session_state['nb_chaud'] = 0
    
    if 'price_pcs' not in st.session_state :
        st.session_state['price_pcs'] = 0
        
    if 'fre_chgm' not in st.session_state :
        st.session_state['fre_chgm'] = 0
        
    if 'time_int' not in st.session_state :
        st.session_state['time_int'] = 0
    
    if 'time_prod' not in st.session_state :
        st.session_state['time_prod'] = False
    
    if 'tp_yes_no' not in st.session_state :
        st.session_state['tp_yes_no'] = 'Non'
        
    if 'chx_int' not in st.session_state :
        st.session_state['chx_int'] = False
        
    if 'chx_maint' not in st.session_state :
        st.session_state['chx_maint'] = 'Non'
        
    if 'time_int_nett' not in st.session_state :
        st.session_state['time_int_nett'] = 0
        
    if 'fre_nett' not in st.session_state :
        st.session_state['fre_nett'] = 0
        
    if 'cbx_nett_prod' not in st.session_state :
        st.session_state['cbx_nett'] = False
    
    if 'nett_yn' not in st.session_state :
        st.session_state['nett_yn'] = 'Non'
    
    if 'time_int_nett_presta' not in st.session_state :
        st.session_state['time_int_nett_presta'] = 0
        
    if 'fre_nett_presta' not in st.session_state :
        st.session_state['fre_nett_presta'] = 0
        
    if 'cbx_nett_presta' not in st.session_state :
        st.session_state['cbx_nett_presta'] = False
    
    if 'nett_yn_presta' not in st.session_state :
        st.session_state['nett_yn_presta'] = 'Non'
        
    if 'gpl_price' not in st.session_state :
        st.session_state['fre_nett_presta'] = 500
    
    if 'gpl_maint' not in st.session_state :
        st.session_state['fre_maint'] = 0
        
    if 'hum_area' not in st.session_state :
        st.session_state['hum_area'] = False
        
    if 'gpl_maint_choice' not in st.session_state :
        st.session_state['gpl_maint_choice'] = 'Opérateurs interne'
        
    if 'hybrid_empl' not in st.session_state :
        st.session_state['hybrid_empl'] = 0
        
    if 'hybrid_presta' not in st.session_state :
        st.session_state['hybrid_presta'] = 0
        
    if 'hyb_dk' not in st.session_state :
        st.session_state['hyb_dk'] = False
        
    if 'gpl_cost_maint' not in st.session_state :
        st.session_state['gpl_cost_maint'] = 0
        
    if 'gpl_nb_empl' not in st.session_state :
        st.session_state['gpl_nb_empl'] = 0
        
    if 'gpl_presta' not in st.session_state :
        st.session_state['gpl_presta'] = 0
        
    if 'gpl_presta_unknow' not in st.session_state :
        st.session_state['gpl_presta_unknow'] = False
        
    if 'max_gpl_price' not in st.session_state :
        st.session_state['max_gpl_price'] = 2000
    
    if 'base_gpl_price' not in st.session_state :
        st.session_state['base_gpl_price'] = 500
    
    if 'tot_cost_hfo' not in st.session_state :
        st.session_state['tot_cost_hfo'] = 0
        
    if 'tot_cost_gpl' not in st.session_state :
        st.session_state['tot_cost_gpl'] = 0
    
    if 'eco' not in st.session_state :
        st.session_state['eco'] = False
        
    if 'rend_ram' not in st.session_state :
        st.session_state['rend_ram'] = 0
        
    if 'model_use' not in st.session_state :
        st.session_state['model_use'] = False
        
    if 'hfo_model_cost_opex' not in st.session_state :
        st.session_state['hfo_model_cost_opex'] = 0
    
    if 'model_want' not in st.session_state :
        st.session_state['model_want'] = False
        
    if 'rand_gpl' not in st.session_state :
        st.session_state['rand_gpl'] = 0
        
    if 'cost_hfo_maint' not in st.session_state :
        st.session_state['cost_hfo_maint'] = 0
        
    if 'en_hfo_GJ' not in st.session_state :
        st.session_state['en_hfo_GJ'] = 0
        
    if 'teneur_soufre' not in st.session_state :
        st.session_state['teneur_soufre'] = 0
        
    if 'con_soufre' not in st.session_state :
        st.session_state['con_soufre'] = 0
    
    if 'coef_filtre' not in st.session_state :
        st.session_state['coef_filtre'] = 1
        
    if 'lang' not in st.session_state :
        st.session_state['lang'] = 'Français'
        
    if 'investment_gpl' not in st.session_state :
        st.session_state['investment_gpl'] = 'Investissement client'
        
    if 'cost_investment' not in st.session_state :
        st.session_state['cost_investment'] = 0
    
    if 'duration_investment' not in st.session_state :
        st.session_state['duration_investment'] = 0
        
    if 'invest_details' not in st.session_state :
        st.session_state['invest_details'] = False
        
    if 'name_gpl_inv' not in st.session_state :
        st.session_state['name_gpl_inv'] = ''
    
    if 'cost_eq_gpl_inv' not in st.session_state :
        st.session_state['cost_eq_gpl_inv'] = 0
        
    if 'nb_eq_gpl_inv' not in st.session_state :
        st.session_state['nb_eq_gpl_inv'] = 0
        
    if 'but_gpl_inv' not in st.session_state :
        st.session_state['but_gpl_inv'] = False
        
    if 'inv_det' not in st.session_state :
        st.session_state['inv_det'] = []
        
    if 'cost_inv_year' not in st.session_state :
        st.session_state['cost_inv_year'] = 0
        
    if 'cost_investment_totalen' not in st.session_state :
        st.session_state['cost_investment_totalen'] = 0
        
    if 'inv_yes' not in st.session_state :
        st.session_state['inv_yes'] = False
        
    #Functions to change language
    #def change_fr_to_en() : 
       # if st.session_state.fr : 
            #st.session_state.en = False
            
       # elif st.session_state.fr == False : 
           # st.session_state.en = True 
            
       # elif st.session_state.fr == False and st.session_state.en == False :
           # st.session_state.fr == True

   # def change_en_to_fr() : 
        #if st.session_state.en : 
           # st.session_state.fr = False
            
       # elif st.session_state.en == False : 
           # st.session_state.fr = True
            
       # elif st.session_state.fr == False and st.session_state.en == False :
            #st.session_state.fr == True
            
            
    #Selection Menu
    st.session_state.choose = st.selectbox("Estimations", ("Page d'accueil","HFO", "GPL","Comparaison", "Proposition d'optimisation"))
    st.divider()
    
    #Select language
    st.session_state.lang = st.selectbox("Langues",("Français", "English"))
    
    
#French language
if st.session_state.lang == 'Français' :
    #Home page
    if st.session_state.choose == "Page d'accueil":
        #Enter informations
        st.subheader("Veuillez entrer les informations ci-dessous :")
        fcol1, fcol2 = st.columns(2)
        st.session_state.conso = fcol1.number_input("**Consommation annuelle de Fioul (en tonnes) :**")
        st.session_state.price_hfo = fcol2.number_input("**Prix de la tonne de Fioul Lourd (monnaie locale) :**")
        country = st.selectbox("**Pays**",("-- Selectionné --","Afrique du Sud", "Côte d'Ivoire", "France","Ile Maurice", "Sénégal", "Tunisie","Autres"), )
        st.session_state.pci_hfo = st.number_input("PCI du Fioul lourd(kWh/kg) :")
        st.session_state.teneur_soufre = st.number_input("Teneur en soufre dans le fioul (%)")
        #Use OPEX Modelisation
        st.session_state.model_want = st.checkbox("Je souhaite utiliser une approximation des OPEX")
        
        if st.session_state.model_want == False : 
            st.session_state.model_use = st.checkbox("Je ne connais pas tous les coûts suivants")
           
            col1, col2 = st.columns(2)
            st.session_state.pui = col1.number_input("**Puissance de l'installation (en KW) :**")
            st.session_state.price_kWh = col2.number_input("**Coût d'un Kwh :**")
            st.session_state.nb_h_per_day = col1.number_input("**Nombre d'heures de fonctionnement de l'installation par jour :**", min_value=0, max_value=24)
            st.session_state.nb_day_per_week = col2.number_input("**Nombre de jours de fonctionnement de l'installation par semaine :**", min_value=0, max_value=7, step= 1)
            
            st.session_state.eau = st.number_input("Combien de m3 d'eau traités pour la maintenance de la chaudière :", step = 1)
            col11, col22 = st.columns(2)
            st.session_state.eau_l = col11.number_input("Coût d'un m3 d'eau traité :")
            st.session_state.eau_nb = col22.number_input("Combien de fois par an l'achat de cet eau est effectuée :")
            
            #Choice of money and estimated salary for employees
            franc_cfa = ["Côte d'Ivoire", "Sénégal"]
            euro = ["France"]
            dollar = ["Autres"]
            ZAR = ["Afrique du Sud"]
            dina_tun = ["Tunisie"]
            roupie_mauricienne =["Ile Maurice"]
            
            st.session_state.country = country
            
            if country in franc_cfa :
                st.session_state.salary = 75000
           
            elif country in euro :
                st.session_state.salary = 1539.42
            
            elif country in dollar : 
                st.session_state.salary = 1400
            
            elif country in ZAR :
                st.session_state.salary = 4058.2
            
            elif country in dina_tun :
                st.session_state.salary = 323
                
            elif country in roupie_mauricienne :
                st.session_state.salary = 22404
           
            
            if country in franc_cfa :
                st.session_state.money = " F"
           
            elif country in euro :
                st.session_state.money = " €"
            
            elif country in dollar : 
                st.session_state.money = " $"
            
            elif country in ZAR :
                st.session_state.money = " R"
            
            elif country in dina_tun :
                st.session_state.money = " DT"
                
            elif country in roupie_mauricienne :
                st.session_state.money = " MUR"
                    
                
            #Maintenance
            st.session_state.meth = st.radio("Par quel méthode effectuez-vous votre maintenance ?", ('Personnel interne', 'Prestataire','Hybride', 'Autres'))
            if st.session_state.meth == 'Personnel interne' : 
                st.session_state.nb_employee = st.number_input("**Nombre d'employés à cet usage :** ", step = 1)
                st.write("")
                st.write("")
                st.write("")
           
            elif st.session_state.meth == 'Prestataire' :
                st.session_state.presta = st.number_input("**Coût prestataire annuel :** ", step = 1)
                if st.session_state.presta == 0 :
                    st.session_state.presta_unknow = st.checkbox("**Je ne connais pas les coûts de mes prestataires**")
                    st.write("")
                    st.write("")
                    st.write("")
                    
            elif st.session_state.meth == 'Hybride' :
                st.session_state.nb_employee = st.number_input("Nombre d'employés à cet usage ?")
                st.session_state.presta = st.number_input("Coût de la maintenance effectuée par le prestataire :")
                st.session_state.cost_hfo_maint = st.session_state.salary * st.session_state.nb_employee + st.session_state.presta
                st.session_state.other_unknow = st.checkbox("**Je ne connais pas les coûts** ")
                st.write("")
                st.write("")
                st.write("")
                
                
            elif st.session_state.meth == 'Autres' : 
                st.session_state.meth_other = st.text_input("Veuillez entrer votre méthode de maintenance : ")
                st.session_state.price_other_meth = st.number_input("**Coût annuel de cette méthode :**")
                if st.session_state.price_other_meth ==0 :
                    st.session_state.other_unknow = st.checkbox("**Je ne connais pas les coûts de ma méthode**")
                    st.write("")
                    st.write("")
                    st.write("")
            
            
            #Scarpe
            st.session_state.ram = st.checkbox("Faites-vous des ramonages ?")
            if st.session_state.ram : 
                st.session_state.nb_ram = st.number_input("**Fréquence de ramonage (en mois) :**")
                st.session_state.ram_cost= st.number_input("**Coût d'un ramonage :**")
                st.write("")
                st.write("")
                st.write("")
            
            
            #Filters
            st.session_state.filter = st.checkbox("Avez-vous des filtres ?")
            if st.session_state.filter : 
                 st.session_state.nb_fil = st.number_input("**Nombre de filtres :**", step = 1)  
                 if st.session_state.nb_fil != 0 :
                     
                     df = pd.DataFrame(data = np.zeros((1,st.session_state.nb_fil)), columns = ('Filtre %d' % i for i in range(1,1 + st.session_state.nb_fil)), index = ["Taille (μm)"])
                     udf = st.data_editor(df)
                     st.write("")
                     st.write("")
                     st.write("")
            else : 
                st.session_state.coef_filtre = 0.9
            
            #Change of parts
            st.session_state.pieces = st.checkbox("Avez-vous changé des pièces durant les 10 dernières années ?")
            if st.session_state.pieces :
                st.session_state.change_pcs = st.text_input("Nom de l'équipement changé :")
                st.session_state.price_pcs = st.number_input("Prix de la pièce :")
                st.session_state.fre_chgm = st.number_input("Fréquence de changement de la pièce (en mois) :")
                st.session_state.time_int = st.number_input("Durée de l'intervenetion (en heures) :")
                st.session_state.time_prod = st.checkbox("Cette intervention a-t-elle causée un arrêt de production ?")
                st.session_state.cbx_int = st.checkbox("Cette intervention est-elle contenue dans le coût de la maintenance ?")
                
                if st.session_state.time_prod :
                    st.session_state.tp_yes_no = "Oui"
                else : 
                    st.session_state.tp_yes_no = "Non"
                    
                if st.session_state.cbx_int :
                    st.session_state.chx_maint = "Oui"
                else : 
                    st.session_state.chx_maint = "Non"


                st.session_state.but_pcs = st.button("Ajouter dans le tableau")
                
                #Put the values into a list
                if st.session_state.but_pcs :
                    st.session_state.c += [np.transpose(np.array([st.session_state.change_pcs,st.session_state.price_pcs, st.session_state.fre_chgm, st.session_state.time_int,st.session_state.tp_yes_no, st.session_state.chx_maint])).tolist()]

                    
                if len(st.session_state.c) != 0 : 
                    df1 = pd.DataFrame(data = st.session_state.c, index = ('Pièces %d' % i for i in range(1,1 + len(st.session_state.c))), columns = ["Nom de la pièce", "Prix de la pièce", "Fréquence de changement de la pièce (en mois)", "Durée de l'intervention (en heures)", "Cela empiète-t-il sur la production ?(Oui ou Non)", "Coût compris dans celui de la mainteneace "])
                    udf1 = st.data_editor(df1)
                    npdf1 = udf1.to_numpy()
                    for i in range(len(st.session_state.c)):
                        st.session_state.c[i][1] = npdf1[i,1]
                        st.session_state.c[i][2] = npdf1[i,2]
                        st.session_state.c[i][3] = npdf1[i,3]
                        st.session_state.c[i][4] = npdf1[i,4]
                        
                    #Sum of costs of changement
                    if (float(st.session_state.c[-1][2]) != 0) and (float(st.session_state.c[-1][1]) != 0) and (st.session_state.c[-1][5] == "Non"):
                        st.session_state.sum_pcs += ((float(st.session_state.c[-1][1]) * (12/float(st.session_state.c[-1][2]))))
                st.write("")
                st.write("")
                st.write("")
            
          
            #Equipment cleaning
            st.session_state.nett = st.checkbox("Faites-vous du nettoyage (Filtres, brûleurs)?")
            if st.session_state.nett :
                st.session_state.nett_meth = st.radio("Par quelle moyen nettoyez-vous votre installation ?", ('Opérateurs interne', 'Prestataire'))
                if st.session_state.nett_meth == 'Opérateurs interne':
                    st.session_state.same_empl = st.checkbox("Ces opérateurs sont-ils différents de ceux s'occupant de la maintenance ?")
                    if st.session_state.same_empl :
                        st.session_state.nb_empl2 = st.number_input("Combien d'employées sont dédiés à cette tâche ?", step = 0.1)
                        st.session_state.nett_co_emp = st.session_state.nb_empl2 * st.session_state.salary
                        st.session_state.nett_cost = st.session_state.nett_co_emp
                        
                    st.session_state.nett_eq = st.text_input("Nom de l'équipement nettoyé :")
                    st.session_state.time_int_nett = st.number_input("Durée de l'intervention (en heures)")
                    st.session_state.fre_nett = st.number_input("Fréquence des interventions (en mois)")
                    st.session_state.cbx_nett_prod = st.checkbox("Cette intervention a-t-elle causée un arrêt de production ? ")
                    
                    if st.session_state.cbx_nett_prod :
                        st.session_state.nett_yn = "Oui"
                    else : 
                        st.session_state.nett_yn = "Non"
                    
                    
                    st.session_state.but_nett = st.button("Ajouter dans le tableau ")
                    
                    if st.session_state.but_nett :
                        st.session_state.ne += [np.transpose(np.array([st.session_state.nett_eq,st.session_state.time_int_nett,st.session_state.fre_nett,st.session_state.nett_yn]))]
                        
                    if len(st.session_state.ne) != 0 : 
                        df2 = pd.DataFrame(data = st.session_state.ne, index = ('Equipement %d' % i for i in range(1,1 + len(st.session_state.ne))), columns = ["Nom de l'équipement", "Durée de l'intervention (en heures)", "Fréquence des interventions (en mois)", "Cela empiète-t-il sur la production ?(Oui/Non)"])
                        udf2 = st.data_editor(df2)
                        npdf2 = udf2.to_numpy()
                        for i in range(len(st.session_state.ne)):
                            st.session_state.ne[i][1] = npdf2[i,1]
                            st.session_state.ne[i][2] = npdf2[i,2]
                            st.session_state.ne[i][3] = npdf2[i,3]
                        
                        #Time of Production Downtime
                        if (float(st.session_state.ne[-1][2]) != 0) and (float(st.session_state.ne[-1][1]) != 0) and (st.session_state.ne[-1][3] == 'Oui'):
                            st.session_state.sum_nett += (float(st.session_state.ne[-1][1]) * (12/ float(st.session_state.ne[-1][2])))
                         
                st.write("")
                st.write("")
                st.write("")
                
            
            if st.session_state.nett_meth == 'Prestataire' :
                st.session_state.nett_presta = st.number_input("Coût annuel du prestataire lié au nettoyage des équipements :")
                st.session_state.nett_cost = st.session_state.nett_presta
                
                st.session_state.nett_eq = st.text_input("Nom de l'équipement nettoyé :")
                st.session_state.time_int_nett_presta = st.number_input("Durée de l'intervention (en heures)")
                st.session_state.fre_nett_presta = st.number_input("Fréquence des interventions (en mois)")
                st.session_state.cbx_nett_presta = st.checkbox(" Cette intervention a-t-elle causée un arrêt de production ? ")
                
                if st.session_state.cbx_nett_presta :
                    st.session_state.nett_yn_presta = "Oui"
                else : 
                    st.session_state.nett_yn_presta = "Non"
                
                st.session_state.but_nett = st.button("Ajouter dans le tableau ")
                
                if st.session_state.but_nett :
                    st.session_state.ne += [np.transpose(np.array([st.session_state.nett_eq,st.session_state.time_int_nett_presta,st.session_state.fre_nett_presta,st.session_state.nett_yn_presta]))]
                    
                if len(st.session_state.ne) != 0 : 
                    df2 = pd.DataFrame(data = st.session_state.ne, index = ('Equipement %d' % i for i in range(1,1 + len(st.session_state.ne))), columns = ["Nom de l'équipement", "Durée de l'intervention (en heures)", "Fréquence des interventions (en mois)", "Cela empiète-t-il sur la production ?(Oui/Non)"])
                    udf2 = st.data_editor(df2)
                    npdf2 = udf2.to_numpy()
                    for i in range(len(st.session_state.ne)):
                        st.session_state.ne[i][1] = npdf2[i,1]
                        st.session_state.ne[i][2] = npdf2[i,2]
                        st.session_state.ne[i][3] = npdf2[i,3]

                    #Time of Production Downtime
                    if (float(st.session_state.ne[-1][2]) != 0) and (float(st.session_state.ne[-1][1]) != 0) and (st.session_state.ne[-1][3] == 'Oui'):
                        st.session_state.sum_nett += (float(st.session_state.ne[-1][1]) * (12/ float(st.session_state.ne[-1][2])))
                     
                st.write("")
                st.write("")
                st.write("")
            
            #Additives
            st.session_state.additif = st.checkbox("Utilisez-vous des additifs ?")
            if st.session_state.additif:
                st.session_state.name_add = st.text_input("Nom de l'additif :")
                st.session_state.cost_add = st.number_input("Coût d'un litre d'additif :")
                st.session_state.cons_add = st.number_input("Consommation annuelle de cet additif :")
                st.session_state.but_add = st.button("Ajouter dans le tableau  ")
                
                if st.session_state.but_add :
                    st.session_state.add += [np.transpose(np.array([st.session_state.name_add,st.session_state.cost_add,st.session_state.cons_add]))]
               
                if len(st.session_state.add) != 0 : 
                    df_add = pd.DataFrame(data = st.session_state.add, index = ('Additif %d' % i for i in range(1,1 + len(st.session_state.add))), columns = ["Nom de l'additif", "Coût d'un litre d'additif", "Consommation annuelle de cet additif"])
                    udf_add = st.data_editor(df_add)
                    npdf_add = udf_add.to_numpy()
                    for i in range(len(st.session_state.add)):
                        st.session_state.add[i][1] = npdf_add[i,1]
                        st.session_state.add[i][2] = npdf_add[i,2]
                        
                    #Cost of additives
                    if (float(st.session_state.add[-1][2]) != 0) and (float(st.session_state.add[-1][1]) != 0) :
                        st.session_state.sum_add += (float(st.session_state.add[-1][1]) * (float(st.session_state.add[-1][2])))

                st.write("")
                st.write("")
                st.write("")
            
            #Number Boilers for Production Stoppages
            st.session_state.chaud = st.checkbox("Possédez-vous plusieurs chaudières ?")
            if st.session_state.chaud : 
                st.session_state.nb_chaud = st.number_input("Combien en possédez-vous ?", step = 1)
                st.write("")
                st.write("")
                st.write("")
                
                
            #Possession of an Economizer
            st.session_state.eco = st.checkbox("Possédez-vous un économiseur ?")  
                            
        else :
            if st.session_state.conso != 0:
                #Using OPEX Modelisation
                st.session_state.hfo_model_cost_opex = round(st.session_state.conso * 230.73/((st.session_state.conso/12)**0.264))
            else : 
                #HFO Consumption needs  to calculate OPEX 
                st.write("Veuillez renseigner votre consommation de fioul")
                
    #HFO Page           
    if st.session_state.choose == "HFO" : 
        if st.session_state.conso != 0:
            #Using OPEX Modelisation
            if st.session_state.model_use :
                st.session_state.hfo_model_cost_opex = round(st.session_state.conso * 230.73/((st.session_state.conso/12)**0.264))
            
            #Calculate the energy of HFO
            en_hfo = round(st.session_state.conso * st.session_state.pci_hfo*1000)
            #Save the value to convert in GJ
            st.session_state.en_hfo_GJ = en_hfo
            
            #Calculate the cost of HFO
            cost_hfo = round(st.session_state.conso * st.session_state.price_hfo)
            #Calculate the cost of energy
            cost_en = round(st.session_state.price_kWh * st.session_state.pui * st.session_state.nb_h_per_day * st.session_state.nb_day_per_week*52.1429)
            
            if st.session_state.meth == 'Prestataire' and st.session_state.presta != 0:
                st.session_state.cost_hfo_maint = round(st.session_state.presta)  
            elif st.session_state.meth == 'Personnel interne':
                st.session_state.cost_hfo_maint = round(st.session_state.nb_employee * st.session_state.salary)
            elif st.session_state.meth == 'Autres' and st.session_state.price_other_meth != 0:
                st.session_state.cost_hfo_maint = round(st.session_state.price_other_meth)
            elif ((st.session_state.meth == 'Autres' and st.session_state.other_unknow == True and st.session_state.price_other_meth == 0)or (st.session_state.meth == 'Prestataire' and st.session_state.presta_unknow == True and st.session_state.presta == 0)):
                if st.session_state.money == " €":
                    st.session_state.cost_hfo_maint = round(2.19 * st.session_state.conso)
                elif st.session_state.money == " $":
                    st.session_state.cost_hfo_maint = round(euro_to_dollar(2.19) * st.session_state.conso)
                elif st.session_state.money == " F":
                    st.session_state.cost_hfo_maint = round(dollar_to_CFA(euro_to_dollar(2.19)) * st.session_state.conso)
                elif st.session_state.money == " R":
                    st.session_state.cost_hfo_maint = round(dollar_to_ZAR(euro_to_dollar(2.19)) * st.session_state.conso)
                elif st.session_state.money == " DT":
                    st.session_state.cost_hfo_maint = round(dollar_to_din_tun(euro_to_dollar(2.19)) * st.session_state.conso)
                elif st.session_state.money == " MUR":
                    st.session_state.cost_hfo_maint = round(dollar_to_mur(euro_to_dollar(2.19)) * st.session_state.conso)
                    
            #Display only the HFO cost and OPEX
            if st.session_state.model_want : 
                c1, c2 = st.columns(2)
                c1.metric("Voici le coût de la molécule HFO :", space_in_numbers(str(round(cost_hfo))) + st.session_state.money)
                c2.metric("Voici le coût des OPEX de l'installation :", space_in_numbers(str(round(st.session_state.hfo_model_cost_opex))) + st.session_state.money)
           
            #Display all parts of OPEX
            else :
                c1, c2, c3 = st.columns(3)
                c1.metric("Voici le coût de la molécule HFO :", space_in_numbers(str(round(cost_hfo))) + st.session_state.money)
                c2.metric("Voici le coût énergétique lié au HFO :", space_in_numbers(str(round(cost_en))) + st.session_state.money)
                c3.metric("Coût annuel moyen lié à la maintenance du site :", space_in_numbers(str(round(st.session_state.cost_hfo_maint))) + st.session_state.money)
                
                        
                if st.session_state.eau !=0:
                    c2.metric("Coût annuel global de l'eau traitée :", space_in_numbers(str(round(st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb))) + st.session_state.money)
                else :
                    c2.metric("Coût annuel global de l'eau traitée :", str(0) + st.session_state.money)
               
                
                if st.session_state.ram :
                    c1.metric("Coût annuel lié aux ramonages :", space_in_numbers(str(round(st.session_state.ram_cost * (st.session_state.nb_ram/12)))) + st.session_state.money)
                else :
                    c1.metric("Coût annuel lié aux ramonages :", str(0) + st.session_state.money)
                
                
                if len(st.session_state.c) != 0:
                    c3.metric("Coût total lié au changement de pièce :", space_in_numbers(str(round(st.session_state.sum_pcs))) + st.session_state.money)
                else :
                    c3.metric("Coût total lié au changement de pièce :", str(0) + st.session_state.money)
                
                
                if st.session_state.nett :
                    c1.metric("Coût total lié au nettoyage du site", space_in_numbers(str(round(st.session_state.nett_cost))) + st.session_state.money)
                    
                    if st.session_state.sum_nett != 0:
                        c2.metric("Temps de production perdu :", space_in_numbers(str(round(st.session_state.sum_nett)))+" heures")
                
                else:
                    c1.metric("Coût total lié au nettoyage du site", str(0) + st.session_state.money)
                    c2.metric("Temps de production perdu :", str(0)+" heures")
                
                if st.session_state.sum_add != 0 :
                    c3.metric("Coût total des additifs", space_in_numbers(str(round(st.session_state.sum_add))) + st.session_state.money)
                else : 
                    c3.metric("Coût total des additifs", str(0) + st.session_state.money)
               

               
                
            #Summarize with total cost
            st.divider()
            col1, col2 = st.columns([2,1.5])
            st.subheader("Coût annuel total de fonctionnement de votre installation HFO : ")
            if st.session_state.hfo_model_cost_opex < (cost_en + st.session_state.cost_hfo_maint + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram)) :
                st.title(space_in_numbers(str(round(cost_hfo + cost_en + st.session_state.cost_hfo_maint + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram)))) + st.session_state.money)
            else :
                st.title(space_in_numbers(str(cost_hfo + st.session_state.hfo_model_cost_opex))+ st.session_state.money)
            
            st.subheader("Coût global d'une tonne de HFO : ")
            if st.session_state.hfo_model_cost_opex < (cost_en + st.session_state.cost_hfo_maint + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram)) :
                st.session_state.tot_cost_hfo = round(cost_hfo + cost_en + st.session_state.cost_hfo_maint + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * (st.session_state.nb_ram/st.session_state.conso)))
                st.title(space_in_numbers(str(round(st.session_state.tot_cost_hfo/st.session_state.conso))) + st.session_state.money)
                st.divider()
                st.write("")
                st.write("")
                st.write("")
            else : 
                st.session_state.tot_cost_hfo = round(st.session_state.hfo_model_cost_opex + cost_hfo)
                st.title(space_in_numbers(str(round((st.session_state.tot_cost_hfo + st.session_state.hfo_model_cost_opex)/st.session_state.conso))) + st.session_state.money)
                st.divider()
                st.write("")
                st.write("")
                st.write("")
            
            #Show the distribution in OPEX
            if cost_en != 0 or st.session_state.cost_hfo_maint != 0 or st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb != 0 or st.session_state.ram_cost * st.session_state.nb_ram != 0 or st.session_state.sum_pcs != 0 or st.session_state.nett_cost != 0 or st.session_state.sum_add != 0 :
                cost_list = np.array([cost_en,st.session_state.cost_hfo_maint, st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb, st.session_state.ram_cost * st.session_state.nb_ram, st.session_state.sum_pcs, st.session_state.nett_cost, st.session_state.sum_add])
                data_chart=[]
                for i in range(8):
                    data_chart +=  [cost_list* (1.003**i) ]
                
                chart_data_hfo = pd.DataFrame(data= data_chart, columns = ["Coût énergétique", "Coût maintenance du site", "Coût de l'eau","Coût ramonages", "Coût pièces", "Coût nettoyages", "Coût additifs"])
                st.bar_chart(chart_data_hfo)
                
            #Pie chart to put in evidence the part of OPEX by using HFO
            if st.session_state.model_want or (st.session_state.hfo_model_cost_opex > (cost_en + st.session_state.cost_hfo_maint + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram))):
                df_pie = pd.DataFrame(data = np.array([[cost_hfo, "Molécule"],[st.session_state.hfo_model_cost_opex, "OPEX"]]), index=["Coût de la molécule", "Coût des OPEX"], columns = ["Coût", "Coût associé"])
                fig = px.pie(df_pie, values= 'Coût', names = 'Coût associé')
                tab, pie = st.columns(2)
                with tab:
                    st.write(df_pie)
                with pie:
                    st.write(fig)
            else :
                df_pie = pd.DataFrame(data = np.array([[cost_hfo, "Molécule"],[cost_en, "Energie"],[(st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb),"Eau"],[st.session_state.cost_hfo_maint,"Maintenance"],[(st.session_state.ram_cost * st.session_state.nb_ram),"Ramonage"],[st.session_state.sum_pcs,"Pièces"], [st.session_state.nett_cost, "Nettoyage"], [st.session_state.sum_add,"Additif"]]), index=["Coût de la molécule", "Coût de l'énergie","Coût de l'eau", "Coût de la maintenance","Coût des ramonages","Coût des pièces","Coût du nettoyage", "Coût des additifs"], columns = ["Coût", "Coût associé"])
                fig = px.pie(df_pie, values= 'Coût', names = 'Coût associé')
                tab, pie = st.columns(2)
                with tab:
                    st.write(df_pie)
                with pie:
                    st.write(fig)
                
            #List the disadvantages of HFO 
            with st.expander("Inconvénients liés au HFO"):
                c1,c2 = st.columns(2)
                with c1:
                    st.write(" -  Emissions de particules, fumées noires et haute teneur en soufre")
                    st.write(" -  Filtres nécessaires pour éviter d'augmenter les pertes de rendement et d'endommager les buses et les pompes")
                    st.write(" -  Le ramonge récurrent (tous les trimestres) est nécessaire")
                    st.write(" -  Corrosion de nombreux équipements (fond de cuve, boucle de chauffage,...)")
                    st.write(" -  Pompage et manipulation difficile avant le stockage")
                    st.write(" -  Mauvaise pulvérisation")
                    st.write(" -  Haute teneur en eau")
                    st.write(" -  Abrasiion sur les moteurs de type 'Marin'")
                    st.write(" -  Résidus de carbone")
                    st.write(" -  Risque de fissuration de la chambre de combustion")
                    st.write(" -  Point d'écoulement trop élevé")
                    st.write(" -  PCI faible")
                    
                with c2:
                    st.write(" -  Colmatage des équipements (tuyaux, filtres, bols de centrifugeuse,...)")
                    st.write(" -  Pertes de rendement dues à l'obstruction des canalisations")
                    st.write(" -  Cavitation des pompes")
                    st.write(" -  Mauvaise centrifugation")
                    st.write(" -  Viscosité inadaptée")
                    st.write(" -  Difficultés de pompage")
                    st.write(" -  Risques élevés d'incendie et d'explosion")
                    st.write(" -  Haute teneur en cendres ((Al et Si), (Ca et Zn))")
                    st.write(" -  Haute teneur en sédiments/ Précipitation d'asphaltènes")
                    st.write(" -  CCAI trop élevé")
                    st.write(" -  Point éclair trop bas")
                    st.write(" -  Problèmes de voisinages")
                
        else :
            #Demand to complete the Home page information
            st.write("Veuillez renseigner les informations de la page d'accueil ")
            
    
    #GPL Page
    if st.session_state.choose == "GPL" : 
        if st.session_state.conso != 0 :
            #Definition of an efficiency coefficient as a function of the number of chimney sweeps
            if (st.session_state.nb_ram == 0) or (st.session_state.ram == False) or (st.session_state.nb_ram > 18):
                st.session_state.rend_ram = 0.85
                
            elif (st.session_state.nb_ram >0)  or (st.session_state.nb_ram < 6):
                st.session_state.rend_ram = 0.935
            
            elif (st.session_state.nb_ram >5)  or (st.session_state.nb_ram < 18):
                st.session_state.rend_ram = 0.9
            
            #Definition of a coefficient to model the best combustion of LPG
            rend_rand = st.session_state.rand_gpl
            coeff_rand = (100-rend_rand)/100
            
            
            #Range of GPL price
            if st.session_state.money == " €":
                st.session_state.max_gpl_price = 2000
                st.session_state.base_gpl_price = 500
                
            #Choose money
            elif st.session_state.money == " $":
                st.session_state.max_gpl_price = round(euro_to_dollar(st.session_state.max_gpl_price))
                st.session_state.base_gpl_price = round(euro_to_dollar(st.session_state.base_gpl_price))
            elif st.session_state.money == " F":
                st.session_state.max_gpl_price = round(dollar_to_CFA(euro_to_dollar(st.session_state.max_gpl_price)))
                st.session_state.base_gpl_price = round(dollar_to_CFA(euro_to_dollar(st.session_state.base_gpl_price)))
            elif st.session_state.money == " R":
                st.session_state.max_gpl_price = round(dollar_to_ZAR(euro_to_dollar(st.session_state.max_gpl_price)))
                st.session_state.base_gpl_price = round(dollar_to_ZAR(euro_to_dollar(st.session_state.base_gpl_price)))
            elif st.session_state.money == " DT":
                st.session_state.max_gpl_price = round(dollar_to_din_tun(euro_to_dollar(st.session_state.max_gpl_price)))
                st.session_state.base_gpl_price = round(dollar_to_din_tun(euro_to_dollar(st.session_state.base_gpl_price)))
            elif st.session_state.money == " MUR":
                st.session_state.max_gpl_price = round(dollar_to_mur(euro_to_dollar(st.session_state.max_gpl_price)))
                st.session_state.base_gpl_price = round(dollar_to_mur(euro_to_dollar(st.session_state.base_gpl_price)))
            
            #Choice of GPL price
            st.session_state.gpl_price = st.slider("Prix de la tonne de GPL :", 0,st.session_state.max_gpl_price , st.session_state.base_gpl_price)
            #Estimate the equivalent GPL quantity
            quantity_gpl = round(st.session_state.coef_filtre * st.session_state.rend_ram * 0.96 *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800)))
            
            st.subheader("Pour la même quantité d'énergie, voici la consommation de GPL équivalente :")
            st.title(space_in_numbers(str(quantity_gpl))+" tonnes")
            #Calculate the cost of GPL
            cost_gpl = quantity_gpl * st.session_state.gpl_price
            st.subheader("Pour la même quantité d'énergie, voici le coût de la molécule GPL :")
            st.title(space_in_numbers(str(cost_gpl)) + st.session_state.money)
            
            
            #Estimate the cost of a GPL installation maintenance
            st.session_state.gpl_maint_choice = st.radio("Par quelle méthode effectuez-vous votre maintenance ?", ('Personnel interne', 'Prestataire','Hybride', 'Autres'))
            if st.session_state.gpl_maint_choice == 'Personnel interne' : 
                st.session_state.gpl_nb_empl = st.number_input("**Nombre d'employés à cet usage :** ", step = 1)
                st.session_state.gpl_cost_maint = st.session_state.salary * st.session_state.gpl_nb_empl
                if st.session_state.gpl_cost_maint :
                    st.session_state.hum_area = st.checkbox("Le site est-il situé dans un milieu humide ?")
                    if st.session_state.hum_area :
                        st.session_state.gpl_cost_maint = 5000
                    else : 
                        st.session_state.gpl_cost_maint = 1000
                        
                st.write("")
                st.write("")
                st.write("")
           
            elif st.session_state.gpl_maint_choice == 'Prestataire' :
                st.session_state.gpl_presta = st.number_input("**Coût prestataire annuel :** ", step = 1)
                st.session_state.gpl_cost_maint = st.session_state.gpl_presta
                if st.session_state.gpl_presta == 0 :
                    st.session_state.gpl_presta_unknow = st.checkbox("**Je ne connais pas les coûts de mes prestataires**")
                    if st.session_state.gpl_presta_unknow :
                        st.session_state.hum_area = st.checkbox("Le site est-il situé dans un milieu humide ?")
                        if st.session_state.hum_area :
                            st.session_state.gpl_cost_maint = 5000
                        else : 
                            st.session_state.gpl_cost_maint = 1000
                    st.write("")
                    st.write("")
                    st.write("")
                  
                    
            elif st.session_state.gpl_maint_choice == 'Hybride' :
                st.session_state.hybrid_empl = st.number_input("Nombre d'employés à cet usage ?")
                st.session_state.hybrid_presta = st.number_input("Coût de la maintenance effectuée par le prestataire :")
                st.session_state.gpl_cost_maint = st.session_state.salary * st.session_state.hybrid_empl + st.session_state.hybrid_presta
                st.session_state.hyb_dk = st.checkbox("Je ne connais pas ces coûts")
                if st.session_state.hyb_dk :
                    st.session_state.hum_area = st.checkbox("Le site est-il situé dans un milieu humide ?")
                    if st.session_state.hum_area :
                        st.session_state.gpl_cost_maint = 5000
                    else : 
                        st.session_state.gpl_cost_maint = 1000
                        
           
            elif st.session_state.gpl_maint_choice == 'Autres' : 
                st.session_state.meth_other = st.text_input("Veuillez entrer votre méthode de maintenance : ")
                st.session_state.price_other_meth = st.number_input("**Coût annuel de cette méthode :**")
                st.session_state.gpl_cost_maint = st.session_state.price_other_meth 
                if st.session_state.price_other_meth ==0 :
                    st.session_state.other_unknow = st.checkbox("**Je ne connais pas les coûts de ma méthode**")
                    if st.session_state.other_unknow :
                        st.session_state.hum_area = st.checkbox("Le site est-il situé dans un milieu humide ?")
                        if st.session_state.hum_area :
                            st.session_state.gpl_cost_maint = 5000
                        else : 
                            st.session_state.gpl_cost_maint = 1000
                    st.write("")
                    st.write("")
                    st.write("")
           
            #Investment to change to GPL
            st.session_state.inv_yes = st.checkbox("Prendre en compte l'investissement pour transitionner")
            if st.session_state.inv_yes :
                st.session_state.investment_gpl = st.radio("Quelle est la méthode d'investissement privilégiée ?", ('Investissement client','Investssement TotalEnergies', 'Hybride', 'Autres'))
                if st.session_state.investment_gpl == "Investissement client" : 
                    st.session_state.cost_investment = st.number_input("Coût d'investissement estimé pour passer du HFO au GPL")
                    st.session_state.duration_investment = st.number_input("Durée de l'amortissement de l'investissement (en année)")
                    st.session_state.invest_details = st.checkbox("Détailler les coûts d'investissement")
                    if st.session_state.invest_details :
                        st.session_state.name_gpl_inv = st.text_input("Nom de l'équipement")
                        st.session_state.cost_eq_gpl_inv = st.number_input("Coût de cet équipement")
                        st.session_state.nb_eq_gpl_inv = st.number_input("Nombre nécessaire de cet équipement", step = 1)
                        st.session_state.but_gpl_inv = st.button("Ajouter dans le tableau   ")
                        
                        if st.session_state.but_gpl_inv :
                            st.session_state.inv_det += [np.transpose(np.array([st.session_state.name_gpl_inv,st.session_state.cost_eq_gpl_inv,st.session_state.nb_eq_gpl_inv]))]
                       
                        if len(st.session_state.inv_det) != 0 : 
                            df_inv = pd.DataFrame(data = st.session_state.inv_det, index = ('Equipement %d' % i for i in range(1,1 + len(st.session_state.inv_det))), columns = ["Nom de l'équipement", "Coût de cet équipement", "Nombre nécessaire de cet équipement"])
                            udf_inv = st.data_editor(df_inv)
                            npdf_inv = udf_inv.to_numpy()
                            for i in range(len(st.session_state.inv_det)):
                                st.session_state.inv_det[i][1] = npdf_inv[i,1]
                                st.session_state.inv_det[i][2] = npdf_inv[i,2]
                   
                    if st.session_state.duration_investment != 0:            
                        st.session_state.cost_inv_year = st.session_state.cost_investment / st.session_state.duration_investment
                    
                if st.session_state.investment_gpl == "Investssement TotalEnergies" : 
                    st.session_state.cost_inv_year = 0
                    
                if st.session_state.investment_gpl == "Hybride" :
                    st.session_state.cost_investment = st.number_input("Coût d'investissement du client estimé pour passer du HFO au GPL")
                    st.session_state.duration_investment = st.number_input("Durée de l'amortissement de l'investissement du client(en année)")
                    st.session_state.invest_details = st.checkbox("Détailler les coûts d'investissement")
                    if st.session_state.invest_details :
                        st.session_state.name_gpl_inv = st.text_input("Nom de l'équipement")
                        st.session_state.cost_eq_gpl_inv = st.number_input("Coût de cet équipement pris en charge par le client")
                        st.session_state.nb_eq_gpl_inv = st.number_input("Nombre nécessaire de cet équipement", step = 1)
                        st.session_state.but_gpl_inv = st.button("Ajouter dans le tableau    ")
                        
                        if st.session_state.but_gpl_inv :
                            st.session_state.inv_det += [np.transpose(np.array([st.session_state.name_gpl_inv,st.session_state.cost_eq_gpl_inv,st.session_state.nb_eq_gpl_inv]))]
                       
                        if len(st.session_state.inv_det) != 0 : 
                            df_inv = pd.DataFrame(data = st.session_state.inv_det, index = ('Equipement %d' % i for i in range(1,1 + len(st.session_state.inv_det))), columns = ["Nom de l'équipement", "Coût de cet équipement", "Nombre nécessaire de cet équipement"])
                            udf_inv = st.data_editor(df_inv)
                            npdf_inv = udf_inv.to_numpy()
                            for i in range(len(st.session_state.inv_det)):
                                st.session_state.inv_det[i][1] = npdf_inv[i,1]
                                st.session_state.inv_det[i][2] = npdf_inv[i,2]
                        
                        if st.session_state.duration_investment != 0:
                            st.session_state.cost_inv_year = st.session_state.cost_investment / st.session_state.duration_investment
                        
                        st.session_state.cost_investment_totalen = st.number_input("Coût d'investissement pris en charge par TotalEnergies")
                        
                    
            
            #Bar chart to compare directly GPL and HFO total cost     
            st.subheader("Comparaison coût annuel GPL vs HFO (hors coût d'investissement)")
            st.bar_chart({"GPL": cost_gpl + st.session_state.gpl_cost_maint,"HFO" : st.session_state.tot_cost_hfo})
            st.session_state.tot_cost_gpl = cost_gpl + st.session_state.gpl_cost_maint


            #Visualize the evolution of cost during time (Random evolution)
            #Same evolution
            st.subheader("Comparaison coût annuel GPL vs HFO sur 10 ans (coût d'investissement compris)")
            data_line1 = []
            data_line_gpl =[]
            data_line_hfo =[]
            data_line_hfo += [st.session_state.tot_cost_hfo]
            data_line_gpl += [cost_gpl + st.session_state.gpl_cost_maint +  st.session_state.cost_inv_year]
            
            for i in range(10) : 
                pos_neg = np.random.randint(0,3)
                rand_prog = np.random.randint(0,11)
                if pos_neg == 0 : 
                    coeff_prog = (100 - rand_prog)/100
                    data_line_gpl += [(data_line_gpl[-1])* coeff_prog]
                    data_line_hfo += [(data_line_hfo[-1])* coeff_prog]
                else :
                    coeff_prog = (100 + rand_prog)/100
                    data_line_gpl += [(data_line_gpl[-1])* coeff_prog]
                    data_line_hfo += [(data_line_hfo[-1])* coeff_prog]
            
            data_line1=np.array([data_line_gpl,data_line_hfo]).T
            df_data_line1= pd.DataFrame(data_line1, columns=["GPL","HFO"])
            st.line_chart(df_data_line1)
            
            #Different evolutions
            data_line2 = []
            data_line_gpl2 =[]
            data_line_hfo2 =[]
            data_line_hfo2 += [st.session_state.tot_cost_hfo]
            data_line_gpl2 += [cost_gpl + st.session_state.gpl_cost_maint +  st.session_state.cost_inv_year]
            
            for i in range(10) : 
                pos_neg = np.random.randint(0,3)
                rand_prog = np.random.randint(0,11)
                if pos_neg == 0 : 
                    coeff_prog = (100 - rand_prog)/100
                    data_line_gpl2 += [(data_line_gpl2[-1])* coeff_prog]
                else :
                    coeff_prog = (100 + rand_prog)/100
                    data_line_gpl2 += [(data_line_gpl2[-1])* coeff_prog]
            
            for i in range(10) : 
                pos_neg = np.random.randint(0,3)
                rand_prog = np.random.randint(0,11)
                if pos_neg == 0 : 
                    coeff_prog = (100 - rand_prog)/100
                    data_line_hfo2 += [(data_line_hfo2[-1])* coeff_prog]
                else :
                    coeff_prog = (100 + rand_prog)/100
                    data_line_hfo2 += [(data_line_hfo2[-1])* coeff_prog]
                    
            data_line2=np.array([data_line_gpl2,data_line_hfo2]).T
            df_data_line2= pd.DataFrame(data_line2, columns=["GPL","HFO"])
            st.line_chart(df_data_line2)
            
        else :
            #Demand to complete the Home page information
            st.write("Veuillez renseigner votre consommation ")
            
            
    #Comparison Page       
    if st.session_state.choose == "Comparaison" : 
        #Comparison of costs and emissions
        st.title("Comparaison des énergies")
        col1, col2 = st.columns(2)
        with col1 :
            st.title("HFO")
            st.metric("Coûts totaux du HFO", value = space_in_numbers(str(st.session_state.tot_cost_hfo))+ st.session_state.money)
            st.write("")
            st.metric("Coût de la molécule", value = space_in_numbers(str(round(st.session_state.conso * st.session_state.price_hfo))) + st.session_state.money)
            st.write("")
            if st.session_state.hfo_model_cost_opex < (st.session_state.cost_hfo_maint + round(st.session_state.price_kWh * st.session_state.pui * st.session_state.nb_h_per_day * st.session_state.nb_day_per_week*52.1429)
            + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram)) :
                st.metric("Coûts des OPEX",value = space_in_numbers(str(round( st.session_state.cost_hfo_maint + round(st.session_state.price_kWh * st.session_state.pui * st.session_state.nb_h_per_day * st.session_state.nb_day_per_week*52.1429)
                + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram)))) + st.session_state.money)
            else :
                st.metric("Coût des OPEX", value = space_in_numbers(str(st.session_state.hfo_model_cost_opex))+ st.session_state.money)   
            st.write("")
            st.write("")
            st.metric("Facteur d'émissions de CO2", value = space_in_numbers(str(round(3.12 * st.session_state.conso))) + " tonnes")
            st.write("")
            st.metric("Concentration de SOx dans les fumées", value = space_in_numbers(str(round(1700 * st.session_state.teneur_soufre))) + " mg/Nm3")
            st.write("")
            st.metric("Facteur d'émissions de NOx", value = space_in_numbers(str(round(0.0036*st.session_state.en_hfo_GJ*1967/1000))) + " kg")
            st.write("")
            st.write("")
            st.metric("Facteur d'émissions de CO", value = space_in_numbers(str(round(0.0036*st.session_state.en_hfo_GJ*92/1000))) + " kg")
       
        with col2 :
            st.title("GPL")
            st.metric("Coûts totaux du GPL", value = space_in_numbers(str(round(st.session_state.gpl_cost_maint + st.session_state.gpl_price * (st.session_state.coef_filtre * st.session_state.rend_ram * 0.96 *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800)))))) + st.session_state.money, delta = space_in_numbers(str(round((st.session_state.gpl_cost_maint + st.session_state.gpl_price * (st.session_state.coef_filtre * st.session_state.rend_ram * 0.96 *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800)))) - st.session_state.tot_cost_hfo )))+ st.session_state.money, delta_color= "inverse")
            st.metric("Coût de la molécule", value = space_in_numbers(str(round(st.session_state.gpl_price * (st.session_state.coef_filtre * st.session_state.rend_ram * 0.96 *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800)))))) + st.session_state.money, delta = space_in_numbers(str(round((st.session_state.gpl_price * (st.session_state.coef_filtre * st.session_state.rend_ram * 0.96 *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800))))- st.session_state.conso * st.session_state.price_hfo))) + st.session_state.money, delta_color= "inverse")
            
            if st.session_state.model_want or (st.session_state.hfo_model_cost_opex > ((st.session_state.price_kWh * st.session_state.pui * st.session_state.nb_h_per_day * st.session_state.nb_day_per_week*52.1429) + st.session_state.cost_hfo_maint + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram))):
                st.metric("Coût des OPEX", value = space_in_numbers(str(round(st.session_state.gpl_cost_maint)))+ st.session_state.money, delta = space_in_numbers(str(round((st.session_state.gpl_cost_maint)- st.session_state.hfo_model_cost_opex))) + st.session_state.money,  delta_color= "inverse") 
            else:
                st.metric("Coût des OPEX", value = space_in_numbers(str(round(st.session_state.gpl_cost_maint)))+ st.session_state.money, delta = space_in_numbers(str(round((st.session_state.gpl_cost_maint)- ((st.session_state.price_kWh * st.session_state.pui * st.session_state.nb_h_per_day * st.session_state.nb_day_per_week*52.1429) + st.session_state.cost_hfo_maint + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram))))) + st.session_state.money,  delta_color= "inverse") 
           
            st.metric("Facteur d'émissions de CO2", value = space_in_numbers(str(round(63.1 * st.session_state.en_hfo_GJ * 0.0036/1000))) +" tonnes", delta = space_in_numbers(str(round((63.1 * st.session_state.en_hfo_GJ * 0.0036/1000)-(3.12 * st.session_state.conso)))) + " tonnes", delta_color= "inverse")
            st.metric("Concentration de SOx dans les fumées", value = str(325) + " mg/Nm3", delta = str(round((2.2 *0.0036*st.session_state.en_hfo_GJ/1000)-(1700 * st.session_state.teneur_soufre)))+ " mg/Nm3", delta_color= "inverse")
            st.metric("Facteur d'émissions de NOx", value = space_in_numbers(str(round(0.0036*st.session_state.en_hfo_GJ*60/1000)))+ " kg", delta = space_in_numbers(str(round((0.0036*st.session_state.en_hfo_GJ*60/1000)-(0.0036*st.session_state.en_hfo_GJ*1967/1000))))+ " kg", delta_color= "inverse")
            st.metric("Facteur d'émissions de CO", value = space_in_numbers(str(round(0.5*0.0036*st.session_state.en_hfo_GJ*92/1000)))+ " kg", delta = space_in_numbers(str(round((0.5*0.0036*st.session_state.en_hfo_GJ*92/1000)-(0.0036*st.session_state.en_hfo_GJ*92/1000))))+" kg", delta_color= "inverse")
            
        #Save data to create an Excel File
        if st.session_state.hfo_model_cost_opex < (st.session_state.cost_hfo_maint + round(st.session_state.price_kWh * st.session_state.pui * st.session_state.nb_h_per_day * st.session_state.nb_day_per_week*52.1429)
        + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram)) :
            data_excel = {'Pays' : st.session_state.country,
                      'Consommation HFO' : st.session_state.conso,
                      'Prix de la tonne de HFO' : st.session_state.price_hfo,
                      'PCI HFO' : st.session_state.pci_hfo,
                      'Teneur en soufre' : st.session_state.teneur_soufre,
                      'Coût molécule' : st.session_state.conso*st.session_state.price_hfo,
                      'Coût des OPEX' : st.session_state.hfo_model_cost_opex,
                      "Coût global d'une molécule de HFO" : ((st.session_state.conso*st.session_state.price_hfo)+ st.session_state.hfo_model_cost_opex)/st.session_state.conso,
                      'Consommation estimée de GPL': (st.session_state.coef_filtre * st.session_state.rend_ram * 0.96 *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800))),
                      'Coût du GPL' : (st.session_state.coef_filtre * st.session_state.rend_ram * 0.96 *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800)) *st.session_state.gpl_price),
                      'Coût maintenance GPL' : st.session_state.gpl_cost_maint,
                      "Coût global d'une molécule de GPL" : ((st.session_state.coef_filtre * st.session_state.rend_ram * coeff_rand *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800)) *st.session_state.price_gpl)+st.session_state.gpl_cost_maint)/((st.session_state.coef_filtre * st.session_state.rend_ram * coeff_rand *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800)))),
                      }
        
        else :
              
            data_excel = {'Pays' : [st.session_state.country],
                      'Consommation HFO' : [st.session_state.conso],
                      'Prix de la tonne de HFO' : [st.session_state.price_hfo],
                      'PCI HFO' : [st.session_state.pci_hfo],
                      'Teneur en soufre' : [st.session_state.teneur_soufre],
                      'Coût molécule' : [st.session_state.conso*st.session_state.price_hfo],
                      'Coût des OPEX' : [st.session_state.hfo_model_cost_opex],
                      "Coût global d'une molécule de HFO" : [((st.session_state.conso*st.session_state.price_hfo)+ st.session_state.hfo_model_cost_opex)/st.session_state.conso],
                      'Consommation estimée de GPL': [(st.session_state.coef_filtre * st.session_state.rend_ram * 0.96 *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800)))],
                      'Coût du GPL' : [(st.session_state.coef_filtre * st.session_state.rend_ram * 0.96 *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800)) *st.session_state.gpl_price)],
                      'Coût maintenance GPL' : [st.session_state.gpl_cost_maint],
                      "Coût global d'une molécule de GPL" : [((st.session_state.coef_filtre * st.session_state.rend_ram * 0.96 *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800)) *st.session_state.gpl_price)+st.session_state.gpl_cost_maint)/((st.session_state.coef_filtre * st.session_state.rend_ram * 0.96 *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800))))],
                      }
            
        
        def to_excel_data(df):
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            df.to_excel(writer, index=False, sheet_name='Coûts estimés')
            workbook = writer.book
            worksheet = writer.sheets['Coûts estimés']
            format1 = workbook.add_format({'num_format': '0.00'}) 
            worksheet.set_column('A:A', None, format1)  
            writer.close()
            processed_data = output.getvalue()
            return processed_data
        
        df_data=pd.DataFrame(data_excel)
        df_xlsx = to_excel_data(df_data)
        st.download_button(label='📥  Téléchager le fichier Excel regroupant les coûts', data=df_xlsx, file_name = 'donnees.xlsx')
                
       # def create_excel(data):
        # Créez un DataFrame à partir du dictionnaire
            #df = pd.DataFrame(data)
            # Spécifiez le nom du fichier Excel que vous souhaitez créer
            #nom_fichier_excel = 'donnees.xlsx'
            #Créer un fichier Excel
            #writer
            # Enregistrez le DataFrame dans un fichier Excel
           # df.to_excel(nom_fichier_excel, index=False)
            
        #def create_excel1(data):
            # Créez un DataFrame à partir du dictionnaire
            #df = pd.DataFrame(data)
        
            # Spécifiez le nom du fichier Excel que vous souhaitez créer
           # nom_fichier_excel = 'donnees.xlsx'
        
            # Obtenir le chemin absolu du répertoire courant
            #chemin_repertoire_courant = os.getcwd()
        
            # Concaténer le nom du fichier Excel avec le chemin absolu du répertoire courant
           # chemin_complet_fichier_excel = os.path.join(chemin_repertoire_courant, nom_fichier_excel)
        
            # Enregistrez le DataFrame dans un fichier Excel dans le répertoire courant
            #df.to_excel(chemin_complet_fichier_excel, index=False)
            
       # exl = st.button("Générer un bilan Excel", on_click = create_excel(data_excel))
        #st.download_button("Télécharger le fichier Excel", data=data_excel, file_name = "donnees.xlsx" )
        
    #Optimisation proposal 
    if st.session_state.choose == "Proposition d'optimisation" :
        #Show the benefits to use an econimizer
        if st.session_state.conso != 0:
            if st.session_state.eco :
                st.subheader("Vous possédez déjà un économiseur")
            else :
                st.subheader("Améliorer son rendement à l'aide d'un économiseur")
            
            co1, co2 = st.columns(2,gap="medium")
            with co1:
                st.title("Economiseur HFO")
                st.write("On peut gagner 5% de consommation de HFO à l'aide d'un économiseur sur ce type de fuel")
                st.subheader("Voici la consommation espérée en utilisant un économiseur :")
                st.title(space_in_numbers(str(round(0.95*st.session_state.conso)))+ " tonnes par an")
                st.write("")
                st.write("")
                colon1, colon2 = st.columns(2)
                with colon1 :
                    st.metric(label = "Coût molécule sans économiseur ", value = (space_in_numbers(str(round(st.session_state.conso*st.session_state.price_hfo)))+ st.session_state.money) )
                with colon2 :
                    st.metric(label = "Coût molécule avec économiseur ", value = (space_in_numbers(str(round(0.95 * st.session_state.conso*st.session_state.price_hfo)))+ st.session_state.money),delta = space_in_numbers(str(round(0.05 * st.session_state.conso*st.session_state.price_hfo)))+ st.session_state.money)
            with co2 : 
                st.title("Economiseur GPL")
                st.write("On peut gagner 7.5% de consommation de HFO à l'aide d'un économiseur sur ce type de fuel")
                st.subheader("Voici la consommation espérée en utilisant un économiseur :")
                st.title(space_in_numbers(str(round(0.925*round(st.session_state.rend_ram * ((100-st.session_state.rand_gpl)/100) * 11774 * (st.session_state.conso/13800)))))+ " tonnes par an")
                st.write("")
                st.write("")
                colo1, colo2 = st.columns(2)
                with colo1:
                    st.metric(label = "Coût molécule sans économiseur ", value = (space_in_numbers(str(round(round(st.session_state.gpl_price * st.session_state.rend_ram * ((100-st.session_state.rand_gpl)/100) * 11774 * (st.session_state.conso/13800)))))+ st.session_state.money) )
                with colo2:
                    st.metric(label = "Coût molécule avec économiseur ", value = (space_in_numbers(str(round(0.925 * st.session_state.gpl_price * st.session_state.rend_ram * ((100-st.session_state.rand_gpl)/100) * 11774 * (st.session_state.conso/13800))))+ st.session_state.money),delta = space_in_numbers(str(round(0.075 * st.session_state.gpl_price * st.session_state.rend_ram * ((100-st.session_state.rand_gpl)/100) * 11774 * (st.session_state.conso/13800))))+ st.session_state.money)
            with st.expander("Information investissement"):
                st.write("A noter que généralement, le coût d'un économiseur pour le HFO est **2 fois plus élevé** que pour le GPL")
            
        else :  
            #Demand to complete the Home page information
            st.write("Veuillez renseigner votre consommation")

        



#Same in English language
if st.session_state.lang == 'English'  :       
    val = st.button("Generate the invoive", on_click = gen_pdf())
    if val == True : 
        with open("/Users/nass/Documents/pdf_generated.pdf","rb") as file : 
            
            #data = "/Users/nass/Documents/Streamlit-app/generated_pdf.pdf"
            st.download_button("Download the invoice", data  = file, file_name='facture.pdf', mime = 'document/pdf')
    
    
    if st.session_state.choose == "HFO" : 
        if st.session_state.conso != 0:
            en_hfo = round(st.session_state.conso *11774,2)
            cost_hfo = price_hfo(st.session_state.conso)
            st.write("This is the energy produce by the HFO :")
            st.write (str(en_hfo)+"kWh")
            st.write("The cost of molecule HFO :")
            st.write(str(cost_hfo) + "€")
        else :
            st.write("Veuillez renseigner votre consommation ")
        
        
    if st.session_state.choose == "GPL" : 
        if st.session_state.conso != 0 :
            quantity_gpl = round(calcul_conso_gpl(calcul_energy_hfo(st.session_state.conso)), 2)
            st.write("Pour la même quantité d'énergie, voici la consommation de GPL équivalente :")
            st.write(str(quantity_gpl)+" tonnes")
            cost_gpl = price_gpl(quantity_gpl)
            st.write("Pour la même quantité d'énergie, voici le coût de la molécule GPL :")
            st.write(str(cost_gpl) + "€")
        else :
            st.write("Veuillez renseigner votre consommation ")
            
    if st.session_state.choose == "Comparaison" : 
        st.write("Ici sera afficher des grahiques comme l'amortissement sur 10 ans entre le HFO et le GPL, compoaraison de la quatité de CO2 économiser")
  
        
