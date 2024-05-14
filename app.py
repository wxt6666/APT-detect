#Streamlit库构建的基础网页应用程序
import streamlit as st
import apt, training

from streamlit_option_menu import option_menu
#设置页面的配置，例如页面标题和布局方式
st.set_page_config(page_title='APT Attack Detection', layout='wide')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
PAGES = {
    'APT Detection': apt,
    'Traning': training,
}

def run():
    state = st.session_state
    #用户可以在 "APT Detection" 和 "Training" 之间进行选择，这两个选项分别对应不同的功能
    with st.sidebar:
        selection = option_menu(None, ["APT Detection", "Traning"],
                                icons=["list-task", 'gear'],
                                menu_icon="cast", default_index=0,
                                styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "red", "font-size": "20px"},
            "nav-link": {"font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#0B435E"},
        }
        )

        if 'tab' not in state:
            state['tab'] = selection
        else:
            state['tab'] = selection

    PAGES[state.tab].write(state)

if __name__ == '__main__':
    run()
