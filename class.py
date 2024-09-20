import streamlit as st

class Buttons:
    def __init__(self,num):
        if st.button(f"Button Number is {num}"):
            self.calc(num*num)

    def calc(self, num):
        if num % 2 == 0:
            st.balloons()
        else:
            st.snow()

for i in range(10):
        Buttons(i)