import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

st.title('Анализ пропусков по болезни среди сотрудников')
uploaded_file = st.file_uploader("Загрузите CSV-файл с данными", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    data['Пол'] = data['Пол'].astype('category')
    data['Возрастная группа'] = np.where(data['Возраст'] > 35, 'Старше', 'Младше')

    st.subheader('Распределение пропусков по болезни по полу')
    fig, ax = plt.subplots()
    sns.violinplot(x='Пол', y='Количество больничных дней', data=data, ax=ax)
    st.pyplot(fig)

    st.subheader('Распределение пропусков по болезни по возрасту')
    fig2, ax2 = plt.subplots()
    sns.violinplot(x='Возрастная группа', y='Количество больничных дней', data=data, ax=ax2)
    st.pyplot(fig2)

    male_days = data[(data['Пол'] == 'М') & (data['Количество больничных дней'] > 2)]['Количество больничных дней']
    female_days = data[(data['Пол'] == 'Ж') & (data['Количество больничных дней'] > 2)]['Количество больничных дней']
    t_stat_gender, p_value_gender = stats.ttest_ind(male_days, female_days)

    older_days = data[(data['Возрастная группа'] == 'Старше')  & (data['Количество больничных дней'] > 2)]['Количество больничных дней']
    younger_days = data[(data['Возрастная группа'] == 'Младше')  & (data['Количество больничных дней'] > 2)]['Количество больничных дней']
    t_stat_age, p_value_age = stats.ttest_ind(older_days, younger_days)

    st.subheader('Результаты проверки гипотез')
    st.write(f"Гипотеза 1: t-статистика = {t_stat_gender:.4f}, p-значение = {p_value_gender:.4f}")
    st.write(f"Гипотеза 2: t-статистика = {t_stat_age:.4f}, p-значение = {p_value_age:.4f}")

    if p_value_gender < 0.05:
        st.write("Мужчины значительно чаще пропускают работу по болезни.")
    else:
        st.write("Различий между мужчинами и женщинами нет.")

    if p_value_age < 0.05:
        st.write("Сотрудники старше 35 лет чаще болеют и пропускают работу.")
    else:
        st.write("Различий между возрастными группами нет.")
