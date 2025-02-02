# -*- coding: utf-8 -*-
"""Askarchik.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_nD0_DBj51hHYbdnkmmnpTEhIL2vhPxY
"""



import pandas as pd
import matplotlib.pyplot as plt


def plot_books_2023(ax, df):
    ax.plot(df['Месяц'], df['Книги'], marker='o', color='red', linestyle='-', label='Прочитано книг')
    ax.set_title('Прочитанные книги 2023')
    ax.set_xlabel('Месяцы')
    ax.set_ylabel('Количество книг')
    ax.legend()
    ax.grid(True)

def plot_pages_2024(ax, df):
    ax.bar(df['Месяц'], df['Страницы'], color='green', label='Прочитано страниц')
    ax.set_title('Прочитанные страницы 2024')
    ax.set_xlabel('Месяцы')
    ax.set_ylabel('Количество страниц')
    ax.legend()
    ax.grid(True)

def main():
    df = pd.read_csv("/content/books (2).csv")
    df_2023 = df[df['Год'] == 2023]
    df_2024 = df[df['Год'] == 2024]
    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    plot_books_2023(axes[0], df_2023)
    plot_pages_2024(axes[1], df_2024)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()