import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write("プログレスバーの表示")
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i +1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done!!!!!'

st.write("DataFrame")


""" グラフを作る"""
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a','b','c']
 )
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

""" 表を作る """
st.write(df)
# 表のサイズを選ぶなど引数を使う場合
st.dataframe(df,width=100, height=100)
#　最大値をハイライト
st.dataframe(df.style.highlight_max(axis=0))

# static 静的なテーブルの時はtable
st.table(df)

""" マップを作る  """
# 緯度けいど
df = pd.DataFrame(
    np.random.rand(100, 2)/[50,50] +[35.69, 139.70],
    columns=['lat','lon']
 )
st.map(df)

st.write("Display Image")

if st.checkbox('Show Image'):
    img = Image.open('ダウンロード.jpeg')
    st.image(img, caption = 'Ted', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    range(1, 11)
)

"あなたの好きな数字は、",option,"です"

st.sidebar.write('Interactive Widgets')
# sidebarと言えると左側のサイドバーにできる
option2 = st.sidebar.text_input('あなたの趣味を教えてください')
"あなたの趣味は",option2,"です"

condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
'コンディション；',condition

# 2カラム
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')