#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:35:21 2024

@author: ryanestes
"""

class SalesPerson:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.sales = []

    def add_sale(self, sale):
        self.sales.append(sale)

    def iter_sales(self):
        return iter(self.sales)

    def get_total_sales(self):
        return sum(self.sales)

    def get_min_sale(self):
        return min(self.sales)

    def get_max_sale(self):
        return max(self.sales)

    def get_average_sale(self):
        return sum(self.sales) / len(self.sales)


def main():
    sales_people = []
    company_total_sales = 0

    for i in range(3):  # Assuming we want to enter data for three salespeople
        name = input(f"Please enter sales person name: ")
        title = input(f"Please enter your sales person title: ")
        sales_person = SalesPerson(name, title)

        num_sales = int(input("How many sales values will you enter for this sales person? "))
        for j in range(num_sales):
            sale = float(input(f"Please enter sales figure for {name}: "))
            sales_person.add_sale(sale)

        sales_people.append(sales_person)

    print("\n----------------------------------------------------\n")

    for sales_person in sales_people:
        total_sales = sales_person.get_total_sales()
        min_sales = sales_person.get_min_sale()
        max_sales = sales_person.get_max_sale()
        average_sales = sales_person.get_average_sale()
        company_total_sales += total_sales

        print(f"Sales person: {sales_person.name}")
        print(f"Total Sales: ${total_sales:,.2f}")
        print(f"Min Sales: ${min_sales:,.2f}")
        print(f"Max Sales: ${max_sales:,.2f}")
        print(f"Average Sales: ${average_sales:,.2f}")
        print("----------------------------------------------------\n")

    print(f"Company total sales: ${company_total_sales:,.2f}")

if __name__ == "__main__":
    main()
