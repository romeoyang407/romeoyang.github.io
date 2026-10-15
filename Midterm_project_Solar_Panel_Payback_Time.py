import matplotlib.pyplot as plt
import math

# My project doesn't need external file data since everything comes from the user
# Python midterm project
print('Energy consumption vs solar panel analysis: Ask user for their energy consumption through multiple questions. Calculate energy costs, how many solar cells, what kind, maintenance frequency, and most importantly “how long will it take to pay off a solar panel”. Show graphs of solar panel use over time and how it would overtake their “usual” energy costs after some time.')

# questions to calculate energy cost
print('\nEnergy quesitons\n==================================')

while True:
    avg_bill = float(input('Average monthly eletricity bill (Avg ~160$): $'))
    sunlight = float(input('Average sunlight hours per day: '))
    solar_type = int(input('What type of solar panel do you prefer (enter 1 or 2)? \n1. Monocrystalline (high efficiency, more costly) \n2. Polycrystalline (lower efficiency, less costly)\n'))

    # Panel type parameters
    if solar_type == 1:
        panel = 'Monocrystalline'
        panel_cost = 300
        efficiency = 0.22
    elif solar_type == 2:
        panel = 'Polycrystalline'
        panel_cost = 200
        efficiency = 0.15

    ### Calculations ###
    yearly_bill = avg_bill * 12

    # Average eletric rate is 35 cents/ kWh
    eletricity_rate = 0.35
    yearly_usage = yearly_bill / eletricity_rate
    panel_kw = 0.4

    # Yearly energy (Calculates energy per day for the year)
    panel_yearly_energy = panel_kw * sunlight * 365 * efficiency

    # Panels needed
    panels_needed = yearly_usage / panel_yearly_energy
    panels_needed = math.ceil(panels_needed)

    # Cost of panels
    solar_cost = panels_needed * panel_cost

    # Payback
    payback_years = solar_cost / yearly_bill

    # Setting up graph
    years = list(range(0, 21))
    # Using list comprehension
    normal_cost = [yearly_bill * year for year in years]

    # Cost with solar
    solar_cost_over_time = [solar_cost for year in years]

    plt.plot(years, normal_cost, label='Electricity without solar panels')
    plt.plot(years, solar_cost_over_time, label='Solar panel cost')
    #Labeling where the solar panels paythemselves off
    payback_cost = yearly_bill * payback_years
    plt.scatter(payback_years, payback_cost, color='red', s=20, label=f'Payback ({payback_years:.2f} years)')

    plt.xlabel('Years')
    plt.ylabel('Cost ($)')
    plt.title('Solar Panels vs Normal Eletricity Costs')
    plt.legend()
    plt.grid(True)

    plt.show()

    ### Output ###
    print('\nResults\n==================================')

    print(f'Average monthly bill: ${avg_bill:.2f}')
    print(f'Estimated yearly bill: ${yearly_bill:.2f}')
    print(f'Average sunlight: {sunlight:.1f} hours')
    print(f'Panel type: {panel}')
    print(f'Estimated panels needed: {panels_needed}')
    print(f'Estimated solar panel cost: ${solar_cost:.2f}')
    print(f'Estimated payback time: {payback_years:.2f} years')

    cont = input('\nWould you like to enter another scenario (Y or N)?: ').lower()

    if cont == 'n':
        break

print('Goodbye!')
