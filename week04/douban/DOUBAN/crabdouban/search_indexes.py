import datetime
from haystack import indexes
from .models import Moviebang


class MoviebangIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='name')
    updated = indexes.DateTimeField(model_attr='updated')
    short = indexes.CharField(model_attr='short')
    star = indexes.IntegerField(model_attr='n_start')

    def get_model(self):
        return Moviebang

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        # return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
        return self.get_model().objects.all()