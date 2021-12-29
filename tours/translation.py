from modeltranslation.translator import register, TranslationOptions

from tours.models import TourModel


@register(TourModel)
class TourTranslationOptions(TranslationOptions):
    fields = ('title', 'long_description', 'price',)
