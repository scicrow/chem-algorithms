# randles sevcik equation for calculating the diffusion controlled co-effient of cyclic voltammetry

import sys


def randles_Sevcik(ip, n, a, c, v):
    # ip == peak current in amperes, n == electrons transferred (usually 1),
    # a == electrode surface area (cm2), c == bulk concentration (mol*cm-3)
    # d == diffusion coefficient cm2*s-1, v == sweep rate (Vs-1).

    # originally Ip = 2.69 * 10**5 + N**(3/2) * A * C * D^(1/2) * V**(1/2)
    # rearranged to find D:
    n_three_over_two = n ** (3.0/2.0)
    v_one_over_two = v ** (1.0/2.0)
    result = ip / (2.69 * 10.0 ** 5.0 * n_three_over_two * a * c * v_one_over_two)
    d = result ** 2
    return d


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# if variable == type, then do thing??? isinstance though apparently there are issues with this
# http://www.canonical.org/~kragen/isinstance/

def main():
    if len(sys.argv) != 6:  # Including the script name, there should be 5 arguments
        print("Invalid input. Usage: python script_name.py arg1 arg2 arg3 arg4")
        return

    input_values = sys.argv[1:]  # Skip the first argument (script name)
    float_values = []

    for value in input_values:
        if is_float(value):
            float_values.append(float(value))
        else:
            print(f"Invalid input: {value} is not a valid float.")
            return

    if len(float_values) != 5:
        print("Invalid input: Four valid float values are required.")
        return

    ip, n, a, c, v = map(float, input_values)
    result = randles_Sevcik(ip, n, a, c, v)
    print("Diffusion coefficient:", result)

if __name__ == "__main__":
    main()

# randles_Sevcik(rs_input[0], rs_input[1], rs_input[2], rs_input[3], rs_input[4])
