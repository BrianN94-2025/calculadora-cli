def suma(a: float, b: float) -> float:
    return a + b

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 4 and sys.argv[1] == "suma":
        print(suma(float(sys.argv[2]), float(sys.argv[3])))
    else:
        print("Uso: python calc.py suma <a> <b>")
