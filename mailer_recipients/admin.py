from django.contrib import admin

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.utils.translation import ungettext, ugettext_lazy as _

from .fields import ContentTypeChoiceField
from .models import Recipient


class RecipientAdmin(admin.ModelAdmin):

    list_display = ('email', 'model_verbose_name')

    def model_verbose_name(self, object):
        return object.content_type.model_class()._meta.verbose_name.capitalize()
    model_verbose_name.short_description = _(u'content type')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'content_type':
            kwargs['form_class'] = ContentTypeChoiceField
            kwargs['queryset'] = self.get_content_types()
        return super(RecipientAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    def get_content_types(self):
        models = getattr(settings, 'MAILER_RECIPIENTS_MODELS', ())
        queryset = ContentType.objects.all()
        if not models:
            return queryset.none()
        q = Q()
        for model in models:
            app_label, model = model.split('.')
            q |= Q(app_label=app_label, model=model.lower())
        return queryset.filter(q)


admin.site.register(Recipient, RecipientAdmin)
