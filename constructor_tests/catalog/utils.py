from main.models import Tests


class DataTestMixin:
    def get_mixin_context(self, context, test_id, **kwargs):
        test = Tests.object.get(pk=test_id)
        question = test.questions_set.get(question_ordinal=1)
        context[question] = question
        context.update(kwargs)
        return context