import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import requests

# Defining Page Title,Icon
st.set_page_config(
    page_title="Train Running Status",
    page_icon="🚅",
    menu_items={
        "About":"You can conveniently access the live status of Indian Railways trains through the Train Running Status."
    }
)

st.write("<h3>Train running status | Spot your train | Live train status</h3>",unsafe_allow_html=True)

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



