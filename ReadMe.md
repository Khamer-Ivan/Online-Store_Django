# MEGANO Online Store

MEGANO is a project coding in Python using the Django framework.

## Project structure
### The project consists of the following parts
1. Applications:
 - `cart` - the application of the user's cart of goods with the ability to add and remove goods, as well as change the quantity.
 - `orders` - application of orders. Contains services for ordering, payment, and viewing order history;
 - `products` - the app of the store's products. Contains services for viewing products, filtering and sorting, as well as adding reviews to the product;
 - `profile` - the user's application. It contains the services of registration, login/logout, password change, as well as the user's personal account;
2. Documentation:
 - `ReadMe.md` - Project Description;
 - `requirements.txt` - Connecting dependencies;

## Project Installation
To install the source code of the online store, clone the repository from GitHub or enter the following command:
```
https://github.com/Khamer-Ivan/Online-Store_Django.git
```
In order for the project to work correctly, you need to install the dependencies using the command:
```
git install -r requirements.txt
```
Next, you need to create a superuser to access the admin panel
```
python manage.py createsuperuser
```
Now you can start the server by entering the command
```
python manage.py runserver
```

You will be taken to the main menu of the store and will be able to use the entire interface.

