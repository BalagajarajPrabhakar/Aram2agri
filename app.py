import cv2
import streamlit as st
import io
from matplotlib import image 
from matplotlib import pyplot as plt 
st.title("Hydroponic System for predictive maintenance using Artificial Intelligence (AI) to analyze plant growth , health, ect..")
st.header("Uploaded File")
s1=st.file_uploader
s2=st.file_uploader
uploaded_file = s1("Choose a ...thermal images", type=["jpg"])
temporary_location = False
if uploaded_file is not None:
    g = io.BytesIO(uploaded_file.read())  
    temporary_location = "testout_simple.jpg"
    with open(temporary_location, 'wb') as out: 
        out.write(g.read())
    out.close()
uploaded_file1 = s2("Choose a ...field image ", type=["jpg"])
temporary_location1 = False
if uploaded_file1 is not None:
    g = io.BytesIO(uploaded_file1.read())  
    temporary_location1 = "testout_simple1.jpg"
    with open(temporary_location1, 'wb') as out: 
        out.write(g.read())
    out.close()
def Capture_Event(event, x, y, flags, params):
     if event == cv2.EVENT_LBUTTONDOWN:
        plt.show() 
        st.title("Image with Point")
        st.image('testout_simple.jpg')
        st.write(f"({x}, {y})")
        return x,y
def detect():
      if __name__=="__main__":
            img = cv2.imread("testout_simple.jpg", 1)
            cv2.imshow('image', img)
            cv2.setMouseCallback('image', Capture_Event)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
def pp():
     d = image.imread('testout_simple1.jpg')
     st.title("Image with Point")
     fig, pp = plt.subplots()
     pp.imshow(d)
     pp.plot(38, 263, marker = 'o', ms = 10, mec = 'r', mfc = 'r')
     st.pyplot(fig)
if st.button("Agriculture field thermal image plot"):
         detect()
if st.button("Agriculture field image plot"):
          pp()


