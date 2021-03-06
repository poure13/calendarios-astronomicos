import sys
from convertdate import hebrew
from convertdate import islamic
from convertdate import julianday
from flask import Flask, request
from pyluach import hebrewcal

app = Flask(__name__)


def get_islamic(year, month, day):
    return islamic.from_gregorian(year, month, day)


def get_hebrew(year, month, day):
    return hebrew.from_gregorian(year, month, day)


def get_hebrew_month(year, month, day):
    year, month, _ = get_hebrew(year, month, day)
    return hebrewcal.Month(year, month).name


def get_islamic_month(year, month, day):
    year, month, _ = get_islamic(year, month, day)
    islamic_months = [
        "Muharram",
        "Safar",
        "Rabi I",
        "Rabi II",
        "Yumada I",
        "Yumada II",
        "Rayab",
        "Sha'bán",
        "Ramadán",
        "Shawwal",
        "Du al-Qa'da",
        "Du al-Hiyya",
    ]
    return islamic_months[month - 1]


def convert_format(year, month, day):
    return "Fecha con <strong>formato ISO-8601</strong>: <br>{}-{}-{}<br>".format(year, month, day)


def convert_hebrew(year, month, day):
    return "Fecha en el <strong>calendario judío</strong>: <br>{0} {1} ({3}) {2}<br>".format(
        *get_hebrew(year, month, day), get_hebrew_month(year, month, day)
    )


def convert_islamic(year, month, day):
    return "Fecha en el <strong>calendario musulmán</strong>: <br>{0} {1} ({3}) {2}<br>".format(
        *get_islamic(year, month, day), get_islamic_month(year, month, day)
    )


def convert_julianday(year, month, day):
    return "Día de la <strong>data juliana</strong>: <br>{}".format(
        julianday.from_gregorian(year, month, day)
    )


@app.route("/", methods=["GET", "POST"])
def easy_calendar():
    if request.method == "POST":
        year, month, day = str(request.form["gregorian"]).split("-")
        year, month, day = int(year), int(month), int(day)
        return """<link href="https://fonts.googleapis.com/css2?family=Merriweather&display=swap" rel="stylesheet"> 
       <body style="background-color:#ffddd3;color:#522959; font-family: 'Merriweather', serif;">
        <div style="margin-top: 15%;margin-left: auto;margin-right: auto;width: 45%;border: 1.5px solid #522959;padding: 10px;text-align: center;background-color:white;">
      <img style="max-width:7%;height:auto;" src="https://openmoji.org/data/color/svg/1F5D3.svg" alt="Calendarios astronomicos">
      <br><br>
      {}<br/>{}<br/>{}<br/>{} </br></br><button style="color:#522959;font-family: 'Merriweather', serif;" onclick="location.href='/'" type="button">
         Volver</button><br></div><div style="margin-top: 10%;margin-left: auto;margin-right: auto;width: 18%;text-align: center;border: 1.5px solid #522959;padding: 10px;text-align: center;background-color:white;">
        <small>¡Gracias por usar Calendarios Astronómicos!</small>
      </div>
      """.format(
            convert_format(year, month, day),
            convert_hebrew(year, month, day),
            convert_islamic(year, month, day),
            convert_julianday(year, month, day),
        )

    else:
        return """
        <link href="https://fonts.googleapis.com/css2?family=Merriweather&display=swap" rel="stylesheet"> 
       <body style="background-color:#ffddd3;color:#522959; font-family: 'Merriweather', serif;">
        <div style="margin-top: 15%;margin-left: auto;margin-right: auto;width: 45%;border: 1.5px solid #522959;padding: 10px;text-align: center;background-color:white;">
      <img style="max-width:7%;height:auto;" src="https://openmoji.org/data/color/svg/1F5D3.svg" alt="Calendarios astronomicos">
      <h1 style="margin-top: 1%;">Calendarios astronómicos</h1>
      <p>Es un conversor de fechas con capacidad de transformar las fechas del calendario gregoriano al calendario judío, al calendario musulmán y a la data juliana. <br><br> También devuelve la fecha en formato ISO-8061.</p>
      <form action="/" method="post">
        <input style="color:#522959;font-family: 'Merriweather', serif;" type="date" id="gregorian" name="gregorian" required></br></br>
        <input style="color:#522959;font-family: 'Merriweather', serif;" type="submit" value="Convertir">
      </form>
      </div>
      <div style="margin-top: 15%;margin-left: auto;margin-right: auto;width: 12%;text-align: center;border: 1.5px solid #522959;padding: 10px;text-align: center;background-color:white;">
        <small>Paula González Falqué - USC</small>
      </div>
      """


def run_web():
    app.run(debug=True, port="3000", host="0.0.0.0")


def run_terminal():
    while True:
        user_input = input("Introduce una fecha (ej. 12 Feb 2015): ")
        user_input = user_input.split()

        if len(user_input) != 3:
            print("El número de argumentos es incorrecto.")
            continue

        day, month, year = user_input

        if day.isdecimal() is not True:
            print(f"Has introducido {day}, que no es un número")
            continue

        if month.isalpha() is not True:
            print(f"Has introducido {month}, que no sigue el formato correcto")
            continue

        if year.isdecimal() is not True:
            print(f"Has introducido {year}, que no es un número")
            continue

        day = int(day)
        month = month.lower()
        year = int(year)

        if day < 1 or day > 31:
            print(f"Has introducido {day}, que es un día incorrecto")
            continue

        if year < 1 or year > 3000:
            print(f"Has introducido {year}, que es un año incorrecto")
            continue

        month_names = [
            "jan",
            "feb",
            "mar",
            "apr",
            "may",
            "jun",
            "jul",
            "aug",
            "sep",
            "oct",
            "nov",
            "dec",
        ]

        try:
            month_number = month_names.index(month) + 1
        except ValueError:
            print("El mes introducido no coincide con las abreviaturas de un mes.")
            continue

        print(convert_format(year, month_number, day))
        print(convert_hebrew(year, month_number, day))
        print(convert_islamic(year, month_number, day))
        print(convert_julianday(year, month_number, day))

        break


if len(sys.argv) > 2:
    print(
        "El número de argumentos no es válido, si necesitas ayuda, utiliza: calendarios-astronomicos help"
    )
elif len(sys.argv) == 1:
    run_terminal()
elif sys.argv[1] == "web":
    run_web()
elif sys.argv[1] == "help":
    print(
        """Descripción: 

calendarios-astronomicos es un conversor de fechas con capacidad de transformar 
las fechas del calendario gregoriano al calendario judío, al calendario musulmán y a la data juliana. 

También devuelve la fecha en formato ISO-8061.
  
Argumentos:

  web       Crea un servicio web para acceder de forma más cómoda al conversor.
  help      Muestra este mensaje de ayuda.
  """
    )
else:
    print(
        "Argumento desconocido. Si necesitas ayuda, utiliza: calendarios-astronomicos help"
    )
