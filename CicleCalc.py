import math

def circle_calc(radius):
     area = math.pi * (radius**2)
     cic = 2*math.pi*radius
     diamet = 2*radius
     return round(area,2), round(cic,2), diamet

def main():
    in_radius = float(input("Enter radius : "))
    results = circle_calc(in_radius)
    print(f'Area : {results[0]}, Circumference : {results[1]}, Diameter: {results[2]}')

if __name__ == '__main__':
    main()
