import os
import requests
import dash
from dash import html

app = dash.Dash(__name__)
API_URL = "http://api:8000/example_db_func"

try:
    resp = requests.get(API_URL)
    resp.raise_for_status()
    data = resp.json()
    item_string = data.get("string_ex", "N/A")
    item_id = data.get("id", "N/A")
    item_name = data.get("name", "N/A")
except Exception as e:
    print("❌ Failed to get API data:", e)
    item_string = "Error"
    item_id = "Error"
    item_name = "Error"

app.layout = html.Div([
    html.H1("Item from Database"),
    html.Div(f"string_ex: {item_string}"),
    html.Div(f"ID: {item_id}"),
    html.Div(f"Name: {item_name}")
])

server = app.server