all_districts = []
vaccinated_districts = []
no_of_all_districts = int(input("Enter the total number of districts: "))
for n in range(no_of_all_districts):
	dist = input("Please enter the name of the districts: ")
	all_districts.append(dist)
print(f"All the districts are: {all_districts}")
no_of_vaccinated_districts = int(input("Enter the number of districts that have been vaccinated: "))
for n in range(no_of_vaccinated_districts):
	dist = input("Please enter the name of the districts that have been vaccinated: ")
	vaccinated_districts.append(dist)
print(f"All districts that have been vaccinated are: {vaccinated_districts}")
un_vaccinated_districts = []
districts_for_covishield = []
districts_for_covaxin = []

for districts in all_districts:
	if districts not in vaccinated_districts:
		un_vaccinated_districts.append(districts)

for district in un_vaccinated_districts:
	if un_vaccinated_districts.index(district) % 2 == 0:
		districts_for_covishield.append(district)
	else:
		districts_for_covaxin.append(district)
print(f"Un-vaccinated districts are: {un_vaccinated_districts}")
print(f"Covishield will be provided to the following districts: {districts_for_covishield}")
print(f"Covaxin will be provided to the following districts: {districts_for_covaxin}")
