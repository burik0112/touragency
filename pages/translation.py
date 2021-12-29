from modeltranslation.translator import register, TranslationOptions

from pages.models import HomeModel, PlaceModel
from posts.models import PostModel


@register(HomeModel)
class HomeTranslationOptions(TranslationOptions):
    fields = ('title', 'remains', 'place',)


@register(PlaceModel)
class HomeTranslationOptions(TranslationOptions):
    fields = ('title', 'price',)
