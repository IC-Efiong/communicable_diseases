import numpy as np
import streamlit as st
import pickle

# loading the saved model
loaded_model = pickle.load(open('model1.pkl', 'rb'))

#creating a function for prediction

def communicable_disease_prediction(input_data):
    disease_mapping = {
        0: 'Cold',
        1: 'Covid',
        2: 'Flu'
    }
    input_data_as_numpy = np.asarray(input_data)
    input_data_reshape = input_data_as_numpy.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshape)

    predicted_disease = disease_mapping[prediction[0]]

    if (prediction[0]==0):
        result = f'This patient does not have a Communicable Disease - {predicted_disease}'
    else:
        result = f'This patient has a Communicable Disease - {predicted_disease}'
    
    return result
def main():

    #giving title for the interface
    st.title('Communicable Disease Web App')

    #getting the input from user

    MUSCLE_ACHES = st.text_input('Muscles Aches')
    TIREDNESS = st.text_input('Tiredness')
    SORE_THROAT = st.text_input('Sore Throat')
    RUNNY_NOSE = st.text_input('Runny Nose')
    STUFFY_NOSE = st.text_input('Stuffy Nose')
    FEVER = st.text_input('Fever')
    NAUSEA = st.text_input('Nausea')
    VOMITING = st.text_input('Vomiting')
    DIARRHEA = st.text_input('Diarrhea')
    SHORTNESS_OF_BREATH = st.text_input('Shortness of Breath')
    DIFFICULTY_BREATHING = st.text_input('Difficulty in Breathing')
    LOSS_OF_TASTE = st.text_input('Loss of Taste')
    LOSS_OF_SMELL = st.text_input('Loss of Smell')
    ITCHY_NOSE = st.text_input('Itchy Nose')
    ITCHY_EYES = st.text_input('Itchy Eyes')
    ITCHY_MOUTH = st.text_input('Itchy Mouth')
    ITCHY_INNER_EAR = st.text_input('Itchy Inner Ear')
    SNEEZING = st.text_input('Sneezing')
    PINK_EYE = st.text_input('Pink Eye')

    #code for Prediction

    diagnosis = ''

    #creating a button for prediction

    if st.button('Test Result'):
        diagnosis = communicable_disease_prediction([MUSCLE_ACHES, TIREDNESS, SORE_THROAT, RUNNY_NOSE, STUFFY_NOSE, FEVER, NAUSEA, VOMITING,
                                                     DIARRHEA, SHORTNESS_OF_BREATH, DIFFICULTY_BREATHING, LOSS_OF_TASTE, LOSS_OF_SMELL, 
                                                     ITCHY_NOSE, ITCHY_EYES, ITCHY_MOUTH, ITCHY_INNER_EAR, SNEEZING, PINK_EYE])

    st.success(diagnosis)
if __name__ == '__main__':
    main()



