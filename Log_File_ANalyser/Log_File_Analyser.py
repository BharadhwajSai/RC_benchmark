'''Log File Analyser'''
'''Ideaforge Propulsion and Flight log analyser script'''
# '''Developed by Matha Sai Bharadhwaj'''

from ctypes import sizeof
import pandas as pd
import numpy as np
import streamlit as st
# import plotly as px
import matplotlib.pyplot as plt
from operator import index
import tkinter as tk
from turtle import right
from scipy import interpolate

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
    
    # st.write(x_axis)
    # st.write(y_axis)
    # New Data Set
    # x_new = np.array(x_axis)
    # y_new = np.array(y_axis)
    
    # X_axis = np.linspace(x_new.min(), x_new.max())
    # X_Y_Spline = interpolate.make_interp_spline(x_new, y_new)
    # Y_axis = X_Y_Spline(X_axis)
    
    fig = plt.figure(figsize=[6,3])
    plt.plot(x_axis,y_axis)
        
    title = st.text_input("Enter the Title for the Graph:")
    legend =[]
    for i in range(len(data_file)):
        legend.append(st.text_input("Enter legend for graph %i:"%(i), key = legend))
    plt.title(title)
    plt.legend(legend, loc = "best")
    plt.xlabel(x_axis_att)
    plt.ylabel(y_axis_att)
    st.pyplot(fig)
    
    
def Load_data():
    # file_loc = []
    data_file = []
    file_list = []
    try:    
        file_list = st.file_uploader("Upload file",accept_multiple_files= True)
        for file in file_list:
            data_file.append(pd.read_csv(file, index_col= "Time (s)", error_bad_lines=False))
            
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
        # k = []
        # for file in data_file:
        #     k.append(sizeof(file.columns))
        # if max(k)>min(k):
        #     index_column = max(k)
        # else:
        #     index_column = min(k)
        try :
            x_axis_val = st.selectbox("Select X-axis attribute:",data_file[0].columns,index=0)
            y_axis_val = st.selectbox("Select Y-axis attribute:",data_file[0].columns,index=0)
            #ToDo RCB1580 and RCB1520
            #ToDo multiple graphs from a single file
            disp_graph(data_file, x_axis_val, y_axis_val)
        except IndexError:
            #st.error("Index Error")
            pass
        return data_file
    except UnicodeDecodeError:
        st.error("Not a valid file")
    # except ValueError:
    #     st.error("Value Error")   

if log_type == 'RC_Benchmark':
    
    st.subheader("Analyzing RC bench mark Logs")
    # n = st.number_input("Enter the number of files to be analysed:", min_value=0)
    data_file = Load_data()
    
    
    
elif log_type =='Flight_Logs':
    st.subheader("Analyzing Flight Logs")

elif log_type =='PX4_Logs':
    st.subheader("Analyzing PX4_Logs")



#TODO Exception for any other file type
# Done - used an Unicodedecode error exception-> ToDo -> Check for any other exceptions/errors
