import factory
from factory import fuzzy

from django.contrib.auth.models import User

from issue_tracker.models import Issue


class UserFactory(factory.DjangoModelFactory):

    username = factory.Faker('user_name')
    password = fuzzy.FuzzyText(length=10)
    email = 'user@test.cz'

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        manager = cls._get_manager(model_class)
        # The default would use ``manager.create(*args, **kwargs)``
        return manager._create_user(*args, **kwargs)

    class Meta:
        model = User


class IssueFactory(factory.DjangoModelFactory):

    name = fuzzy.FuzzyText(length=10)
    created_by = factory.SubFactory(UserFactory)
    solver = factory.SubFactory(UserFactory)
    leader = factory.SubFactory(UserFactory)

    class Meta:
        model = Issue
