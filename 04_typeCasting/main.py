a = 10;
b = "10";

c = a + int(b);  # Type casting b to integer
print("Sum of a and b after type casting:", c);
print("Type of c:", type(c));

d = str(a) + b;  # Type casting a to string
print("Concatenation of a and b after type casting:", d);