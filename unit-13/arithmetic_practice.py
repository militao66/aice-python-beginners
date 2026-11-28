
#Online Store Checkout & Packaging
item_price = 15000
quantity = 3
delivery_fee = 2500
discount = 5000
tottal_stock = 50
box_capacity = 8
loyal_tier = 2

# Subtotal for the items
subtotal = item_price * quantity

total_before_discount = subtotal + delivery_fee

final_total = total_before_discount - discount

split_bill = final_total / 2

full_boxes = tottal_stock // box_capacity

leftover_items = tottal_stock % box_capacity

bonus_points = 10 ** loyal_tier

print("---- Store Checkout & Packaging ----")
print(f"Items Subtotal: {subtotal}")
print(f"Initial Total Price: {total_before_discount}")
print(f"Dsicounted Total Price: {final_total}")
print(f"Shared Bill: {split_bill}")
print(f"Filled No Of Boxes: {full_boxes}")
print(f"Items Left Unpacked: {leftover_items}")
print(f"Bonus Point For Loyal Customers: {bonus_points}")

