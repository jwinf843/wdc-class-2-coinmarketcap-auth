# Coinmarketcap auth

Remember the [https://coinmarketcap.com/](https://coinmarketcap.com/) clone we did in our [previous class](https://github.com/rmotr-curriculum/wdc-class-1-coinmarketcap-clone)? 💪 Today we will augment it with some authentication capabilities. 🙌

We want users to be able to log in and log out from the app, using the built-in Django authentication views. Check the official documentation for extra details:
[https://docs.djangoproject.com/en/2.0/topics/auth/default/](https://docs.djangoproject.com/en/2.0/topics/auth/default/)

## 1) Adding log in and log out views

There's no need to implement the log in and log out features, Django comes with it out of the box. Just set the proper URLs, and add the link in your navbar like this:

![image](https://user-images.githubusercontent.com/1155573/38334488-dddf9f5e-3831-11e8-9728-fb4a2bcb3726.png)

The view will look by default for a template called `templates/registration/login.html`. Just create a template with that name, and give it the styles you want. It should look something like this:

![image](https://user-images.githubusercontent.com/1155573/38334570-0ebede00-3832-11e8-8b4f-0ad6353479a1.png)

For the log out view, you won't need any template. Just point the link to the URL you configured in your `utls.py` module, and that's it.

## 2) Creating new coins

As a second step, we want the users of our app to be able to create new Cryptocurrencies. For that we need to create a custom Django ModelForm, which will handle all the fields validation for us, according to the rules configured in the `Cryptocurrency` model.

Add a button in the main page, with a link to `/create`. Should look something like:

![image](https://user-images.githubusercontent.com/1155573/38335714-ad1c1cfe-3835-11e8-9000-a5792b28ac08.png)

In the `/create` template, we will render a form with only a few of the required models to create a Cryptocurrency object. Check the following screenshot for extra details:

![image](https://user-images.githubusercontent.com/1155573/38335769-e0800a24-3835-11e8-978a-b83fadbaba28.png)

The ModelForm will handle all the fields validation, but you will need to show errors in the template properly if they are present.

*hint: check the `django-bootstrap4` library for easy integration of Bootstramp v4 in templates*

## 3) Let's practice some foreign relationships between models.

We want to add a new `FavouriteCoin` model. It will have two new `ForeignKey` fields, one pointing to `User` and one to `Cryptocurrency`. Once you have the code in `models.py`, make sure to create the needed migrations.

If you are done, open the Django Shel (run `django-admin shell` command), and play with the new model, creating or fetching them from the DB.

That's all! 🎉 We just did a second iteration to the Coinmarketcap clone, adding some more advanced functionalities of the Django framework.
