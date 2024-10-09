import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title("Biểu đồ Matplotlib trên Streamlit")
    
    # Tạo dữ liệu mẫu
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Vẽ biểu đồ
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Đồ thị hàm sin')
    
    # Hiển thị biểu đồ trên Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()
