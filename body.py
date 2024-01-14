import dash
import pandas as pd
import plotly.express as px
from dash import html, dcc, dash_table

# Загрузка данных
url = 'https://raw.githubusercontent.com/Evgen0712/LaboratoryWorkDashboard/test/heart.csv'
df = pd.read_csv(url)

# Определение всех графиков
# Гистограмма возрастов
fig_histogram_of_ages = px.histogram(df, x='Age', nbins=10, title='Распределение возрастов')

# Диаграмма рассеяния пульса и артериального давления
fig_scatter_pulse_bp = px.scatter(df, x='RestingBP', y='MaxHR', color='Sex', title='Пульс vs. артериальное давление')

# Круговая диаграмма по полу
fig_pie_gender = px.pie(df, names='Sex', title='Соотношение мужчин и женщин')

# Линейный график изменения холестерина по возрасту
fig_line_cholesterol_age = px.line(df, x='Age', y='Cholesterol', title='Изменение холестерина по возрасту')

# Диаграмма рассеяния зависимости уровня сердечных заболеваний от возраста
fig_scatter_heart_disease_age = px.scatter(
    df,
    x='Age',
    y='HeartDisease',
    title='Зависимость уровня сердечных заболеваний от возраста',
    labels={'HeartDisease': 'Сердечные заболевания', 'Age': 'Возраст'},
    trendline='ols',
)

# Инициализация приложения Dash
app = dash.Dash(__name__)

# Определение макета приложения
app.layout = html.Div([
    # Заголовок панели
    html.H1('Информационная панель о сердечных заболеваниях'),
    
    # Описание панели
    html.P('Данный дашборд представляет собой визуализацию данных по сердечным заболеваниям. Включает в себя статистику по возрасту, полу, пульсу, артериальному давлению и холестерину'),

    # Раздел с табличными данными
    html.Div([
        # Компонент DataTable для отображения табличных данных
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            page_size=10,
            style_table={'height': '400px', 'overflowY': 'auto'},
            filter_action='native',
            sort_action='native',
            sort_mode='multi'
        )
    ], style={'padding': '10px'}),

    # Раздел с диаграммами рассеяния
    html.Div([
        dcc.Graph(id='scatter_heart_disease_age', figure=fig_scatter_heart_disease_age),
    ], style={'padding': '10px'}),

    # Раздел с группировкой графиков для анализа возрастной структуры
    html.Div([
        dcc.Graph(figure=fig_histogram_of_ages),
        dcc.Graph(figure=fig_scatter_pulse_bp),
    ], style={'display': 'flex', 'padding': '10px'}),

    # Раздел с графиками по полу и холестерину
    html.Div([
        dcc.Graph(figure=fig_pie_gender),
        dcc.Graph(figure=fig_line_cholesterol_age),
    ], style={'display': 'flex', 'padding': '10px'})
])

# Запуск сервера приложения Dash
if __name__ == '__main__':
    app.run_server(debug=True)
