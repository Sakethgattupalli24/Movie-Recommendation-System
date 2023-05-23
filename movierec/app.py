import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distances=similarity[index]
    li=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    l=[]
    for i in li:
        l.append(movies.iloc[i[0]].title)
    return l
movies_dict=pickle.load(open('moviesdict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.title('Movie Recommendation ')
option=st.selectbox('select movie',movies['title'].values)
if st.button('Recommend'):
    m=recommend(option)
    for i in m:
        st.write(i)


