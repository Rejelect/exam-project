import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('22.csv')

column_descriptions = {
    "Unnamed: 0": "Har bir qator uchun indeks yoki identifikator.",
    "Employee ID": "Har bir xodim uchun noyob identifikator.",
    "Age": "Xodimning yoshi.",
    "Gender": "Xodimning jinsi.",
    "Years at Company": "Xodim kompaniyada ishlagan yillar soni.",
    "Job Role": "Xodimning kompaniyadagi roli yoki lavozimi.",
    "Monthly Income": "Xodimning oylik maoshi.",
    "Work-Life Balance": "Xodimning ish-hayot balansi bahosi.",
    "Job Satisfaction": "Xodimning ishidan qoniqish darajasi.",
    "Performance Rating": "Xodimning ish samaradorligi reytingi.",
    "Number of Promotions": "Xodim olgan lavozim ko‘tarilishlar soni.",
    "Overtime": "Xodimning ortiqcha ishlashi ko'rsatiladi.",
    "Distance from Home": "Xodimning uyi va ish joyi orasidagi masofa.",
    "Education Level": "Xodimning oliy ta'lim darajasi.",
    "Marital Status": "Xodimning oilaviy holati.",
    "Number of Dependents": "Xodimning qaramog'idagi shaxslar soni.",
    "Job Level": "Kompaniyada xodimning lavozimi yoki darajasi.",
    "Company Size": "Kompaniya hajmi.",
    "Company Tenure": "Xodimning kompaniyadagi xizmat muddati.",
    "Remote Work": "Xodim masofadan ishlayotganligini ko'rsatadi.",
    "Leadership Opportunities": "Rahbarlik imkoniyatlari.",
    "Innovation Opportunities": "Innovatsion loyihalar yoki vazifalar imkoniyatlari.",
    "Company Reputation": "Kompaniyaning xodim tomonidan qabul qilingan obro'si.",
    "Employee Recognition": "Xodimning ishdagi yutuqlari uchun tan olinish.",
    "Attrition": "Xodim kompaniyani tark etganligini ko'rsatadi."
}

st.title("Xodimlar Ma'lumotlari Dashboard")

menu = st.sidebar.selectbox('Menu', ["Ma'lumotlar Haqida",  'Null Qiymatlar', 'Grafiklar',])

sns.set_theme(style="whitegrid")
color_palette = sns.color_palette(["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"])

if menu == "Ma'lumotlar Haqida":
    st.header("Ma'lumotlar Haqida")
    st.write("Ushbu dataset xodimlar haqida ma'lumotlarni o'z ichiga oladi.")
    
    st.subheader('Sutun Tavsifi')
    for column, description in column_descriptions.items():
        st.write(f"**{column}**: {description}")

    st.subheader("Dataset Ma'lumotlari")
    st.write(f"Jami qatorlar soni: {df.shape[0]}")
    st.write(f"Jami ustunlar soni: {df.shape[1]}")
    st.write(df.dtypes)
    
    st.subheader('Namunaviy Ma\'lumotlar')
    st.write(df.head())


elif menu == 'Null Qiymatlar':
    st.header('Null Qiymatlarni To\'ldirish')
    st.write("**Har bir ustun uchun null qiymatlar soni:**")
    null_counts = df.isnull().sum()
    st.dataframe(null_counts[null_counts > 0].reset_index().rename(columns={'index': 'Ustun', 0: 'Null Qiymatlar'}))
    
    column_to_fill = st.selectbox('To\'ldiriladigan Ustunni Tanlang', df.columns)
    
    grouping_column = st.selectbox('Guruplash uchun Ustunni Tanlang', df.columns)
    
    fill_method = st.selectbox('To\'ldirish Usulini Tanlang', ['Mode', 'Median', 'Mean'])
    
    null_counts_before = df[column_to_fill].isnull().sum()
    
    if st.button('To\'ldirishni Boshla'):
        if fill_method == 'Mode':
            df[column_to_fill] = df.groupby(grouping_column)[column_to_fill].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else np.nan))
        elif fill_method == 'Median':
            df[column_to_fill] = df.groupby(grouping_column)[column_to_fill].transform(lambda x: x.fillna(x.median()))
        elif fill_method == 'Mean':
            df[column_to_fill] = df.groupby(grouping_column)[column_to_fill].transform(lambda x: x.fillna(x.mean()))
        
        null_counts_after = df[column_to_fill].isnull().sum()
        
        st.write(f"**To\'ldirishdan oldin**:")
        st.write(f"Null qiymatlar soni: {null_counts_before}")
        
        st.write(f"**To\'ldirishdan keyin**:")
        st.write(f"Null qiymatlar soni: {null_counts_after}")

        unique_values_before = df[column_to_fill].dropna().nunique()
        df[column_to_fill] = df[column_to_fill].fillna(method='bfill').fillna(method='ffill')
        unique_values_after = df[column_to_fill].nunique()
        
        

        fig, ax = plt.subplots(1, 2, figsize=(18, 6))
        
        sns.histplot(df[column_to_fill].dropna(), kde=True, ax=ax[0], color=color_palette[0])
        ax[0].set_title('To\'ldirishdan oldin')
        ax[0].set_xlabel(column_to_fill)
        ax[0].set_ylabel('Ta\'siri')
        
        sns.histplot(df[column_to_fill], kde=True, ax=ax[1], color=color_palette[1])
        ax[1].set_title('To\'ldirishdan keyin')
        ax[1].set_xlabel(column_to_fill)
        ax[1].set_ylabel('Ta\'siri')

        st.header('Null Qiymatlarni O\'chirish')
    
    column_to_remove_nulls = st.selectbox('Null qiymatlarni o\'chirish uchun ustunni tanlang', df.columns)
    
    if st.button('Null Qiymatlarni O\'chirish'):


        df_cleaned = df.dropna(subset=[column_to_remove_nulls])
        
        rows_before = len(df)
        rows_after = len(df_cleaned)
        
        st.write(f"**Tanlangan ustunda mavjud null qiymatlar soni**: {df[column_to_remove_nulls].isnull().sum()}")
        st.write(f"**Qatnashuvchi satrlar soni (Tozalashdan oldin)**: {rows_before}")
        st.write(f"**Qatnashuvchi satrlar soni (Tozalashdan keyin)**: {rows_after}")
        
        st.write("**Tozalangan Ma'lumotlar**:")
        st.dataframe(df_cleaned.head())

        fig, ax = plt.subplots(1, 2, figsize=(18, 6))
        
        sns.histplot(df[column_to_remove_nulls].dropna(), kde=True, ax=ax[0], color=color_palette[0])
        ax[0].set_title('To\'zalashdan oldin')
        ax[0].set_xlabel(column_to_remove_nulls)
        ax[0].set_ylabel('Ta\'siri')
        
        sns.histplot(df_cleaned[column_to_remove_nulls], kde=True, ax=ax[1], color=color_palette[1])
        ax[1].set_title('To\'zalashdan keyin')
        ax[1].set_xlabel(column_to_remove_nulls)
        ax[1].set_ylabel('Ta\'siri')
        
        st.pyplot(fig)
elif menu == 'Grafiklar':
    st.header('Grafiklar')
    
    tab1, tab2, tab3 = st.tabs(["Countlar", "Statistik Grafiklar", "Advenced Grafiklar"])
    
    with tab1:
        st.subheader('Hisoblar')
        
        st.subheader('Jins Ta\'qsimoti')
        st.write("Ushbu count plot xodimlar jinsga ko'ra taqsimotini ko'rsatadi.")
        fig, ax = plt.subplots()
        sns.countplot(x='Gender', data=df, ax=ax, palette=color_palette)
        ax.set_title('Jins Ta\'qsimoti', fontsize=15)
        st.pyplot(fig)

        st.subheader('Ish-Hayot Balansi va Ishdan Qoniqish Taqqoslashi')
        st.write("Ushbu count plot ish-hayot balansi reytinglari va ishdan qoniqish darajalari o'rtasidagi munosabatni ko'rsatadi.")
        fig, ax = plt.subplots()
        sns.countplot(x='Work-Life Balance', hue='Job Satisfaction', data=df, ax=ax, palette=color_palette)
        ax.set_title('Ish-Hayot Balansi va Ishdan Qoniqish Taqqoslashi', fontsize=15)
        st.pyplot(fig)

    with tab2:
        st.subheader('Yosh Ta\'qsimoti')
        st.write("Ushbu histogram tanlangan yosh oralig'idagi xodimlar yoshini taqsimotini ko'rsatadi.")
        min_age = int(df['Age'].min())
        max_age = int(df['Age'].max())
        age_range = st.slider('Yosh Oraliqni Tanlang', min_age, max_age, (min_age, max_age))
        
        filtered_data = df[(df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1])]
        
        median_age = filtered_data['Age'].median()
        mode_age = filtered_data['Age'].mode()
        mean_age = filtered_data['Age'].mean()
        
        avg_income = filtered_data['Monthly Income'].mean()
        max_income = filtered_data['Monthly Income'].max()
        min_income = filtered_data['Monthly Income'].min()
        
        st.write(f"**Yosh Oralig‘i**: {age_range[0]} - {age_range[1]}")
        st.write(f"**Median (Median Yosh)**: {median_age:.2f}")
        st.write(f"**Mode (Eng Ko‘p Takrorlanadigan Yosh)**: {mode_age[0]:.2f}")
        st.write(f"**Mean (O‘rtacha Yosh)**: {mean_age:.0f}")
        st.write(f"**Oylik Maosh (O‘rtacha)**: {avg_income:.2f}$")
        st.write(f"**Oylik Maosh (Eng Yaxshi)**: {max_income:.2f}$")
        st.write(f"**Oylik Maosh (Eng Kam)**: {min_income:.2f}$")
  

        fig, ax = plt.subplots()
        sns.histplot(filtered_data['Age'].dropna(), kde=True, ax=ax, color=color_palette[0])
        ax.set_title('Yosh Ta\'qsimoti', fontsize=15)
        st.pyplot(fig)

        
        st.subheader('Yoshning Oylik Maoshga Ta’siri')
        st.write("Ushbu chiziqli grafik yoshning oylik maoshga qanday ta’sir qilishini ko'rsatadi.")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        df_sorted = df.sort_values(by='Age')
        sns.lineplot(x='Age', y='Monthly Income', data=df_sorted, ax=ax, color=color_palette[2])
        ax.set_title('Yoshning Oylik Maoshga Ta’siri', fontsize=15)
        ax.set_xlabel('Yosh')
        ax.set_ylabel('Oylik Maosh')
        st.pyplot(fig)

        st.subheader('Oylik Maosh va Ishdagi Mamnuniyat')
        st.write("Ushbu box plot oylik maoshning ishdagi mamnuniyat darajasiga qanday ta’sir qilishini ko'rsatadi.")
        satisfaction_order = ["Very High", "High", "Medium", "Low"]


        df['Job Satisfaction'] = pd.Categorical(df['Job Satisfaction'], categories=satisfaction_order, ordered=True)
        
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.boxplot(x='Monthly Income', y='Job Satisfaction', data=df, ax=ax, palette=color_palette)
        ax.set_title('Oylik Maosh va Ishdagi Mamnuniyat', fontsize=15)
        ax.set_xlabel('Oylik Maosh')
        ax.set_ylabel('Ishdagi Mamnuniyat')
        st.pyplot(fig)

        st.subheader('Turmush Holati va Ishdan Qoniqish')
        st.write("Ushbu barplot turli turmush holatlari uchun ishdan qoniqish darajasini ko'rsatadi.")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(x='Marital Status', hue='Gender', data=df, palette=color_palette, ax=ax)
        ax.set_title('Turmush Holati va Ishdan Qoniqish', fontsize=15)
        ax.set_xlabel('Turmush Holati')
        ax.set_ylabel('Ishdan Qoniqish')
        plt.xticks(rotation=45)
        st.pyplot(fig)

        st.subheader('Soha va Oylik Maosh Taqqoslashi')
        st.write("Ushbu box plot turli lavozimlardagi oylik maoshlarning taqsimotini ko'rsatadi.")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(x='Job Role', y='Monthly Income', data=df, ax=ax, palette=color_palette)
        plt.xticks(rotation=90)
        ax.set_title('Soha va Oylik Maosh Taqqoslashi', fontsize=15)
        st.pyplot(fig)
    
    with tab3:
        st.subheader('Advenced Grafiklar')
        
        st.subheader('Korrelatsiya Heatmap')
        st.write("Ushbu heatmap datasetdagi turli raqamli ustunlar o'rtasidagi korrelatsiya koeffitsientlarini ko'rsatadi.")
        fig, ax = plt.subplots(figsize=(10, 8))
        numeric_df = df.select_dtypes(include=['float64', 'int64']) 
        correlation_matrix = numeric_df.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
        ax.set_title('Korrelatsiya Heatmap', fontsize=15)
        st.pyplot(fig)

        st.subheader('Lavozimlar Bo‘yicha Oylik Maoshning Violin Ploti')
        st.write("Ushbu violin plot turli lavozimlarda oylik maoshlarning taqsimotini ko'rsatadi.")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.violinplot(x='Job Level', y='Monthly Income', data=df, ax=ax, palette=color_palette)
        plt.xticks(rotation=90)
        ax.set_title('Lavozimlar Bo‘yicha Oylik Maoshning Violin Ploti', fontsize=15)
        st.pyplot(fig)

        

       

