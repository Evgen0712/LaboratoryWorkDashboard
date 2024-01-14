import dash
import pandas as pd
from dash import html, dcc, dash_table

app = dash.Dash(__name__)

# Загружаем данные из CSV
url = 'https://raw.githubusercontent.com/Evgen0712/LaboratoryWorkDashboard/test/heart.csv'
df = pd.read_csv(url)

# Сортируем DataFrame по столбцу 'age' для получения топ-10 записей
top_df = df.sort_values(by='age', ascending=False).head(10)

app.layout = html.Div(children=[
    html.H1(children='Топ-10 по возрасту'),

    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in top_df.columns],
        data=top_df.to_dict('records'),
        style_table={'height': '400px', 'overflowY': 'auto'}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
