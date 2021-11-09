def application(name, city, company, email='bulletil@gmail.com', *args, **kwargs):
    print(f"{name} works in {city} at {company}, his email is {email}.")


application('ilya', 'gomel', 'itechart', 'hi also like j', 'hh', 75000)