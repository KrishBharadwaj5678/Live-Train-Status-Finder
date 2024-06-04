import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import requests

# Defining Page Title,Icon
st.set_page_config(
    page_title="Train Tracker: Live Train Status Updates",
    page_icon="data:image/png;base64,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",
    menu_items={
        "About":"Welcome to Train Tracker, your one-stop solution for tracking train status in real-time. Our platform provides accurate and up-to-date information on train schedules, delays, and cancellations, helping you plan your journey better."
    }
)

st.write("<h3 style='color:#FF8A08;'>Plan your trip better with our accurate and reliable train status information.</h3>",unsafe_allow_html=True)
st.write("<h5>Get real-time updates on train schedules, delays, and cancellations with Train Tracker. Enter your train number to check its current status and stay informed about your journey.</h3>",unsafe_allow_html=True)

train_number=st.text_input("Enter the train number")

def getStatus():
    full_data=[]
    # Extracting Data
    url=requests.get(f"https://rappid.in/apis/train.php?train_no={train_number}")
    if(url.status_code==200):
        train_data=url.json()
        train_name=train_data["train_name"]
        train_message=train_data["message"]
        updated_time=train_data["updated_time"]
        st.write(f"<h4><span style='color:#FFA732'>Train Name :</span> {train_name}</h4>",unsafe_allow_html=True)
        st.write(f"<h4><span style='color:#FFA732'>Last Update :</span> {updated_time}</h4>",unsafe_allow_html=True)
        st.write(f"<h4><span style='color:#FFA732'>Train Information :</span> {train_message}</h4>",unsafe_allow_html=True)
        schedule_length=len(train_data["data"])
        arr=["Station Name","Distance","Arrival Time","Departure Time","Delay","Platform","Stoppage"]
        full_data.append(arr)
        for i in range(0,schedule_length):
            station_name=train_data["data"][i]["station_name"]
            distance=train_data["data"][i]["distance"]
            timing=train_data["data"][i]["timing"]
            delay=train_data["data"][i]["delay"]
            platform=train_data["data"][i]["platform"]
            halt=train_data["data"][i]["halt"]
            endtime=timing[0:5]
            startime=timing[5:]
            if(i==(schedule_length-1)):
                arr=[station_name,distance,"-","Destination",delay,platform,halt]
                full_data.append(arr)
            else:
                arr=[station_name,distance,f"{startime}",f"{endtime}",delay,platform,halt]
                full_data.append(arr)

        pd_Data=pd.DataFrame(
            full_data
        )
    
        data_html = pd_Data.to_html(index=False, header=False, escape=False)
        st.write(data_html, unsafe_allow_html=True)

    else:
        st.warning("Please Enter a Valid Train Number.")

btn=st.button("Check Live Status")
if btn:
    getStatus()
