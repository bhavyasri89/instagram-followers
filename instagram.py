import streamlit as st
import pickle
import numpy as np

with open('Model(1).pkl','rb') as f:
    model = pickle.load(f)


def predict(Likes,Saves,Comments,Shares,From_Home,From_Hashtags,From_Explore,From_Other):
    arr=np.array([[Likes,Saves,Comments,Shares,From_Home,From_Hashtags,From_Explore,From_Other]])
    prediction=model.predict(arr)[0]
    #print(f'EXpected Followers :- {prediction} hundreds')

    #input_data=np.array([[Likes,Saves,Comments,Shares,From_Home,From_Hashtags,From_Explore,From_Other]])

    return model.predict(arr)[0]

if __name__ == '__main__':
    st.header('Instagram followers prediction')

    col1,col2 =st.columns([2,1])

    Likes =  col1.slider('No.Of Likes ', max_value=10000,min_value=10,value=5)
    Shares= col1.slider('No.Of Shares',max_value=10000,min_value=10,value=5)
    Comments= col1.slider('No.Of Comments',max_value=10000,min_value=10,value=5)
    Saves= col1.slider('saves',max_value=10000,min_value=500,value=1000,step=250)
    From_Home= col1.slider('From_Home',max_value=10000,min_value=10,value=5)
    From_Hashtags=col1.slider(' From_Hashtags',max_value=10000,min_value=10,value=5)
    From_Other= col1.slider('From_Others',max_value=10000,min_value=10,value=5)
    From_Explore=col1.slider('From_Explore',max_value=10000,min_value=10,value=5)

    result=predict(Likes,Saves,Comments,Shares,From_Home,From_Hashtags,From_Explore,From_Other)
    col2.image('https://th.bing.com/th/id/OIP.prebR-lGpqIH8gcfODezzQAAAA?rs=1&pid=ImgDetMain',use_column_width=True)

    col2.write(f'The Predicted value is :{result} hundreds')
