import unittest


from ClassTasks.OOP import person


class MyTestCase(unittest.TestCase):
        def test_something_person_class_exists(self, true=None):
            person.Person("John", 11)

        def test_that_get_name_returns_name(self):
            akerele = person.Person("Akerele", 12)
            self.assertEqual(akerele.get_name(), "Akerele")

        def test_that_get_name_returns_age(self):
            akerele = person.Person("Akerele", 12)
            self.assertEqual(akerele.get_age(), 12)

        def test_that_greeet_method_works(self):
            akerele = person.Person("Akerele", 12)
            self.assertEqual(akerele.greet(), "hello-ip=pohio-nie")

        def test_that_user_age_cannot_be_more_150(self):
            eniola = person.Person("Eniola", 161)
            expected_error = "Age must not be less than 0 or greater to 13"
            self.assertEqual(expected_error, eniola.get_age())


