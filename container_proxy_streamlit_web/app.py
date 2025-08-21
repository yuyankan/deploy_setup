import pandas as pd
# import myquery_db as query_db # 假设这个模块存在，但在此示例中不直接使用
import streamlit as st

st.set_page_config(page_title='SPC_ANALYZE_PLATFORM', layout="wide")

# --- 主标题部分 ---
header_text = 'SPC_ANALYZE_PLATFORM'
st.markdown(
    f"<div style='text-align: center; border: 0px solid red; padding: 10px; border-radius: 8px; margin-bottom: 20px;'>" # 外层 div，增加底部边距
    f"<span style='color:#00008B; font-weight:bold; font-size:50px;'>{header_text}</span>"
    f"</div>",
    unsafe_allow_html=True
)

# --- 定义一个辅助函数来创建可点击的带边框链接模块 ---
def create_styled_link_module(link_label, page_path, font_size='20px', border_color='grey'):
    """
    创建一个带有边框、居中且可点击的链接模块。
    通过 HTML <a> 标签模拟 st.page_link 的跳转。
    """
    # 使用 st.columns 来创建一个居中的容器
    # 调整比例可以控制链接模块的宽度和居中程度
    col_left, col_center, col_right = st.columns([1, 2, 1]) # 左右列为边距，中间列放内容

    with col_center:
        st.markdown(
            # 使用 <a> 标签包裹 div，使整个 div 可点击并跳转
            f"""
            <a href="{page_path}" target="_self" style="text-decoration: none; color: inherit;">
                <div style='text-align: center; border: 1px solid {border_color}; padding: 10px; border-radius: 8px; width: 100%; margin: 10px auto; background-color: #F8F8F8; cursor: pointer;'>
                    <span style='color:#00008B; font-weight:bold; font-size:{font_size};'>{link_label}</span>
                </div>
            </a>
            """,
            unsafe_allow_html=True
        )

# --- 组织你的链接模块 ---
# 第一个大模块：REAL TIME MONITOR
# 注意：你的原始代码中 page1_title 变量被重复使用，我将其修正为 `monitor_title`，
# 并且将其作为外部容器的标题，而不是每个子链接的标题。
c1, c2, c3, c4, c5 = st.columns([1.5, 2, 2,2,1.5])
with c1:
    st.markdown("<h3 style='text-align: center; color: #333;'>REAL TIME MONITOR</h3>", unsafe_allow_html=True) # 模块标题

# page1_text, page2_text, page3_text 将作为链接的标签
# 假设这些路径是你的 Streamlit 应用中的其他页面
monitor_page1_path = "./pages/app_maintain_spc_control.py" # 假设的路径
monitor_page2_path = "./pages/app_monitor_alarm.py" # 假设的路径
monitor_page3_path = "./pages/app_maintain_spec.py" # 假设的路径

create_styled_link_module('MONITOR_SPC', monitor_page1_path, font_size='20px')
create_styled_link_module('MONITOR_ALARM', monitor_page2_path, font_size='20px')
create_styled_link_module('TRACKING_FUNCTION', monitor_page3_path, font_size='20px')


# --- 第二个模块：SPC CONTROL SETUP (你的原始代码中单独的灰色框) ---
# 注意：这里 page1_text 被重用，我建议为变量使用更清晰的名称
spc_control_setup_link_text = 'SPC_CONTROL_SETUP'
spc_control_setup_page_path = './pages/app_maintain_spc_control.py' # 假设的路径

st.write("") # 添加一点垂直间距
st.markdown("<h3 style='text-align: center; color: #333;'>CONFIGURATION & MAINTENANCE</h3>", unsafe_allow_html=True) # 模块标题

create_styled_link_module(spc_control_setup_link_text, spc_control_setup_page_path, font_size='20px')

# --- 另一个模块：SPEC_MAINTAIN (你的原始代码中单独的 st.page_link) ---
spec_maintain_link_text = 'SPEC_MAINTAIN'
spec_maintain_page_path = './pages/app_maintain_spec.py'

create_styled_link_module(spec_maintain_link_text, spec_maintain_page_path, font_size='20px')

# --- 原始代码中剩余的 st.page_link (如果仍想使用，可以放在侧边栏等位置) ---
# st.page_link(page='./pages/app_maintain_spc_control.py', label='SPC_CONTROL_SETUP', icon="1️⃣")
# st.page_link(page='./pages/app_maintain_spec.py', label='SPEC_MAINTIAN', icon="2️⃣")

st.write("---")
st.write("请注意：为了实现自定义边框和居中样式，并且同时具备链接功能，我们使用了 HTML 的 `<a>` 标签包裹了自定义样式的 `div`。")
st.write("`st.page_link` 组件本身不直接支持这些复杂的样式嵌入。")