"""
Buy-a-Mattress as a Web App
"""
import streamlit as st

TAX_RATE = 0.0625
SEALY = 1800  # King size mattress
SIMMONS = 2000
SEALY_QUEEN = -400
SEALY_TWIN = -900
SIMMONS_QUEEN = -600
SIMMONS_FULL = -1000
SEALY_FIRM = 400
SEALY_EXTRAFIRM = 600
SIMMONS_FIRM = 500
SIMMONS_EXTRAFIRM = 1000
PROMOCODE = 'SLEEP'
DISCOUNT_RATE = 0.1

price = 0.0
discount = 0.0

#print("Welcome!\n")
st.title("Welcome to Buy-A-Mattress")

#brand = input("Please select the mattress brand (1 - Sealy, 2 - Simmons): ")
#while not (brand == '1' or brand == '2'):
#    print(f"Invalid brand name!")
#    brand = input("Please select the mattress brand: 1 - Sealy, 2 - Simmons: ")

brand = st.radio("Please select the mattress brand:", ("Sealy", "Simmons"))
st.write("Brand=", brand)
#if brand == "1":
if brand == "Sealy":
    #size = input("Please select the size (K - King, Q - Queen, T - Twin): ").upper()
    size = st.selectbox("Please select the size: " ,("King", "Queen", "Twin"))

    #while size not in 'KQT':
    #    print("Invalid size!")
    #    size = input("Please select the size (K - King, Q - Queen, T-Twin): ").upper()

    #comfort = input("Please select the comfort level (M - Medium, F - Firm, E - Extra Firm): ").upper()
    comfort = st. selectbox ("Please select the comfort level:",
                       ("Medium", "Firm", "Extra Firm"))

    #while comfort not in 'MFE':
    #    print("Invalid comfort level!")
    #    comfort = input("Please select the comfort level (M - Medium, F - Firm, E - Extra Firm): ").upper()
else:
    #size = input("Please select the size (K - King, Q - Queen, F - Full): ").upper()
    size = st. selectbox ("Please select the size: ", ("King", "Queen", "Full"))

    #while size not in 'KQF':
    #    print("Invalid size!")
    #    size = input("Please select the size (K - King, Q - Queen, F - Full): ").upper()

    #comfort = input("Please select the comfort level (C - Cushion Firm, F - Firm, E - Extra Firm): ").upper()
    comfort = st. selectbox ("Please select the comfort level:",
                       ("Cushion Firm", "Firm", "Extra Firm"))

    #while comfort not in 'CFE':
    #    print("Invalid comfort level!")
    #    comfort = input("Please select the comfort level (C - Cushion Firm, F - Firm, E - Extra Firm): ").upper()

#box = input("Do you like to have box springs (Y - Yes, N - No)? ").upper()
box = st.radio("Do you like to have box springs?",
                       ("Yes","No"))

#while not (box == 'Y' or box == 'N'):
#    print("Invalid selection! ")
#   box = input("Do you like to have box springs (Y - Yes, N - No)? ").upper()

#shipping = input("Which shipping mode do you like (S - Standard, N - Next Day)? ").upper()
shipping = st.radio("Which shipping mode do you like?",
                       ("Standard","Next Day"))

#while shipping != 'S' and shipping != 'N':
#    print("Invalid shipping mode!")
#    shipping = input("Which shipping mode do you like (S - Standard, N - Next Day)? ").upper()

#promo = input("Promotion code: ").upper()
promo = st.text_input("Promotion code: ")
# these lines are new
if  promo != PROMOCODE:
    st.write("That promotion code is not valid!")
else:
    st.write("That promotion code is valid.")

#if brand == '1':
#    brand = "Sealy"
if brand == "Sealy":
    price = SEALY  # king size
#   if size == "Q":
    if size == "Queen":
    #    size = "Queen"
        price += SEALY_QUEEN
    #elif size == "T":
    elif size == "Twin":
    #    size = "Twin"
        price += SEALY_TWIN
    else:
        size = "King"

#    if comfort == "F":
#        comfort = "Firm"
    if comfort == "Firm":
        price += SEALY_FIRM
#    elif comfort == 'E':
#        comfort = "Extra firm"
    elif comfort == "Extra Firm":
        price += SEALY_EXTRAFIRM
    else:
        comfort = "Medium"
else:
    brand = "Simmons"
    price = SIMMONS  # king size
#    if size == "Q":
#        size = "Queen"
    if size == "Queen":
        price += SIMMONS_QUEEN
#    elif size == "F":
#        size = "Full"
    elif size == "Full":
        price += SIMMONS_FULL
    else:
        size = "King"

#    if comfort == "F":
#        comfort = "Firm"
    if comfort == "Firm":
        price += SIMMONS_FIRM
#    elif comfort == 'E':
#        comfort = "Extra firm"
    if comfort == "Extra Firm":
        price += SIMMONS_EXTRAFIRM
    else:
        comfort = "Cushion Firm"

boxprice = 0.0
#if box == 'Y':
if box == "Yes":
    if size == 'King':
        boxprice = 400
    elif size == 'Queen':
        boxprice = 300
    elif size == 'Full':
        boxprice = 200
    else:
        boxprice = 100

if promo.upper() == PROMOCODE:
    discount = (price + boxprice) * DISCOUNT_RATE

subtotal = price + boxprice - discount
tax = subtotal * TAX_RATE

#if shipping == "S":
if shipping == "Standard":
#    shipping = "Standard"
    shippingprice = 100
else:
#    shipping = 'Next-day'
    shippingprice = 300

total = subtotal + tax + shippingprice

# """
#
# print()
# print("="*15 + "Order Summary" + "="*20)
# print(f"{brand} mattress, {size} size, {comfort}:")
# print(f"Mattress:\t\t\t${price:>8,.2f}")
# if box == 'Y':
#     print(f"Box springs:\t\t${boxprice:>8,.2f}")
# if discount != 0.0:
#     print(f"Discount:\t\t\t${-discount:>8,.2f}")
# print(f"Subtotal:\t\t\t${subtotal:>8,.2f}")
# print(f"{shipping}:\t${shippingprice:>8,.2f}")
# print(f"Tax:\t\t\t\t${tax:>8,.2f}")
# print("-"*48)
# print(f"Total:\t\t\t\t${total:>8,.2f}")
# """
st.header("Order Summary")
st.text("="*15 + "Order Summary" + "="*20)
st.text(f"{brand} Mattress, {size} size, {comfort} comfort:")
st.text(f"{'Mattress':20s}\t\t${price:>8,.2f}")
if box == 'Yes':
    st.text(f"{'Box springs':20s}\t\t${boxprice:>8,.2f}")
if discount != 0.0:
    st.text(f"{'Discount:':20s}\t\t${-discount:>8,.2f}")
st.text(f"{'Subtotal:':20s}\t\t${subtotal:>8,.2f}")
st.text(f"{shipping}{' Shipping:':12s}\t\t${shippingprice:>8,.2f}")
st.text(f"{'Tax:':20s}\t\t${tax:>8,.2f}")
st.text("-"*48)
st.text(f"{'Total:':20s}\t\t${total:>8,.2f}")
