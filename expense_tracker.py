import csv
import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# File to store expenses
FILE_NAME = "expenses.csv"

# Ensure file exists with headers
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    date = input("Enter date (YYYY-MM-DD) [leave blank for today]: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category (Food/Travel/Shopping/Other): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("✅ Expense added successfully!\n")

def view_expenses():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses found.\n")
        return
    print("\n📊 All Expenses:\n")
    print(df.to_string(index=False))
    print("\n")

def monthly_summary():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses found.\n")
        return

    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.strftime('%Y-%m')

    summary = df.groupby('Month')['Amount'].sum()
    print("\n📅 Monthly Summary:\n")
    print(summary)

    # Optional: Plot
    summary.plot(kind='bar', title="Monthly Expense Summary")
    plt.ylabel("Amount Spent")
    plt.show()

def category_summary():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses found.\n")
        return

    summary = df.groupby('Category')['Amount'].sum()
    print("\n📂 Category-wise Summary:\n")
    print(summary)

    # Optional: Plot
    summary.plot(kind='pie', autopct='%1.1f%%', title="Expenses by Category")
    plt.ylabel("")
    plt.show()

def menu():
    while True:
        print("\n==== Personal Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            monthly_summary()
        elif choice == '4':
            category_summary()
        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    menu()
