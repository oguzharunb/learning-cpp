#ifndef PHONEBOOK_HPP
#define PHONEBOOK_HPP

#include "Contact.hpp"

class PhoneBook {
	public:
		PhoneBook();
		void addContact(Contact &contact);
		void searchContact();

	private:
		Contact _contacts[8];
};

#endif