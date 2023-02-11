import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')
st.write("DataFrame")

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.write(df.style.highlight_max(axis=0))

"""
# 賞
## 見出し
### コミ出し

```
st.title('Streamlit 超入門')
st.write("DataFrame")
```

"""

df = pd.DataFrame(np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
                columns=['lat', 'lon'])

st.dataframe(df)

st.map(df)

if st.checkbox('Show Image'):
    img = Image.open("/Users/ishiishuto/Desktop/スクリーンショット 2022-01-19 17.53.31.png")
    st.image(img, caption='メタグロス', use_column_width=True)

option = st.sidebar.selectbox("好きな数字　",list(range(10)))
condition = st.sidebar.slider("アナとの調子", 0, 100, 50)

f"あなたの好きな数字は{option}です。"
f"コンディション: {condition}"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration: {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)