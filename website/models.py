"""
Create or customize your page models here.
"""
from modelcluster.fields import ParentalKey
from coderedcms.forms import CoderedFormField
from coderedcms.models import (
    CoderedArticlePage,
    CoderedArticleIndexPage,
    CoderedEmail,
    CoderedFormPage,
    CoderedWebPage,
)

# Developer Added
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.images.edit_handlers import ImageChooserPanel

class ArticlePage(CoderedArticlePage):
    """
    Article, suitable for news or blog content.
    """

    class Meta:
        verbose_name = "Article"
        ordering = ["-first_published_at"]

    # Only allow this page to be created beneath an ArticleIndexPage.
    parent_page_types = ["website.ArticleIndexPage"]

    template = "coderedcms/pages/article_page.html"
    search_template = "coderedcms/pages/article_page.search.html"


class ArticleIndexPage(CoderedArticleIndexPage):
    """
    Shows a list of article sub-pages.
    """

    class Meta:
        verbose_name = "Article Landing Page"

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "website.ArticlePage"

    # Only allow ArticlePages beneath this page.
    subpage_types = ["website.ArticlePage"]

    template = "coderedcms/pages/article_index_page.html"


class FormPage(CoderedFormPage):
    """
    A page with an html <form>.
    """

    class Meta:
        verbose_name = "Form"

    template = "coderedcms/pages/form_page.html"


class FormPageField(CoderedFormField):
    """
    A field that links to a FormPage.
    """

    class Meta:
        ordering = ["sort_order"]

    page = ParentalKey("FormPage", related_name="form_fields")


class FormConfirmEmail(CoderedEmail):
    """
    Sends a confirmation email after submitting a FormPage.
    """

    page = ParentalKey("FormPage", related_name="confirmation_emails")


class WebPage(CoderedWebPage):
    """
    General use page with featureful streamfield and SEO attributes.
    """

    class Meta:
        verbose_name = "Web Page"

    template = "coderedcms/pages/web_page.html"

# ------ E-Commerce Section: Snipcart ------

class ProductsIndexPage(CoderedWebPage):
    # Landing page for Products
    class Meta:
        verbose_name = "Products Landing Page"

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = 'website.ProductsPage'

    # Only allow ProductPages beneath this page.
    subpage_types = ['website.ProductsPage']

    template = 'website/pages/products_index_page.html'

class ProductsPage(CoderedWebPage):
    # Custom page for individual products

    class Meta:
        verbose_name = "Products Page"

    # Only allow this page to be created beneath a ProductsIndexPage.
    parent_page_types = ['website.ProductsIndexPage']

    template = "website/pages/products_page.html"

    # Products Page model fields
    description = RichTextField(
        verbose_name="Products Description",
        null=True,
        blank=True,
        default=""
    )
    photo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Product Photo',
    )
    DAYS_CHOICES = (
        ("Weekends Only", "Weekends Only"),
        ("Monday-Friday", "Monday-Friday"),
        ("Tuesday/Thursday", "Tuesday/Thursday"),
        ("Seasonal", "Seasonal"),
    )
    days_available = models.CharField(
        choices = DAYS_CHOICES,
        max_length=20,
        default=""
    )

    # Add custom fields to the body
    body_content_panels = CoderedWebPage.body_content_panels + [
        FieldPanel("description"),
        FieldPanel("photo"),
        FieldPanel("days_available"),
    ]