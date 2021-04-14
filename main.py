from flask import Flask, render_template, request
from smtplib import SMTP

email = "chaterprakash@gmail.com"
password = "pcchater@160997"

app = Flask(__name__)

@app.route('/')
def get_home():
    return render_template("index.html")

@app.route('/index')
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_send=True)
    return render_template("contact.html", msg_send=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with SMTP("smtp.gmail.com") as smtp:
        smtp.starttls()
        smtp.login(user=email,
                   password=password
                   )
        smtp.sendmail(from_addr=email, to_addrs=email, msg=email_message)


if __name__ == "__main__":
    app.run(debug=True)