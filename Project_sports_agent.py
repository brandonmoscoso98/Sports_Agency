agent_rate = 0.05
def main():
    keep_going = 'y'
    print('Welcome to Sports Agency Calculation Centre ')
    input('How may I assist you today? ')
    print('You want to calculate how much money you will make as a sports agent? Sure thing! ')
    while keep_going == 'y':
        name = input('May I have your name? ')
        years = int (input('Enter the amount of years that the player is signed onto the contract. '))
        endorsement = float (input('How much is the player getting paid for their endorsement? '))
        gross = endorsement * agent_rate
        state = input ('What state do you live in? (Use state abbreviation) ')
        tax_rate = 0.0
        if state == 'AK' or state == 'DE' or state == 'MT' or state == 'NH' or state == 'OR':
            tax_rate = 0.0
        elif state == 'FL' or state == 'DC' or state == 'IA' or state == 'ID' or state == 'KY' or state == 'MD' or state == 'MI' or state == 'PA' or state == 'SC' or state == 'VT' or state == 'WV':
            tax_rate = 0.06
        elif state == 'CO':
            tax_rate = 0.029
        elif state == 'AL' or state == 'GA' or state == 'HI' or state == 'NY' or state == 'WY':
            tax_rate = 0.04
        elif state == 'MO':
            tax_rate = 0.0423
        elif state == 'LA':
            tax_rate = 0.0445
        elif state == 'OK' or state == 'SD':
            tax_rate = 0.045
        elif state == 'NC':
            tax_rate = 0.0475
        elif state == 'ND' or state == 'WI':
            tax_rate = 0.05
        elif state == 'NM':
            tax_rate = 0.0513
        elif state == 'VA':
            tax_rate = 0.053
        elif state == 'ME' or state == 'NE':
            tax_rate = 0.055
        elif state == 'AZ':
            tax_rate = 0.056
        elif state == 'OH':
            tax_rate = 0.0575
        elif state == 'UT':
            tax_rate = 0.061
        elif state == 'IL' or state == 'MA' or state == 'TX':
            tax_rate = 0.0625
        elif state == 'CT':
            tax_rate = 0.0635
        elif state == 'AR' or state == 'KS' or state == 'WA':
            tax_rate = 0.065
        elif state == 'NJ':
            tax_rate = 0.0663
        elif state == 'NV':
            tax_rate = 0.0685
        elif state == 'MN':
            tax_rate = 0.0688
        elif state == 'IN' or state == 'MS' or state == 'RI' or state == 'TN':
            tax_rate = 0.07
        elif state == 'CA':
            tax_rate = 0.0725


        commission = gross(gross * tax_rate)
        input('The gross pay is generally calculated by multiplying the agent rate and the endorsement amount (press enter to confirm)')
        print('The gross pay is $',
              format(gross, ',.2f'), sep='')
        input("You can find out your commission by multiplying the tax rate of the state you have selected by the gross pay (confirm) ")
        input('Here is the tax rate for your selected state (press enter to confirm when done):')
        print('States\tTaxes')
        print('--------------')
        print(state, '\t', tax_rate)
        print('The commission for your selected state is $',
              format(commission, ',.2f'), sep='')
        input('We will now see the total commission you will be given per year by multiplying the years by the commission (confirm)')
        total_commission = commission * years
        print('The total commission per year is $',
              format(total_commission, ',.2f'), sep='')
        keep_going = input('Do you need help with anything else? ' + \
    '(Enter y for yes and n for no): ')
    print('Thank you for visiting the Sports Agency Calculation Center, ',name,'. We hope to see you again soon ')

main()
