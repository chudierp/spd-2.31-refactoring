# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.
def get_price(): {
    if (base_price() > 1000) {
        return base_price() * 0.95;
    }
    else {
        return base_price * 0.98;
    }
}
double basePrice() {
  return quantity * itemPrice;
}

