from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from bs4 import BeautifulSoup
from tkinter import *
from tkcalendar import *
from datetime import *
import csv
import asyncio
import model
import tqdm as notebook_tqdm
import tkinter as tk
import threading

root = tk.Tk()
root.geometry("400x200")
root.title("Input Data!")

# creating header
header_label = tk.Label(root, text="Scraping Data",
                        font=('sans-serif', 10, 'bold'), justify='center')
header_label.pack()


# creating input form
input_form = tk.Frame(root)
input_form.pack()

# company name
company_name = tk.StringVar()

# input date
start_date = date.today()
end_date = date.today()

# creating components in input form
name_company = tk.Label(
    input_form, text="Enter the name of company: ", font=('sans-serif', 10, 'normal'))
name_entry = tk.Entry(input_form, font=(
    'sans-serif', 10, 'normal'), justify='left')

start_date_text = tk.Label(input_form, text="Choose start date: ",
                           font=('sans-serif', 10, 'normal'))
end_date_text = tk.Label(input_form, text="Choose end date: ",
                         font=('sans-serif', 10, 'normal'))
cal_start = DateEntry(input_form, selectmode='day', date_pattern='dd/mm/yyyy')
cal_end = DateEntry(input_form, selectmode='day', date_pattern='dd/mm/yyyy')

# creating auto update start date function when choose in Date Entry


def update_start_date(event):
    global start_date
    start_date = cal_start.get_date()
    check_date_range()

# creating auto update end date function when choose in Date Entry


def update_end_date(event):
    global end_date
    end_date = cal_end.get_date()
    check_date_range()

# creating check valid date function


def check_date_range():
    if start_date and end_date and start_date > end_date:
        messagebox.showerror(
            "Error", "End date must be greater than start date.")

# creating set start date function when click set button


def get_date_start():
    # triggered on Button Click
    l1 = tk.Label(input_form, text='data', bg='yellow')
    l1.grid(row=2, column=2, sticky='w', padx=(10, 0))
    l1.config(text=cal_start.get_date().strftime("%d/%m/%Y"))

# creating set end date function when click set button


def get_date_end():
    check_date_range()
    l2 = tk.Label(input_form, text='data', bg='yellow')
    l2.grid(row=3, column=2, sticky='w', padx=(10, 0))
    l2.config(text=cal_end.get_date().strftime("%d/%m/%Y"))


def crape_data():
    # Setup Selenium driver for access website without open new tab
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service("./chromedriver.exe")
    main_driver = webdriver.Chrome(service=service, options=chrome_options)
    sub_driver = webdriver.Chrome(service=service, options=chrome_options)

    ticker_symbol = company_name
    start_date = "01/01/2022"  # Specify the start date
    end_date = "31/12/2023"  # Specify the end date
    url = f"https://s.cafef.vn/tin-doanh-nghiep/{ticker_symbol}/Event.chn"
    base_url = "https://s.cafef.vn"
    date_format = "%d/%m/%Y"
    start_date = datetime.strptime(start_date, date_format).date()
    end_date = datetime.strptime(end_date, date_format).date()
    result = []

    # Scrape the main page
    main_driver.get(url)
    # The current news list index, starting with 0
    page_counter = 0
    # Check if should the driver continue to click next button
    is_while = True
    # Define next button
    next_button = main_driver.find_element(By.ID, "spanNext")

    # class Article

    class Article:
        def __init__(self, title, content, date):
            self.title = title
            self.content = content
            self.date = date
            self.sentiment = {"Negative": 0, "Positive": 0,
                              "Neutral": 0}  # Default level

        def __str__(self):
            return f"Title: {self.title}\nDate: {(self.date)}\nContent: {self.content}\nSentiment Percentages: {self.sentiment}\n"

    # May take very long time to scrape (~3 mins), time will depend on the speed of internet connection
    while is_while:
        soup = BeautifulSoup(main_driver.page_source, "html.parser")
        news_list = soup.find("div", id="divEvents").find_all("li")

        for news_item in news_list:
            news_link = news_item.find("a")["href"]
            news_title = news_item.find("a").text.strip()
            created_date_time = news_item.find("span").text.strip()
            created_date = created_date_time.split(" ")[0]
            created_date = datetime.strptime(created_date, date_format).date()

            if (created_date > end_date):
                continue
            # All the li after are created before start_date
            elif (created_date < start_date):
                is_while = False
                break

            # Access article from the link
            sub_driver.get(base_url+news_link)

            new_soup = BeautifulSoup(sub_driver.page_source, "html.parser")
            news_div = new_soup.find("div", id="newscontent")
            news_content = news_div.get_text(strip=True)
            if (len(news_content) < 300):
                continue
            temp_article = Article(news_title, news_content, created_date)
            result.append(temp_article)

        # Scrape 30 page of item list only
        if (page_counter < 30):
            next_button.click()
            page_counter += 1
        else:
            is_while = False

    for article in result:
        sentiment_rs = model.analyze_sentiment(article.title)
        article.sentiment["Negative"] = sentiment_rs[0]
        article.sentiment["Positive"] = sentiment_rs[1]
        article.sentiment["Neutral"] = sentiment_rs[2]

    for article in result:
        print(article)

    main_driver.quit()
    sub_driver.quit()


def on_button_click():
    company_name = name_entry.get()
    print(company_name)
    thread = threading.Thread(target=crape_data)
    thread.start()


# creating button set
button_start = tk.Button(
    input_form, text='Set', command=get_date_start)
button_end = tk.Button(input_form, text='Set', command=get_date_end)
submit = tk.Button(input_form, text='SUBMIT', command=on_button_click)

# auto update when selected date entry
cal_start.bind("<<DateEntrySelected>>", update_start_date)
cal_end.bind("<<DateEntrySelected>>", update_end_date)

# creating all components
name_company.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
start_date_text.grid(row=2, column=0, sticky='e')
cal_start.grid(row=2, column=1, sticky='w')
button_start.grid(row=2, column=1, sticky='e')
end_date_text.grid(row=3, column=0, sticky='e')
cal_end.grid(row=3, column=1, sticky='w')
button_end.grid(row=3, column=1, sticky='e')
submit.grid(row=4, column=1, sticky='w')

root.mainloop()
