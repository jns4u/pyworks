class AddressBookEntry(object):
	version = 0.1
	def __init__(self, name, phone):
		self.name = name
		self.phone = phone
	
	def update_phone(self, phone):
		self.phone = phone

baby = AddressBookEntry('Bhupriya Singh', '408-555-1212')
dns = AddressBookEntry('Dhruv Narayan Singh', '650-555-1212')

print(baby.phone)
baby.update_phone("345-567-2345")
print(baby.phone)
