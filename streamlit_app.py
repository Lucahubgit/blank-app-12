import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="My application for DV4S",
    layout="wide",
    initial_sidebar_state="expanded"
    )

st.title("🎈 My new app for DV4S")

st.header('_Hi_ :green[DV4S]!') #The _..._ is to do the corsivo, while :green[] is to do the text green

st.subheader('Welcome to the class!')   #Come ha messo la faccina?

st.write(
    "Let's start **building**! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)." # **...** is to have the bold text
)

st.write('----------------------------------------------------')

value = st.slider('Select a value: ', 0, 100, 30)
st.write('You selected: ', value)

st.write('----------------------------------------------------')

st.markdown('<p style="color:yellow; font-size:20px;">I should be yellow</p>',
            unsafe_allow_html=True) #Possiamo usare codice html per cambiare aspetto del testo

st.write('----------------------------------------------------')

sports_list=['soccer','basket','football','tennis']

button_pressed=st.button('Push me for sports list',type="primary")
if button_pressed:  #se il bottone è cliccato, vogliamo mostrare quello che c'è nella lista. Il valore è un booleano
    st.write(sports_list)

st.write('----------------------------------------------------')
check_pressed=st.checkbox('I like it')
if check_pressed:  #se il bottone è cliccato, vogliamo mostrare quello che c'è nella lista. Il valore è un booleano
    st.write('Pressed')
else:
    st.write('Not pressed')

st.write('----------------------------------------------------')

chosen_item=st.radio('What sport do you like?', sports_list)
st.write('I knew that you liked ' + chosen_item)

st.write('----------------------------------------------------')

chosen_item_again=st.selectbox('What sport do you like?', sports_list)
st.write('I knew that you liked ' + chosen_item_again)

st.write('----------------------------------------------------')

multi_item=st.multiselect('What sport do you like?', sports_list)
#Potremmo stampare le scelte selecìzionate usando un ciclo for

st.write('----------------------------------------------------')

age=st.slider('Your age range:',18,65,(25,50))
st.write('Your age range is: ',age)

st.write('----------------------------------------------------')

user_name=st.text_input('Your name:',placeholder='Write your name here') #When we press enter in the app, the variable of our name is saved
st.write('Your name is: ',user_name)

st.write('----------------------------------------------------')

user_age=st.number_input('Your age:',
                         min_value=18,
                         max_value=65,
                         value=25,
                         step=1)

st.write('----------------------------------------------------')

match_date=st.date_input('Select date ranges:',
                         value=(datetime(2025,3,15),datetime(2025,3,25))
                         )

st.write('----------------------------------------------------')

with st.form('User information'):   #Can be used instead of the try catch. Usually used to open a file
    user_name=st.text_input('Your name:',placeholder='Write your name here') #When we press enter in the app, the variable of our name is saved
    user_age=st.number_input('Your age:',
                         min_value=18,
                         max_value=65,
                         value=25,
                         step=1)
    submitted=st.form_submit_button('Submit it')
if submitted:
    st.write('You submitted it')

st.write('----------------------------------------------------')