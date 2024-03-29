from django.apps import AppConfig


class FinancialApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "financial_api"

    def ready(self):
        import financial_api.signals
