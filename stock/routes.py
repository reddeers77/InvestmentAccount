from flask import render_template,request,flash
from stock import app
from stock.action import Action

months = ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']

@app.route("/", methods=["POST","GET"])
def main():         
        
    if request.method=="POST":  
        name = request.form.get('name')
        amount = request.form.get('amount')
        amount=int(amount)
        day = request.form.get('daySelect')
        month = request.form.get('monthSelect')            
        year = request.form.get('yearSelect')
        try:

            date = "{}-{}-{}".format(year,month,day)
            result = Action(name,date,amount) 

            day=int(day)
            month=int(month)-1
            year=int(year)

            iname = result.TickerName()
            buy_price = result.Buy_Price()  
            sell_price = result.Sell_Price()
            today_amount = result.Today_Money(buy_price,sell_price)
            return render_template("return.html" ,months=months, day=day, year=year, month=month ,name=name, amount=amount, iname=iname, result = result, buy_price = buy_price, sell_price = sell_price, today_amount=today_amount) 
        except:
            flash('Hisse veya tarih hatalı','danger')
            day=int(day)
            month=int(month)-1
            year=int(year)
            return render_template("main.html",months=months, name=name, amount=amount, day=day, month=month, year=year)

    else:
        return render_template("main.html",months=months)
        

    