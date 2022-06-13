'''Log File Analyser'''
'''Ideaforge Propulsion and Flight log analyser script'''

import pandas as pd
import numpy as np
import streamlit as st
import plotly as px
import matplotlib.pyplot as plt
from operator import index
from turtle import right

st.title("LOG FILES ANALYZER")


log_type = st.selectbox("Select the Log File type", ('Select...','RC_Benchmark','Flight_Logs','PX4_Logs'), index = 0)

def disp_rawdata(data_list):
    for i in range(len(data_list)):
        # data_list[i].dropna(how = 'any', inplace = True)
        st.write(data_list[i])
                     
def disp_graph(data_file,x_axis_att,y_axis_att):
    
    x_data_list = []
    y_data_list = []
    
    for data_list_x in data_file:
        x_data_list.append(data_list_x[x_axis_att])

    for data_list_y in data_file:
        y_data_list.append(data_list_y[y_axis_att])
    
    x_axis = list(zip(*x_data_list))
    y_axis = list(zip(*y_data_list))
    
    fig = plt.figure(figsize=[6,3])
    plt.plot(x_axis,y_axis)
        
    title = st.text_input("Enter the Title for the Graph:")
    legend =[]
    for i in range(len(data_file)):
        legend.append(st.text_input("Enter legend for graph %i:"%(i), key = legend))
    plt.title(title)
    plt.legend(legend, loc = "lower right")
    plt.xlabel(x_axis_att)
    plt.ylabel(y_axis_att)
    st.pyplot(fig)
    
    
def Load_data():
    # file_loc = []
    data_file = []
    file_list = []
    
    file_list = st.file_uploader("Upload file",accept_multiple_files= True)
    for file in file_list:
        data_file.append(pd.read_csv(file, index_col= "Time (s)"))
        
    # for i in range(n):
    #         loc = st.text_input(r"File Location_%i"%(i+1))
    #         file_loc.append(loc)
    # # while file_loc != None:
    # try:
    #     for loc in file_loc:
    #         data_file.append(pd.read_csv(loc, index_col= "Time (s)"))
    # except FileNotFoundError:
    #     #do nothing
    #     pass

    if st.checkbox("Show Raw Data", False):
        st.subheader("\tRaw Data")
        # st.write(data_file)
        disp_rawdata(data_file)
    st.subheader("Analyzing......")
    try :
        x_axis_val = st.selectbox("Select X-axis attribute:",data_file[0].columns,index=0)
        y_axis_val = st.selectbox("Select Y-axis attribute:",data_file[0].columns,index=0)
        disp_graph(data_file, x_axis_val, y_axis_val)
    except IndexError:
        pass
    return data_file
    

if log_type == 'RC_Benchmark':
    
    st.subheader("Analyzing RC bench mark Logs")
    # n = st.number_input("Enter the number of files to be analysed:", min_value=0)
    data_file = Load_data()
    
    
    
elif log_type =='Flight_Logs':
    st.subheader("Analyzing Flight Logs")

elif log_type =='PX4_Logs':
    st.subheader("Analyzing PX4_Logs")
