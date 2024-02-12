import os
from django import conf, http, urls, apps
from django.core.handlers.asgi import ASGIHandler

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "djangodb"),
        "USER": os.environ.get("POSTGRES_USER", "djan"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "djanpass"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": int(os.environ.get("POSTGRES_PORT", 5432)),
        "OPTIONS": {
            "pool": {
                "min_size":2,
                "max_size":5,
            }
        }
    }
}

conf.settings.configure(DATABASES=DATABASES, ALLOWED_HOSTS="*", ROOT_URLCONF=__name__)
apps.apps.populate(["messages"])
app = ASGIHandler()

urlpatterns = [urls.path("", urls.include("messages.app"))]


def main():
    from django.core.management import execute_from_command_line
    apps.apps.populate(["messages"])
    execute_from_command_line(["", "makemigrations"])
    execute_from_command_line(["", "migrate"])


if __name__ == "__main__":
    main()
