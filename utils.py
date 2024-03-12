from datetime import datetime, timedelta


def custom_weather_data(data: dict, city: str) -> str:
    target_date = (datetime.now() + timedelta(days=1)).strftime('%d.%m.%Y')
    res = [f'Погода на {target_date}, в городе {city}:\n']
    for k, v in data['forecast'][target_date].items():
        res.append(f'Время: {k} - Температура: {v["temp"]} °C, {v["weather"]}')
    return '\n'.join(res)




