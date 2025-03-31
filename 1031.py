def _1031_exchange_analysis(sale_price, original_purchase_price, reinvestment_cost):
    """
    Analyzes the deferred capital gains tax in a 1031 exchange scenario.

    Args:
    sale_price (float): The sale price of the property.
    original_purchase_price (float): The original purchase price of the property.
    reinvestment_cost (float): The cost of reinvesting in a new property.

    Returns:
    float: Deferred capital gains tax if reinvestment cost is greater than or equal to sale price; otherwise, 0.
    """
    capital_gains = sale_price - original_purchase_price
    deferred_tax = capital_gains * 0.2  # Assuming 20% capital gains tax rate
    return deferred_tax if reinvestment_cost >= sale_price else 0

# Example values
sale_price = 1200000
original_purchase_price = 800000
reinvestment_cost = 1500000

# Calculate deferred tax
deferred_tax = _1031_exchange_analysis(sale_price, original_purchase_price, reinvestment_cost)

# Print result
print(f"Deferred Capital Gains Tax: ${deferred_tax:,.2f}")
