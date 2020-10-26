def DivideNumber(num1, num2):
    try:
        results = float(num1)/float(num2)
    except ZeroDivisionError as e:
        print("Divide by Zero error")
        results = None
    except TypeError as e:
        print("Type Error , please check the input type ")
        results = None
    except Exception as e:
        print("Exceptiob :", type(e).__name__)
        results = None
    return results


if __name__ == "__main__":
    no1 = input("enter number1")
    no2 = input("enter number2")
    print(DivideNumber(no1, no2))