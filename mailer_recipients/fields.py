from django import forms


class ContentTypeChoiceField(forms.ModelChoiceField):

    def label_from_instance(self, object):
        return object.model_class()._meta.verbose_name.capitalize()
