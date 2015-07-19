from django.apps import AppConfig
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pretix.base.plugins import PluginType


class TicketOutputPdfApp(AppConfig):
    name = 'pretix.plugins.ticketoutputpdf'
    verbose_name = _("PDF ticket output")

    class PretixPluginMeta:
        type = PluginType.PAYMENT
        name = _("PDF ticket output")
        author = _("the pretix team")
        version = '1.0.0'
        description = _("This plugin allows you to print out tickets as PDF files")

    def ready(self):
        from . import signals  # NOQA

    @cached_property
    def compatibility_errors(self):
        errs = []
        try:
            import reportlab  # NOQA
        except ImportError:
            errs.append("Python package 'reportlab' is not installed.")
        return errs

default_app_config = 'pretix.plugins.ticketoutputpdf.TicketOutputPdfApp'
