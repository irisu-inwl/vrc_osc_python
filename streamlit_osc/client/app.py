"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""

import argparse
import random
import time
import os

from pythonosc import udp_client
import streamlit as st


@st.cache
def load_osc_client():
    host = os.environ.get("HOST", "localhost")
    port = os.environ.get("PORT", 9001)
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default=host,
        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=port,
        help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)
    return client


st.session_state.client = load_osc_client()

def send_message_to_vrchat():
    endpoint = st.session_state.endpoint
    parameter = st.session_state.parameter
    print(endpoint, parameter)
    st.session_state.client.send_message(endpoint, parameter)

st.session_state.endpoint = st.text_input("OSC Endpoint", "/hello")
param_type = st.radio("Parameter Type", ("int", "float"))
match param_type:
    case "float": 
        st.session_state.parameter = st.slider("Parameter to send", 0.0, 1.0, 0.0)
    case "int":
        st.session_state.parameter = st.slider("Parameter to send", 0, 10, 0)
st.button("send", on_click=send_message_to_vrchat)