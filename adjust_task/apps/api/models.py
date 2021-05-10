"""Api models file."""
from django.db import models
from django.utils.translation import ugettext as _


class Dataset(models.Model):
    """Dataset model class.

    Parameters
    ----------
    models : django.db
    """

    date = models.DateField(_("date"), null=True, blank=True, db_index=True)
    channel = models.CharField(_("channel"), max_length=50, blank=True)
    country = models.CharField(_("country"), max_length=10, blank=True)
    os = models.CharField(_("os"), max_length=10, blank=True)
    impressions = models.PositiveIntegerField(
        _("impressions"), null=True, blank=True
    )
    clicks = models.PositiveIntegerField(_("clicks"), null=True, blank=True)
    installs = models.PositiveIntegerField(
        _("installs"), null=True, blank=True
    )
    spend = models.DecimalField(
        _("spend"), null=True, blank=True, max_digits=10, decimal_places=2
    )
    revenue = models.DecimalField(
        _("revenue"), null=True, blank=True, max_digits=10, decimal_places=2
    )
    created_at = models.DateField(
        _("created_at"),
        auto_now_add=True,
        help_text=_("the date when dataset was created"),
    )

    class Meta:  # noqa: D106
        verbose_name = "dataset"
        verbose_name_plural = "datasets"

    def __str__(self):
        """Str representation of dataset model.

        Returns
        -------
        str
            containing id and date of the given object
        """
        return f"{self.id}-{self.date}"
