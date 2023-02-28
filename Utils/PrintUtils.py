import jinja2


def create_html(ders_adi,questions):

    data = {"questions": questions, "ders_adi": ders_adi}

    jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader("form_template"))  # "../../form_template"
    t = jinja2_env.get_template("girdi.html")

    my_html = t.render(data)

    file = open("form_template/cikti.html", "w", encoding="utf-8")  # "../../form_template/cikti.html"
    file.write(my_html)
    file.close()