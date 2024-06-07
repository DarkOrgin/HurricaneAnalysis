from operator import itemgetter


# Names of hurricanes
names = [
    'Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II',
    'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet',
    'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
    'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina',
    'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael'
]

# Month of hurricane occurances
months = [
    'October', 'September', 'September', 'November', 'August', 'September',
    'September', 'September', 'September', 'September', 'September', 'October',
    'September', 'August', 'September', 'September', 'August', 'August',
    'September', 'September', 'August', 'October', 'September', 'September',
    'July', 'August', 'September', 'October', 'August', 'September', 'October',
    'September', 'September', 'October'
]

# Year of hurricane occurance
years = [
    1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961,
    1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004,
    2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018
]

# Maximum sustained winds (mph) of hurricane
max_sustained_winds = [
    165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
    175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175,
    165, 180, 175, 160
]

# Areas affected by each hurricane
areas_affected = [
    ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
    [
        'Lesser Antilles', 'The Bahamas', 'United States East Coast',
        'Atlantic Canada'
    ], ['The Bahamas', 'Northeastern United States'],
    [
        'Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas',
        'Bermuda'
    ], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'],
    ['Jamaica', 'Yucatn Peninsula'],
    ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
    [
        'Southeastern United States', 'Northeastern United States',
        'Southwestern Quebec'
    ], ['Bermuda', 'New England', 'Atlantic Canada'],
    ['Lesser Antilles', 'Central America'],
    ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
    ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
    ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'],
    ['Mexico'], ['The Caribbean', 'United States East coast'],
    ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
    ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
    ['The Caribbean', 'United States East Coast'],
    ['The Bahamas', 'Florida', 'United States Gulf Coast'],
    ['Central America', 'Yucatn Peninsula', 'South Florida'],
    ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
    ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
    ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'],
    ['Bahamas', 'United States Gulf Coast'],
    ['Cuba', 'United States Gulf Coast'],
    ['Greater Antilles', 'Central America', 'Florida'],
    ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
    [
        'Antilles', 'Venezuela', 'Colombia', 'United States East Coast',
        'Atlantic Canada'
    ],
    [
        'Cape Verde', 'The Caribbean', 'British Virgin Islands',
        'U.S. Virgin Islands', 'Cuba', 'Florida'
    ],
    [
        'Lesser Antilles', 'Virgin Islands', 'Puerto Rico',
        'Dominican Republic', 'Turks and Caicos Islands'
    ],
    [
        'Central America',
        'United States Gulf Coast (especially Florida Panhandle)'
    ]
]

# Damages (USD($)) caused by hurricane
damages = [
    'Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M',
    '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M',
    '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
    '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B',
    '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B'
]

# Death toll for each hurricane
deaths = [
    90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
    2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603,
    138, 3057, 74
]


# Converts damges from string format to float format.
def convert_damages(damages):
    new_damages = []
    for string in damages:
        if 'Damages not recorded' in string:
            new_damages.append(string)

        if 'M' in string:
            new_string = string.replace("M", "")
            new_damages.append(float(new_string) * 1_000_000)

        elif 'B' in string:
            new_string = string.replace("B", "")
            new_damages.append(float(new_string) * 1_000_000_000)

    return new_damages


# Update Recorded Damages
conversion = {"M": 1000000, "B": 1000000000}
####### ^^^^^^^^^^^^^ ########
##! Is there a better way? !##
####### ^^^^^^^^^^^^^ ########







# Testing function by updating damages
converted_damages = convert_damages(damages)
#print(converted_damages, '\n')

# Creates hurricane dictionary
hurricane_dict = []
index = -1
for name in names:
    index += 1
    hurricane_dict.append({
        "Name": names[index],
        "Month": months[index],
        "Year": years[index],
        "Max Sustained Wind": max_sustained_winds[index],
        "Areas Affected": areas_affected[index],
        "Damage": converted_damages[index],
        "Deaths": deaths[index]
    })

# View the hurricane dictionary
#print(hurricane_dict)

# Sorting by Year
#sort_by_year = sorted(hurricane_dict, key=lambda field: field['Year'], reverse=True)


sort_by_year = sorted(hurricane_dict, key=itemgetter("Year"), reverse=True)


#print(sort_by_year)


# Organizing by Year
def list_of_years(hurricanes, year):
    new_dict_list = []
    for record in hurricanes:
        current_year = record["Year"]
        if current_year == year:
            new_dict_list.append(record)
    return new_dict_list


year_1932 = list_of_years(hurricane_dict, 1932)

#print(year_1932, '\n')


# Counting Damaged Area by individual location
def damage_count(hurricanes, area):
    current_count = 0
    for record in hurricanes:
        current_area = record["Areas Affected"]
        for item in current_area:
            if area == item:
                current_count += 1
    return current_count


cuba_affect = damage_count(hurricane_dict, "Cuba")
#print(cuba_affect, '\n')


# Creates a set of unique areas to use later in counting damaged areas
_areas = []
for list in areas_affected:
    for item in list:
        _areas.append(item)
        
uniqe_areas = set(_areas)
#print(uniqe_areas , '\n')



# Create dictionary of areas to store the number of hurricanes involved in
new_hurricane_dict = {}
for item in uniqe_areas:
    new_hurricane_dict[item] = damage_count(hurricane_dict, item)
#print(new_hurricane_dict, '\n')



# Calculating Maximum Hurricane Count in one location
_most_canes = max(new_hurricane_dict.values())
#print(_most_canes)



# Find most frequently affected area and the number of hurricanes
area_most_affected = max(new_hurricane_dict), max(new_hurricane_dict.values())
#print(area_most_affected)



# Calculating the Deadliest Hurricane
max_deaths = max(hurricane_dict, key=lambda field: field['Deaths'])
#print(max_deaths, '\n')



# Found highest mortality hurricane and the number of deaths
#print('Hurricane ', max_deaths['Name'], ' had  the  most  deaths: ', max_deaths['Deaths'],'\n')



# Rating Hurricanes by Mortality
listed_by_deaths = sorted(hurricane_dict, key=lambda field: field['Deaths'], reverse=True)
#print(listed_by_deaths[:5], '\n')




# Categorized hurricanes in new dictionary with mortality severity as key
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}

def categorize_hurricanes(data, scale):
    hurricane_categories = {key: [] for key in scale}
    
    for hurricane in data:
        mortality = hurricane['Deaths']
    
        for category, max_mortality in sorted(scale.items(), reverse=True):
            if mortality >= max_mortality:
                hurricane_categories[category].append(hurricane)
                break
    
    return hurricane_categories

hurricane_categories = categorize_hurricanes(hurricane_dict, mortality_scale)

# This could also be done within the function if you know you want the deaths
# in that order
for category in hurricane_categories.values():
    category.sort(key=itemgetter('Deaths'))
    
#print("Category 0: ", hurricane_categories[0], '\n')
#print("Category 1: ", hurricane_categories[1], '\n')
#print("Category 2: ", hurricane_categories[2], '\n')
#print("Category 3: ", hurricane_categories[3], '\n')
#print("Category 4: ", hurricane_categories[4], '\n')

# 8 Calculating Hurricane Maximum Damage


def calculate_hurricane_damage(hurricane_data, scale):
    hurricane_categories = {key: [] for key in scale}

    for hurricane in hurricane_data:
        if hurricane['Damage'] == 'Damages not recorded':
            hurricane['Damage'] = 0
            
        damage = int(hurricane['Damage'])
        
        for category, max_damage in sorted(scale.items(), reverse=True):
            if damage >= max_damage:
                hurricane_categories[category].append(hurricane)
                break
    
    return hurricane_categories



# Rating Hurricanes by Damage
damage_scale = {
    0: 0,
    1: 100_000_000,
    2: 1_000_000_000,
    3: 10_000_000_000,
    4: 50_000_000_000
}

hurricane_damage_category = calculate_hurricane_damage(hurricane_dict, damage_scale)
for category in hurricane_damage_category.values():
    category.sort(key=itemgetter('Damage'))

# highest damage in USD inducing hurricane and its total cost

highest_damage_hurricane = hurricane_damage_category[4][-1]


#print('Hurricane', highest_damage_hurricane['Name'], 'was resposible for  $', highest_damage_hurricane['Damage'], 'in recorded damages', '\n')



# categorize hurricanes in new dictionary with damage severity as key

print("Damage Category 0 in USD: ", hurricane_damage_category[0], '\n')
print("Damage Category 1 in USD: ",hurricane_damage_category[1], '\n')
#print("Damage Category 2 in USD: ",hurricane_damage_category[2], '\n')
#print("Damage Category 3 in USD: ",hurricane_damage_category[3], '\n')
print("Damage Category 4 in USD: ",hurricane_damage_category[4], '\n')









