def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# remove leading dollar sign and return the amount as float
def dollars_to_float(d):
    d_wo_dollar=d.replace("$", "")
    return float(d_wo_dollar)

# remove trailing percentage sign and return the percentage as a flat
def percent_to_float(p):
    p_wo_percent=p.replace("%", "")
    div100=float(p_wo_percent)/100
    return div100

main()