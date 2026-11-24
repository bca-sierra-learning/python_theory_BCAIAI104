def calculate_gst(room_price):
    return 0.18*room_price

# to collect individual room details
def get_room_details():
    bookings={}
    for i in range(5):
        room_id=int(input("Enter room number:"))
        customer_name=input("Enter customer number:")
        contactno=input("Enter customer contact number:")
        booking_amount=int(input("Enter booking amount:"))
        date=input("Enter booking date:")
        gst=calculate_gst(booking_amount)
        bookings[i]={"roomno":room_id,
                     "name":customer_name,
                     "mobileno":contactno,
                     "amount":booking_amount,
                     "date":date,
                     "gst":gst,
                     }
    return bookings
    
 

# to display main dictionary
def display_booking():
    pass

#to get total room price
def get_total_room_price():
    


# to get total gst
def get_total_gst():
    pass

booking_info=get_room_details()
print(booking_info)
total_room_price=get_total_room_price(booking_info)
total_gst=get_total_gst(booking_info)
display_booking()
print(f"Total Room Price:{total_room_price}")
print(f"Total GST:{total_gst}")









