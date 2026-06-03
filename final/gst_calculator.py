# GST Calculator - India
def gst_calc(amount, rate, inclusive=False):
    if inclusive:
        base = amount / (1 + rate/100)
        gst  = amount - base
    else:
        gst  = amount * rate / 100
        base = amount
    total = base + gst
    print(f"Base Amount:  Rs {base:,.2f}")
    print(f"GST ({rate}%):   Rs {gst:,.2f}")
    print(f"Total:        Rs {total:,.2f}")

print("GST EXCLUSIVE:")
gst_calc(10000, 18)
print("\nGST INCLUSIVE:")
gst_calc(11800, 18, inclusive=True)
