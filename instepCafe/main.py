import tkinter as tk
from tkinter import *

#region CLASSES
class order:
    def __init__(self, orderNum, name, drink, size, flavor, pumps, total):
        self.orderNum = orderNum
        self.name = name
        self.drink = drink
        self.size = size
        self.flavor = flavor
        self.pumps = pumps
        self.total = total

class drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class flavor:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} per pump"

class size:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"
#endregion

#region LISTS OF ITEMS
Small = size("Small", 0)
Medium = size("Medium", .45)
Large = size("Large", .9)
global Sizes
Sizes = [Small, Medium, Large]

Vanilla = flavor("Vanilla", .3)
Caramel = flavor("Caramel", .3)
Mocha = flavor("Mocha", .3)
NoFlavor = flavor("NA", 0)
global Flavors
Flavors = [Vanilla, Caramel, Mocha, NoFlavor]

BlackCoffee = drink("Black Coffee", 2.45)
Latte = drink("Latte", 2.95)
Espresso = drink("Espresso", 1.95)
IcedCoffee = drink("Iced Coffee", 2.75)
global Drinks
Drinks = [BlackCoffee, Latte, Espresso, IcedCoffee]
#endregion

#region FUNCTIONS
def get_name():
    name = nameEntry.get()
    global customerName
    customerName = name
    goto_order()

def destroy_all_widgets():
    for widget in window.winfo_children():
        if (widget != image) & (widget != background_label):
            widget.destroy()

def drink_select(drinkSelection):
    selectedDrinkOption.set(drinkSelection.name)
    global selectedDrink
    selectedDrink = next((Drink for Drink in Drinks if Drink.name == drinkSelection.name), None)

def flavor_select(flavorSelection):
    selectedFlavorOption.set(flavorSelection.name)
    global selectedFlavor
    selectedFlavor = next((Flavor for Flavor in Flavors if Flavor.name == flavorSelection.name), None)

def size_select(sizeSelection):
    selectedSizeOption.set(sizeSelection.name)
    global selectedSize
    selectedSize = next((Size for Size in Sizes if Size.name == sizeSelection.name), None)

def pump_select(pumps):
    global numOfPumps
    numOfPumps = pumps

def goto_order():
    destroy_all_widgets()
    window.title("ORDER")
    label = tk.Label(window, text="Welcome " + customerName + "! What can we get for you today?", foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    label.pack(pady=10)
    global selectedDrink
    selectedDrink = Drinks[0]
    global selectedDrinkOption
    selectedDrinkOption = tk.StringVar(window)
    selectedDrinkOption.set(Drinks[0])
    drinkDropdown = tk.OptionMenu(window, selectedDrinkOption, *Drinks, command=lambda drinkSelection: drink_select(drinkSelection))
    drinkDropdown.config(foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    drinkDropdown.pack(pady=10)
    global selectedFlavor
    selectedFlavor = Flavors[0]
    global selectedFlavorOption
    selectedFlavorOption = tk.StringVar(window)
    selectedFlavorOption.set(Flavors[0])
    flavorDropdown = tk.OptionMenu(window, selectedFlavorOption, *Flavors, command=lambda flavorSelection: flavor_select(flavorSelection))
    flavorDropdown.config(foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    flavorDropdown.pack(pady=10)
    global numOfPumps
    numOfPumps = 0
    pumpSpinbox = tk.Spinbox(window, from_=0, to=10, command=lambda: pump_select(pumpSpinbox.get()), foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    pumpSpinbox.pack(pady=10)
    global selectedSize
    selectedSize = Sizes[0]
    global selectedSizeOption
    selectedSizeOption = tk.StringVar(window)
    selectedSizeOption.set(Sizes[0])
    sizeDropdown = tk.OptionMenu(window, selectedSizeOption, *Sizes, command=lambda sizeSelection: size_select(sizeSelection))
    sizeDropdown.config(foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    sizeDropdown.pack(pady=10)
    summaryButton = tk.Button(window, text="That's what I want!", command=get_summary, foreground='#F2D69D', background="#6F4E37", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    summaryButton.pack(pady=10)

def get_summary():
    destroy_all_widgets()
    window.title("ORDER SUMMARY")
    drinkLabel = tk.Label(window, text="Drink: " + selectedDrink.name, foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    drinkLabel.pack(pady=10)
    flavorLabel = tk.Label(window, text="Flavor: " + selectedFlavor.name, foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    flavorLabel.pack(pady=10)
    pumpsLabel = tk.Label(window, text="Pumps: " + str(numOfPumps), foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    pumpsLabel.pack(pady=10)
    sizeLabel = tk.Label(window, text="Size: " + selectedSize.name, foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    sizeLabel.pack(pady=10)
    global total
    total = selectedDrink.price + selectedSize.price + int(numOfPumps) * selectedFlavor.price
    total = round(total, 2)
    global totalStr
    totalStr = "{:.2f}".format(total)
    totalLabel = tk.Label(window, text="Total: $" + totalStr, foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    totalLabel.pack(pady=10)
    submitButton = tk.Button(window, text="Submit Order", command=submit_order, foreground='#F2D69D', background="#6F4E37", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    submitButton.pack(pady=10)
    changeButton = tk.Button(window, text="Change Order", command=goto_order, foreground='#F2D69D', background="#6F4E37", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    changeButton.pack(pady=10)

def submit_order():
    destroy_all_widgets()
    newOrder = order(101, customerName, selectedDrink, selectedSize, selectedFlavor,numOfPumps, total)
    nameLabel = tk.Label(window, text="Name: " + newOrder.name, foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    nameLabel.pack(pady=10)
    orderNumLabel = tk.Label(window, text="Order #" + str(newOrder.orderNum), foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    orderNumLabel.pack(pady=10)
    drinkLabel = tk.Label(window, text="Drink: " + newOrder.drink.name, foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    drinkLabel.pack(pady=10)
    flavorLabel = tk.Label(window, text="Flavor: " + newOrder.flavor.name, foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    flavorLabel.pack(pady=10)
    pumpsLabel = tk.Label(window, text="Pumps: " + str(newOrder.pumps), foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    pumpsLabel.pack(pady=10)
    sizeLabel = tk.Label(window, text="Size: " + newOrder.size.name, foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    sizeLabel.pack(pady=10)
    totalLabel = tk.Label(window, text="TOTAL: $" + totalStr, foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    totalLabel.pack(pady=10)
    window.title("ORDER COMPLETE")
    label = tk.Label(window, text="Thank you for your order " + customerName + "!", foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
    label.pack(pady=10)


#endregion

#region TKINTER
window = tk.Tk()
window.geometry("600x400")
window.title("Welcome to Instep Cafe!")
image = tk.PhotoImage(file="instepCafeBG.png")
background_label = tk.Label(window, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

firstLabel = tk.Label(window, text="What's your name?", foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
firstLabel.pack(pady=10)
nameEntry = tk.Entry(window, foreground='#6F4E37', background="#FFFFFF", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
nameEntry.pack(pady=10)
nameButton = tk.Button(window, text="That's my name!", command=get_name, foreground='#F2D69D', background="#6F4E37", highlightthickness=3, highlightbackground = "#6F4E37", highlightcolor= "#6F4E37")
nameButton.pack(pady=10)
#endregion

window.mainloop()