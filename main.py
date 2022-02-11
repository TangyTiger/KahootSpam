from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/spam', methods=['POST'])
def spam():
    game_pin = request.form['game_pin']
    user_name = request.form['user_name']
    quantity_string = request.form['quantity']
    quantity = int(quantity_string)
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://kahoot.it")

    element = driver.find_element_by_id('game-input')
    element.send_keys(game_pin)
    time.sleep(4)
    element.send_keys(Keys.ENTER)
    time.sleep(5)
    element2 = driver.find_element_by_id('nickname')
    iString = str(i)
    element2.send_keys(user_name+iString)
    time.sleep(2)
    element2.send_keys(Keys.ENTER)

    for i in range(0, quantity-1): 
        
        driver.get("https://kahoot.it")

        element = driver.find_element_by_id('game-input')
        element.send_keys(game_pin)
        time.sleep(4)
        element.send_keys(Keys.ENTER)
        time.sleep(5)
        element2 = driver.find_element_by_id('nickname')
        iString = str(i)
        element2.send_keys(user_name+iString)
        time.sleep(2)
        element2.send_keys(Keys.ENTER)

    time.sleep(10000)
    #begin()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)