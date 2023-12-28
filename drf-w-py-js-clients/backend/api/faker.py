from articles.models import Article
from products.models import Product
from django.contrib.auth.models import User
from faker import Faker
from django.utils import timezone


def unique_product_names(fake, num_names):
    names = set()
    product_terms = ["Pro", "Max", "Ultra", "Plus", "Mini", "Smart", "Eco", "Flex"]
    while len(names) < num_names:
        name = f"{fake.word()} {fake.random_element(product_terms)}"
        names.add(name.capitalize())
    return list(names)


def run():
    User.objects.all().exclude(username="admin").delete()
    Article.objects.all().delete()
    Product.objects.all().delete()
    fake = Faker()

    for _ in range(10):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        first_name = fake.first_name()
        last_name = fake.last_name()
        is_staff = fake.boolean()
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
        )

    product_names = unique_product_names(fake, 200)

    article_categories = [
        "Technology",
        "Health",
        "Education",
        "Sport",
        "Art",
        "Science",
        "Travel",
        "Finance",
        "Culinary",
    ]

    for _ in range(200):
        selected_user_for_product = User.objects.order_by("?").first()
        product_name = product_names.pop()
        Product.objects.create(
            title=product_name,
            content=fake.text(),
            price=fake.pydecimal(left_digits=2, right_digits=2, positive=True),
            public=fake.boolean(),
            user=selected_user_for_product,
        )

        selected_user_for_article = User.objects.order_by("?").first()
        publish_date = fake.date_time_between(start_date="-1y", end_date="now")
        publish_date_aware = timezone.make_aware(publish_date)
        tags = ", ".join(
            fake.random_elements(elements=article_categories, unique=True, length=2)
        )
        Article.objects.create(
            title=fake.sentence(),
            body=fake.text(),
            tags=tags,
            make_public=fake.boolean(),
            publish_date=publish_date_aware,
            user=selected_user_for_article,
        )

    print("Finished")
