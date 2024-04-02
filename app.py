import streamlit as st

col1, col2 = st.columns([0.6, 0.4])

with col1:
   st.markdown(" ")
   st.markdown(" ")
   st.header(
            "😊Hi, my name is :orange[Chenxi]. I am a :blue[UX designer] based in :green[Seattle]☔️"
            )
   st.markdown(" ")
   with open("Chenxi Guo_Resume_UX designer.png", "rb") as file:
    btn = st.download_button(
            label="Download My Resume",
            data=file,
            file_name="Chenxi Guo_Resume_UX designer.png",
            mime="Chenxi Guo_image/png"
          )

with col2:
   st.image("/Users/guochenxi/Desktop/510/Techin510_lab1_2/Chenxi_image.JPG")

st.divider()

st.subheader("Education")

col1, col2 = st.columns([0.2, 0.8])
with col1:
   st.markdown(" ")
   st.image("/Users/guochenxi/Desktop/510/Techin510_lab1_2/University_of_Washington_Block_W_logo_RGB_brand_colors.svg")
with col2:
   st.markdown("     **University of Washington**")
   st.write("     Program: Master of Science in Technology Innovation")
   st.write("     2023-2025")
   st.markdown(" ")
   st.markdown(" ")
col1, col2 = st.columns([0.2, 0.8])
with col1:
   st.markdown(" ")
   st.image("/Users/guochenxi/Desktop/510/Techin510_lab1_2/2560px-Pratt_Institute_Logo.svg.png")
with col2:
   st.markdown("     **Pratt Institute**")
   st.write("     Program: Industrial Design")
   st.write("     2017-2021")


st.divider()

st.subheader("Work Experience")

st.subheader("UX Designer")
col1, col2 = st.columns([0.8, 0.2])

with col1:
   st.write("Bosch Information Technology Service Co.")

with col2:
   st.write("Mar - July 2023")
  
st.markdown("- Design an end-to-end contract management system for B2B business, including document management and cross-department communication features, improving work & communication efficiency by 2 times.")
st.markdown("- Crafted and iterated a UX project in accordance with the Bosch design system, with user satisfaction rates of 4.5/5.0 and UI satisfaction rates of 4.3/5.0.")
st.markdown("- Organized hackathons and UX training activities, successfully sell one business with clients, promoting business digital transformation.")

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:40px;
}
</style>
''', unsafe_allow_html=True)

st.markdown(" ")

st.subheader("Product Designer")

col1, col2 = st.columns([0.8, 0.2])

with col1:
   st.write("Shanghai Chicmax Cosmetics Company")

with col2:
   st.write("Jun 2021 - Jun 2022")
  
st.markdown("- Designed and launched 20+ product in the market in 12 months; Collaborated with marketing teams and manufactures to establish trends and design feasibility.")
st.markdown("- Conducted competitor analysis and market research over 50+ skincare products, to explore user needs for skincare products.")
st.markdown("- Led a team of designers to enhance the design of 6 established products; elaborate on new visual languages and brand style.")

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:40px;
}
</style>
''', unsafe_allow_html=True)

st.divider()


st.write("Linkedin: www.linkedin.com/in/cguoo")

st.write("Skills: user research, graphic design")

st.write("Hobby: drawing🖼, hiking🚶, traveling🛫")

st.write("Pet: Quanquan Cat🐱")

