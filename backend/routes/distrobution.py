from datetime import datetime

from app import app
from han_port.han_port_data import get_han_data
from nilm.nilm import get_applience_consumption


@app.get("/get_distrobution")
def get_distrobution():
    detail_data = get_han_data()

    from_date = datetime.strptime(detail_data[0][1], "%Y-%m-%DT:%M:&SS")
    to_date = datetime.strptime(detail_data[-1][1], "%Y-%m-%DT:%M:&SS")

    print(get_applience_consumption(from_date, to_date))

    return "helloo"
