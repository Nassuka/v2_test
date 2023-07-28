#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 09:32:03 2023

@author: nass
"""
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
#import plotly.express as px

#from fonctions import calcul_conso_gpl,rendement, calcul_energy_hfo, price_hfo, price_gpl, euro_to_dollar, dollar_to_CFA, dollar_to_ZAR, dollar_to_din_tun, dollar_to_mur, space_in_numbers, courbe
#from gen_pdf import gen_pdf
#from bokeh.plotting import figure

import altair as alt
#from vega_datasets import data

#Icône et nom de l'onglet
st.set_page_config(page_title='Comparaison HFO vs GPL',page_icon='Logo_TotalEnergies.png', initial_sidebar_state="expanded", layout = "wide")

#Titre de l'application
st.header('Application de comparaison des coûts de fonctionnement entre le HFO et le GPL')




#Sidebar
with st.sidebar : 
    st.header('Menu')
    st.divider()
    
    

    
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
        
    
        
    
    def change_fr_to_en() : 
        if st.session_state.fr : 
            st.session_state.en = False
            
        elif st.session_state.fr == False : 
            st.session_state.en = True 
            
        elif st.session_state.fr == False and st.session_state.en == False :
            st.session_state.fr == True

    def change_en_to_fr() : 
        if st.session_state.en : 
            st.session_state.fr = False
            
        elif st.session_state.en == False : 
            st.session_state.fr = True
            
        elif st.session_state.fr == False and st.session_state.en == False :
            st.session_state.fr == True
            
            
   # if st.session_state.eco != True :
    st.session_state.choose = st.selectbox("Estimations", ("Page d'accueil","HFO", "GPL","Comparaison", "Proposition d'optimisation"))
    #else : 
         #st.session_state.choose = st.selectbox("Estimations", ("Page d'accueil","HFO", "GPL","Comparaison"))
    
    st.divider()
    
    #st.write("**Veuillez saisir les informations suivantes :** ")
    
    #country = st.selectbox("**Pays**",("-- Selectionné --","Afrique du Sud", "Côte d'Ivoire", "France","Ile Maurice", "Sénégal", "Tunisie","Autres"), )
    #franc_cfa = ["Côte d'Ivoire", "Sénégal"]
    #euro = ["France"]
    #dollar = ["Autres"]
    #ZAR = ["Afrique du Sud"]
    #dina_tun = ["Tunisie"]
    #roupie_mauricienne =["Ile Maurice"]
    
    #if country in franc_cfa :
        #st.session_state.money = " F"
   
    #elif country in euro :
        #st.session_state.money = " €"
    
    #elif country in dollar : 
        #st.session_state = " $"
    
    #elif country in ZAR :
        #st.session_state.money = " R"
    
    #elif country in dina_tun :
        #st.session_state.money = " DT"
        
    #elif country in roupie_mauricienne :
        #st.session_state.money = " MUR"
    
    
    #st.session_state.conso = st.number_input("**Consommation mensuelle de Fioul (en tonnes):**")
    
    #lang = st.selectbox( "Langues",("Français", "English"))
    
    #scol1, scol2 = st.columns([1.8,3])
    

    #scol2 .image("/Users/nass/Documents/Streamlit-app/drap_fr.png",width = 30)
    #scol2.write("")
    #scol2 .image("/Users/nass/Documents/Streamlit-app/drap_en.webp",width = 30)
    
    #fr  = scol1.checkbox("Français" , key = "fr", on_change = change_fr_to_en)
    #scol1.write("")
    #scol1.write("")
    #en = scol1.checkbox("English", key = "en", on_change = change_en_to_fr)
    

#French language
if fr :
    st.session_state.rand_gpl = np.random.randint(3,6)
    if st.session_state.choose == "Page d'accueil":
        #st.write(st.session_state.c)
        #with st.form("my_form"):
        st.subheader("Veuillez entrer les informations ci-dessous :")
        fcol1, fcol2 = st.columns(2)
        st.session_state.conso = fcol1.number_input("**Consommation annuelle de Fioul (en tonnes) :**")
        st.session_state.price_hfo = fcol2.number_input("**Prix de la tonne de Fioul Lourd (monnaie locale) :**")
        country = st.selectbox("**Pays**",("-- Selectionné --","Afrique du Sud", "Côte d'Ivoire", "France","Ile Maurice", "Sénégal", "Tunisie","Autres"), )
        st.session_state.pci_hfo = st.number_input("PCI du Fioul lourd(kWh/kg) :")
        st.session_state.teneur_soufre = st.number_input("Teneur en soufre dans le fioul (%)")
        st.session_state.model_want = st.checkbox("Je souhaite utiliser une approximation des OPEX")
        
        if st.session_state.model_want == False : 
            st.session_state.model_use = st.checkbox("Je ne connais pas tous les coûts suivants")
           
            col1, col2 = st.columns(2)
            
            st.session_state.pui = col1.number_input("**Puissance de l'installation (en KW) :**")
            st.session_state.price_kWh = col2.number_input("**Coût d'un Kwh :**")
            st.session_state.nb_h_per_day = col1.number_input("**Nombre d'heures de fonctionnement de l'installation par jour :**", min_value=0, max_value=24)
            st.session_state.nb_day_per_week = col2.number_input("**Nombre de jours de fonctionnement de l'installation par semaine :**", min_value=0, max_value=7, step= 1)
            #st.session_state.salary = col2.number_input("**Salaire des employés (monnaie locale) :**")
            
            #st.session_state.nb_fil = st.number_input("**Nombre de filtres :**", step = 1)
           
            #st.session_state.nb_ram = st.number_input("**Nombre de ramonages par an :**", step = 1)
            
            st.session_state.eau = st.number_input("Combien de m3 d'eau traités pour la maintenance de la chaudière :", step = 1)
            col11, col22 = st.columns(2)
            st.session_state.eau_l = col11.number_input("Coût d'un m3 d'eau traité :")
            st.session_state.eau_nb = col22.number_input("Combien de fois par an l'achat de cet eau est effectuée :")
            
            
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
                    
                #submitted = st.form_submit_button("Soumettre")
            
            #st.write(st.session_state.conso)
            
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
                st.session_state.gpl_cost_maint = st.session_state.salary * st.session_state.nb_employee + st.session_state.presta
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
            
            
            st.session_state.ram = st.checkbox("Faites-vous des ramonages ?")
            if st.session_state.ram : 
                st.session_state.nb_ram = st.number_input("**Fréquence de ramonage (en mois) :**")
                st.session_state.ram_cost= st.number_input("**Coût d'un ramonage :**")
                st.write("")
                st.write("")
                st.write("")
                
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
                    
                #st.write(st.session_state.change_pcs)
                st.session_state.but_pcs = st.button("Ajouter dans le tableau")
                
                if st.session_state.but_pcs :
                    st.session_state.c += [np.transpose(np.array([st.session_state.change_pcs,st.session_state.price_pcs, st.session_state.fre_chgm, st.session_state.time_int,st.session_state.tp_yes_no, st.session_state.chx_maint])).tolist()]
                    #st.session_state.c += [st.session_state.change_pcs,0,0]
                    
                    #st.write(st.session_state.c[0])
                    #k = st.session_state.c[0].values()
                    #st.write(k)
                    #st.session_state.cl = list(st.session_state.c[0].values())
                    #st.write(st.session_state.cl)
                    
                if len(st.session_state.c) != 0 : 
                    df1 = pd.DataFrame(data = st.session_state.c, index = ('Pièces %d' % i for i in range(1,1 + len(st.session_state.c))), columns = ["Nom de la pièce", "Prix de la pièce", "Fréquence de changement de la pièce (en mois)", "Durée de l'intervention (en heures)", "Cela empiète-t-il sur la production ?(Oui ou Non)", "Coût compris dans celui de la mainteneace "])
                    udf1 = st.data_editor(df1)
                    npdf1 = udf1.to_numpy()
                    for i in range(len(st.session_state.c)):
                        st.session_state.c[i][1] = npdf1[i,1]
                        st.session_state.c[i][2] = npdf1[i,2]
                        st.session_state.c[i][3] = npdf1[i,3]
                        st.session_state.c[i][4] = npdf1[i,4]
                        st.session_state.c[i][5] = npdf1[i,5]
                        #st.write(st.session_state.c)
                        #st.write(st.session_state.c[i][1])
                        #st.write(st.session_state.c[i][2])
                    if (float(st.session_state.c[-1][2]) != 0) and (float(st.session_state.c[-1][1]) != 0) and (st.session_state.c[-1][5] == "Non"):
                        st.session_state.sum_pcs += ((float(st.session_state.c[-1][1]) * (12/float(st.session_state.c[-1][2]))))
                st.write("")
                st.write("")
                st.write("")
            
          
            
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
                            #st.write(st.session_state.ne[i][0])
                            #st.write(st.session_state.ne[i][1])
                            #st.write(st.session_state.ne[i][2])
                        if (float(st.session_state.ne[-1][2]) != 0) and (float(st.session_state.ne[-1][1]) != 0) and (st.session_state.ne[-1][3] == 'Oui'):
                            st.session_state.sum_nett += (float(st.session_state.ne[-1][1]) * (12/ float(st.session_state.ne[-1][2])))
                            #st.write(st.session_state.sum_nett)
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
                        #st.write(st.session_state.ne[i][0])
                        #st.write(st.session_state.ne[i][1])
                        #st.write(st.session_state.ne[i][2])
                    if (float(st.session_state.ne[-1][2]) != 0) and (float(st.session_state.ne[-1][1]) != 0) and (st.session_state.ne[-1][3] == 'Oui'):
                        st.session_state.sum_nett += (float(st.session_state.ne[-1][1]) * (12/ float(st.session_state.ne[-1][2])))
                        #st.write(st.session_state.sum_nett)
                st.write("")
                st.write("")
                st.write("")
            
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
                        #st.session_state.add[i][3] = npdf2[i,3]
                        #st.write(st.session_state.ne[i][0])
                        #st.write(st.session_state.ne[i][1])
                        #st.write(st.session_state.ne[i][2])
                    if (float(st.session_state.add[-1][2]) != 0) and (float(st.session_state.add[-1][1]) != 0) :
                        st.session_state.sum_add += (float(st.session_state.add[-1][1]) * (float(st.session_state.add[-1][2])))
                        #st.write(st.session_state.sum_nett)
                st.write("")
                st.write("")
                st.write("")
                
            st.session_state.chaud = st.checkbox("Possédez-vous plusieurs chaudières ?")
            if st.session_state.chaud : 
                st.session_state.nb_chaud = st.number_input("Combien en possédez-vous ?", step = 1)
                st.write("")
                st.write("")
                st.write("")
            
            st.session_state.eco = st.checkbox("Possédez-vous un économiseur ?")
                #df_add = pd.DataFrame(data = np.array([[0,0],[0,0]]), columns = ["Combien de litres d'additif pour" , "combien de litres de HFO"])
                #udf_add = st.data_editor(df_add)
            
                        #st.write(st.session_state.sum_nett)  
    
                            
                    #if st.session_state.ne[-1][2] != 0 and st.session_state.ne[-1][1] != 0:
                        #st.session_state.sum_pcs += float(st.session_state.ne[-1][2]) * float(st.session_state.c[-1][1]/10)
            
            #if st.session_state.nett :
                #st.session_state.nett_meth = st.radio("Par quelle moyen nettoyez-vous votre installation ?", ('Opérateurs interne', 'Prestataire'))
                #if st.session_state.nett_meth == 'Opérateurs interne':
                   # st.session_state.same_empl = st.checkbox("Ces opérateurs sont-ils différents de ceux s'occupant de la maintenance ?")
                    #if st.session_state.same_empl : 
                        #st.session_state.nett_choice = st.multiselect("Que nettoyez-vous ?",["Filtres", "Tuyauteries", "Brûleurs", "Autres"])
                        #if len(st.session_state.nett_choice) != 0:
                            #for i in range(len(st.session_state.nett_choice)) :
                                #st.session_state.n += [st.session_state.nett_choice[-1]]
                                
                        #for i in range(len(st.session_state.n)):
                           # st.session_state.ne += [st.session_state.n[i]]
                            
                        #st.write(st.session_state.n)
                        #st.write(len(st.session_state.ne))
                        #st.write(st.session_state.ne)
            
            
            
            
            #st.write(st.session_state.c)
            #st.write(st.session_state.sum_pcs)
            
            
            #st.write(udf1)
            #st.write(udf)
            #st.write(st.session_state)
            
            
            
            #if submitted :
                    #val = st.button("Générer la facture", on_click = gen_pdf())
                    #if val == True : 
               # gen_pdf()
               # with open("/Users/nass/Documents/Streamlit-app/pdf_generated.pdf","rb") as file : 
                    
                            #data = "/Users/nass/Documents/generated_pdf.pdf"
                            #st.download_button("Télécharger la facture", data  = data, file_name='facture.pdf', mime = 'document/pdf')
                            
        else :
            if st.session_state.conso != 0:
                st.session_state.hfo_model_cost_opex = round(st.session_state.conso * 230.73/((st.session_state.conso/12)**0.264))
            else : 
                st.write("Veuillez renseigner votre consommation de fioul")
                
                
    if st.session_state.choose == "HFO" : 
        #st.write(st.session_state)
        #st.write(st.session_state.conso)
        if st.session_state.conso != 0:
            if st.session_state.model_use :
                st.session_state.hfo_model_cost_opex = round(st.session_state.conso * 230.73/((st.session_state.conso/12)**0.264))
            
            en_hfo = round(st.session_state.conso * st.session_state.pci_hfo*1000)
            st.session_state.en_hfo_GJ = en_hfo
            
            
            #if st.session_state.money == " €":
            cost_hfo = round(st.session_state.conso * st.session_state.price_hfo)
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
                    
            
            #else :
                #On convertit les euros en dollars
                #cost_hfo = round(st.session_state.conso * st.session_state.price_hfo)
                #cost_hfo = round(euro_to_dollar(cost_hfo))
                
                #if st.session_state.money == " F":
                    #cost_hfo = round(dollar_to_CFA(cost_hfo),2)
                
                #elif st.session_state.money == " R":
                    #cost_hfo = round(dollar_to_ZAR(cost_hfo),2)
                    
                #elif st.session_state.money == " DT":
                    #cost_hfo = round(dollar_to_din_tun(cost_hfo),2)
                    
                #elif st.session_state.money == " MUR":
                    #cost_hfo = round(dollar_to_mur(cost_hfo),2)"""
               
            #st.write("Voici l'énergie produit par le HFO :")
            #st.write (space_in_numbers(str(en_hfo))+"kWh")
            
            #st.write(cost_hfo)
            #st.write(cost_en)
            #st.write(cost_mtn)
            #st.write(st.session_state.sum_nett)
            
            if st.session_state.model_want : 
                c1, c2 = st.columns(2)
                c1.metric("Voici le coût de la molécule HFO :", str(cost_hfo) + st.session_state.money)
                c2.metric("Voici le coût des OPEX de l'installation :", str(st.session_state.hfo_model_cost_opex) + st.session_state.money)
            else : 
                c1, c2, c3 = st.columns(3)
                c1.metric("Voici le coût de la molécule HFO :", str(cost_hfo) + st.session_state.money)
                c2.metric("Voici le coût énergétique lié au HFO :", str(cost_en) + st.session_state.money)
                c3.metric("Coût annuel moyen lié à la maintenance du site :", str(st.session_state.cost_hfo_maint) + st.session_state.money)
                
               #st.write("Voici le coût de la molécule HFO :")
                #st.write(str(cost_hfo) + st.session_state.money)
                #st.write("Voici le coût énergétique lié au HFO :")
                #st.write(str(cost_en) + st.session_state.money)
               # st.write("Coût annuel moyen lié à la maintenance du site :")
                #st.write(str(cost_mtn) + st.session_state.money)
                
                if st.session_state.eau !=0:
                    c2.metric("Coût annuel global de l'eau traitée :", str(round(st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb)) + st.session_state.money)
                else :
                    c2.metric("Coût annuel global de l'eau traitée :", str(0) + st.session_state.money)
               
                
                if st.session_state.ram :
                    c1.metric("Coût annuel lié aux ramonages :", str(round(st.session_state.ram_cost * (st.session_state.nb_ram/12))) + st.session_state.money)
                else :
                    c1.metric("Coût annuel lié aux ramonages :", str(0) + st.session_state.money)
                
                
                if len(st.session_state.c) != 0:
                    c3.metric("Coût total lié au changement de pièce :", str(round(st.session_state.sum_pcs)) + st.session_state.money)
                else :
                    c3.metric("Coût total lié au changement de pièce :", str(0) + st.session_state.money)
                
                
                if st.session_state.nett :
                    c1.metric("Coût total lié au nettoyage du site", str(st.session_state.nett_cost) + st.session_state.money)
                    
                    if st.session_state.sum_nett != 0:
                        c2.metric("Temps de production perdu :", str(st.session_state.sum_nett)+" heures")
                
                else:
                    c1.metric("Coût total lié au nettoyage du site", str(0) + st.session_state.money)
                    c2.metric("Temps de production perdu :", str(0)+" heures")
                
                if st.session_state.sum_add != 0 :
                    c3.metric("Coût total des additifs", str(st.session_state.sum_add) + st.session_state.money)
                else : 
                    c3.metric("Coût total des additifs", str(0) + st.session_state.money)
               

                    
            
                
            
            st.divider()
            col1, col2 = st.columns([2,1.5])
            st.subheader("Coût annuel total de fonctionnement de votre installation HFO : ")
            if st.session_state.hfo_model_cost_opex < (cost_en + st.session_state.cost_hfo_maint + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram)) :
                st.title(str(round(cost_hfo + cost_en + st.session_state.cost_hfo_maint + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram))) + st.session_state.money)
            else :
                st.title(str(cost_hfo + st.session_state.hfo_model_cost_opex))
            
            st.subheader("Coût global d'une tonne de HFO : ")
            #st.title(str(round((cost_hfo + cost_en + cost_mtn + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram)))/st.session_state.conso) + st.session_state.money)
            if st.session_state.hfo_model_cost_opex < (cost_en + st.session_state.cost_hfo_maint + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram)) :
                st.session_state.tot_cost_hfo = round(cost_hfo + cost_en + st.session_state.cost_hfo_maint + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * (st.session_state.nb_ram/st.session_state.conso)))
                st.title(str(round(st.session_state.tot_cost_hfo/st.session_state.conso)) + st.session_state.money)
                st.divider()
                st.write("")
                st.write("")
                st.write("")
            else : 
                st.session_state.tot_cost_hfo = round(st.session_state.hfo_model_cost_opex + cost_hfo)
                st.title(str(round((st.session_state.tot_cost_hfo + st.session_state.hfo_model_cost_opex)/st.session_state.conso)) + st.session_state.money)
                st.divider()
                st.write("")
                st.write("")
                st.write("")
            
            if cost_en != 0 or st.session_state.cost_hfo_maint != 0 or st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb != 0 or st.session_state.ram_cost * st.session_state.nb_ram != 0 or st.session_state.sum_pcs != 0 or st.session_state.nett_cost != 0 or st.session_state.sum_add != 0 :
                cost_list = np.array([cost_en,st.session_state.cost_hfo_maint, st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb, st.session_state.ram_cost * st.session_state.nb_ram, st.session_state.sum_pcs, st.session_state.nett_cost, st.session_state.sum_add])
                data_chart=[]
                for i in range(8):
                    data_chart +=  [cost_list* (1.003**i) ]
                
                chart_data_hfo = pd.DataFrame(data= data_chart, columns = ["Coût énergétique", "Coût maintenance du site", "Coût de l'eau","Coût ramonages", "Coût pièces", "Coût nettoyages", "Coût additifs"])
                st.bar_chart(chart_data_hfo)
                
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
                #(cost_en + st.session_state.cost_hfo_maint + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram)
            
             
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
            def go_base():
                st.session_state.choose = "Page d'accueil"
                return st.session_state.choose 
            st.write("Veuillez renseigner les informations de la page d'accueil ")
            #st.button("Aller à la page d'accueil", on_click = go_base())
        
        
    if st.session_state.choose == "GPL" : 
        if st.session_state.conso != 0 :
            if (st.session_state.nb_ram == 0) or (st.session_state.ram == False) or (st.session_state.nb_ram > 18):
                st.session_state.rend_ram = 0.85
                
            elif (st.session_state.nb_ram >0)  or (st.session_state.nb_ram < 6):
                st.session_state.rend_ram = 0.935
            
            elif (st.session_state.nb_ram >5)  or (st.session_state.nb_ram < 18):
                st.session_state.rend_ram = 0.9
            
            rend_rand = st.session_state.rand_gpl
            coeff_rand = (100-rend_rand)/100
            
            if st.session_state.money == " €":
                st.session_state.max_gpl_price = 2000
                st.session_state.base_gpl_price = 500
                
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
            
            st.session_state.gpl_price = st.slider("Prix de la tonne de GPL :", 0,st.session_state.max_gpl_price , st.session_state.base_gpl_price)
            quantity_gpl = round(st.session_state.coef_filtre * st.session_state.rend_ram * coeff_rand *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800)))
            st.subheader("Pour la même quantité d'énergie, voici la consommation de GPL équivalente :")
            st.title(str(quantity_gpl)+" tonnes")
            cost_gpl = quantity_gpl * st.session_state.gpl_price
            st.subheader("Pour la même quantité d'énergie, voici le coût de la molécule GPL :")
            st.title(str(cost_gpl) + st.session_state.money)
            
            
            
            st.session_state.gpl_maint_choice = st.radio("Par quel méthode effectuez-vous votre maintenance ?", ('Personnel interne', 'Prestataire','Hybride', 'Autres'))
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
            #di = {"GPL": cost_gpl + st.session_state.gpl_cost_maint,"HFO" : st.session_state.tot_cost_hfo}
            #df_comp = pd.DataFrame(np.array(list(di.values())).T, columns=list(di.keys()))       
            st.bar_chart({"GPL": cost_gpl + st.session_state.gpl_cost_maint,"HFO" : st.session_state.tot_cost_hfo})
            
            st.session_state.tot_cost_gpl = cost_gpl + st.session_state.gpl_cost_maint
            
            data_line1 = []
            data_line_gpl =[]
            data_line_hfo =[]
            data_line_hfo += [st.session_state.tot_cost_hfo]
            data_line_gpl += [cost_gpl + st.session_state.gpl_cost_maint]
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
            
            #st.write(data_line1)
            df_data_line1= pd.DataFrame(data_line1, columns=["GPL","HFO"])
            st.line_chart(df_data_line1)
            
            data_line2 = []
            data_line_gpl2 =[]
            data_line_hfo2 =[]
            data_line_hfo2 += [st.session_state.tot_cost_hfo]
            data_line_gpl2 += [cost_gpl + st.session_state.gpl_cost_maint]
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
            
            
            
            #st.write(data_line1)
            df_data_line2= pd.DataFrame(data_line2, columns=["GPL","HFO"])
            st.line_chart(df_data_line2)
            #scale = alt.Scale(domain = ["Coût total GPL","Coût total HFO"], range = ["#1f77b4","#aec7e8"])
            #click = alt.selection_multi(encodings=["color"])
            #color = alt.Color( scale = scale)
            #brush = alt.selection_interval(encodings=["x"])
            #bars =(alt.Chart().mark_bar().encode(x = "Energie", y = "Coût total", color= alt.condition(click, color, alt.value("lightgray"))).transform_filter(brush).properties(width=550).add_selection(click))
            #test_bar_chart = pd.DataFrame(np.array([[st.session_state.tot_cost_gpl],[st.session_state.tot_cost_hfo]]).T)
            #, columns = ["Coût total GPL", "Coût total HFO"]
            #chart = alt.vconcat(data = test_bar_chart, title = "Visualisation des coûts annuels des installations GPL et HFO")
            
            #st.altair_chart(chart,theme="streamlit", use_container_width = True)

            
        else :
            st.write("Veuillez renseigner votre consommation ")
            
            
            
    if st.session_state.choose == "Comparaison" : 
        
        #source = data.population.url

        #slider = alt.binding_range(min=1850, max=2000, step=10)
        #select_year = alt.selection_point(name='year', fields=['year'],
                                          # bind=slider, value={'year': 2000})

        #base = alt.Chart(source).add_params(
         #   select_year
        #).transform_filter(
        #    select_year
        #).transform_calculate(
         #   gender=alt.expr.if_(alt.datum.sex == 1, 'Female', 'Male')
        #).properties(
        #    width=250
        #)
        

       # color_scale = alt.Scale(domain=['HFO', 'GPL'],
                                #range=['#fb4a61', '#b41f2c'])
        
        #left = encode(
            #alt.Y('age:O').axis(None),
            #alt.X('sum(people):Q')
                #.title('Coûts')
                #.sort('descending'),
           # alt.Color('gender:N')
                #.scale(color_scale)
                #.legend(None)
        #).mark_bar().properties(title='HFO')
        
        
        #middle = base.encode(
            #alt.Y('age:O').axis(None),
            #alt.Text('age:Q'),
        #).mark_text().properties(width=20)

        #right = base.transform_filter(
           # alt.datum.gender == 'Male'
       # ).encode(
           # alt.Y('age:O').axis(None),
            #alt.X('sum(people):Q').title('population'),
            #alt.Color('gender:N').scale(color_scale).legend(None)
        #).mark_bar().properties(title='Male')

        #st.altair_chart(alt.hconcat(left, middle,right, spacing=1),use_container_width=True )
        
        #st.altair_chart(alt.hconcat(left,right, spacing=1),use_container_width=True)
        
        st.title("Comparaison des énergies")
        
        col1, col2 = st.columns(2)
        with col1 :
            st.title("HFO")
            #st.subheader("Coûts totaux du HFO")
            st.metric("Coûts totaux du HFO", value = str(st.session_state.tot_cost_hfo)+ st.session_state.money)
            st.write("")
            st.metric("Coût de la molécule", value = str(round(st.session_state.conso * st.session_state.price_hfo)) + st.session_state.money)
            st.write("")
            if st.session_state.hfo_model_cost_opex < (st.session_state.cost_hfo_maint + round(st.session_state.price_kWh * st.session_state.pui * st.session_state.nb_h_per_day * st.session_state.nb_day_per_week*52.1429)
            + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram)) :
                st.metric("Coûts des OPEX",value = str(round( st.session_state.cost_hfo_maint + round(st.session_state.price_kWh * st.session_state.pui * st.session_state.nb_h_per_day * st.session_state.nb_day_per_week*52.1429)
                + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram))) + st.session_state.money)
            else :
                st.metric("Coût des OPEX", value = str(st.session_state.hfo_model_cost_opex)+ st.session_state.money)   
            st.write("")
            st.write("")
            st.metric("Facteur d'émissions de CO2", value = str(round(3.12 * st.session_state.conso)) + " tonnes")
            st.write("")
            #st.metric("Facteur CO2(en tonnes)", value = round((319*st.session_state.en_hfo_GJ/1000)/1000))
            #if st.session_state.teneur_soufre > 2:
               # st.session_state.con_soufre = 1557.5*((st.session_state.teneur_soufre)**2) - 4382.5 *st.session_state.teneur_soufre + 5940
           # else :
                #st.session_state.con_soufre =2.642*643.45*st.session_state.teneur_soufre**0.8941
                
            #st.metric("Concentration de SOx dans les fumées", value = str(round(st.session_state.con_soufre)) + " mg/Nm3")
            st.metric("Concentration de SOx dans les fumées", value = str(round(1700 * st.session_state.teneur_soufre)) + " mg/Nm3")
            st.write("")
            st.metric("Facteur d'émissions de NOx", value = str(round(0.0036*st.session_state.en_hfo_GJ*1967/1000)) + " kg")
            st.write("")
            st.write("")
            st.metric("Facteur d'émissions de CO", value = str(round(0.0036*st.session_state.en_hfo_GJ*92/1000)) + " kg")
       
        with col2 :
            st.title("GPL")
            #st.subheader("Coûts totaux du HFO")
            st.metric("Coûts totaux du GPL", value = str(round(st.session_state.gpl_cost_maint + st.session_state.gpl_price * st.session_state.rend_ram * 0.96 *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800)))) + st.session_state.money, delta = str(round((st.session_state.gpl_cost_maint + st.session_state.gpl_price * st.session_state.rend_ram * 0.96 *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800))) - st.session_state.tot_cost_hfo ))+ st.session_state.money, delta_color= "inverse")
            st.metric("Coût de la molécule", value = str(round(st.session_state.gpl_price * st.session_state.rend_ram * 0.96 *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800)))) + st.session_state.money, delta = str(round((st.session_state.gpl_price * st.session_state.rend_ram * 0.96 *1000*st.session_state.pci_hfo * (st.session_state.conso/(12800)))- st.session_state.conso * st.session_state.price_hfo)) + st.session_state.money, delta_color= "inverse")
            
            if st.session_state.model_want or (st.session_state.hfo_model_cost_opex > ((st.session_state.price_kWh * st.session_state.pui * st.session_state.nb_h_per_day * st.session_state.nb_day_per_week*52.1429) + st.session_state.cost_hfo_maint + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram))):
                st.metric("Coût des OPEX", value = str(round(st.session_state.gpl_cost_maint))+ st.session_state.money, delta = str(round((st.session_state.gpl_cost_maint)- st.session_state.hfo_model_cost_opex)) + st.session_state.money,  delta_color= "inverse") 
            else:
                st.metric("Coût des OPEX", value = str(round(st.session_state.gpl_cost_maint))+ st.session_state.money, delta = str(round((st.session_state.gpl_cost_maint)- ((st.session_state.price_kWh * st.session_state.pui * st.session_state.nb_h_per_day * st.session_state.nb_day_per_week*52.1429) + st.session_state.cost_hfo_maint + st.session_state.sum_pcs + st.session_state.nett_cost + st.session_state.sum_add + (st.session_state.eau * st.session_state.eau_l * st.session_state.eau_nb) + (st.session_state.ram_cost * st.session_state.nb_ram)))) + st.session_state.money,  delta_color= "inverse") 
           
            st.metric("Facteur d'émissions de CO2", value = str(round(63.1 * st.session_state.en_hfo_GJ * 0.0036/1000)) +" tonnes", delta = str(round((63.1 * st.session_state.en_hfo_GJ * 0.0036/1000)-(3.12 * st.session_state.conso))) + " tonnes", delta_color= "inverse")
            #st.metric("Emission de SOx", value = str(round(2.2 *0.0036*st.session_state.en_hfo_GJ/1000 ))+ " kg", delta= str(round((2.2 *0.0036*st.session_state.en_hfo_GJ/1000)-(0))) )
            st.metric("Concentration de SOx dans les fumées", value = str(325) + " mg/Nm3", delta = str(round((2.2 *0.0036*st.session_state.en_hfo_GJ/1000)-(1700 * st.session_state.teneur_soufre)))+ " mg/Nm3", delta_color= "inverse")
            st.metric("Facteur d'émissions de NOx", value = str(round(0.0036*st.session_state.en_hfo_GJ*60/1000))+ " kg", delta = str(round((0.0036*st.session_state.en_hfo_GJ*60/1000)-(0.0036*st.session_state.en_hfo_GJ*1967/1000)))+ " kg", delta_color= "inverse")
            st.metric("Facteur d'émissions de CO", value = str(round(0.5*0.0036*st.session_state.en_hfo_GJ*92/1000))+ " kg", delta = str(round((0.5*0.0036*st.session_state.en_hfo_GJ*92/1000)-(0.0036*st.session_state.en_hfo_GJ*92/1000)))+" kg", delta_color= "inverse")
            
            
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
        
        def create_excel(data):
        # Créez un DataFrame à partir du dictionnaire
            df = pd.DataFrame(data)
            
            # Spécifiez le nom du fichier Excel que vous souhaitez créer
            nom_fichier_excel = 'donnees.xlsx'
            #Créer un fichier Excel
            #writer
            # Enregistrez le DataFrame dans un fichier Excel
            df.to_excel(nom_fichier_excel, index=False)
            
            
        
        exl = st.button("Générer un bilan Excel", on_click = create_excel(data_excel))
        #if exl :
            #st.download_button("Télécharger le fichier", data  = pd.DataFrame(data_excel).to_excel("donnees.xlsx", index=False), file_name='Excel.xlsx', mime = "excl/xlsx")
    
       #st.write("Ici sera afficher des grahiques comme l'amortissement sur 10 ans entre le HFO et le GPL, compoaraison de la quatité de CO2 économiser")
        #chart_data = pd.DataFrame(courbe(1,2,20), columns=["a","b"])
        #st.bar_chart(chart_data)
        #p = figure(title = 'Le rendement en fonction des mois', x_axis_label = 'Mois', y_axis_label = 'Rendement')
        #x = [i for i in range(60)]
        #p.line(x ,rendement(60), legend_label = 'Rendement', line_width = 4)
        #st.bokeh_chart(p, use_container_width = True)
        #k= np.zeros((2,60))
        
        #for i in range(60):
            #k[0][i]= rendement(60)[i]
            #k[1][i] = 1
        
        #k=k.T
        
        #ind = [i for i in range(60)]
        #k = np.array([rendement(60), 1 for i in range(60)]).T
        #dfp = pd.DataFrame(k,index = ind, columns = ['rendement HFO', 'rendement GPL'])
        #st.subheader("Rendement en fonction du temps (mois) :")
        #st.line_chart(dfp)
        #st.area_chart(dfp)
        #st.bar_chart(dfp)
            
        
        #CO2_HFO = round((st.session_state.conso * 25440) / 8000)
        #CO2_GPL = round((st.session_state.conso * 19614) / 8000)
        #st.write(CO2_HFO)    
        #st.metric(label = "Emission de CO2 eq", value = str(CO2_GPL) + " tons eq CO2", delta = str((CO2_HFO-CO2_GPL)*100/CO2_GPL) + " % de tons eq CO2 gagnée")
    
    
    
    if st.session_state.choose == "Proposition d'optimisation" :
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
                st.title(str(round(0.95*st.session_state.conso))+ " tonnes par an")
                st.write("")
                st.write("")
                colon1, colon2 = st.columns(2)
                with colon1 :
                    st.metric(label = "Coût molécule sans économiseur ", value = (str(round(st.session_state.conso*st.session_state.price_hfo))+ st.session_state.money) )
                with colon2 :
                    st.metric(label = "Coût molécule avec économiseur ", value = (str(round(0.95 * st.session_state.conso*st.session_state.price_hfo))+ st.session_state.money),delta = str(round(0.05 * st.session_state.conso*st.session_state.price_hfo))+ st.session_state.money)
            with co2 : 
                st.title("Economiseur GPL")
                st.write("On peut gagner 7.5% de consommation de HFO à l'aide d'un économiseur sur ce type de fuel")
                st.subheader("Voici la consommation espérée en utilisant un économiseur :")
                st.title(str(round(0.925*round(st.session_state.rend_ram * ((100-st.session_state.rand_gpl)/100) * 11774 * (st.session_state.conso/13800))))+ "tonnes par an")
                st.write("")
                st.write("")
                colo1, colo2 = st.columns(2)
                with colo1:
                    st.metric(label = "Coût molécule sans économiseur ", value = (str(round(round(st.session_state.gpl_price * st.session_state.rend_ram * ((100-st.session_state.rand_gpl)/100) * 11774 * (st.session_state.conso/13800))))+ st.session_state.money) )
                with colo2:
                    st.metric(label = "Coût molécule avec économiseur ", value = (str(round(0.925 * st.session_state.gpl_price * st.session_state.rend_ram * ((100-st.session_state.rand_gpl)/100) * 11774 * (st.session_state.conso/13800)))+ st.session_state.money),delta = str(round(0.075 * st.session_state.gpl_price * st.session_state.rend_ram * ((100-st.session_state.rand_gpl)/100) * 11774 * (st.session_state.conso/13800)))+ st.session_state.money)
            with st.expander("Information investissement"):
                st.write("A noter que généralement, le coût d'un économiseur pour le HFO est **2 fois plus élevé** que pour le GPL")
            
        else :  
            st.write("Veuillez renseigner votre consommation")





        
#English language
if en :       
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
  
        
