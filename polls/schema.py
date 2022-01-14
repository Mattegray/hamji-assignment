import graphene
from graphene_django import DjangoObjectType
from .models import Question, Choice, Comment


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "question_text", "pub_date", "closed")


class Query(graphene.ObjectType):
    questions = graphene.List(QuestionType)

    def resolve_questions(root, info, **kwargs):
        return Question.objects.all()


class UpdateQuestion(graphene.Mutation):
    class Arguments:
        question_text = graphene.String(required=True)
        id = graphene.ID()

    question = graphene.Field(QuestionType)

    @classmethod
    def mutate(cls, root, info, question_text, id):
        question = Question.objects.get(pk=id)
        question.question_text = question_text
        question.save()

        return UpdateQuestion(question=question)


class CreateQuestion(graphene.Mutation):
    class Arguments:
        question_text = graphene.String(required=True)
        pub_date = graphene.Date(required=True)

    question = graphene.Field(QuestionType)

    @classmethod
    def mutate(cls, root, info, question_text, pub_date):
        question = Question()
        question.question_text = question_text
        question.pub_date = pub_date
        question.save()

        return CreateQuestion(question=question)


class Mutation(graphene.ObjectType):
    update_question = UpdateQuestion.Field()
    create_question = CreateQuestion.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

