from django.db import models
from django.utils.translation import ugettext_lazy as _


class Account(models.Model):
   
    number = models.PositiveIntegerField(_("Número"), unique=True, blank=False, null=False, editable=True)
    initial_value = models.DecimalField(_("Saldo Inicial"), 
                default=0, max_digits=10, decimal_places=2, blank=False, null=False, editable=True)
    created = models.DateField(_("Criado em"), auto_now_add=True)

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")

    def __str__(self):
        return self.number.__str__()


class History(models.Model):

    OPERATION_CHOICES = (
        ("C", "Credito"),
        ("D", "Debito"),
    )

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='histories')
    short_description = models.CharField(_("Descrição"), max_length=100, blank=False)
    operation = models.CharField(_("Operação"), max_length=1, choices= OPERATION_CHOICES)
    value = models.DecimalField(_("Valor"), max_digits=10, decimal_places=2)    

    class Meta:
        verbose_name = _("history")
        verbose_name_plural = _("histories")

    def __str__(self):
        return self.short_description