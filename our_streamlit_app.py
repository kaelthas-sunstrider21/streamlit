## Step 1: Install Stremalit
## pip install streamlit
import streamlit as st
#
# ## Step 2 Let's put an image
# ## Make the default width setting span the entire screen
st.set_page_config(layout="wide")
random_url = "https://assets.phenompeople.com/CareerConnectResources/prod/HONEUS/images/1920-568-coding-blog-1616781712070.png"
st.image(random_url, use_column_width="always")
#
# ## Step 3: Let's Write Some Text
st.title("Streamlit 3000")
st.markdown("# Streamlit 6000")
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
# ## Step 4: Let's display a Dataframe
import pandas as pd

df = pd.read_csv("countries of the world.csv", decimal=",")
df
# ## Btw you can easily print debug while working
st.write(df.dtypes.values.tolist()[2:4])
# ## Step 5: Let's get interactive
cols = df.columns.values.tolist()
cols = [c for c, t in zip(cols, df.dtypes.values.tolist())
        if "float" in str(t).lower() or "int" in str(t).lower()]
our_chosen_col = st.selectbox(label="Select A Column", options=cols)

# ## Step 6: Let's use the value
c1, c2, c3 = st.columns(3)
with c1:
    st.header("Mean")
    st.metric(label="Mean", value=df[our_chosen_col].mean().round(1),
              delta=None)
with c2:
    st.header("Median")
    st.metric(label="Median",
              value=df[our_chosen_col].median().round(1),
              delta=(df[our_chosen_col].mean() - df[
                  our_chosen_col].median()).round(1))
with c3:
    st.header("Sum")
    st.metric(label="Sum", value=df[our_chosen_col].sum().round(1))

# ## Step 7: All of Plotly, Matplolib, Seaborn and others do work!
# ## pip install plotly
import plotly.express as px

fig = px.scatter(df, x=our_chosen_col, y="Area (sq. mi.)",
                 # size="pop",
                 color="Region",
                 hover_name="Country",
                 log_x=True)
st.plotly_chart(fig, use_container_width=True)
#
# ## Step 8: Just to show of
df_lat = pd.read_csv("country_lat_lon.csv")
df_lat.columns = ["_", "Country", "lat", "lon"]
df["Country"] = df["Country"].apply(lambda x: x.strip())
## use our colum again and select only the top-10
df = pd.merge(
    df.sort_values(our_chosen_col, ascending=False).head(30), df_lat,
    on="Country", how='left').dropna()
st.map(df)
